# Generated by Django 2.2 on 2020-06-23 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_otp_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='phone_no',
        ),
        migrations.AlterField(
            model_name='match',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='match_by', to='userprofile.Users'),
        ),
    ]
