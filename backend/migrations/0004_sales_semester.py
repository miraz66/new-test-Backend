# Generated by Django 4.2.2 on 2023-06-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=20),
        ),
    ]