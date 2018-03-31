from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.user.username

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    activities = models.TextField()
    start_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)], null=True)
    end_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)], null=True, blank=True)
    
    def __str__(self):
        return self.school

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)], null=True)
    end_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)], null=True, blank=True)

    def __str__(self):
        return self.company

class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='award')
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.CharField(max_length=4, validators=[MinLengthValidator(4)], null=True)
    
    def __str__(self):
        return self.name
