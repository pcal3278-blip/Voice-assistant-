import unittest
from unittest.mock import Mock, patch

from newscast_module import NewscastManager


class TestNewscastManager(unittest.TestCase):
    def setUp(self):
        self.manager = NewscastManager()

    @patch("newscast_module.requests.get")
    def test_fetch_news_headlines(self, mock_get):
        good_response = Mock(status_code=200)
        good_response.json.return_value = {"headlines": ["h1", "h2"]}
        mock_get.return_value = good_response

        data = self.manager.fetch_news_headlines()
        self.assertEqual(data["ABC"], ["h1", "h2"])

    @patch("newscast_module.requests.get")
    def test_fetch_weather_data(self, mock_get):
        good_response = Mock(status_code=200)
        good_response.json.return_value = {"weather": {"temp": 70}}
        mock_get.return_value = good_response

        data = self.manager.fetch_weather_data("NYC")
        self.assertEqual(data, {"temp": 70})

    def test_fetch_weather_data_invalid_county(self):
        with self.assertRaises(ValueError):
            self.manager.fetch_weather_data("InvalidCounty")


if __name__ == "__main__":
    unittest.main()
