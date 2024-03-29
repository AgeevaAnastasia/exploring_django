"""Создание первого проекта

В Django различаются термины проект и приложение. Проект представляет из
себя пакет Python с базовыми настройками. Приложение также является
пакетом. Но он входит в состав проекта. При этом каждый проект может
состоять из нескольких приложений. А приложения можно переносить из
одного проекта в другой.


Создание проекта

Для создания нового проекта в Django необходимо выполнить команду

django-admin startproject <project_name>.

Эта команда создаст структуру проекта, которая будет содержать все
необходимые файлы и папки для работы с фреймворком.

Внимание! Убедитесь что вы находитесь в нужном каталоге и виртуальное
окружение с установленным фреймворком активно.

Пример:

django-admin startproject myproject

В результате выполнения команды будет создана структура вашего проекта.


Обзор структуры проекта

Структура проекта Django имеет следующий вид:
myproject/
 manage.py
 myproject/
 __init__.py
 settings.py
 urls.py
 asgi.py
 wsgi.py


Рассмотрим каждый из созданных файлов.

● manage.py - файл, который используется для управления проектом. С его
помощью можно запустить сервер, создать миграции, создать
суперпользователя и т.д.

● myproject/ - директория, которая содержит основные файлы проекта.

● __init__.py - файл, который сообщает Python, что директория myproject
является пакетом.

● settings.py - файл, который содержит настройки проекта, такие как базы
данных, шаблоны, статические файлы и т.д.

● urls.py - файл, который содержит маршруты приложения.

● asgi.py - файл, который используется для запуска проекта в ASGIсовместимых серверах.

● wsgi.py - файл, который используется для запуска проекта в WSGIсовместимых серверах.


Далее мы будем вносить изменения в некоторые из файлов проекта. Но уже в
текущем виде он готов к запуску.


Запуск сервера и проверка работоспособности

Для запуска сервера необходимо выполнить команду

python manage.py runserver.

Эта команда запустит сервер на локальном хосте и порту 8000.


Внимание! Команда должна выполняться из каталога, который содержит файл
manage.py. Не забудьте перейти в него командой cd <имя проекта>

Пример:

python manage.py runserver

Первый запуск вернёт примерно следующую информацию в консоль:

Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
You have 18 unapplied migration(s). Your project may not work properly
until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 29, 2023 - 10:34:32
Django version 4.2.1, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

После запуска сервера можно открыть браузер и перейти по адресу
http://localhost:8000/. Если все настроено правильно, то вы увидите страницу
"The install worked successfully! Congratulations!" с ракетой.


Особенности встроенного сервера

Сервер Django используется лишь при разработке и тестировании проекта. Он
способен раздавать статику в виде изображений, CSS файлов, JavaScript кода и
т.п. Так же сервер отслеживает изменения, которые вы вносите в файлы
проекта. После каждого такого изменения сервер автоматически
перезагружается.

Важно! Встроенный сервер нельзя использовать в продакшене. Он подходит
только для разработки проекта.

В процессе работы над проектом мы будем использовать режим отладки. В
файле настроек settings.py есть пара строко кода:

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

Как вы догадались, отладка помогает нам в создании проекта, но должна быть
отключена перед запуском в продакшен.

Предупреждение о непринятых миграциях

Первый запуск сервера выводит предупреждение о том, что в проекте есть
непринятые миграции.

You have 18 unapplied migration(s). Your project may not work properly
until you apply the migrations for app(s): admin, auth, contenttypes,
sessions.

Не стоит переживать за него. Проект будет нормально работать без миграций.
Они понадобятся позже, когда начнётся работа с базой данных, создание
моделей.


Пара дополнительных параметров runserver

При запуске сервера можно явно заменить порт 8000 на другой. Например так
мы воспользуемся портом 8080

python manage.py runserver 8080

Кроме того можно изменить IP-адрес сервера. Для этого он передаётся вместе с
портом

python manage.py runserver 0.0.0.0:8080

Указав в качестве IP нули мы стали прослушивать все адреса. Если ваш
компьютер находится в локальной сети, доступ к проекту можно получить с
других устройств этой же сети. Достаточно указать в адресной строке браузера
IP-адрес компьютера, на котором запущен сервер. При этом Django может
сообщить об ошибке вида:

DisallowedHost at /
Invalid HTTP_HOST header: '127.0.0.1:8000'. You may need to add
'127.0.0.1' to ALLOWED_HOSTS.

В константу ALLOWED_HOSTS файла settings.py необходимо добавить
допустимые адреса в виде списка строк. Например так:

ALLOWED_HOSTS = [
 '127.0.0.1',
 '192.168.1.47',
]


Важно! Вы всё ещё используете сервер для разработки. Следовательно
демонстрируете в локальной сети проект коллегам, а не даёте доступ
конечному пользователю."""