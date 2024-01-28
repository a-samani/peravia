# Generated by Django 3.2.3 on 2022-04-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_blog', '0004_alter_blogpost_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-updated_on'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
