from django.urls import path

from .views import home, external_slots, external_details, external_confirmation, internal_slots
from . import views

app_name = "booking"

urlpatterns = [
    path("", home, name="home"),
    path("external/slots/", external_slots, name="external_slots"),
    path("internal/slots/", internal_slots, name="internal_slots"),   # ✅ ADD THIS
    path("external/details/", external_details, name="external_details"),
    path("external/confirmation/", external_confirmation, name="external_confirmation"),
    path("internal/login/", views.internal_login, name="internal_login"),
    path("internal/signup/", views.signup, name="signup"),
    path("internal/verify-otp/",views.verify_otp,name="verify_otp"),
    path("internal/logout/", views.internal_logout, name="internal_logout"),
    path("internal/details/", views.internal_details, name="internal_details"),
    path("internal/confirmation/", views.internal_confirmation, name="internal_confirmation"),

]
