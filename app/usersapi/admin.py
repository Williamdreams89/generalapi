from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display=['email', "is_superuser", "date_joined"]

admin.site.register(get_user_model(), UserAdmin)
