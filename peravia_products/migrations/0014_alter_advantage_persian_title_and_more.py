# Generated by Django 5.0.1 on 2024-02-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_products', '0013_alter_category_persian_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='persian_title',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='persian_description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='persian_title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='persian_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='persian_title',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specification',
            name='persian_title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]