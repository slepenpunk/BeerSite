from django import forms
from django.core.exceptions import ValidationError
from .models import *


class EntryBeer(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryBeer, self).__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category not selected'

    class Meta:
        model = Beer
        fields = ['nickname',
                  'name',
                  'price',
                  'rating',
                  'content',
                  'photo',
                  'cat']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 5})
        }

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if len(nickname) > 50:
            raise ValidationError('Length exceeds 50 characters!')
        return nickname
