from django.core.exceptions import ValidationError
from django import forms
from django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator
#from respository import models
#from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


class LoginForm(forms.Form):
    username = fields.CharField(
        label='用户名',
        required=True,
        widget=widgets.TextInput(attrs={'class': "form-control",
                                        'placeholder': '请输入用户名',
                                        'value': '',
                                        'required': 'required'}),
        min_length=3,
        max_length=12,
        strip=True,
        error_messages={'required': '用户名不能为空',}
    )
    pwd = fields.CharField(
        label='密码',
        widget=widgets.PasswordInput(attrs={'class': "form-control",
                                            'placeholder': '请输入密码',
                                            'value': '',
                                            'required': 'required'},render_value=True),
        required=True,
        min_length=3,
        max_length=12,
        strip=True,
        error_messages={'required': '密码不能为空!', }
    )

    def clean_username(self):
        #error_dict = {}
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError('User name does not exist!')
        return username

    def clean_pwd(self):
        #error_dict = {}
        username = self.cleaned_data.get('username')
        pwd = self.cleaned_data.get('pwd')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(pwd):
                raise forms.ValidationError('Password Error!')
        return pwd




class RegisterForm(forms.Form):
    username = fields.CharField(
        label='用户名',
        required=True,
        widget=widgets.TextInput(attrs={'class': 'form-control',
                                        'placeholder': '用户名为3-12个字符','required': 'required'}),
        min_length=3,
        max_length=12,
        strip=True,
        error_messages={'required': '标题不能为空',
                        'min_length': '用户名最少为3个字符',
                        'max_length': '用户名最不超过为12个字符'},
    )
    pwd = fields.CharField(
        label='密码',
        widget=widgets.PasswordInput(attrs={'class': "form-control",
                                            'placeholder': '密码为3-12个字符，必须包含数字和字母'},render_value=True),
        required=True,
        min_length=3,
        max_length=12,
        strip=True,
        validators=[
            # 下面的正则内容一目了然，我就不注释了
            RegexValidator(r'((?=.*\d))^.{3,12}$', '必须包含数字'),
            RegexValidator(r'((?=.*[a-zA-Z]))^.{3,12}$', '必须包含字母'),
            #RegexValidator(r'((?=.*[^a-zA-Z0-9]))^.{3,12}$', '必须包含特殊字符'),
            #RegexValidator(r'^.(\S){3,10}$', '密码不能包含空白字符'),
        ],
        #用于对密码的正则验证
        error_messages={'required': '密码不能为空!',
                        'min_length': '用户名最少为3个字符',
                        'max_length': '用户名最不超过为12个字符',
                        'invalid': 'Must contain letters and Numbers'},
    )
    pwd_again = fields.CharField(
        label='密码确认',
        # render_value会对于PasswordInput，错误是否清空密码输入框内容，默认为清除，我改为不清楚
        widget=widgets.PasswordInput(attrs={'class': "form-control",
                                            'placeholder': '请再次输入密码!'},render_value=True),
        required=True,
        strip=True,
        error_messages={'required': '请再次输入密码!',}
    )

    def clean_username(self):
        # 对username的扩展验证，查找用户是否已经存在
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username).count()
        if users:
            raise forms.ValidationError('User name already exists!')
        return username
    '''
    def clean_email(self):
        # 对email的扩展验证，查找用户是否已经存在
        email = self.cleaned_data.get('email')
        email_count = User.objects.filter(email=email).count() #从数据库中查找是否用户已经存在
        if email_count:
            raise forms.ValidationError('该邮箱已经注册！')
        return email
    '''

    def clean_pwd_again(self): #查看两次密码是否一致
        password1 = self.cleaned_data.get('pwd')
        password2 = self.cleaned_data.get('pwd_again')
        if password1 and password2:
            if password1 != password2:
                # self.error_dict['pwd_again'] = '两次密码不匹配'
                raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data

    '''

    def clean(self):
        #是基于form对象的验证，字段全部验证通过会调用clean函数进行验证
        self._clean_new_password2() #简单的调用而已
    

    def clean(self):  # 必须命名为clean
        # 判断是否都通过检测,都不为None
        if self.cleaned_data.get("pwd") and self.cleaned_data.get("pwd_again"):
            if self.cleaned_data.get("pwd") == self.cleaned_data.get("pwd_again"):
                return self.cleaned_data  # 如果两次密码相同,返回干净的字典数据
            else:
                raise ValidationError("输入密码不一致")  # 没通过检测返回异常信息
        else:
            return self.cleaned_data
    '''


