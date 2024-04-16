# Generated by Django 3.2.25 on 2024-04-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240415_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='business_trip',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='contact_information',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='contract',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='current_process',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='customer_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='one_word_appeal',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='post',
            name='period',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='person',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='project_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='status_status',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='unit_price',
            field=models.CharField(max_length=200),
        ),
    ]
