"""Отрисовка шаблона

В представлении мы используем функцию render() для пробрасывания формы в
шаблон user_form.html. Создадим каталог templates внутри приложения, а в нём
каталог с именем приложения. В нашем случае каталог myapp4/.


💡 Внимание! Как и в прошлых занятиях мы не используем вёрстку, чтобы
сосредоточить внимание на Django и бекенд разработке.

Файл base.html в каталоге templates проекта:

<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>{% block title %}Формы{% endblock %}</title>
</head>
<body>
{% block content %}
Контент скоро появится...
{% endblock %}
</body>
</html>


Файл user_form.html в первой итерации. Каталог templates/myapp4 приложения:

{% extends 'base.html' %}
{% block content %}
{{ form }}
{% endblock %}


На первый взгляд кажется, что мы сделали всё необходимое. Переходим по адресу
http://127.0.0.1:8000/les4/user/add/ и смотрим на содержимое страницы. Обычно
клавиша F12 для доступа к коду. В нашем случае получилась следующая страница:

<!DOCTYPE html>
<html lang="ru"><head>
<meta charset="UTF-8">
<title>Формы</title>
</head>
<body wfd-invisible="true">
<label for="id_name">Name:</label>
<input type="text" name="name" maxlength="50" required=""
id="id_name">
<label for="id_email">Email:</label>
<input type="email" name="email" required="" id="id_email">
<label for="id_age">Age:</label>
<input type="number" name="age" min="0" max="120" required=""
id="id_age">
</body>
</html>

Класс UserForm был преобразован в набор полей label и input. Но тег form и кнопка
отправки отсутствуют. За их добавление, а также за шифрование данных отвечает
разработчик.


Доработка шаблона

Чтобы мы действительно увидели форму ввода, внесём правки в шаблон
user_form.html

{% extends 'base.html' %}
{% block content %}
<form action="" method="post">
{% csrf_token %}
{{ form }}
<input type="submit" value="Отправить">
</form>
{% endblock %}

Мы добавили тег формы указав что при нажатии кнопки отправить нужно
использовать тот же url адрес для отправки данных и метод POST для пересылки.

Так же был добавлен тег csrf_token. Он обеспечивает защиту данных формы от
изменений злоумышленниками. Так называемая защита от CSRF атак.

Кроме того вручную добавлена кнопка отправки и закрывающий тег формы.

🔥 Важно! Четыре добавленные строки являются обязательными для
правильного отображения любой формы через шаблоны Django.


Подведём предварительный итог. Для работы с формами необходимо создать класс
формы в файле forms.py. Далее создаётся представление, которое отправялет
экземпляр формы в шаблон. Сам шаблон должен отрисовать html теги формы и
передать csrf_token и экземпляр формы. При этом стоит помнить про настройку
маршрутов.
"""