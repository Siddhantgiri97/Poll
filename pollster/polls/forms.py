from django import forms
from .models import Choice, Question


class CreateQuestion(forms.ModelForm):
    choice1 = forms.CharField(label='Choice 1', max_length=100, widget=forms.TextInput(
        attrs={"class": 'form-control'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, widget=forms.TextInput(
        attrs={"class": 'form-control'}))
    choice3 = forms.CharField(label='Choice 3', max_length=100, widget=forms.TextInput(
        attrs={"class": 'form-control'}))
    choice4 = forms.CharField(label='Choice 4', max_length=100, widget=forms.TextInput(
        attrs={"class": 'form-control'}))

    class Meta:
        model = Question
        fields = ['question_text', 'choice1',
                  'choice2', 'choice3', 'choice4', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
        }
