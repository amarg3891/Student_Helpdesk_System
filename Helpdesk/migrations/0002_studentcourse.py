# Generated by Django 3.1.5 on 2021-04-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('full_form', models.CharField(max_length=150)),
                ('desc', models.TextField()),
                ('course', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('course_fees', models.CharField(max_length=100)),
            ],
        ),
    ]