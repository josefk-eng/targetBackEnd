# Generated by Django 4.1.4 on 2023-01-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0021_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(default='Sales', max_length=100),
        ),
    ]
