# Generated by Django 4.1.4 on 2023-01-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0009_season_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='', upload_to='img/banners'),
            preserve_default=False,
        ),
    ]