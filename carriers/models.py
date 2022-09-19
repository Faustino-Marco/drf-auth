from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Carrier(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    trip = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trip