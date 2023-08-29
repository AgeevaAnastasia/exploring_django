"""Создание форм

В Django для создания форм используются классы, которые наследуются от класса
forms.Form.


Создаём класс формы

Рассмотрим пример определения формы для ввода данных о пользователе. Для
этого создадим файл forms.py в приложении:

from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

В данном примере создается класс UserForm, который наследуется от класса
forms.Form. В классе определены три поля формы: name, email и age. Каждое поле
представлено отдельным классом, который определяет тип поля и его атрибуты.

● Поле name определено с помощью класса CharField, который представляет
текстовое поле. Аргумент max_length указывает максимальную длину текста,
которую можно ввести в поле.
● Поле email определено с помощью класса EmailField, который представляет
поле для ввода email-адреса. Этот класс автоматически проверяет
введенный адрес на корректность.
● Поле age определено с помощью класса IntegerField, который представляет
числовое поле. Аргументы min_value и max_value указывают минимальное и
максимальное значение, которое можно ввести в поле.
"""