from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/patient/', views.dashboard_patient, name='dashboard_patient'),
    path('dashboard/doctor/', views.dashboard_doctor, name='dashboard_doctor'),
]
