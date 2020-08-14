from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=200, null=True, blank=True)
    profileSummary = models.TextField(null=True, blank=True)
    profileImage = models.ImageField(
        upload_to='ProfileImage/', null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fullName


class Project(models.Model):
    userProfile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')
    summary = models.TextField()
    detail = models.TextField()
    github_link = models.CharField(blank=True, max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)


@receiver(post_delete, sender=Project)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
