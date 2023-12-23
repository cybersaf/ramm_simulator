class liquidityPool():
    def __init__(self, goodsSupply,cryptoSupply,k):
        self.goodsSupply = goodsSupply
        self.cryptoSupply = cryptoSupply
        self.k = k

    def get_price(self):
        return self.cryptoSupply / self.goodsSupply

    def trade_crypto_for_goods(self, crypto_amount):
        new_crypto_supply = self.crypto_supply + crypto_amount
        new_goods_supply = self.k / new_crypto_supply
        goods_amount = self.goods_supply - new_goods_supply
        self.cryptoSupply = new_crypto_supply
        self.goodsSupply = new_goods_supply
        return goods_amount

    def trade_goods_for_crypto(self, goods_amount):
        new_goods_supply = self.goods_supply + goods_amount
        new_crypto_supply = self.k / new_goods_supply
        crypto_amount = self.crypto_supply - new_crypto_supply
        self.crypto_supply = new_crypto_supply
        self.goods_supply = new_goods_supply
        return crypto_amount
    
