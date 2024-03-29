# Generated by Django 5.0.1 on 2024-02-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peravia_team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='persian_family',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='persian_name',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='persian_position',
            field=models.CharField(blank=True, choices=[('Co-Founder & CEO', 'Co-Founder & CEO'), ('International Procurement Manager', 'International Procurement Manager'), ('Procurement Manager', 'Procurement Manager'), ('Administrative Manager', 'Administrative Manager'), ('Financial Manager', 'Financial Manager'), ('Industrial Accountant', 'Industrial Accountant'), ('IT Manager', 'IT Manager'), ('Brand Manager', 'Brand Manager')], default='', max_length=200, null=True),
        ),
    ]
