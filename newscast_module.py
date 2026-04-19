import requests

class NewscastManager:
    def __init__(self):
        self.news_sources = {
            'ABC': 'https://abc.com/news',
            'CBS': 'https://cbs.com/news',
            'FOX': 'https://fox.com/news'
        }
        self.weather_sources = {
            'NYC': 'https://api.weather.com/nyc',
            'Suffolk': 'https://api.weather.com/suffolk',
            'Nassau': 'https://api.weather.com/nassau'
        }

    def fetch_news_headlines(self):
        headlines = {}
        for source, url in self.news_sources.items():
            response = requests.get(url)
            if response.status_code == 200:
                headlines[source] = response.json()['headlines']
            else:
                headlines[source] = None
        return headlines

    def fetch_weather_data(self, county):
        if county not in self.weather_sources:
            raise ValueError(f'No weather source for {county}')
        response = requests.get(self.weather_sources[county])
        if response.status_code == 200:
            return response.json()['weather']
        else:
            return None

# Example usage:
# manager = NewscastManager()
# news = manager.fetch_news_headlines()
# weather_nyc = manager.fetch_weather_data('NYC')