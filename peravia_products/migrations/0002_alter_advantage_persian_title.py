# Generated by Django 5.0.1 on 2024-02-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='persian_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
