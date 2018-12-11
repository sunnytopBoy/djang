
from django import forms


class UserForm(forms.Form):

    username = forms.CharField(min_length=2, required=True,
                               error_messages={
                                 'required': '用户名必填',
                                 'min_length': '用户名必须大于一个字符'
                               })
    pwd = forms.CharField(min_length=2,  required=True,
                          error_messages={
                                'required': '密码必填',
                                'min_length': '密码最少两个字',
                            })



