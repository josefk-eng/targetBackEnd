# Generated by Django 4.1.4 on 2023-01-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0026_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='serialNumber',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stockId',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(default='untagged', max_length=100),
        ),
    ]