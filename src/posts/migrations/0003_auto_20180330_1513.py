# Generated by Django 2.0.3 on 2018-03-30 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180330_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]
