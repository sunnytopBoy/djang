
from django import forms


class AddArtForm(forms.Form):
    #  required=True表示必填项
    title = forms.CharField(min_length=2, max_length=10, required=True,
                            error_messages={
                                'required': '标题必填',
                                'max_length': '文章标题最多十个字',
                                'min_length': '文章标题最少两个字',
                            })
    desc = forms.CharField(min_length=5, required=True,
                           error_messages={
                               'required': '简短描述必填',
                               'min_length': '简短描述最少五个字',
                           })
    content = forms.CharField(required=True)
    icon = forms.ImageField(required=True, error_messages={
        'required': '首图必填'
    })