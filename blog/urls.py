from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog_view, name='create_blog'),
    path('my/', views.my_blogs_view, name='my_blogs'),
    path('category/<str:category>/', views.category_blogs_view, name='category_blogs'),
]
