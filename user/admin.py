from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminEditForm, RegisterForm

User = get_user_model()
# from .models import User

class UserAdmin(BaseUserAdmin):
    add_form = RegisterForm
    form = UserAdminEditForm

    list_display = ('email', 'admin', 'staff', 'active')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
