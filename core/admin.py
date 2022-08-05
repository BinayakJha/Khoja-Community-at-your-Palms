from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.Eca)
admin.site.register(models.EcaApply)