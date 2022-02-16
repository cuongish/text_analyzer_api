# coding: utf-8

import json
import unittest

import responses

from app.helper import collect_names
from app.helper import count_word
from app.helper import scrape_paragraph

from app.classes import PrettyJSONResponse
from app.classes import InputJSON
from app.classes import OutputJSON


class TextAnalyzerHelperTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = "https://test.website"
        cls.passage = ""

    @responses.activate
    def test_retrieve_weather_using_responses(fake_weather_info):
        """Given a city name, test that a HTML report about the weather is generated
        correctly."""
        api_uri = API.format(city_name="London", api_key=API_KEY)
        responses.add(responses.GET, api_uri, json=fake_weather_info, status=HTTPStatus.OK)

        weather_info = retrieve_weather(city="London")
        assert weather_info == WeatherInfo.from_dict(fake_weather_info)
        pass

    @responses.activate
    def test_scape_paragraph__sends_requests_to_onetrust(self):
        responses.add(responses.GET, url=self.url,
                      json={'content': self.subject_correct_response}, status=200)

        get_all_new_subject_requests(onetrust_api_key=self.onetrust_api_key)

        self.assertEqual(1, len(responses.calls))
        pass

    def test_count_word__adsjfoa(self):
        pass

    def test_count_word__adsjfoa(self):
        pass

    def test_collect_names__if_no_names_is_found(self):
        pass

    def test_collect_names__raises_error_if_input_is_wrong_data_type(self):
        pass