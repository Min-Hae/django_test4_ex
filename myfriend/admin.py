from django.contrib import admin
from myfriend.models import Friends

# Register your models here.

class FriendAdmin(admin.ModelAdmin):
    list_display =('id', 'irum', 'juso', 'nai')

admin.site.register(Friends, FriendAdmin)