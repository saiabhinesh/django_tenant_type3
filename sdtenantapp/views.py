from django.shortcuts import render
from .utils import *
from .models import *

def our_team(request):
    tenant=get_tenant(request)
    print(tenant)
    members=Member.objects.filter(tenant=tenant)
    return render(request,'index.html',{'tenant':tenant,'members':members})