from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractUser):
    """Model representing a User information."""

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField("email address", blank=False, null=False, unique=True)

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("email",)
BLOOD_GROUP = [
    ("A+ (A positive) ", "A+ (A positive)"),
    ("A- (A negative) ", "A- (A negative)"),
    ("B+ (B positive) ", "B+ (B positive)"),
    ("B- (B negative) ", "B- (B negative)"),
    ("AB+ (AB positive) ", "AB+ (AB positive)"),
    ("AB- (AB negative) ", "AB- (AB negative)"),
    ("O+ (O positive) ", "O+ (O positive)"),
    ("O- (O negative) ", "O- (O negative)"),
]


class Donor(models.Model):
    """Model representing a Donor information."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="donor"
    )
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    GENDER_CHOICES = {("male", "Male"), ("female", "Female"), ("other", "Other")}
    gender = models.CharField(
        max_length=10, null=True, blank=True, choices=GENDER_CHOICES
    )
    photo = models.ImageField(null=True, blank=True)
    contact_number = PhoneNumberField()
    contact_number.help_text = "Format: +8801537377302"
    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUP)
    date_of_birth = models.DateField(
        blank=False, null=False, help_text="Format: YYYY-MM-DD"
    )

    last_donation_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.contact_number})"

    class Meta:
        verbose_name = _("Donor")
        verbose_name_plural = _("Donors")
        
