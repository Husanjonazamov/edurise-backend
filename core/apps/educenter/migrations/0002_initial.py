# Generated by Django 5.1.3 on 2025-01-20 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educenter', '0001_initial'),
        ('students', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmodel',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.courcemodel'),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='educenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_education', to='educenter.educentermodel'),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_teacher', to='users.usermodel'),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='groups', to='students.studentmodel'),
        ),
        migrations.AddField(
            model_name='journalmodel',
            name='educenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_journal', to='educenter.educentermodel'),
        ),
        migrations.AddField(
            model_name='journalmodel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenter.groupmodel'),
        ),
        migrations.AddField(
            model_name='journalmodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentmodel'),
        ),
        migrations.AddField(
            model_name='registermodel',
            name='educenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenter.educentermodel'),
        ),
        migrations.AddField(
            model_name='roomsmodel',
            name='educenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educenter.educentermodel'),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_room', to='educenter.roomsmodel'),
        ),
    ]
