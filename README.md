# Tesla Stock Price News Analysis
A Python application that analyzes the correlation between Tesla stock price changes and news headlines, utilizing AlphaVantage API for stock data and NewsAPI for relevant news articles.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![API](https://img.shields.io/badge/AlphaVantage-API-red)
![News](https://img.shields.io/badge/NewsAPI-Integration-green)
![Analysis](https://img.shields.io/badge/Stock-Analysis-orange)

## 🎯 Overview
This project creates a comprehensive stock analysis tool that:
1. Fetches real-time Tesla stock data
2. Correlates price movements with news
3. Identifies potential impact factors
4. Generates detailed reports
5. Saves analysis in JSON format

## 📊 Analysis Features
### Data Collection
- Real-time stock price tracking
- News article aggregation
- Date-based correlation
- Price change calculations
- Impact analysis

### Processing Components
- Stock data organization
- News sentiment linking
- Change rate calculation
- JSON data storage
- Daily trend analysis

## 🔧 Technical Components
### News Analysis System
```python
def get_news_text(self, rate, cur_day_date, prev_day_date):
    sign = "🔺" if rate > 0 else "🔻"
    return {
        'rate': f'{sign}{rate}%',
        'change_date': f'{prev_day_date}/{cur_day_date}',
        'headline': f'{self.heading}',
        'content': f'{self.content}'
    }
```

### Key Features
1. **Stock Analysis**
   - Daily price tracking
   - Percentage change calculation
   - Trading volume analysis
   - Historical data comparison

2. **News Integration**
   - Headline extraction
   - Content analysis
   - Date correlation
   - Impact assessment

3. **Data Processing**
   - API data handling
   - JSON formatting
   - Rate calculations
   - Error management

## 💻 Implementation Details
### Class Structure
- `TeslaNews`: News data fetching and processing
- `TeslaStock`: Stock price analysis and calculations
- API integration management

### Data Management
- Stock price organization
- News article storage
- Change rate tracking
- JSON data structuring

## 🚀 Usage
1. Install required packages:
```bash
pip install requests
```

2. Configure API keys:
```python
NEWSAPI_API_KEY = "your_news_api_key"
ALPHAVANTAGE_API_KEY = "your_alphavantage_key"
```

3. Run the analysis:
```bash
python main.py
```

## 🎯 Analysis Rules
1. Set up environment variables
2. Configure API access
3. Run daily analysis
4. Review generated reports
5. Monitor price impacts

## 🛠️ Project Structure
```
tesla-stock-analysis/
├── stock_market_api.py  # Stock data handling and application initialization
├── news_api.py          # News data processing
├── tesla_stock_prices.json        # Stock data
├── tesla_stock_news.json          # News data
└── what_affected_change_in_stock_price.json
```

## 📊 Features
### Input Processing
- API data validation
- Date range handling
- Price calculations
- News filtering

### Output Management
- JSON data storage
- Change rate tracking
- News correlation
- Impact assessment

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL