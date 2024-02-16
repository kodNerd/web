# Generated by Django 5.0 on 2024-02-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
        migrations.AddField(
            model_name='students',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='./students/static/media'),
        ),
    ]