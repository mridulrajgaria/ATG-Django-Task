from django.db import models
from django.contrib.auth.models import User

USER_TYPE_CHOICES = (
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_pic = models.ImageField(upload_to='profiles/')
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
