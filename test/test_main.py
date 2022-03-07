import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app
from app.main import url

client = TestClient(app)


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.base_case = {
            "url": url
        }
        cls.edge_case = {
            "url": [url]
        }
        cls.test_passage = "Paragraph with John Doe and Jane Doe"
        cls.test_html = f"""<!DOCTYPE html>
                <html>
                <body>
                <h1>My First Heading</h1>
                <p>{cls.test_passage}</p>
                </body>
                </html>"""
        cls.base_response = {
            "word_counts": {'doe': 2, 'paragraph': 1, 'with': 1, 'john': 1, 'and': 1, 'jane': 1},
            "names": ["John Doe", "Jane Doe"]
        }

    def test_home__displays_space_physics_word_count_and_names(self):
        response = client.get("/")
        self.assertEqual(len(response.json()), 2)

    def test_load__returns_422_if_putting_wrong_data_type(self):
        response = client.put("/analyze",
                              json=self.edge_case)
        self.assertEqual(response.status_code, 422)

    def test_scape_paragraph__parses_only_p_if_no_crashes(self):
        with patch('app.helper.urlopen') as mock_requests:
            mock_requests.status = 200
            mock_requests.return_value = self.test_html

            response = client.put("/analyze",
                                  json=self.base_case)

            self.assertEqual(self.base_response, response.json())
