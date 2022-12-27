from django import forms
from.models import Article,question


class MyForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=('title','summary','body')


class MyquestionForm(forms.ModelForm):
    class Meta:
        model=question
        fields=('__all__')