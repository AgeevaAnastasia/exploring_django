"""Пользовательская валидация данных с помощью метода clean()

Мы можем прописать свои методы, которые начинаются со слова clean_ и далее
указать имя поля. Такой метод будет применяться для дополнительной проверки
поля на корректность. Рассмотри пример формы UserForm из начала занятия, но
добавим пару своих проверок:

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
    '''Плохой пример. Подмена параметра min_length.'''
    name = self.cleaned_data['name']
    if len(name) < 3:
        raise forms.ValidationError('Имя должно содержать не менее 3 символов')
    return name

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or
            email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту')
    return email


В данном примере класс UserForm, который наследуется от класса forms.Form. В
классе определены три поля формы: name, email и age. Для каждого поля
определены соответствующие типы данных: CharField для поля name, EmailField для
поля email и IntegerField для поля age.

Далее определены два метода clean_name() и clean_age(), которые осуществляют
пользовательскую валидацию данных.

В методе clean_name() проверяется длина имени, и если она меньше трех символов,
то выбрасывается исключение ValidationError с соответствующим сообщением. Это
антипаттерн. Мы написали пять строк кода, которые делают тоже самое, что и
параметр min_length=3.

Для поля email встроенные механизмы Django проверяют, что введённый текст
похож на электронную почту, с собакой, точкой и т.п. Далее в методе clean_email()
мы проверяем окончание почты. Если оно не совпадает с одним из корпоративных
окончаний, выбрасывается соответствующее сообщение.
"""