# Generated by Django 3.0.4 on 2020-03-15 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aatooseetrii', '0002_auto_20200315_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cattable',
            old_name='kcatfact',
            new_name='catfact',
        ),
        migrations.RenameField(
            model_name='cattable',
            old_name='kfactname',
            new_name='factname',
        ),
    ]