# coding: utf-8

import unittest
import responses
from unittest.mock import patch

from app.helper import collect_names
from app.helper import count_word
from app.helper import scrape_paragraph


class TextAnalyzerHelperTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_url = "https://test.url"
        cls.test_url_no_https = "http://test.url"

        cls.test_passage = "My first paragraph."
        cls.test_html = f"""<!DOCTYPE html>
        <html>
        <body>
        <h1>My First Heading</h1>
        <p>{cls.test_passage}</p>
        </body>
        </html>"""

        cls.passage_empty = ""
        cls.passage_with_English_name = "This is a passage with Jones and Rajesh."
        cls.passage_with_no_names = "This is a passage with no names."
        cls.passage_with_special_char = "That's a special character."

    def test_scape_paragraph__parses_only_p_if_no_crashes(self):
        with patch('app.helper.urlopen') as mock_requests:
            mock_requests.status = 200
            mock_requests.return_value = self.test_html
            result = scrape_paragraph(url=self.test_url)
            self.assertEqual(self.test_passage, result)

    @responses.activate
    def test_scape_paragraph__raises_exception_if_url_does_not_start_with_https(self):
        responses.add(responses.GET, url=self.test_url_no_https, status=200)
        with self.assertRaises(ValueError):
            scrape_paragraph(url=self.test_url_no_https)

    @responses.activate
    def test_scape_paragraph__raises_exception_if_http_response_status_code_is_not_200(self):
        responses.add(responses.GET, url=self.test_url, status=404)
        with self.assertRaises(Exception):
            scrape_paragraph(url=self.test_url)

    def test_count_word__raises_error_if_input_passage_is_empty(self):
        with self.assertRaises(ValueError):
            count_word(passage=self.passage_empty)

    def test_count_word__word_counter_does_not_ignore_special_character(self):
        expected = {"that's": 1, 'a': 1, 'special': 1, 'character.': 1}
        result = count_word(self.passage_with_special_char)
        self.assertEqual(expected, result)

    def test_collect_names__if_no_names_is_found(self):
        result = collect_names(self.passage_with_no_names)

        self.assertEqual(0, len(result))

    def test_collect_names__if_English_names_are_found(self):
        result = collect_names(self.passage_with_English_name)

        self.assertEqual(1, len(result))

    def test_collect_names__raises_error_if_input_passage_is_empty(self):
        with self.assertRaises(ValueError):
            collect_names(passage=self.passage_empty)
