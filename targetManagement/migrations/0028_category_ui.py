# Generated by Django 4.1.4 on 2023-02-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0027_alter_product_cost_price_alter_product_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ui',
            field=models.CharField(default='', max_length=100),
        ),
    ]
