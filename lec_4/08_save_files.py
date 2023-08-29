"""Сохранение изображений (файлов)


В финале поговорим про возможности форм Django сохранять изображения
пользователя на сервере.


💡 Внимание! Аналогично можно сохранять любые файлы, а не только
картинки. Для этого заменяем ImageFied на FileField.


Загрузка изображений через форму Django происходит с помощью класса виджета
ImageField. Для этого необходимо создать форму, которая будет содержать поле
ImageField, а также представление, которое будет обрабатывать данные формы и
сохранять загруженное изображение.

Форма forms.py
Пример кода формы:

class ImageForm(forms.Form):
    image = forms.ImageField()

Настройка settings.py

Теперь позаботимся о том, чтобы Django создал каталог для наших изображений.
Перейдём в settings.py и пропишем следующие пару констант:

...
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
...

Все присланные файлы, в том числе и изображения, будут сохраняться в каталоге
media в корне проекта.



Представление views.py

Далее создадим представление:

...
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageForm
...
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})



Если поступил POST запрос, форма заполняется не только из request.POST, но и из
request.FILES. Там содержится наше изображение. Если проверка формы успешно
завершены, выполняем три действия:
1. Сохраняем изображение в переменной image
2. Создаём экземпляр класса FileSystemStorage для работы с файлами силами
Django
3. Просим экземпляр fs сохранить изображение. Метод save принимает имя
файла и сам файл



Маршрут urls.py

Пропишем представление в списке маршрутов:

from django.urls import path
from .views import user_form, many_fields_form, add_user, upload_image

urlpatterns = [
    ...
    path('upload/', upload_image, name='upload_image'),
]


Шаблон templates/myapp4

Финальный этап - создать шаблон upload_image.html:

{% extends 'base.html' %}
{% block content %}
<h2>Загрузите изображение</h2>
<form method="post" enctype="multipart/form-data">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">Загрузить</button>
</form>
{% endblock %}


🔥 Важно! Чтобы форма отправляет файлы необходимо в теге форм
прописать enctype="multipart/form-data". Без этого мы не получим доступ к
файлам.


Итоги

Как видите формы Django являются удобным инструментом для получения данных
от пользователя и сохранения их в базе данных, на сервере. Если ваш сайт не
является личным блогом, а подразумевает взаимодействие с читателями, освоение
форм будет обязательным пунктом в создании проекта.
"""