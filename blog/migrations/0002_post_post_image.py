# Generated by Django 2.2.6 on 2019-11-04 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='blog/media/', upload_to='blog/media/'),
        ),
    ]