# Generated by Django 3.0.7 on 2020-06-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_main_picname'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl2',
            field=models.TextField(default=''),
        ),
    ]
