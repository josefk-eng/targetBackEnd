# Generated by Django 4.1.4 on 2023-01-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0025_alter_category_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='img/cats'),
        ),
    ]
