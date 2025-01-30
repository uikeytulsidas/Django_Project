# Generated by Django 5.1.4 on 2025-01-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRST_NAME', models.CharField(max_length=30)),
                ('MIDDLE_NAME', models.CharField(max_length=30)),
                ('LAST_NAME', models.CharField(max_length=30)),
                ('EMAIL', models.EmailField(max_length=254, unique=True)),
                ('PHONE', models.CharField(max_length=15)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('GENDER', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('EMP_ID', models.CharField(max_length=6, unique=True)),
                ('DEPT_NAME', models.CharField(max_length=50)),
                ('DESIGNATION', models.CharField(max_length=50)),
                ('DATE_OF_JOINING', models.DateField()),
                ('EMP_TYPE', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=10)),
                ('ADDRESS', models.CharField(blank=True, max_length=200, null=True)),
                ('CITY', models.CharField(blank=True, max_length=50, null=True)),
                ('POSTAL_CODE', models.CharField(blank=True, max_length=10, null=True)),
                ('STATUS', models.BooleanField(default=True)),
            ],
        ),
    ]
