# Generated by Django 3.0.4 on 2020-03-15 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aatooseetrii', '0003_auto_20200315_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cattable',
            old_name='catfact',
            new_name='kcatfact',
        ),
        migrations.RenameField(
            model_name='cattable',
            old_name='factname',
            new_name='kfactname',
        ),
    ]