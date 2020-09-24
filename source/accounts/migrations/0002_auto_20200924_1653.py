# Generated by Django 2.2 on 2020-09-24 16:53

from django.db import migrations


def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]
