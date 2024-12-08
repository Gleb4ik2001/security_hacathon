from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Поля, которые будут отображаться в списке пользователей
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')  # Фильтры для удобства
    search_fields = ('email',)  # Поле для поиска пользователей

    # Конфигурация отображения формы редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Конфигурация отображения формы создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    ordering = ('email',)  # Сортировка по email
    filter_horizontal = ('groups', 'user_permissions')  # Для удобства редактирования групп и прав


# Регистрируем модель пользователя
admin.site.register(CustomUser, CustomUserAdmin)
