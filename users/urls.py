from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from users import views  # ✅ Import views from the users app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirect root to login
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('blogs/', include('blog.urls')),
    path('dashboard/patient/', views.dashboard_patient, name='dashboard_patient'),
    path('dashboard/doctor/', views.dashboard_doctor, name='dashboard_doctor'),
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
