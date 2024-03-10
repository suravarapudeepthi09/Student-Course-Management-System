# Generated by Django 5.0 on 2024-02-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0023_remove_uploadwork_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadwork',
            name='uploded_file',
        ),
        migrations.AddField(
            model_name='uploadwork',
            name='uploaded_file',
            field=models.FileField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]