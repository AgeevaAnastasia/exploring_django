"""Что такое административная панель в Django?

Django — это один из наиболее популярных фреймворков для создания
веб-приложений на Python. Он предоставляет множество инструментов и
функциональных возможностей, которые значительно упрощают процесс
разработки.
Одним из таких инструментов является административная панель.

Административная панель в Django — это готовый интерфейс, который позволяет
управлять данными вашего приложения. Она предоставляет возможность
создавать, редактировать и удалять записи в базе данных, а также осуществлять
множество других действий, связанных с управлением приложением.
Среди разработчиков административную панель часто называют коротким словом
“админка”. Этот же термин используют и те, кто не создаёт административные
панели, но пользуется ими — пользователи с доступом к админке.


Зачем нужна административная панель?

Во-первых, она значительно упрощает работу разработчиков, позволяя им быстро и
удобно управлять данными.

Во-вторых, административная панель может быть использована в качестве
удобного инструмента для администрирования приложения, что позволяет
упростить жизнь не только разработчикам, но и другим пользователям приложения.

В этой лекции мы рассмотрим основы работы с административной панелью в
Django, настроим ее и создадим пользовательские модели. Также мы рассмотрим
примеры использования административной панели и обсудим основные моменты
ее работы.


Вместо старта
Если вы создавали новое приложение для каждого занятия, выполните команды:

>cd myproject
>python manage.py startapp myapp5

Отлично! Новое приложение создано в проекте. Сразу подключим его в настройках
setting.py
INSTALLED_APPS = [
'django.contrib.admin',
...
'myapp5',
]

Всё готово к началу изучения админки на практике.


Настройка административной панели

Перед тем как начать работать с административной панелью впервые, необходимо
сделать несколько обязательных действий. Далее в админку можно будет просто
заходить для внесения правок в данные приложения.


Первоначальная настройка

Адрес по которому мы можем зайти в админ панель был настроен при создании
проекта (начало лекции 1). Заглянем в urls.py проекта, уюедимся что часть работы
Django сделал за нас.

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
...
]

● импортирован модуль admin из django.contrib
● в urlpatterns добавлена строка, которая будет указывать на адрес
административной панели

Стартуем сервер и переходим по адресу административной панели:
http://127.0.0.1:8000/admin

Мы автоматически попадаем на форму ввода логина и пароля. Но какие бы данные
мы не ввели, доступ будет закрыт.


Настройка языка

А почему мы изучаем курс на русском языке, а Django общается с нами на
английском? В фреймворке есть возможность использовать не только английский,
но и другие популярные языки. Откроем файл settings.py и изменим языковую
константу с английского на русский:

LANGUAGE_CODE = 'ru-ru'

Перезагружаем сервер. Теперь при попытке зайти в админ даже предупреждение
мы видим на русском:

Пожалуйста, введите корректные имя пользователя и пароль учётной записи. Оба
поля могут быть чувствительны к регистру.

Но смена языка не помогла на попасть в админку.

💡 Внимание! Вы можете оставить язык по умолчанию или указать тот,
который вам удобен. На код в рамках курса это не повлияет. Только на
стандартный текст.
"""