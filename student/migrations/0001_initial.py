# Generated by Django 3.0.8 on 2020-08-18 10:16

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.SlugField(default=student.models.random_student_code, unique=True)),
                ('enroll_date', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('contact_details', models.TextField()),
                ('parent_contact', models.TextField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
