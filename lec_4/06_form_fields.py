"""Поля и виджеты форм

Разберемся подробнее в том какие поля мы можем создавать внутри класса формы.
По сути каждое поле — это экземпляр класс <Name>Field из модуля forms, где
<Name> - имя класса поля.


Поля форм

Перечислим некоторые из наиболее популярных классов Field в Django:

● CharField — используется для создания текстовых полей, таких как имя,
фамилия, электронная почта и т.д.
● EmailField — используется для создания поля электронной почты.
● IntegerField — используется для создания поля для ввода целых чисел.
● FloatField — используется для создания поля для ввода чисел с плавающей
точкой.
● BooleanField — используется для создания поля флажка.
● DateField — используется для создания поля даты.
● DateTimeField — используется для создания поля даты и времени.
● FileField — используется для создания поля для загрузки файла.
● ImageField — используется для создания поля для загрузки изображения.
● ChoiceField — используется для создания выпадающего списка с выбором
одного из нескольких вариантов.


Быстрее всего разобраться в различиях полей получится на примере. Создадим
форму для демонстрации разнообразия полей в файле forms.py:

import datetime
from django import forms
...

class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


Мы создали форму на семь различных полей. При этом указали несколько
параметров:

● текстовое поле ограничено 50 символами.
● возраст должен быть не меньше 18
● для поля is_active прописали отсутсвие “галочки” по умолчанию. Обязательно
прописывать для логического поля параметр required
● при вводе дня рождения нам заранее демонстрируется текущая дата
● выбор пола показывается как поле с выбором из двух вариантов. При этом
пользователь видит Male и Female, а в переменную сохраняются M или F.


Для работы с формой надо внести дополнения в код.


Представление

В views.py допишем новое представление

import logging
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm
logger = logging.getLogger(__name__)

...
def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})


Ничего нового мы не добавили. Стандартный вывод пустой формы при GET запросе
и формирование формы с данными при POST запросе с последующей проверкой и
возможной обработкой.


Маршрут

В urls.py допишем новый маршрут

from django.urls import path
from .views import user_form, many_fields_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
]


Теперь по адресу http://127.0.0.1:8000/les4/forms/ мы можем увидеть нашу форму.



Шаблон

Финальный штрих — добавление шаблона many_fields_form.html

{% extends 'base.html' %}
{% block title %}Демонстрация полей формы{% endblock %}
{% block content %}
<form action="" method="post">
{% csrf_token %}
{{ form.as_p }}
<input type="submit" value="Отправить">
</form>
{% endblock %}

В отличии от прошлого шаблона был добавлен вызов метода as_p через точку после
переменной form. Так мы отрисовываем html файл с выводом каждого поля формы
как отдельный абзац.

"""