# Generated by Django 3.2.13 on 2022-06-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_joblisting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='position',
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='position_type',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], max_length=20),
        ),
    ]
