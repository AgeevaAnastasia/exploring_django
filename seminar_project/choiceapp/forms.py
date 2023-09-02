from django import forms


class ChoiceForm(forms.Form):
    game = forms.ChoiceField(choices=[('c', 'coin'), ('cb', 'cube'), ('r', 'random')])
    count = forms.IntegerField(min_value=1, max_value=64)


