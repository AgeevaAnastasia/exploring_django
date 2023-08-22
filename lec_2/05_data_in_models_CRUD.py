"""Работа с данными в моделях

В Django работа с данными в моделях осуществляется через объекты моделей,
которые представляют отдельные записи в базе данных. Рассмотрим
основные операции с объектами модели.

CRUD - акроним, обозначающий четыре базовые функции, используемые при
работе с базами данных: создание (create), чтение (read), модификация
(update), удаление (delete).


Создание объектов модели, create

Для создания нового объекта модели необходимо создать экземпляр класса
модели и заполнить его поля значениями. Например, чтобы создать нового
пользователя, мы можем использовать следующий код в файле

myapp2/management/commands/create_user.py:

from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
    user = User(name='John', email='john@example.com',
    password='secret', age=25)
    user.save()
    self.stdout.write(f'{user}')

Здесь мы создаем новый объект модели "User" с заданными значениями
полей и сохраняем его в базе данных с помощью метода "save()". Далее
выводим на печать сохранённого пользователя.

Если заглянуть в базу данных, таблица myapp2_user получит новую запись.


Добавляем читаемое представление объекта в модель

После запуска команды

python manage.py create_user

вы увидите строку вида:

User object (1)

Не очень удобно для работы с пользователем. Для повышения читаемости
откроем файл models.py с моделью User и добавим дандер метод __str__.

Получим следующий код:
...
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
    return f'Username: {self.name}, email: {self.email}, age: {self.age}'
...


Запускаем команду повторно и видим:

>python manage.py create_user
Username: John, email: john@example.com, age: 25


Внимание! Если вы проверите содержимое таблицы myapp2_user в базе
данных, обнаружите там несколько одинаковых записей. Отличаться они будут
только порядковым номером в поле id. Каждый запуск команды create_user
создаёт новую запись в БД.

Прежде чем двигаться дальше, можем создать ещё несколько тестовых
пользователей, предварительно изменив их данные в коде:

...
user = User(name='Neo', email='neo@example.com', password='secret',
age=58)
...



Получение объектов модели из базы данных, read

Для получения объектов модели из базы данных можно использовать методы
"all()" и "get()" класса модели. Метод "all()" возвращает все объекты модели, а
метод "get()" возвращает один объект, соответствующий заданным условиям.
Например, чтобы получить всех пользователей из базы данных, мы можем
использовать следующий код в файле

myapp2/management/commands/get_all_users.py:

from django.core.management.base import BaseCommand
from myapp2.models import User
class Command(BaseCommand):
    help = "Get all users."
    def handle(self, *args, **kwargs):
    users = User.objects.all()
    self.stdout.write(f'{users}')


А чтобы получить пользователя по его ID, мы можем использовать следующий
код в файле myapp2/management/commands/get_user.py:

from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Get user by id."
    def add_arguments(self, parser):
    parser.add_argument('id', type=int, help='User ID')
    def handle(self, *args, **kwargs):
    id = kwargs['id']
    user = User.objects.get(id=id)
    self.stdout.write(f'{user}')


Метод add_arguments позволяет парсить командную строку. Мы получаем
значение целого типа и сохраняем его по ключу id. Теперь обработчик handler
может получить к идентификатору доступ через ключ словаря kwargs.

Запустим команду

python manage.py get_user 2

В результате в консоли увидим информацию о нашем пользователе

Username: John, email: john@example.com, age: 25


Отлично работает. Но если капнуть глубже, есть нюанс.

Получение объекта или None

Если мы запустим прошлый пример с несуществующим в БД
идентификатором, получим ошибку:

myapp2.models.User.DoesNotExist: User matching query does not exist.

Исправим наш код:

from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Get user by id."
    def add_arguments(self, parser):
    parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
    pk = kwargs['pk']
    user = User.objects.filter(pk=pk).first()
    self.stdout.write(f'{user}')


Во-первых обратите внимание на замену id на pk. Так команда Django ушла от
конфликта между именем переменной и встроенной в Python функцией id().
pk - primary key, первичный ключ в таблице, т.е. ID.

Также для получения пользователя заменили метод get на filter, а далее к
результату применяем метод first().

● Если в базе несколько записей, вернёт одна, первая из результата
запроса
● Если запись одна, first вернёт эту единственную запись
● Если совпадений не найдено, вместо ошибки вернём None


Рассмотрим работу с filter подробнее

Фильтрация объектов модели

Для фильтрации объектов модели по заданным условиям можно использовать
метод "filter()" класса модели. Метод "filter()" возвращает все объекты модели,
удовлетворяющие заданным условиям.

Например, чтобы получить всех пользователей старше <age> лет, мы можем
использовать следующий код в файле

myapp2/management/commands/get_user_age_greater.py:

from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Get user with age greater <age>."
    def add_arguments(self, parser):
    parser.add_argument('age', type=int, help='User age')
    def handle(self, *args, **kwargs):
    age = kwargs['age']
    user = User.objects.filter(age__gt=age)
    self.stdout.write(f'{user}')


Здесь мы используем оператор "__gt" для сравнения значения поля "age" с
заданным значением.

Помимо оператора __gt существуют множество других. Перечислим
некоторые часто используемые:

● exact - точное совпадение значения поля
● iexact - точное совпадение значения поля без учета регистра
● contains - значение поля содержит заданный подстроку
● icontains - значение поля содержит заданный подстроку без учета
регистра
● in - значение поля находится в заданном списке значений
● gt - значение поля больше заданного значения
● gte - значение поля больше или равно заданному значению
● lt - значение поля меньше заданного значения
● lte - значение поля меньше или равно заданному значению
● startswith - значение поля начинается с заданной подстроки
● istartswith - значение поля начинается с заданной подстроки без учета
регистра
● endswith - значение поля заканчивается на заданную подстроку
● iendswith - значение поля заканчивается на заданную подстроку без
учета регистра
● range - значение поля находится в заданном диапазоне значений
● date - значение поля является датой, соответствующей заданной дате
● year - значение поля является годом, соответствующим заданному году


Как вы догадались, приставка i означает, что поиск будет производиться без
учета регистра символов. Например, iexact найдет записи с точным
совпадением значения поля, но не будет учитывать регистр символов при
поиске.


Важно! Помните про двойное подчеркивание перед оператором. Например
для поиска имён начинающихся с S будет использоваться запись вида:
name__startswith='S'

Более подробно познакомиться с возможностью фильтров для методов filter(),
exclude() и get() можно на официальном сайте

https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups



Изменение объектов модели, update

Для изменения объектов модели можно использовать методы поиска get() или
filter() в сочетании с save() экземпляра класса модели. Например, чтобы
изменить имя пользователя с заданным id, мы можем использовать
следующий код в файле
myapp2/management/commands/update_user.py:

from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Update user name by id."
    def add_arguments(self, parser):
    parser.add_argument('pk', type=int, help='User ID')
    parser.add_argument('name', type=str, help='User name')
    def handle(self, *args, **kwargs):
    pk = kwargs.get('pk')
    name = kwargs.get('name')
    user = User.objects.filter(pk=pk).first()
    user.name = name
    user.save()
    self.stdout.write(f'{user}')


Выполним команду

>python manage.py update_user 2 Smith
Username: Smith, email: john@example.com, age: 25

Здесь мы получаем пользователя с первичным ключом 2, изменяем его имя на
"Smith" и сохраняем изменения в базе данных с помощью метода "save()".



Удаление объектов модели, delete

Для удаления объектов модели можно использовать методы delete()
экземпляра класса модели. Если надо удалить пользователя, мы можем
использовать следующий код в файле

myapp2/management/commands/delete_user.py:

from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Delete user by id."
    def add_arguments(self, parser):
    parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
    pk = kwargs.get('pk')
    user = User.objects.filter(pk=pk).first()
    if user is not None:
    user.delete()
    self.stdout.write(f'{user}')


Здесь мы получаем пользователя по id и удаляем его из базы данных с
помощью метода "delete()".


Внимание! Не стоит злоупотреблять методом delete в проектах. Возможно
данные понадобятся в будущем. Логичнее добавить в модель поле is_deleted =
BooleanField(). В случае “удаления” ставить в поле флаг True
"""