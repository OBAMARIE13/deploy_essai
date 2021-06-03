# Generated by Django 3.2.3 on 2021-06-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='image_site')),
                ('description', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
