"""Миграции

В Django миграции представляют собой автоматически сгенерированные
скрипты для изменения структуры базы данных в соответствии с
изменениями в моделях приложения. Миграции позволяют легко и безопасно
изменять базу данных, не теряя данные.



Как создать миграции для моделей

Для создания миграций для моделей Django используется команда
"makemigrations". Например, чтобы создать миграции для модели "User", мы
должны выполнить следующую команду:

python manage.py makemigrations myapp2

Здесь "myapp2" - это имя нашего приложения, в котором определена модель
"User". Команда "makemigrations" анализирует все изменения в моделях
приложения и создает миграционный файл, который содержит инструкции
для изменения базы данных.


Внимание! Если опустить имя приложения, команда python manage.py
makemigrations попытается найти изменения во всех приложениях проекта и
создать миграции для каждого из них.


Важно! Перед запуском команды убедитесь, что ваше приложение добавлено
в список INSTALLED_APPS файла settings.py вашего проекта:

INSTALLED_APPS = [
...
"myapp2",
...
]
Если заглянуть в каталог /migrations вашего приложения, увидите новый файл
вида 0001_initial.py. Содержимое файла сгенерировано автоматически и
практически никогда не требует ручных правок.


Превращение модели пользователя в миграцию


В файле models.py мы создали следующую модель пользователя:

class User(models.Model):
name = models.CharField(max_length=100)
email = models.EmailField()
password = models.CharField(max_length=100)
age = models.IntegerField()


После миграции она превратилась в следующий набор кода:

migrations.CreateModel(
name='User',
fields=[
('id', models.BigAutoField(auto_created=True,
primary_key=True, serialize=False, verbose_name='ID')),
('name', models.CharField(max_length=100)),
('email', models.EmailField(max_length=254)),
('password', models.CharField(max_length=100)),
('age', models.IntegerField()),
],
),

В базу данных автоматически будет добавлено поле id как первичный ключ.
Также для почты автоматически введено ограничение на длину поля. Django
делает часть преобразований самостоятельно, там где они подразумеваются.
Внимание! Создание миграций не изменяет таблицы базы данных. Это лишь
подготовка к изменениям.



Применение миграций

Вспомните запуск сервера

>python manage.py runserver
...

You have 19 unapplied migration(s). Your project may not work properly
until you apply the migrations for app(s): admin, auth, contenttypes,
myapp2, sessions.

Run 'python manage.py migrate' to apply them.

Теперь Django указывает на 19 неприменённых миграций, вместо 18 ранее. В
список добавилось приложение myapp2 после команды makemigrations.
После создания миграционного файла мы должны применить его к базе
данных с помощью команды "migrate":

python manage.py migrate

Команда "migrate" выполняет все накопленные миграции в порядке их
создания и применяет изменения к базе данных. В первый раз получим нечто
подобное:

>python manage.py migrate

Operations to perform:
Apply all migrations: admin, auth, contenttypes, myapp2, sessions
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying admin.0003_logentry_add_action_flag_choices... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying auth.0009_alter_user_last_name_max_length... OK
Applying auth.0010_alter_group_name_max_length... OK
Applying auth.0011_update_proxy_permissions... OK
Applying auth.0012_alter_user_first_name_max_length... OK
Applying myapp2.0001_initial... OK
Applying sessions.0001_initial... OK


База данных при этом наполнится таблицами, включая пользователя, которого
мы создали ранее. А если вы оставили модели товары и заказы при создании
миграций, эти таблицы также будут созданы в БД


Важно отметить, что при каждом изменении модели необходимо создать
новые миграции для этих изменений. Затем применить их к базе данных,
мигрировать в базу. Это позволяет обновлять базу данных без потери данных
и сохранять целостность базы данных.
"""