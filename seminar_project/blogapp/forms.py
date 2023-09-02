from django import forms
import datetime
from . import models


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    lastname = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField(label='e-mail', max_length=100)
    bio = forms.CharField(label='Биография', widget=forms.Textarea)
    birthdate = forms.DateField(label='Дата рождения', initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'type': 'date'}))


class PostForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    content = forms.CharField(label='Содержание', widget=forms.Textarea)
    public_date = forms.DateField(label='Дата публикации', initial=datetime.date.today)
    category = forms.CharField(label='Категория', max_length=100)
    author = forms.ModelChoiceField(label='Авторы', queryset=models.Author.objects.all())
    ispublic = forms.BooleanField(required=True, label='Опубликовать')

