# Generated by Django 5.0 on 2024-02-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0011_coursecontent_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='course_code',
            field=models.CharField(max_length=50),
        ),
    ]