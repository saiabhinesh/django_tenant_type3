
from django.contrib import admin
from django.urls import path
from sdtenantapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('our_team/',our_team,name='our_team')
]
