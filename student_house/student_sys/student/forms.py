# coding:utf-8

from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    # 添加了一个提交表单的功能
    def clean_qq(self):
        # 这个函数主要是控制用户qq只能输入数字
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            # raise主要是打印错误信息，如果填写的数据类型不对就会打印 “必须是数据！”
            raise forms.ValidationError('必须是数字！')
        # 返回的就是正确的数据，必须是数据所以这里用例int来确保一定是数字，不是小数
        return int(cleaned_data)

    class Meta:
        # 定义表单需要提交的数据有哪些
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )