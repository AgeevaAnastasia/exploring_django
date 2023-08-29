"""Представление для формы

Следующий этап — использовать представление для перевода формы из класса в
видимый пользователем HTML, а также для обработки данных, которые
пользователь введёт в форму и отправит на сервер.

Для вывода формы по GET запросу и обработки данных по POST запросу в Django
можно использовать следующий код:

import logging
from django.shortcuts import render
from .forms import UserForm

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})
    
    
    
В данном случае мы импортируем модуль render для рендеринга шаблона, а также
импортируем нашу форму UserForm. Далее определяем функцию user_form, которая
будет обрабатывать запросы на адрес /user_form/.

Если запрос пришел методом POST, то мы создаем экземпляр формы UserForm с
переданными данными из запроса. Если форма проходит валидацию (все поля
заполнены корректно), то мы получаем данные из формы и можем с ними работать.

Если запрос пришел методом GET, то мы просто создаем пустой экземпляр формы
UserForm и передаем его в шаблон user_form.html.
"""