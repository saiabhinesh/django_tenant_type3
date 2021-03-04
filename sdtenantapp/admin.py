from django.contrib import admin
from .models import *
admin.site.register(Tenant)
admin.site.register(Member)
admin.site.register(Tenantawaremodel)
#admin.site.register(Tenant)
