from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,render_to_response, get_object_or_404, get_list_or_404
from login.forms import LoginForm,RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponseRedirect('/login/')
    # return HttpResponse("Hello Django!")


# 登陆
def login_action(req):
    if req.method == 'POST':
        obj = LoginForm(req.POST)
        if obj.is_valid():
            username = obj.cleaned_data['username']
            pwd = obj.cleaned_data['pwd']
            #user = auth.authenticate(username=username, password=pwd)#用这个一直认证失败是什么问题？
            user = User.objects.filter(username=username).first()
            auth.login(req, user)  # 登录
            req.session['user'] = username
            response = HttpResponseRedirect('/welcome/')
            return response
        else:
            #es = obj.errors
            #print(type(obj.errors))
            #print(obj.errors)
            #print(es.get("__all__"))
            return render_to_response('login.html', {'obj': obj},)
    else:
        obj = LoginForm()
    return render_to_response('login.html', {'obj': obj},)


# 注册

def register(req):
    if req.method == 'POST':
        obj = RegisterForm(req.POST)
        if obj.is_valid():

            #获得表单数据
            username = obj.cleaned_data['username']
            password = obj.cleaned_data['pwd']
            #添加到数据库
            user = User.objects.create_user(username=username, password=password)
            user.is_active = True
            user.save()
            #obj = LoginForm()
            return render_to_response('register.html', {'obj': obj,'Success': 'Register Success!'}, )
        else:
            return render_to_response('register.html', {'obj': obj},)
    else:
        obj = RegisterForm()
    return render_to_response('register.html', {'obj': obj},)


# 登陆成功
@login_required
def welcome(request):
    username = request.session.get('user', '')  # 读取浏览器session
    #username = request.COOKIES.get('username','')
    #return render_to_response('welcome.html', {'username':username})
    return render(request, "welcome.html", {"user": username})


# 退出登录
@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response
