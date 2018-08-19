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
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    access_token = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    is_authenticated = True
    is_anonymous = False
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['access_token', 'password']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name


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