# Generated by Django 3.2.25 on 2024-04-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240415_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='customer_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
