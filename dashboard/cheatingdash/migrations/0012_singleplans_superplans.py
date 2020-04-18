# Generated by Django 2.2.10 on 2020-04-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheatingdash', '0011_ordermanagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='singlePlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=4, null=True)),
                ('description', models.CharField(blank=True, max_length=4, null=True)),
                ('Ty', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='superPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.CharField(blank=True, max_length=4, null=True)),
                ('durationMonth', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]