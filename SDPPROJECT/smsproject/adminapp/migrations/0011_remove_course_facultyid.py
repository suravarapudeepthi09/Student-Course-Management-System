# Generated by Django 5.0 on 2024-03-09 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_course_facultyid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='facultyid',
        ),
    ]
