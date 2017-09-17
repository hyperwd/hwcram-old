from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField('账户名',primary_key=True, max_length=20)
    user_name = models.CharField('用户名', max_length=20,default='若使用帐户名登录，此项填写账户名')
    password = models.CharField('密码', max_length=20)
    #pid_north1 = models.CharField('项目ID-华北1', max_length=40,default='在我的凭证中查看项目列表获取')
    pidcn_north_1 = models.CharField('项目ID-华北1', max_length=40,default='在我的凭证中查看项目列表获取')
    pidcn_east_2 = models.CharField('项目ID-华东2', max_length=40)
    pidcn_south_1 = models.CharField('项目ID-华南1', max_length=40)
