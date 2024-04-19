from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomAdminUser(admin.ModelAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    model = CustomUser
    

admin.site.register(CustomUser, CustomAdminUser)
