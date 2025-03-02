# Generated by Django 5.1.3 on 2025-01-20 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last_name')),
                ('phone', models.CharField(max_length=100, verbose_name='phone')),
                ('age', models.CharField(max_length=100, verbose_name='Teacher age')),
                ('educenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenter.educentermodel')),
            ],
            options={
                'verbose_name': 'StaffModel',
                'verbose_name_plural': 'StaffModels',
                'db_table': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last_name')),
                ('phone', models.CharField(max_length=100, verbose_name='phone')),
                ('age', models.CharField(max_length=100, verbose_name='Teacher age')),
                ('educenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenter.educentermodel')),
            ],
            options={
                'verbose_name': 'TeacherModel',
                'verbose_name_plural': 'TeacherModels',
                'db_table': 'teacher',
            },
        ),
    ]
