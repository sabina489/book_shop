from django.contrib import admin

from account.models import User,Profile, Register

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        # "email",
        # "password",
    )

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "password",
    )