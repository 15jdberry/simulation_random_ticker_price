import random
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


class RandomTickerPriceSimulation:
    def __init__(self, ticker, n_days=1):
        """
        Random motion simulation of a stock price over the next n_days with start price = last closing price
        :param ticker: Stock/Crypto Ticker Symbol
        :param n_days: Duration of simulation in days
        """
        self.ticker = str(ticker)
        self.n_days = n_days
        self.start_price = self.get_current_ticker_price(self.ticker)
        self.n_minutes = int(self.n_days * 24 * 60)
        self.range_max = int(10)  # abs value Min and Max ranges price typically varies per minute
        self.new_price_vector = np.zeros(self.n_minutes)
        self.new_price_vector[0] = int(self.start_price)
        self.new_price_vector[0] = self.start_price
        print(f"Simulating {self.ticker} (starting at {self.start_price}) for {self.n_minutes} minutes...")
        self.run_simulation()

    @staticmethod
    def get_current_ticker_price(ticker):
        """
        Get the current price of a stock ticker with the YahooFinance API
        :param ticker: Ticker symbol on stock market
        :return: current price of ticker
        """
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        return round(last_quote, 2)

    def run_simulation(self):
        """Simulate the price change with random motion"""
        for i in range(1, len(self.new_price_vector)):
            rando = random.randint(0, 10)
            if rando > 5:
                self.new_price_vector[i] = self.new_price_vector[i - 1] + self.range_max
            elif rando == 5:
                self.new_price_vector[i] = self.new_price_vector[i - 1]
            elif rando < 5:
                self.new_price_vector[i] = self.new_price_vector[i - 1] - self.range_max
        print(f"The total price change was: {round(self.new_price_vector[-1] - self.start_price, 2)}")

    def draw_graphs(self):
        """Plot results on a graph"""
        n_minutes_vector = np.arange(self.n_minutes)
        fig, ax1 = plt.subplots(num=f"Random Simulation of {self.ticker}")
        ax1.plot(n_minutes_vector, self.new_price_vector, label='New Price')
        ax1.set_xlabel('Time, minutes', color='black')
        ax1.set_ylabel('Price, $', color='black')
        plt.title(f"{self.ticker} Price over {self.n_days} days")
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    # ! Run the simulation here
    rtps = RandomTickerPriceSimulation(ticker="AMZN", n_days=5)
    rtps.draw_graphs()
