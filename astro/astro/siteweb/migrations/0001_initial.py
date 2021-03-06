# Generated by Django 3.2.3 on 2021-06-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField()),
                ('image_un', models.FileField(upload_to='image_site')),
                ('image_deux', models.FileField(upload_to='image_site')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.CharField(max_length=200)),
                ('nom_Site', models.CharField(max_length=200)),
                ('titre_Home', models.CharField(max_length=200)),
                ('titre_About', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('numero', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
