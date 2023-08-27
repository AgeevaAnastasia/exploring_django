"""Объединяем модели, представления, шаблоны и маршруты


В финале соединим полученные на этой и прошлых лекциях знания в едином
приложении. У нас будет база данных с авторами и постами (создавали на занятии
про модели). Пользователь сможет вводить в адресной строке id автора и получать
информацию о его пяти последних статьях. Также можно получить полный текст
статьи по её id. URL маршруты вызывают соответствующие представлений, которые
в свою очередь обращаются через модель к базе данных и передают её через
контекст в шаблоны.


Модели

Создание моделей

В файл models.py перенесём ранее созданый код:

from django.db import models
class Author(models.Model):
name = models.CharField(max_length=100)
email = models.EmailField()
def __str__(self):
return f'Name: {self.name}, email: {self.email}'
class Post(models.Model):
title = models.CharField(max_length=100)
content = models.TextField()
author = models.ForeignKey(Author, on_delete=models.CASCADE)
def __str__(self):
return f'Title is {self.title}'
def get_summary(self):
words = self.content.split()
return f'{" ".join(words[:12])}...'


Автор имеет имя и почту. Статья состоит из заголовка и содержимого. При этом
каждая статья имеет одного автора, а автор может писать множество статей.


Миграции

Создадим миграции:

python manage.py makemigrations myapp3

Сразу применением их к базе данных:

python manage.py migrate


Наполнение фейковыми данными

Чтобы было что выводить, заполним таблицы фейковыми данными. Для этого
создадим файл myapp3/management/commands/fill_db.py:

from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post
LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing
elit. " \
"Accusamus accusantium aut beatae consequatur
consequuntur cumque, delectus et illo iste maxime " \
21
"nihil non nostrum odio officia, perferendis placeat
quasi quibusdam quisquam quod sunt " \
"tempore temporibus ut voluptatum? A aliquam culpa
ducimus, eaque eum illo mollitia nemo " \
"tempore unde vero! Blanditiis deleniti ex hic,
laboriosam maiores odit officia praesentium " \
"quae quisquam ratione, reiciendis, veniam. Accusantium
assumenda consectetur consequatur " \
"consequuntur corporis dignissimos ducimus eius est eum
expedita illo in, inventore " \
"ipsum iusto maiores minus mollitia necessitatibus neque
nisi optio quasi quo quod, " \
"quos rem repellendus temporibus totam unde vel velit
vero vitae voluptates."
class Command(BaseCommand):
help = "Generate fake authors and posts."
def add_arguments(self, parser):
parser.add_argument('count', type=int, help='User ID')
def handle(self, *args, **kwargs):
text = LOREM.split()
count = kwargs.get('count')
for i in range(1, count + 1):
author = Author(name=f'Author_{i}',
email=f'mail{i}@mail.ru')
author.save()
for j in range(1, count + 1):
post = Post(
title=f'Title-{j}',
content=" ".join(choices(text, k=64)),
author=author
)
post.save()


Для заполнения базы семью авторами необходимо выполнить команду
python manage.py fill_db 7

Отлично! Модели созданы, таблицы в БД существуют и заполнены данными.


Представления

Представление автора

Создадим “вьюшку” для получения 5 последних статей автора:

from django.shortcuts import render, get_object_or_404
from .models import Author, Post
def author_posts(request, author_id):
author = get_object_or_404(Author, pk=author_id)
posts =
Post.objects.filter(author=author).order_by('-id')[:5]
return render(request, 'myapp3/author_posts.html', {'author':
author, 'posts': posts})

Новая функция get_object_or_404 работает аналогично get, т.е. делает select запрос
к базе данных. Но если запрос не вернёт строку из таблицы БД, представление
отрисует страницу с ошибкой 404.

Также обратите внимание на метод order_by('-id'). После фильтрации статей по
автору, мы сортируем их на основе id по убыванию. Об этом говорит знак минус
перед именем. Далее питоновский срез формирует список из пяти статей с
максимальными идентификаторами.

Словарь с контекстом в виде автора и списка статей пробрасываются в шаблон
myapp3/author_posts.html.


Представление статьи

Второе представление должно возвращать шаблон с полным текстом статьи:
def post_full(request, post_id):
post = get_object_or_404(Post, pk=post_id)
return render(request, 'myapp3/post_full.html', {'post':
post})

Сделав select запрос к таблице с постами мы передаём в шаблон
myapp3/post_full.html контекст в виде одной статьи.




Маршруты

Сразу пропишем маршруты для вновь созданных представлений в файле urls.py:

from django.urls import path
...
from .views import author_posts, post_full
urlpatterns = [
...
path('author/<int:author_id>/', author_posts, name='author_posts'),
path('post/<int:post_id>/', post_full, name='post_full'),
]

Мы создаем два URL-адреса - для представлений author_posts и post_full. В обоих
случаях мы используем целочисленный параметр в URL для передачи id автора и
поста соответственно. Мы также добавляем имена для каждого URL-адреса, чтобы
мы могли ссылаться на них в шаблонах с помощью тега url. О теге url вы узнаете
через несколько абзацев.



Шаблоны

Базовый шаблон

Начнём с простейшего базового шаблона. При желании добавить шапку и подвал в
будущем, правки нужно делать только в нём. Создадим base.html:

<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>{% block title %}Блог{% endblock %}</title>
</head>
<body>
{% block content %}
Контент скоро появится...
{% endblock %}
</body>
</html>


🔥 Внимание! Расположите базовый шаблон в каталоге templates проекта.
Дочерние шаблоны сохраняйте в каталоге templates/myapp3/ приложения.


Шаблон с последними статьями автора

Теперь подключим его в дочернем шаблоне author_posts.html для вывода 5
последних статей автора:

{% extends 'base.html' %}
{% block title %}{{ author.name }}'s Posts{% endblock %}
{% block content %}
<h2>Последние 5 статей автора: {{ author.name }}</h2>
<table>
{% for post in posts %}
<tr>
<td><a href="{% url 'post_full' post.id %}">{{
post.title }}</a>
<td>{{ post.get_summary }}</td>
</tr>
{% endfor %}
</table>
{% endblock %}


Внутри шаблона мы обращаемся к переменным author и post как к экземплярам
класса. Для получения имени автора используем точечную нотацию author.name,
т.к. это свойство прописано в моделе автора. Аналогично получаем заголовок
статьи.

Кроме того в моделе Post есть метод get_summary. Он возвращает 12 первых слов
из содержимого статьи. Используя {{ post.get_summary }} шаблон через контекст
вызывает метод модели.

Отдельного внимания заслуживает тег url. После него в кавычках мы указываем имя
представления, которое хотим вызвать. Внимательно посмотрите на строку из
urls.py

path('post/<int:post_id>/', post_full, name='post_full'),
Мы можем обращаться к post_full по имени, потому что прописали ключевой
аргумент name в функции path.

Передача значения post.id позволяет задать значение параметра post_id внутри
представления post_full.


Шаблон статьи

Финальный штрих — шаблон для вывода полного текста статьи.

{% extends 'base.html' %}
{% block title %}{{ post.title }}{% endblock %}
{% block content %}
<h3>{{ post.title }}</h3>
<p>{{ post.content }}</p>
{% endblock %}

В шаблоне мы также переопределили блок title и добавили содержимое в блок
content. Выводим заголовок и полный текст поста.
"""