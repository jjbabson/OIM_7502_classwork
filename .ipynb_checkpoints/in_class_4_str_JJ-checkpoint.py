import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
import yfinance as yf
sb.set_theme() # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self): #method that downloads data and stores in a DataFrame
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        self.calc_returns(data)
        return data
    
    def calc_returns(self, data): #method that adds change and return columns to data"""
        data['change'] = data['Close'].diff()
        data['instant_return'] = np.log(data['Close']).diff().round(4)

    
    def plot_return_dist(self):         #method that plots instantaneous returns as histogram"""    
        self.data['instant_return'].hist()
        plt.title("Return Distribution")
        plt.show()


    def plot_performance(self): #method that plots stock object performance as percent """
        base = self.data['Close'].iloc[0]
        performance = (self.data['Close'] / base - 1) * 100
        plt.plot(performance)
        plt.title("Stock Performance")
        plt.show()                


def main():
    # uncomment (remove pass) code below to test
    test = Stock(symbol=['AAPL']) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()
    

if __name__ == '__main__':
    main() 