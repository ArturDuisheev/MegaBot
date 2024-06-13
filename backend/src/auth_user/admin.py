from django.contrib import admin

from auth_user.models.user import EsUser, Departament


class DepartamentInline(admin.TabularInline):
    model = Departament
    extra = 2


class UserAdmin(admin.ModelAdmin):
    inlines = [DepartamentInline, ]
    list_display = ('unique_number', 'username', 'ip_address', 'country_and_region')


admin.site.register(EsUser, UserAdmin)
