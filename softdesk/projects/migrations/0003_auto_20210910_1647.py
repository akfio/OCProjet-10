# Generated by Django 3.2.7 on 2021-09-10 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20210910_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributors',
            name='role',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='projects',
            name='contributor',
            field=models.ManyToManyField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL), through='projects.Contributors', to=settings.AUTH_USER_MODEL),
        ),
    ]
