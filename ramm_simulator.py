import math
import matplotlib.pyplot as plt
from datetime import datetime
import time

class Transaction:
    def __init__(self,price):
        self.price = price
        self.time = datetime.now()

class Pool:
    def __init__(self,id,initial_qty,mode_qty,initial_price,max_price,c):
        self.primary = True
        self.id = id
        self.initial_max_price_midpoint = (max_price-initial_price) / 2
        self.b = initial_qty / 2
        self.c = c
        
        self.tokens_sold = 0
        self.transaction_history = []
                
        self.max_price = max_price
        self.initial_qty = initial_qty
        self.initial_price = initial_price
        self.usdc_received = 0

        self.mode_qty = mode_qty
    def generate_curve(self):
        x = range(0,self.initial_qty)
        y = [self.calc_y(xi) for xi in x]
        plt.plot(x, y)
        plt.xlabel('Token Price')
        plt.ylabel('Token Supply')
        plt.title(f'Bonding Curve for {self.id}')
        plt.show()
    
    def price_at(self,x):
        return self.calc_y(x)
    
    def calc_y(self,x):
        y = self.initial_max_price_midpoint * (((x-self.b)/math.sqrt(self.c+((x-self.b)**2))) + 1) + self.initial_price
        return y
    
    def buy(self):
        price = self.price_at(self.tokens_sold+1)
        self.transaction_history.append(Transaction(price))
        self.usdc_received += price
        self.tokens_sold += 1
        return price
    
    
    def show_stats(self):
        print(f'Tokens sold: {self.tokens_sold}')
        print(f'USDC Received: {self.usdc_received}')
        print(f'Transaction Count: {len(self.transaction_history)}')
        print(f'Next Price: {self.calc_y(self.tokens_sold+1)}')
   