
from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True,max_length=10,
                            error_messages={
                                'required': '标题必填',
                                'min_length': '文章标题最少两个字符',
                                'max_length': '文章标题最多十个字符'
                            })
    desc = forms.CharField(min_length=5, required=True,
                           error_messages={
                               'required': '描述必填',
                               'min_length': '描述最少五个字符'
                           })
    content = forms.CharField(required=True, error_messages={
        'required': '内容必填'
    })

    icon = forms.ImageField(required=True, error_messages={
        'required': '图片必填'
    })