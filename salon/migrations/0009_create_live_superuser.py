import os
from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    username = os.environ.get('ADMIN_USERNAME')
    email = os.environ.get('ADMIN_EMAIL')
    password = os.environ.get('ADMIN_PASSWORD')

    if not username or not password:
        return

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'email': email or '',
            'is_staff': True,
            'is_superuser': True,
            'password': make_password(password),
        }
    )

    if not created:
        user.email = email or user.email
        user.is_staff = True
        user.is_superuser = True
        user.password = make_password(password)
        user.save()


def remove_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    username = os.environ.get('ADMIN_USERNAME')

    if username:
        User.objects.filter(username=username).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_seed_services_and_barbers'),
    ]

    operations = [
        migrations.RunPython(create_superuser, remove_superuser),
    ]