import math
from scipy.stats import norm

class BlackScholes:
    def __init__(self, spot, strike, rate, time,volatility,multiplier):
        self.spot = spot  # Current stock price
        self.strike = strike  # Option strike price
        self.rate = rate  # Risk-free interest rate
        self.time = time    # Time to maturity in years
        self.volatility = volatility # Volatility of the underlying stock
        self.multiplier = multiplier
    def d1(self):
        return (math.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * math.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * math.sqrt(self.T)

    def call_option_price(self):
        return self.S * norm.cdf(self.d1()) - self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2())

    def put_option_price(self):
        return self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2()) - self.S * norm.cdf(-self.d1())