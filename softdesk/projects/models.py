from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="author", null=True)
    contributor = models.ManyToManyField(to=User, through="Contributors")


CHOICES = (
    ("OUI", "OUI"),
    ("NON", "NON"),
)


class Contributors(models.Model):
    user_id = models.ForeignKey(to=User, default=None, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Projects, default=None, on_delete=models.CASCADE)
    permission = models.CharField(max_length=100, choices=CHOICES, default="OUI")
    role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        unique_together = ('project_id', 'user_id',)


class Issues(models.Model):
    project_id = models.ForeignKey(to=Projects, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=100, blank=True)
    issue_id = models.AutoField(primary_key=True, default=None)
    status = models.CharField(max_length=100, blank=True)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    assignee_user_id = models.ForeignKey(to=Contributors, on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True, default=None)
    description = models.CharField(max_length=100, blank=True)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    issue_id = models.ForeignKey(to=Issues, default=None, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
