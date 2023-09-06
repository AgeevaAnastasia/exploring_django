"""Персонализация моделей в админ панели


Не всегда таблицы базы данных бывают небольшими. Они могут состоять из
десятков, а иногда и сотен столбцов.


Изменение модели

Например продукт может иметь не только имя и категорию. Вполне возможна
следующая структура:

● Название продукта
● Описание продукта
● Цена продукта
● Категория продукта
● Количество на складе
● Дата добавления продукта
● Рейтинг продукта

Внесём изменения в модель Продукт нашего приложения myapp5, файл models.py:

from django.db import models
...

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


Теперь класс Product имеет следующие поля:

● name — строка (CharField) длиной не более 50 символов, обязательное поле,
содержащее название товара.
● category — внешний ключ (ForeignKey) на модель Category с параметром
on_delete=models.CASCADE, обязательное поле, содержащее категорию
товара.
● description —- текстовое поле (TextField) с параметром default='', то есть
значение поля по умолчанию пустая строка, и параметром blank=True, то есть
поле может быть пустым.
● price — числовое поле с плавающей запятой (DecimalField) с параметрами
default=999999.99 (значение поля по умолчанию), max_digits=8
(максимальное число цифр в числе) и decimal_places=2 (количество цифр
после запятой), обязательное поле, содержащее цену товара.
● quantity — положительное целочисленное поле (PositiveSmallIntegerField) с
параметром default=0 (значение поля по умолчанию), содержащее
количество товара. Для поля PositiveSmallIntegerField допускается диапазон
чисел от 0 до 32767 включительно.
● date_added — поле даты и времени (DateTimeField) с параметром
auto_now_add=True, то есть при создании объекта будет автоматически
заполнено текущей датой и временем.
● rating — числовое поле с плавающей запятой (DecimalField) с параметрами
default=5.0 (значение поля по умолчанию), max_digits=3 (максимальное число
цифр в числе) и decimal_places=2 (количество цифр после запятой),
содержащее рейтинг товара.


Мы уже добавили несколько записей в таблицу продуктов. Для вновь созданных
полей обязательно прописать значения по умолчанию, default. Они будут
применены к существующим в базе данных записям.


Создаём миграции

Параметр default добавлен для всех новых полей кроме date_added. При создании
миграций Django предложит нам выбор:

1) самостоятельно добавить значение по умолчанию для существующих строк
2) прервать создание миграций и прописать default параметр в модели

Мы выбираем первый вариант и соглашаемся с timezone.now как датой добавления
существующих записей.

>py manage.py makemigrations myapp5
It is impossible to add the field 'date_added' with
'auto_now_add=True' to product without providing a default. This
is because the database needs something to populate existing
rows.
1) Provide a one-off default now which will be set on all
existing rows
2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
Accept the default 'timezone.now' by pressing 'Enter' or provide
another value.
The datetime and django.utils.timezone modules are available, so
it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt

[default: timezone.now] >>>
Migrations for 'myapp5':
myapp5\migrations\0002_product_date_added_product_description_pro
duct_price_and_more.py
- Add field date_added to product
- Add field description to product
- Add field price to product
- Add field quantity to product
- Add field rating to product


Применяем миграции

>python manage.py migrate

Operations to perform:
Apply all migrations: admin, auth, contenttypes, myapp2,
myapp3, myapp4, myapp5, sessions
Running migrations:
Applying
myapp5.0002_product_date_added_product_description_product_price_
and_more... OK



Изменения в базе данных зафиксированы. Можно стартовать сервер и проверять
админку http://127.0.0.1:8000/admin


Правим существующие продукты и добавляем новые

Перейдём в админку http://127.0.0.1:8000/admin/myapp5/product/ и отредактируем
уже существующие продукты. Заодно добавим несколько новых.

В зависимости от типа поля в модели, админка создаёт соответствующие поля:
● для строкового имени поле ввода имеет обычный тип type="text".
● для ForeignKey поле выбора select.
● для TextField описание поле ввода текста textarea.
● для цены, количества и рейтинга поля ввода с type="number".
● поле date_added не отображается в админке. Параметр auto_now_add=True
автоматически заполняет поле.

При этом админка следит за валидацией данных. Например попытаемся ввести
данные, выходящие за обозначенные в моделе рамки
http://127.0.0.1:8000/admin/myapp5/product/5/change/ Мы получим
предупреждения


Изменим существующие продукты, чтобы они прошли валидацию. Например так
id  name    category_id date_added                  description             price   quantity    rating

1   колбаса 1           2023-05-20 08:58:26.184100  Много мяса, мало бумаги 1699,5  325         7.77
2   сыр     2           2023-05-20 08:58:26.184100  Сыр из молока           999.97  50          9.7
3   сметана 2           2023-05-20 08:58:26.184100  Вкуснейший творог       250,01  800         7.9
4   творог  2           2023-05-20 08:58:26.184100  Вкусный творог          150,99  125         8.5
5   торт    5           2023-05-20 08:58:26.184100  Просто торт             753,77  4           7.02
6   бисквит 5           2023-05-20 09:22:10.261009  Как торт, но вкуснее    425.25  70          6.95

"""