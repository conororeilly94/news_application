# Generated by Django 3.0.7 on 2020-07-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_main_abouttxt'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='seo_keywords',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='seo_txt',
            field=models.CharField(default='-', max_length=200),
        ),
    ]