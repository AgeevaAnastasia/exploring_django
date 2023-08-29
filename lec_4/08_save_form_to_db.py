"""Сохранение формы в базу данных

После того как форма заполнена пользователем, отправлена Django, проверена и
прошла валидацию данные можно использовать. Обычное использование -
сохранение в базу данных.


Модель данных

Начнём с создания модели.Для этого в файле myapp4/models.py пропишем
следующий код:

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, age: {self.age}'


Обратите внимание, что поля модели очень похожи на поля формы. Но тут
используется импорт из models, а не forms. Впрочем, к похожести мы вернёмся в
следующем разделе лекции.


Перед тем как продолжить создадим и применим миграции:

python manage.py makemigrations myapp4
python manage.py migrate

Форма и шаблон у нас есть, можно переходить к представлениям.



Представление

Доработаем представление из начала урока, чтобы оно сохраняло пользователя в
базу данных.

import logging
from django.shortcuts import render
from .forms import UserForm
from .models import User

logger = logging.getLogger(__name__)

...
    def add_user(request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            message = 'Ошибка в данных'
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                age = form.cleaned_data['age']
                logger.info(f'Получили {name=}, {email=}, {age=}.')
                user = User(name=name, email=email, age=age)
                user.save()
                message = 'Пользователь сохранён'
        else:
            form = UserForm()
            message = 'Заполните форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})



Если форма отправлена как POST запрос и проверки данных прошли успешно,
получаем переданные данные и создаём экземпляр класса User. Метод user.save()
сохраняет запись в таблицу БД.



Шаблон

Дополнительно в код представления добавлена переменная message, которая
принимает различные значения в зависимости от этапа обработки данных. Для её
отображения необходимо поправить шаблон user_form.html.

{% extends 'base.html' %}
{% block content %}
<h3>{{ message }}</h3>
<form action="" method="post">
{% csrf_token %}
{{ form.as_div }}
<input type="submit" value="Отправить">
</form>
{% endblock %}



Маршрут

Финальный этап — подключить представление обработчик, тем самым соединив
между собой модель и форму внутри представления.

from django.urls import path
from .views import user_form, many_fields_form, add_user

urlpatterns = [
    ...
    path('user/', add_user, name='add_user'),
]

Для проверки работы перейдём по адресу http://127.0.0.1:8000/les4/user/
"""