# Generated by Django 4.1.4 on 2023-01-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=1000)),
                ('deviceId', models.CharField(max_length=100)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
