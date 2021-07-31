import django_filters
from .models import *
from django import forms


class DonorFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search by donor location' , 'class':'form-control '}), label='Filter By Donor Current Address')

    blood_group = django_filters.filters.ChoiceFilter(choices=BLOOD_GROUP,widget=forms.Select(attrs={'class': 'form-control'},))

    class Meta:
        model = Donor
        fields = ['blood_group','location']