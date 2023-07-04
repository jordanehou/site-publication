from django.contrib import admin
from .models import Comment, Response, Subject, Course, Module

# Register your models here.

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Comment)
admin.site.register(Response)