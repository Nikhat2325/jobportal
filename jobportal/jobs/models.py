from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Studentuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username


# Job Model
class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Application Model
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')   # prevent duplicate apply

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"