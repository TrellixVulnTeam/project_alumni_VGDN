# Generated by Django 2.2.7 on 2019-11-18 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0010_users_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='image',
            new_name='profileimage',
        ),
    ]
