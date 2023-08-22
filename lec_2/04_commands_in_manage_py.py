"""Пара слов о создании собственных команд manage.py

Прежде чем двигаться дальше, рассмотрим возможности Django по созданию
собственных команд. Они пригодятся при тестировании работы с моделями
данных без создания представлений, добавления маршрутов и отрисовки
шаблонов.


Создаём структуру каталогов

Для начала в каталоге приложения необходимо создать следующие
вложенные друг в друга каталоги: management/ и commands/

Получим следующую структуру

myproject/
    manage.py
    myapp2/
        __init__.py
        management/
            __init__.py
            commands/
                __init__.py
                my_command.py
    ...
...



Создаём файл с кодом команды

При этом простейшее содержимое файла должно быть следующим Назовём
файл my_command.py:

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Print 'Hello world!' to output."
    def handle(self, *args, **kwargs):
    self.stdout.write('Hello world!')


Создаём класс Command как дочерний для BaseCommand. Переменная help
выведет справку по работе команды. А метод handle отработает при вызове
команды в консоли.


Внимание! Вместо привычного print необходимо использовать self.stdout.write
для печати информации в стандартный поток вывода - консоль.


Вызываем команду

Файл my_command.py можно запускать из терминала командой

python manage.py my_comand

В результате мы увидим текст “Hello world!” в консоли.

Отлично. Теперь мы можем вернуться к работе с базой данных.
"""