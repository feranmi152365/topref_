# Generated by Django 3.1.1 on 2021-02-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.CharField(max_length=500),
        ),
    ]
