# Generated by Django 3.2.3 on 2022-05-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_products', '0003_remove_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='peravia_products.Product'),
        ),
    ]
