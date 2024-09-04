from django.contrib import admin
from .models import pendingUsers, assignment 
# Register your models here.
admin.site.register(pendingUsers)
admin.site.register(assignment)