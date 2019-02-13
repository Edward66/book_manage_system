from django import forms
from django.contrib.auth.models import User
from django.forms import widgets


# 用户注册验证

class RegForm(forms.Form):
    name = forms.CharField(
        min_length=6,
        label='用户名',
        error_messages={
            'required': '用户名不能为空',
            'min_length': '不能小于6个字符',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    pwd = forms.CharField(
        min_length=6,
        label='密码',
        error_messages={
            'required': '该字段不能为空',
            'min_length': '不能小于6个字符',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    r_pwd = forms.CharField(
        min_length=6,
        label='确认密码',
        error_messages={
            'required': '该字段不能为空',
            'min_length': '不能小于6个字符',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={'required': '该字段不能为空', 'invalid': '格式错误'},
        widget=widgets.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean_name(self):
        reg_name = self.cleaned_data.get('name')
        db_name = User.objects.filter(username=reg_name)

        if not db_name:
            return reg_name
        else:
            raise forms.ValidationError('该用户已注册！！')

    def clean_email(self):
        reg_email = self.cleaned_data.get('email')
        db_email = User.objects.filter(email=reg_email)

        if not db_email:
            return reg_email
        else:
            raise forms.ValidationError('该邮箱已注册')

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')

        if pwd and r_pwd:
            if pwd == r_pwd:
                return self.cleaned_data
            else:
                raise forms.ValidationError('两次密码不一致')


# 用户登录验证

class LoginForm(forms.Form):
    name = forms.CharField(
        min_length=6,
        label='用户名',
        error_messages={
            'required': '用户名不能为空',
            'min_length': '不能小于6个字符',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    pwd = forms.CharField(
        min_length=6,
        label='密码',
        error_messages={
            'required': '该字段不能为空',
            'min_length': '不能小于6个字符',
        },
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')

        auth = User.objects.filter(username=name, password=pwd)

        if not auth:
            raise forms.ValidationError('用户名或密码错误')
