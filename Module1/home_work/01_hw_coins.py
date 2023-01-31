import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.getrandbits(1)  # random: heads/tails
        return self.side == 0 

quantity_of_coins = int(input())
coin = Coin()
percent = 100

count = sum([1 for i in range(quantity_of_coins) if coin.flip()])
heads = (count/quantity_of_coins) * percent
tails = percent - heads

print(f'Орлов выпало: {heads}%') 
print(f'Решек выпало: {tails}%')
