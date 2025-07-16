from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('mental_health', 'Mental Health'),
    ('heart_disease', 'Heart Disease'),
    ('covid19', 'Covid19'),
    ('immunization', 'Immunization'),
]

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
