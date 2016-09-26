from django.contrib import admin
from blog import models
# Register your models here


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','comment','add_time')


admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.Comment,CommentAdmin)

