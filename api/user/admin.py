from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from user.models import User


# Register your models here.
class UserAdmin(AuthUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )


admin.site.register(User, UserAdmin)
