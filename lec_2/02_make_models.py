"""Создание модели

Для создания модели в Django мы должны перейти в файл models.py внутри
вашего приложения и определить класс Python, который будет наследоваться
от базового класса "models.Model".


Внимание! Если ваш проект состоит из нескольких приложений, создавать
модели нужно в том приложении, которое явно подходит для работы с
создаваемыми данными. В приложении “Пользователь” модель пользователя,
в приложении “Блог” модель статьи и т.д.

Например, вот как можно определить модель для хранения информации о
пользователях:

from django.db import models
class User(models.Model):
name = models.CharField(max_length=100)
email = models.EmailField()
password = models.CharField(max_length=100)
age = models.IntegerField()

Здесь мы создаем класс "User", который наследуется от "models.Model". Мы
определяем несколько полей модели: "name", "email", "password" и "age".
Каждое поле имеет свой тип данных: "CharField" для строк, "EmailField" для
электронных адресов и "IntegerField" для целых чисел.


Поля модели и их типы

Теперь давайте рассмотрим каждое поле более подробно:
● CharField - это поле для хранения строк. Мы указываем максимальную
длину строки с помощью аргумента "max_length".
● EmailField - это поле для хранения электронных адресов. Django
проверяет, что введенный адрес имеет правильный формат.
● IntegerField - это поле для хранения целых чисел.
Кроме того, у каждого поля есть несколько параметров, которые мы можем
использовать для настройки поведения поля. Например, мы можем указать,
что поле "name" обязательно для заполнения, используя параметр
"blank=False".


Наиболее часто используемые поля

На самом деле в Django более трёх полей, которые мы использовали при
создании пользователя. Кратко рассмотрим десяток самых частых полей.

1. CharField - поле для хранения строковых данных. Параметры:
max_length (максимальная длина строки), blank (может ли поле быть
пустым), null (может ли поле содержать значение Null), default (значение
по умолчанию).

2. IntegerField - поле для хранения целочисленных данных. Параметры:
blank, null, default.

3. TextField - поле для хранения текстовых данных большой длины.
Параметры: blank, null, default.

4. BooleanField - поле для хранения логических значений (True/False).
Параметры: blank, null, default.

5. DateField - поле для хранения даты. Параметры: auto_now
(автоматически устанавливать текущую дату при создании объекта),
auto_now_add (автоматически устанавливать текущую дату при
добавлении объекта в базу данных), blank, null, default.

6. DateTimeField - поле для хранения даты и времени. Параметры:
auto_now, auto_now_add, blank, null, default.

7. ForeignKey - поле для связи с другой моделью. Параметры: to (имя
модели, с которой устанавливается связь), on_delete (действие при
удалении связанного объекта), related_name (имя обратной связи).

8. ManyToManyField - поле для связи с другой моделью в отношении
"многие-ко-многим". Параметры: to, related_name.

9. DecimalField - поле для хранения десятичных чисел. Параметры:
max_digits (максимальное количество цифр), decimal_places
(количество знаков после запятой), blank, null, default.

10.EmailField - поле для хранения электронной почты. Параметры:
max_length, blank, null, default.

Далее в рамках лекции и курса мы поработаем с большинством из них на
практике. Полный список всех полей Django доступен по ссылке:
https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types



Несколько примеров моделей

Рассмотрим ещё пару примеров моделей

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


Здесь мы создаем модели для хранения информации о продуктах и заказах. В
модели "Product" мы определяем поля для хранения названия продукта, цены,
описания и изображения. В модели "Order" мы определяем поля для хранения
информации о заказчике, списке продуктов, дате заказа и общей стоимости
заказа. Обратите внимание на использование ForeignKey и ManyToManyField
для определения отношений между таблицами.

● customer = models.ForeignKey(User, on_delete=models.CASCADE) -
каждый заказ делает конкретный пользователь. У одного пользователя
может быть несколько заказов, но заказ числится за одним
пользователем.

● products = models.ManyToManyField(Product) - заказа может содержать
несколько разных продуктов. А продукт может входит в состав
нескольких разных заказов.


Внимание! Для использования в моделях Django поля ImageField необходимо
установить дополнительный модуль Pillow. Выполните команду внутри
виртуального окружения проекта:

pip install Pillow

Данная библиотека нужна для работы Python с изображениями.

В этой части лекции мы рассмотрели, как создавать модели в Django и как
определять поля моделей. Модели представляют собой удобный способ
работы с базами данных в Django, который позволяет создавать, изменять и
удалять записи в базе данных без необходимости написания SQL-запросов."""