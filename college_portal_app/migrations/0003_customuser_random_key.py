# Generated by Django 3.1 on 2020-12-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_portal_app', '0002_auto_20201113_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='random_key',
            field=models.CharField(default=0, max_length=6),
        ),
    ]