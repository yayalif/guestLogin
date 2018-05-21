from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.models import User


# 用户登录接口
def user_login(request):
    #http://127.0.0.1:8000/user_login/?username=aaa&password=a123
    username = request.GET.get("username", '') #用户名
    pwd = request.GET.get("password", '') #密码
    if username=='' or pwd == '':
        return JsonResponse({'status': 10010, 'message': 'Incomplete parameter!'})
    user = User.objects.filter(username=username).first()
    if not user:
        return JsonResponse({'status': 10011, 'message': 'User name does not exist!'})
    elif not user.check_password(pwd):
        return JsonResponse({'status': 10012, 'message': 'Password Error!'})
    return JsonResponse({'status': 10013, 'message': 'Login Success','username':username})


# 用户注册接口
def user_register(request):
    #测试用户的信息并没有添加到数据库里面
    username = request.GET.get("username", "") #用户名
    pwd = request.GET.get("pwd", "") #密码
    pwd_again = request.GET.get("pwd_again", "")  # 密码
    if username=='' or pwd == '' or pwd_again=='':
        return JsonResponse({'status': 10010, 'message': 'Incomplete parameter!'})
    user = User.objects.filter(username=username).first()

    if user:
        return JsonResponse({'status': 10011, 'message': 'User name already exists!'})
    elif pwd and pwd_again:
        if pwd != pwd_again:
            # self.error_dict['pwd_again'] = '两次密码不匹配'
            return JsonResponse({'status': 10012, 'message': 'Passwords do not match'})
    return JsonResponse({'status': 10013, 'message': 'Register Success','username':username})











