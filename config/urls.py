from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("doners/", DonerView.as_view(), name="doners"),
    path("doner_list/", DonerListView.as_view(), name="doners_list"),
    path("doner_update/<int:pk>", DonorUpdateView.as_view(), name="doner_update"),
    path("doner_delete/<int:pk>", DonorDeleteView.as_view(), name="doner_delete"),
    path("sign_up/", SignupView.as_view(), name="sign_up"),
    path(
        "sign_in/",
        auth_views.LoginView.as_view(template_name="auth/sign_in.html"),
        name="sign_in",
    ),
    path(
        "sign_out/",
        auth_views.LogoutView.as_view(template_name="auth/sign_out.html"),
        name="sign_out",
    ),
    path("captcha/", include("captcha.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
