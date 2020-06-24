# Generated by Django 2.2 on 2020-06-23 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20200623_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_by', to='userprofile.Users'),
        ),
    ]
