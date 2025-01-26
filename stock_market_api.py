import requests
import os
import json
from news_api import TeslaNews

class TeslaStock:
    def __init__(self):
        self.api_key = os.environ['ALPHAVANTAGE_API_KEY']
        self.tesla_stock_url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&"
                               f"symbol=TSLA&apikey={self.api_key}")
        # only run one time to get json data of tesla stock prices and save
        #self.request_for_data()
        self.tesla_stock_data = self.organized_data()
        self.news_texts_dict= self.iterate_over_data()
        #print(self.news_texts_dict)
        self.dump()

    @staticmethod
    def load_data() -> dict:
        with open("tesla_stock_prices.json", "r") as file:
            data = json.load(file)
            tsd_data = data['Time Series (Daily)']
            return tsd_data

    def request_for_data(self):
        response = requests.get(self.tesla_stock_url)
        response.raise_for_status()
        with open("tesla_stock_prices.json","w") as out_file:
            json.dump(response.json(),out_file,indent=4)

    def organized_data(self):
        tsd_data = self.load_data()
        data_list = [[date,tsd_data[date]] for date in tsd_data]
        return data_list

    def calculate_daily_change_rate(self,current_day_index):
        #to find what caused to current change in stock price
        cur_day_date = self.tesla_stock_data[current_day_index][0]
        prev_day_date = self.tesla_stock_data[current_day_index + 1][0]

        cur_day_closing = float(self.tesla_stock_data[current_day_index][1]['4. close'])
        prev_day_closing = float(self.tesla_stock_data[current_day_index+1][1]['4. close'])
        percentage_difference = (cur_day_closing - prev_day_closing) / cur_day_closing * 100

        tesla_news = TeslaNews(prev_day_date)
        news_text_dict = tesla_news.get_news_text(percentage_difference,cur_day_date,prev_day_date)

        return news_text_dict

    def iterate_over_data(self):
        news_text_list = [self.calculate_daily_change_rate(data_index) for data_index
                          in range(len(self.tesla_stock_data) - 1)]

        return {'TSLA': {f"{index}": data for index, data in enumerate(news_text_list)}}

    def dump(self):
        with open("what_affected_change_in_stock_price.json","w") as out_file:
            json.dump(self.news_texts_dict, out_file,indent=4)
            print("The json file has been created succesfully")


TeslaStock()



