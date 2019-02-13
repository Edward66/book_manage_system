from django import forms
from django.forms import TextInput

from crud.models import Publish


class PublishForm(forms.ModelForm):
    class Meta:
        model = Publish
        fields = (
            'name', 'city', 'email'
        )

        labels = {
            'name': '姓名',
            'city': '城市',
            'email': '邮箱'
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'})
        }

        error_messages = {
            'name': {
                'max_length': "不能超过32字符",
                "required": "该字段不能为空",
            },

            'city': {
                'max_length': ("不能超过32字符"),
                "required": "该字段不能为空",
            },
            'email': {
                'invalid': '邮箱格式错误',
                "required": "该字段不能为空",
            },
        }