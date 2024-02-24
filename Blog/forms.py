from django import forms


class UserInputForm(forms.Form):
    phrase = forms.CharField(label='Enter a phrase', max_length=100)
