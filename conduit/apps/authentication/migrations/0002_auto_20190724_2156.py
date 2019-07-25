# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-07-24 21:56
from __future__ import unicode_literals
from django.db import migrations

from conduit.apps.authentication.models import User


def create_superuser(apps, schema_editor):
    for x in range(5):
        superuser = User()
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.username = 'admin%i' % x
        superuser.email = 'admin%i@admin.net' % x
        superuser.set_password('admin')
        superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]