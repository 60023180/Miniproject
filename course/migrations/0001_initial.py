# Generated by Django 3.0.8 on 2020-08-18 10:16

import course.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.SlugField(default=course.models.random_course_code, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('teacher_name', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('teaching_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.TeachingPeriod')),
            ],
        ),
    ]
