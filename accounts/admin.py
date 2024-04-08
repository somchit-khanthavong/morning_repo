from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username', 'email','first_name', 'phone', 'is_staff']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'phone', 'date_of_birth', 'address',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'phone', 'date_of_birth', 'address',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)