# Generated by Django 3.0.4 on 2020-03-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kfactname', models.CharField(blank=True, max_length=24)),
                ('kcatfact', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GreatWordsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gwordsstater', models.CharField(blank=True, max_length=32)),
                ('gwords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NatParks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ntitle', models.CharField(max_length=200)),
                ('ndescription', models.TextField()),
                ('npicture', models.ImageField(blank=True, upload_to='')),
                ('nlocation', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seuraaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smaili', models.EmailField(max_length=254)),
                ('skutsumanimi', models.CharField(blank=True, max_length=32)),
                ('saika', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]