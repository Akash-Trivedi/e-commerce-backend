# Generated by Django 4.0.3 on 2022-03-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalUser',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('dob', models.DateField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('ipAddress', models.GenericIPAddressField(default='127.0.0.1')),
                ('browser', models.CharField(default='localhost:chrome', max_length=255)),
                ('homeAddress', models.CharField(default='-', max_length=255, null=True)),
                ('isPublisher', models.BooleanField()),
            ],
        ),
    ]
