"""Проверка работоспособности

Убедитесь, что сервер работает. Если нет, нужно выполнить команду "python
manage.py runserver". После этого можно открыть браузер и перейти на
страницу http://127.0.0.1:8000/ (по умолчанию), чтобы увидеть текст "Hello,
world!". При переходе по адресу http://127.0.0.1:8000/about/ увидим
сообщение "About us" из второго представления


В целом, создание приложения и определение представлений - это основа
работы с Django. Далее можно добавлять модели, формы, роутинг и другие
компоненты для создания полноценного веб-приложения. Всё это будет далее
в рамках курса.


Немного подробнее о path() и include()

Прежде чем двигаться дальше, внесём небольшое изменение в написанный
код. Разберёмся в том как работают функции path и include из пакета
django.urls.

Исправим файл myproject/urls.py. Заменим первый параметр функции path с
пустой строки на какой-нибудь текст, например на prefix:

from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('myapp.urls'))
]


Теперь при попытке перейти по адресу http://127.0.0.1:8000/ получит ошибку
404
Page not found (404)
Request Method: GET
Request URL: http://127.0.0.1:8000/
Using the URLconf defined in myproject.urls, Django tried these URL
patterns, in this order:
admin/
prefix/
The empty path didn't match any of these.


У нас нет маршрута для обработки корневого адреса. Попробуем перейти по
адресу http://127.0.0.1:8000/prefix/about/ Видим, что представление about
отработало свой код и вернула текст.

При вводе адреса в браузер сервер начинает сопоставлять введённый путь с
содержимым списка urlpatterns из urls.py проекта. Найдя совпадение, оно
отбрасывается и оставшееся часть пути передаётся в urls.py указанный внутри
функции include. В нашем примере это myapp/urls.py. Он также просматривает
список urlpatterns в поисках совпадений. В нашем примере будет вызвана
функция views.about()."""