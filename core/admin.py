from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("email",)


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "contact_number",
        "blood_group",
        "date_of_birth",
        "last_donation_date",
        "location",
    )
