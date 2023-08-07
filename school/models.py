from django.db import models
from django.utils import timezone

# Create your models here.
class about(models.Model):
    school_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/', blank=True, null=True)
    established_date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100)
    official_website = models.URLField()
    school_motto = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.school_name


class team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
   

