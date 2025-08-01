from django.db import models
import random


# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

def predict_sales(product, region, date):
    return round(random.uniform(2000, 5000), 2)


class Prediction(models.Model):
    product = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    date = models.DateField()
    predicted_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.region} - {self.date}"



