# Generated by Django 2.2 on 2020-06-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20200419_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]