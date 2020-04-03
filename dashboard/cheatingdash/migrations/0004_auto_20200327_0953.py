# Generated by Django 2.2.10 on 2020-03-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheatingdash', '0003_auto_20200327_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='priority',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]