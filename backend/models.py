from django.db import models


COLOR_CHOICES = (
    ("Black", "Black"),
    ("Yellow", "Yellow"),
    ("Blue", "Blue"),
    ("Red", "Red"),
    ("Green", "Green"),
    ("Ornge", "Ornge"),
    ("Sky", "Sky"),
    ("NavyBlue", "NavyBlue"),
)
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Sales(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rate = models.IntegerField()
    semester = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='1'
    )
