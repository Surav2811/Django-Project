from django.contrib import admin
from home.models import Contact
from api.models import Task

# Register your models here.
admin.site.register(Contact)
admin.site.register(Task)