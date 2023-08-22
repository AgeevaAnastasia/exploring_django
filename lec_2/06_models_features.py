"""Дополнительные возможности моделей

Связи между моделями

Отношения между моделями в Django позволяют описывать связи между
объектами разных моделей. Для этого используются поля моделей, такие как
ForeignKey, ManyToManyField и OneToOneField.

Например, у нас есть модель Post и модель Author, и каждый пост может быть
написан только одним автором, а автор может написать много постов. Для
этого мы можем использовать поле ForeignKey в модели Post, которое будет
ссылаться на модель Author.


Внесём код в models.py учебного приложения:

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


Здесь мы создаем модели Author и Post с полями "name", "email", "title",
"content" и "author". Поле "author" в модели Post является ForeignKey, которое
ссылается на модель Author.


Внимание! Не забываем про миграции после изменения файла models.py

>python manage.py makemigrations
Migrations for 'myapp2':
myapp2\migrations\0002_author_post.py
- Create model Author
- Create model Post
>python manage.py migrate
Operations to perform:
Apply all migrations: admin, auth, contenttypes, myapp2, sessions
Running migrations:
Applying myapp2.0002_author_post... OK



Создание фейковых авторов и статей

Создадим файл myapp2/management/commands/fake_data.py. Он поможет
заполнить базу тестовыми данными.

Внимание! Обычно тестовые данные используются при написании тестов.
Django в этом случае создаёт тестовую базу и не затрагивают основную. Будьте
внимательны, не сломайте базу данных из продакшена фейковыми данными
или случайным удалением данных.

from django.core.management.base import BaseCommand
from myapp2.models import Author, Post

class Command(BaseCommand):
    help = "Generate fake authors and posts."
    def add_arguments(self, parser):
    parser.add_argument('count', type=int, help='User ID')
    def handle(self, *args, **kwargs):
    count = kwargs.get('count')
    for i in range(1, count + 1):
    author = Author(name=f'Name{i}', email=f'mail{i}@mail.ru')
    author.save()
    for j in range(1, count + 1):
    post = Post(title=f'Title{j}', content=f'Text from
    {author.name} #{j} is bla bla bla many long text', author=author)
    post.save()


Запустив команду >python manage.py fake_data 10 получим 10 авторов и 100
статей.
"""