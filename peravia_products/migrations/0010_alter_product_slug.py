# Generated by Django 3.2.3 on 2022-05-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_products', '0009_auto_20220524_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=150),
        ),
    ]
