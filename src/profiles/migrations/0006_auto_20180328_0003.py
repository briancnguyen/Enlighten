# Generated by Django 2.0.3 on 2018-03-28 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_profile_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
    ]
