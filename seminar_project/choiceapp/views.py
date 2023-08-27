from datetime import datetime
from functools import wraps

from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def coin(request):
    throw = randint(0, 1)
    throw = 'Решка' if throw else 'Орёл'
    # logger.info(f'Coin throw result - {throw}')
    context = {
        'game': 'бросок монеты',
        'result': 'У вас ' + str(throw)
    }
    return render(request, 'choiceapp/games.html', context)


def cube(request):
    throw = randint(1, 6)
    context = {
        'game': 'бросок кубика',
        'result': 'У вас выпала грань ' + str(throw)
    }
    return render(request, 'choiceapp/games.html', context)


def random(request):
    random_number = randint(0, 100)
    context = {
        'game': 'случайное число',
        'result': 'Вам выпало ' + str(random_number)
    }
    return render(request, 'choiceapp/games.html', context)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('The main page of choice app. Type coin, cube or random')


"""
# def text(title, result):
#     return f'<h1> {title}</h1> ' \
#            f'<p> Результат для вас: {result} </p>'
#
#
# def coin(request):
#     title = 'Бросок монеты'
#     rnd = randint(0, 1)
#     if rnd == 0:
#         result = "Орёл!"
#     else:
#         result = "Решка!"
#     return HttpResponse(text(title, result))


def coin(request):
    rnd = randint(0, 1)
    if rnd == 0:
        logger.info('Coin page accessed. '
                    f'Было сгенерировано значение "орел"')
        return HttpResponse("<h1> Бросок монеты</h1> <p> Вам выпал орёл!")
    logger.info('Coin page accessed. '
                f'Было сгенерировано значение "решка"')
    return HttpResponse("<h1> Бросок монеты</h1> <p> Вам выпала решка!")


def cube(request):
    rnd = randint(1, 6)
    logger.info(f'Cube page accessed. '
                f'Было сгенерировано значение {rnd}')
    return HttpResponse(f"<h1> Бросок кубика</h1> <p> Ваша грань: {rnd}")


def random(request):
    rnd = randint(1, 1000)
    logger.info('Random page accessed. '
                f'Было сгенерировано значение {rnd}')
    return HttpResponse(f"Ваше случайное число от 1 до 1000: {rnd}")
"""
