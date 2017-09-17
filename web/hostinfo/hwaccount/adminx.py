#import datetime
import xadmin
from xadmin import views
from hwaccount.models import Account
# Register your models here.

class AccountAdmin(object):
    list_display =  ['account_name', 'user_name', 'pidcn_north_1', 'pidcn_east_2', 'pidcn_south_1']
    list_filter = ['account_name', 'user_name']
    search_fields = ['account_name','user_name']
    list_per_page = 10
    #refresh_times = (5,10,20)


xadmin.site.register(Account,AccountAdmin)
