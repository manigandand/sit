from django.db import models
from django.utils import timezone


# Create your models here.


class User(models.Model):
    """
    User table holds the user basic details.
    """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    access_token = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def settime(self):
        self.created_at = timezone.now()
        self.updated_at = timezone.now()
        self.save()

    def full_name(self):
        return '%s %s'.format(self.first_name, self.last_name)


class Issue(models.Model):
    """
    Issue table holds all the issue for the projects
    """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # assignee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee_id = models.IntegerField()
    labels = models.CharField(max_length=50)
    status = models.CharField(max_length=50)