# Generated by Django 3.2.3 on 2022-04-14 15:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_blog', '0007_alter_blogpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='contents'),
        ),
    ]
