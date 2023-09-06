"""Создание суперпользователя

По умолчанию доступ к административной панели имеет только суперпользователь
(superuser). Выполним в командной строке команду:

python manage.py createsuperuser

Далее введём имя пользователя, электронную почту, пароль и повтор пароля

Имя пользователя (leave blank to use 'pk-user'): Admin
Адрес электронной почты: admin@mail.ru
Password:
Password (again):

Введённый пароль слишком похож на имя пользователя.
Введённый пароль слишком короткий. Он должен содержать как
минимум 8 символов.

Введённый пароль слишком широко распространён.

Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.


💡 Внимание! При вводе пароля на экране ничего не отображается. Но Django
учитывает нажатие каждой клавиши.

🔥 Важно! В примере использован пароль admin как пример антипаттерна. Не
используйте короткий, распространённые пароли. Если пароль не
проходит валидацию, придумайте более надёжный.


Таблица пользователя в БД

Если зайти в базу данных, можно найти введённые данные в таблице auth_user. Её
мы создали при выполнении команды migrate в первый раз. Django подготовили
миграции для пользователя заранее. Это 1 из 18 миграций, о которых нам сообщал
Django на первой лекции курса.

Так выглядит наш суперпользователь:

{
"id": 1,
"password":
"pbkdf2_sha256$600000$j7TQ1ugSw6bM24Unk0YAml$yrUbxt8/+7GPip5XahVo
ij7QuL6Z2QTArkWggHft8Sk=",
"last_login": "2023-05-19 15:17:28.471108",
"is_superuser": 1,
"username": "Admin",
"last_name": "",
"email": "admin@mail.ru",
"is_staff": 1,
"is_active": 1,
"date_joined": "2023-05-19 15:12:15.653025",
"first_name": ""
}

Django побеспокоился о безопасности конфиденциальных данных, пароль хранится
в виде хеша.

Кроме логина и пароля в таблице есть поля для имени и фамилии, несколько
флагов, а также фиксация времени регистрации и последней активности.


Сброс пароля

Частая ситуация новичка, забыть свой пароль суперпользователя. В этом случае
можно воспользоваться консольной командой:

python manage.py changepassword <username>

Вместо <username> надо подставить имя пользователя, чей пароль надо изменить.

python manage.py changepassword Admin
Changing password for user 'Admin'
Password:
Password (again):

Отлично! Переходим из консоли в браузер."""