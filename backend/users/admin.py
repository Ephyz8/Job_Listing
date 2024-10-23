from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _ 
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    """
    Custom UserAdmin class to manage the display and behavior of the User model
    in the Django admin interface. It customizes list views, search functionality, 
    and the forms used for user creation and change.
    """
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["email", "first_name", "last_name", "is_staff", "is_active"]
    list_display_links = ["email"]
    list_filter = ["email", "first_name", "last_name", "is_staff", "is_active"]
    search_fields = ["email", "first_name", "last_name"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )

admin.site.register(User, UserAdmin)
