# Generated by Django 3.2.13 on 2022-06-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('salary', models.PositiveSmallIntegerField()),
                ('position', models.CharField(max_length=200)),
                ('position_type', models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'full-time')], max_length=20)),
                ('posted_date', models.DateTimeField(auto_now=True)),
                ('job_description', models.TextField()),
            ],
        ),
    ]
