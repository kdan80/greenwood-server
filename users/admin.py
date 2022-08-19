from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db import models

class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('email', 'username', 'date_created',
                    'last_login', 'is_admin', 'is_staff')
    ordering = ('-date_created',)
    search_fields = ('email', 'username')
    readonly_fields = ('date_created', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ('User details', {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Activity', {'fields': ('date_created', 'last_login')})

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdmin)
