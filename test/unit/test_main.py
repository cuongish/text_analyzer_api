import unittest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.base_case = {
            "url": "https://en.wikipedia.org/wiki/Space_physics"
        }

        cls.edge_case = {
            "url": 1
        }

    def test_read_space_physics__returns_200(self):
        response = client.get("/")
        expected = 200
        self.assertEqual(response.status_code, expected)

    def test_home__displays_space_physics_word_count_and_names(self):
        response = client.get("/")
        self.assertEqual(len(response.json()), 2)

    def test_load__returns_422_if_posts_wrong_cart_value_data_type(self):
        response = client.put("/analyze",
                              json=self.edge_case)
        self.assertEqual(response.status_code, 422)
