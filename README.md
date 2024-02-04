# Overview
The RandomTickerPriceSimulation is a Python script to get the current price of a stock ticker with YahooFinance and run a random simulation for a specified number of days.

# Running the Program
Specify the ticker symbol and duration (in days) you wish to simulate, then call the `draw_graphs` method. Further modify the amount the price can vary per minute by changing the `self.range_max` in the class constructor.

~~~Python
rtps = RandomTickerPriceSimulation(ticker="AMZN", n_days=5)
rtps.draw_graphs()
~~~

# Image
![screenshot](https://github.com/15jdberry/simulation_random_ticker_price/assets/148604533/63befd3d-2c09-4099-974e-ed1d7eaf4a85)


# Dependencies
- [yfinance](https://pypi.org/project/yfinance/)
- [numpy](https://pypi.org/project/numpy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
