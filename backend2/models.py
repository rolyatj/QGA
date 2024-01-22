from django.db import models
from django.contrib.auth.models import User

class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Scorecard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    score = models.IntegerField()