from django.db import models

# Create your models here.
class Tenant(models.Model):
    name=models.CharField(max_length=50)
    subdomain=models.CharField(max_length=50)

class Tenantawaremodel(models.Model):
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE)

class Member(Tenantawaremodel):
    name=models.CharField(max_length=50)



