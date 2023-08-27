"""Из URL во view

Снова возвращаемся к представлениям. Следующая строка кода из myapp3/urls.py
в настоящий момент вызывает ошибки импорта:

from .views import year_post, MonthPost, post_detail


Рассмотрим простейшие вьюшки, которые устранят ошибки в нашем приложении.

Представление через функцию возвращает HttpResponse

from django.http import HttpResponse

def year_post(request, year):
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


Это представление будет доступно по адресу http://127.0.0.1:8000/les3/posts/2022/
При этом год может быть любым целым числом.

🔥 Внимание! Если вы указали другой префикс в корневом urls, ваш адрес
будет отличаться.

Представление через класс возвращает HttpResponse

from django.views import View
from django.http import HttpResponse


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


Вторая вьюшка основана на классе. Работает метод аналогично первой функции. Но
в качестве параметров мы получаем и год и месяц. Например можно перейти по
адресу http://127.0.0.1:8000/les3/posts/2022/6/


Представление через функцию возвращает JSON

from django.http import JsonResponse

def post_detail(request, year, month, slug):
    ... # Формируем статьи за год и месяц по идентификатору.
    Пока обойдёмся без запросов к базе данных
    post = {
    "year": year,
    "month": month,
    "slug": slug,
    "title": "Кто быстрее создаёт списки в Python, list() или
    []",
    "content": "В процессе написания очередной программы
    задумался над тем, какой способ создания списков в Python
    работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


В отличии от двух первых представлений, третье возвращает JSON объект.
Очевидное изменение — использование JsonResponse вместо привычного
HttpResponse. Менее очевидное - русский текст. А если быть более точным, текст в
кодировке UTF-8, а не в ASCII. Для этого мы передаём дополнительный параметр
json_dumps_params={'ensure_ascii': False}. Если вы работали с модулем json из
стандартной библиотеки Python, параметр ensure_ascii вам знаком. Он
подтверждает, что JSON будет содержать не только 127 символов из кодировки
ASCII.

Проверить работу представления можно по адресу наподобие
http://127.0.0.1:8000/les3/posts/2022/6/python/
"""