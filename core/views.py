from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from .filters import DonorFilter
from .forms import DonerForm, RegisterForm
from .models import *

class SignupView(CreateView):
    form_class = RegisterForm
    template_name = "auth/sign_up.html"
    success_url = reverse_lazy("sign_in")

class HomeView(TemplateView):
    template_name = "index.html"
    


class DonerListView(View):
    def get(self, request):
        donors_qs = Donor.objects.all()

       
        filters = DonorFilter(request.GET, queryset=donors_qs)
        
        
        return render(request, "doner_list.html", {"filters": filters})
        


class DonorUpdateView(UpdateView):
    model = Donor
    template_name = "donor_update.html"
    fields = [
        "first_name",
        "last_name",
        "blood_group",
        "last_donation_date",
        "contact_number",
        "location",
    ]
    success_url = reverse_lazy("doners_list")
    redirect_field_name = "/sign_in/"
    login_url = "/sign_in/"


class DonorDeleteView(LoginRequiredMixin, DeleteView):
    model = Donor
    template_name = "donor_delete.html"
    redirect_field_name = "/sign_in/"
    login_url = "/sign_in/"


class DonerView(LoginRequiredMixin, View):
    redirect_field_name = "/sign_in/"
    login_url = "/sign_in/"

    def get(self, request):
        form = DonerForm()
        return render(request, "doner.html", {"form": form})

    def post(self, request):
        form = DonerForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user = request.user
            user.save()
            return redirect("doners_list")

        return render(
            request,
            "doner.html",
            {
                "form": form,
            },
        )



