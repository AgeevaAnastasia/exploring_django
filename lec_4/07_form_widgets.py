"""Виджеты форм

В Django для работы с формами используются виджеты, которые определяют
внешний вид и поведение полей формы на странице. В Django предусмотрены
встроенные виджеты, такие как TextInput, Select, CheckboxInput и др., которые
можно использовать для создания различных типов полей формы.


Вот некоторые из наиболее популярных классов виджетов в Django:

● TextInput — используется для создания текстового поля ввода.
● EmailInput — используется для создания поля ввода электронной почты.
● PasswordInput — используется для создания поля ввода пароля.
● NumberInput — используется для создания поля ввода чисел.
● CheckboxInput — используется для создания флажка.
● DateInput — используется для создания поля ввода даты.
● DateTimeInput — используется для создания поля ввода даты и времени.
● FileInput — используется для создания поля загрузки файла.
● Select — используется для создания выпадающего списка с выбором одного
из нескольких вариантов.
● RadioSelect — используется для создания списка радиокнопок.
● Textarea — используется для создания многострочного текстового поля ввода.


Доработаем пример формы из прошлого раздела, Создадим форму аналогичную
ManyFieldsForm, но добавим в неё виджеты.

import datetime
from django import forms

...
class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))



💡 Внимание! Можно не создавать новые представления, маршруты и
шаблон. Достаточно добавить строку импорта класса формы в views.py и
заменить старую форму на новую в представлении.

В каждом виджете задан атрибут class со значениями form-control, form-check-input,
что позволяет использовать стили Bootstrap для оформления полей формы. Атрибут
placeholder, который определяет текст-подсказку, отображаемый в поле формы до
того, как пользователь введет данные.

Для выбора пола использовали виджет RadioSelect, теперь вместо
раскрывающегося списка у нас перечень значений с возможностью выбрать одно
из них.

Кроме того было добавлено поле message. Это такое же текстовое поле как и name.
Но в качестве виджета был выбран Textarea, теперь текст сообщения можно
вводить в несколько строк.



Ручное изменение типа поля

В большинстве случаев поле формы автоматически используют нужный виджет для
отрисовки html элемента. Если возникают ситуации, когда отрисовку нужно
изменить, используются виджеты. Они позволяют заменить один вид на другой,
например обычное поле ввода на текстовую зону (textarea). Но бывают ситуации,
когда подобного недостаточно. Например в нашем примере даты приходится
вводить вручную. Большинство браузеров могут облегчить задачу. Изменим поле с
днём рождения на следующую строку:

...
birthdate = forms.DateField(initial=datetime.date.today,
widget=forms.DateInput(attrs={'class': 'form-control', 'type':
'date'}))
...

Мы вручную поменяли тип поля на “дата”. Теперь браузер рисует кнопку календаря,
дату можно выбирать, а не вводить.


Обработка данных форм

Если мы воспользуемся формой из примера выше и попробуем ввести неверные
данные, Django автоматически сообщит об этом. Встроенные фильтры не дадут
пройти проверку правильности, метод form.is_valid() вернёт ложь. Однако
встроенных проверок может быть недостаточно.
"""