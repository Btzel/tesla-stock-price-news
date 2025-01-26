import requests
import os
import json
import time
class TeslaNews:
    def __init__(self,date):
        self.api_key = os.environ['NEWSAPI_API_KEY']
        self.params = {
            'q':'tesla',
            'from': date,
            'to':date,
            'sortBy':'popularity',
            'apiKey': self.api_key
        }
        self.tesla_news_url = "https://newsapi.org/v2/everything"
        self.request_for_data()
        self.heading,self.content = self.load_data()

    @staticmethod
    def load_data():
        with open("tesla_stock_news.json", "r") as file:
            data = json.load(file)
            heading = data["articles"][0]["title"]
            content = data["articles"][0]["content"]
            return heading,content

    def request_for_data(self):
        response = requests.get(url=self.tesla_news_url,params=self.params)
        response.raise_for_status()
        with open("tesla_stock_news.json", "w") as out_file:
            json.dump(response.json(), out_file, indent=4)
        time.sleep(0.2)
    def get_news_text(self, rate, cur_day_date, prev_day_date):
        sign = "🔺" if rate > 0 else "🔻"
        return {
            'rate': f'{sign}{rate}%',
            'change_date': f'{prev_day_date}/{cur_day_date}',
            'headline': f'{self.heading}',
            'content': f'{self.content}'
        }
