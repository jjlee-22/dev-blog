# Generated by Django 2.2.6 on 2019-11-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191104_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='misc', max_length=200),
        ),
    ]