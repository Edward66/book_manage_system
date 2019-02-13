from django import forms
from django.forms import widgets


class AuthorForm(forms.Form):
    name = forms.CharField(
        max_length=32,
        label='姓名',
        error_messages={
            'required': '姓名不能为空',
            'max_length': "不能超过32字符",
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    age = forms.IntegerField(
        max_value=134,
        min_value=0,
        label='年龄',
        error_messages={
            'required': '年龄不能为空',
            'max_value': '年龄不能超过134岁',
            'min_value': '年龄不能是负数',
        },
        widget=widgets.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    birthday = forms.DateField(
        label='出生日期',
        required=False,
        error_messages={
            'invalid': '日期格式错误'
        },
        widget=widgets.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        ),
    )
    telephone = forms.IntegerField(
        label='手机号码',
        error_messages={
            'required': '手机号不能为空',
        },
        widget=widgets.NumberInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    addr = forms.CharField(
        max_length=64,
        label='家庭地址',
        error_messages={
            'max_length': '不能超过64个字符',
            'required': '家庭地址不能为空',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),

    )

    def clean_telephone(self):
        val = self.cleaned_data.get('telephone')
        if len(str(val)) == 11:
            return val
        else:
            raise forms.ValidationError('请输入11位手机号')
