# Generated by Django 3.2.7 on 2021-09-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210910_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributors',
            name='permission',
            field=models.CharField(choices=[('1', 'OUI'), ('2', 'NON')], default='1', max_length=100),
        ),
    ]
