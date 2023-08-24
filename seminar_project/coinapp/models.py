from collections import deque

from django.db import models
from datetime import datetime
from random import randint


class Coin(models.Model):
    flip = models.BooleanField()
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        if self.flip == 0:
            res = 'решка!'
        else:
            res = 'орёл!'
        return f'Это {res} Время броска: {self.time}'

    @staticmethod
    def statistics(n: int):
        r = 0
        o = 0
        for _ in range(n):
            coin = Coin(result=randint(0, 1))
            if coin.flip:
                o += 1
            else:
                r += 1

        result_dict = {
            'орёл': o,
            'решка': r
        }
        return result_dict

    # метод с чтением из базы:
    """@staticmethod
    def count_last(n: int) -> dict:
        coins = deque(Coin.objects.all(), maxlen=n)
        result = {'орёл': 0, 'решка': 0}
        for coin in coins:
            if coin.flip:
                result['орёл'] += 1
            else:
                result[''решка] += 1
        return result"""
