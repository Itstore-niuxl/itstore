from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Niuxl'
    site_title = 'Niuxl管理后台'
    index_title = '首页'

custom_site = CustomSite(name='custom_admin')