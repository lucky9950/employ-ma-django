# Generated by Django 5.0 on 2023-12-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]