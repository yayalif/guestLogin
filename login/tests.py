from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from django.contrib.auth.hashers import make_password

'''
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        User.objects.create(username="abc", password='abc123')#密码为明文
        #User.objects.create_user(username="abc", password='abc123')  # 密码经过加密了

    def test_event_models(self):
        result = User.objects.get(username="abc")
        self.assertEqual(result.password, "abc123")#明文验证时正确的！
        #self.assertEqual(result.password, make_password('abc123', None, ))  # 加密后验证时错误的！
'''
'''
class IndexPageTest(TestCase):
    # 测试 index 登录首页
    def test_index_page_renders_index_template(self):
        # 测试 index 视图 
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, 'login.html')

'''
class LoginActionTest(TestCase):
    # 测试登录函数
    def setUp(self):
        User.objects.create_user('aaa', 'a123')
        self.c = Client()

    def test_login_action_username_password_error(self):
        # 用户名密码错误 
        test_data = {'username': 'abc', 'password': '123'}
        response = self.c.post('/login/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"User name does not exist!", response.content)

    def test_login_action_success(self):
        # 登录成功
        test_data = {'username': 'aaa', 'password': 'a123'}
        response = self.c.post('/login/', data=test_data)
        self.assertEqual(response.status_code, 200)


'''
class RegisterTest(TestCase):
    # 测试注册函数
    def setUp(self):
        #User.objects.create_user('aaa', 'a123')
        #注意这里!如果在这创建了用户，代表该用户已经添加到了数据库，
        #以下进行相同用户的测试时，就会出现用户名已存在。
        #如果不在这里进行创建用户，以下初次使用该用户（‘aaa’,'a123'）会提示注册成功！
        #但是该用户会立即注销！
        #self.c = Client()
        self.user = User()
        self.c = Client()

    def test_register_success(self):
        # 注册成功
        print(self.user.username)
        test_data = {'username': 'aaa', 'pwd': 'a123','pwd_again':'a123'}
        response = self.c.post('/register/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Register Success!", response.content)

    def test_register_user_exists_error(self):
        # 用户名已经存在
        User.objects.create_user('aaa', 'a123')
        test_data = {'username': 'aaa', 'pwd': 'a123','pwd_again':'a123'}
        response = self.c.post('/register/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"User name already exists!", response.content)

    def test_register_password_not_match_error(self):
        # 密码不匹配
        test_data = {'username': 'aaa', 'pwd': 'a123','pwd_again':'a321'}
        response = self.c.post('/register/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Passwords do not match", response.content)
'''





