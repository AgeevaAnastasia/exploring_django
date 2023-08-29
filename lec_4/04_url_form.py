"""Прописываем url

В шаблоне user_form.html мы можем вывести нашу форму с помощью тега {{ form }}.

Также можно добавить кнопку Submit для отправки формы. Но ничего этого не
получится, если пользователь не имеет доступа к форме. Переходим в urls.py
проекта и подключаем новое приложение:


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
    path('les4/', include('myapp4.urls')),
]


А теперь прописываем маршрут для связи представления с url-адресом. Для этого
создаём urls.py внутри каталога приложения:

from django.urls import path
from .views import user_form

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
]

Форма будет доступна по адресу http://127.0.0.1:8000/les4/user/add/ Остался
финальный шаг
"""