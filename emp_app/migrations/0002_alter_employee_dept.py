# Generated by Django 5.0 on 2023-12-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.CharField(max_length=50),
        ),
    ]
