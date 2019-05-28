from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Standard)

admin.site.site_header = '停车场后台管理'
admin.site.site_title = '停车场'