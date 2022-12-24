import numpy as np
import pandas as pd
import datetime as dt
from scipy.stats import norm
import yfinance as yf 
from ta.volatility import average_true_range as ATR

class blackScholesCalculator():

    """
        https://www.macroption.com/black-scholes-formula/
        
        s = underlying price ($$$ per share)
        k = strike price ($$$ per share)
        sigma = volatility (% p.a.)
        r = continuously compounded risk-free interest rate (% p.a.)
        q = continuously compounded dividend yield (% p.a.)
        t = time to expiration (% of year)

    """

    def __init__(self, k, sigma = None, r = 0.03, q = 0, ticker = None, ref_date = None) -> None:
        
        self.ticker = ticker
        self.ref_date = ref_date
        self.k = k
        self.r = r
        self.q = q
        self.w = 20

        if sigma is None and ticker is not None:
            self.sigma = self.volatility()
        elif sigma is not None:
            self.sigma = sigma
        else:
            self.sigma = 0.20


    

    def callPrice(self, s, t):

        e = np.exp
        t = t/365
        d1 = (np.log(s/self.k) + t*(self.r - self.q + (self.sigma**2/2)))/(self.sigma*np.sqrt(t))
        d2 = d1 - self.sigma*np.sqrt(t)
        c = (s*e(-self.q*t)*self.N(d1)) - (self.k*e(-self.r*t)*self.N(d2)) 

        return c
    
    def putPrice(self, s, t):
        e = np.exp
        t = t/365
        d1 = (np.log(s/self.k) + t*(self.r - self.q + (self.sigma**2/2)))/(self.sigma*np.sqrt(t))
        d2 = d1 - self.sigma*np.sqrt(t)
        p = (self.k*e(-self.r*t)*self.N(-d2)) - (s*e(-self.q*t)*self.N(-d1))

        return p

    def N(self, d):

        return norm.cdf(d)
    
    def volatility(self):

        sym = yf.Ticker(self.ticker)
        history = sym.history(period = 'max')
        history.sort_index(inplace=True)
        history["Date"] = pd.to_datetime(history.index.tz_localize(None))

        if self.ref_date is not  None:
            history = history.loc[history["Date"] <= pd.to_datetime(self.ref_date), ]

        atr = ATR(high = history.High, low = history.Low, close = history.Close, window = self.w)

        return ((0.50 * atr[-1]) * (np.sqrt(365)))/history.Close[-1]