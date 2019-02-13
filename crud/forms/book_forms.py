from django import forms
from django.forms import TextInput, NumberInput, DateInput, Select, SelectMultiple

from crud.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title', 'price', 'pub_date', 'publish', 'authors'
        )

        labels = {
            'title': '标题',
            'price': '价格',
            'pub_date': '出版日期',
            'publish': '出版社',
            'authors': '作者列表'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'pub_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'publish': Select(attrs={'class': 'form-control', }),
            'authors': SelectMultiple(attrs={'class': 'form-control', })
        }

        error_messages = {
            'title': {
                'max_length': "不能超过32字符",
                "required": "标题不能为空",
                'unique': '书名已存在',
            },

            'price': {
                "required": "价格不能为空",
                'max_digits': '数字不能超过5个（包括小数）',
                'max_decimal_places': '小数最多为2位',
            },
            'pub_date': {
                "required": "出版日期不能为空",
                'invalid': '日期格式错误',
            },
            'publish': {
                'required': '出版社不能为空',
            },
            'authors': {
                'required': '作者不能为空',
            }

        }
