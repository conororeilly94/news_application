# Generated by Django 3.0.7 on 2020-06-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_main_picurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname',
            field=models.TextField(default=''),
        ),
    ]
