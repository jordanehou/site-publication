# Generated by Django 4.2.2 on 2023-07-02 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import students.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='videoDef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to=students.models.rename_video, verbose_name='video_default')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=150)),
                ('profile_image', models.ImageField(blank=True, upload_to=students.models.rename_image)),
                ('type_profile', models.CharField(choices=[('student', 'student'), ('publisher', 'publisher')], default='student', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
