from django.db import models
from django.contrib.auth.models import User



"""
class Users(models.Model):
    user_id = models.IntegerField
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField
    password = models.CharField
"""


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="author")
    contributor = models.ManyToManyField(to=User, through="Contributors", default=author_user_id)

CHOICES =(
    ("1", "OUI"),
    ("2", "NON"),
)


class Contributors(models.Model):
    user_id = models.ForeignKey(to=User, default=None, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Projects, default=None, on_delete=models.CASCADE)
    permission = models.CharField(max_length=100, choices=CHOICES, default="1")
    role = models.CharField(max_length=100, blank=True)


class Issues(models.Model):
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=100, blank=True)
    issue_id = models.AutoField(primary_key=True, default=None)
    status = models.CharField(max_length=100, blank=True)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=Contributors, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True, default=None)
    description = models.CharField(max_length=100, blank=True)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
