"""Добавление пользовательских моделей в административную панель

До этого момента мы не написали ни одной строчки кода. Да, Django даёт огромный
простор при работе с административной панелью на основе того, что уже есть во
фреймворке. Но можно ли добавлять в админку свои таблицы? Ответа — да!


Создание моделей

Добавим в проект пару моделей как мы это делали начиная с лекции про Модели.
Например Категории и Продукты. Таблица "категории" будет иметь уникальный
идентификатор каждой категории, а таблица "продукты" будет иметь столбец,
который связывает каждый продукт с уникальным идентификатором его категории.
Открываем models.py приложения и пишем код:

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,
    on_delete=models.CASCADE)

    def __str__(self):
        return self.name


Мы специально сделали модели максимально простыми:

● Модель Category содержит только одно поле name, которое является
уникальным строковым идентификатором категории.

● Модель Product содержит два поля: name, которое является строковым
именем продукта, и category, которое является внешним ключом на модель
Category. Внешний ключ определяется с помощью поля ForeignKey, которое
указывает на модель Category и использует on_delete=models.CASCADE,
чтобы обеспечить каскадное удаление, когда категория удаляется.


Создаём и применяем миграции

Убедимся, что приложение добавление в список в settings.py проекта:

INSTALLED_APPS = [
'django.contrib.admin',
...
'myapp5',
]

Далее создадим миграции

>python manage.py makemigrations myapp5

Migrations for 'myapp5':
myapp5\migrations\0001_initial.py
- Create model Category
- Create model Product


И финальный штрих — применение миграций:

>python manage.py migrate

Operations to perform:
Apply all migrations: admin, auth, contenttypes, myapp2,
myapp3, myapp4, myapp5, sessions
Running migrations:
Applying myapp5.0001_initial... OK



Подключение моделей к административной панели

Подключим модели категории и товара к админке приложения. Открываем файл
admin.py приложения. Его создал Django в процессе выполнения команды startapp.
Пропишем внутри следующий код:

from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)


Первая строка импортирует доступ к административным свойствам и методам.
Далее импортируем классы моделей, которые создали ранее.

Две нижние строки регистрируют модели в административной панели сайта.

Запускаем сервер и переходим в админ панель http://127.0.0.1:8000/admin
Теперь мы видим раздел с именем приложения и таблицы категории и продукта с
стандартными кнопками добавить и изменить.


💡 Внимание! Названия таблиц будут на английском языке даже при
включении русской локали в настройках. Для перевода создаваемых
разработчиком данных, в том числе названий моделей и полей необходимо
воспользоваться функцией gettext из django.utils.translation. Материал
перевода выходит за рамки курса. Но вы можете изучить его
самостоятельно по ссылке
https://docs.djangoproject.com/en/4.2/topics/i18n/translation/



Добавление записи без внешнего ключа

Модель категория содержит единственное поле “имя”. Через кнопку добавить мы
можем создать несколько категорий продуктов. Например, мясо, молоко, овощи,
фрукты.


💡 Внимание! При добавлении нескольких записей одной модели удобнее
пользоваться кнопкой “Сохранить и добавить другой объект”.



Добавление записи с внешним ключом

Модель продукт содержит помимо имени ссылку - внешний ключ на модель
категория. Админка Django автоматически добавляет поле выбора для создания
связи между продуктом и его категорией.

Например мы можем добавить колбасу и выбрать ей категорию мясо. А далее
добавить сыр, сметану и творог и выбрать им категорию молоко.

При этом кнопка “плюс” рядом с категорией позволяет при редактировании
продуктов, создавать новые категории. Добавим торт и создадим ему категорию
десерты. В отдельно открывшемся окне прописываем категорию “десерты”,
нажимаем сохранить.Категория автоматически подставляется для продукта “торт”.


Подключение моделей из разных приложений

Вернёмся к коду лекции 3. Если вы создавали для каждого занятия свой проект, в
файле models.py из каталога myapp3 у вас будет хранится модель автора и статьи.
Подключим их к админке через admin.py приложения myapp3.

from django.contrib import admin
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)


Теперь админ панель добавила раздел myapp3 с возможностью изменять записи
авторов и постов.

Обратите внимание, что при выводе списка записей Django используйте дандер
__str__ модели. Например у автора прописано:

...
def __str__(self):
return f'Name: {self.name}, email: {self.email}'

В результате перейдя по аресу http://127.0.0.1:8000/admin/myapp3/author/ мы
видим строки:

● Name: Author_1, email: mail1@mail.ru
● Name: Author_2, email: mail2@mail.ru
● …

Как изменить представление по умолчанию узнаем через несколько абзацев
"""