from .models import *

def get_hostname(request):
    print('getting host name is',request.get_host())
    print('returning of getting host is',
          request.get_host().split(':')[0].lower())
    return request.get_host().split(':')[0].lower()

def get_tenant(request):
    hostname=get_hostname(request)
    print('host name is',hostname)
    subdomain=hostname.split('.')[0]
    print('subdomain is ',subdomain)
    return Tenant.objects.filter(subdomain=subdomain).first()