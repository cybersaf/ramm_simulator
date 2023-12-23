import math
import numpy as np

class RAMM:
    def __init__(self, initialPrice, maxPrice, a, b, c, k, stablecoinSupply, goodsSupply):
        self.initialPrice = initialPrice
        self.maxPrice = maxPrice
        self.a = a
        self.b = b
        self.c = c
        self.k = k
        self.stablecoinSupply = stablecoinSupply
        self.goodsSupply = goodsSupply
        self.balance = 10000
        self.tokens_owned = 0

    def get_price(self):
        return self.stablecoinSupply / self.goodsSupply

    def trade_crypto_for_goods(self, crypto_amount):
        new_crypto_supply = self.stablecoinSupply + crypto_amount
        new_goods_supply = self.k / new_crypto_supply
        goods_amount = self.goodsSupply - new_goods_supply
        self.stablecoinSupply = new_crypto_supply
        self.goodsSupply = new_goods_supply
        return goods_amount

    def trade_goods_for_crypto(self, goods_amount):
        new_goods_supply = self.goodsSupply + goods_amount
        new_crypto_supply = self.k / new_goods_supply
        crypto_amount = self.stablecoinSupply - new_crypto_supply
        self.stablecoinSupply = new_crypto_supply
        self.goodsSupply = new_goods_supply
        return crypto_amount

    def sigFormula(self, x):
        return self.a * (np.sqrt(x + self.b) / np.sqrt(self.c + (x + self.b)**2) - 1)

