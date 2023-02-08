# Generated by Django 4.1.4 on 2023-01-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetManagement', '0019_csv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('stockId', models.BigIntegerField()),
                ('serialNumber', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('cost_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('department', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.png', upload_to='products/')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
    ]