# Generated by Django 1.11.28 on 2020-03-04 15:19

"""
Deletes the ENFORCE_JWT_SCOPES waffle switch that has already been deprecated and removed.

See https://github.com/openedx/edx-platform/pull/23188 for the removal
"""

from django.db import migrations

ENFORCE_JWT_SCOPES = 'oauth2.enforce_jwt_scopes'


def delete_switch(apps, schema_editor):
    """ Delete the switch. """
    Switch = apps.get_model('waffle', 'Switch')
    try:
        Switch.objects.filter(name=ENFORCE_JWT_SCOPES).delete()
    except Switch.DoesNotExist:
        pass


def create_switch(apps, schema_editor):
    """ Create the switch if it does not already exist. """
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.update_or_create(name=ENFORCE_JWT_SCOPES, defaults={'active': True})


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_dispatch', '0008_applicationaccess_filters'),
    ]

    operations = [
        migrations.RunPython(delete_switch, reverse_code=create_switch),
    ]
