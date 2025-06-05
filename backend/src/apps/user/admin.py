from django.contrib import admin
from src.apps.user.models import User

from django.contrib.auth.admin import AdminPasswordChangeForm, UserAdmin
from src.apps.user.forms import UserChangeForm, UserCreationForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "firstname", "lastname")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "user_permissions",
                    "groups",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )
    limited_fieldset = (
        (None, {"fields": ("username",)}),
        ("Important dates", {"fields": ("last_login", "created_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ("id", "username", "is_active")
    list_filter = ("is_active",)

    ordering = ("-id",)
    readonly_fields = ("last_login", "created_at")
