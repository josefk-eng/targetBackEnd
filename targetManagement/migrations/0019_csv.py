# Generated by Django 4.1.4 on 2023-01-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0018_item_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csv/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('is_activated', models.BooleanField(default=False)),
            ],
        ),
    ]
