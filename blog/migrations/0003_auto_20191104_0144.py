# Generated by Django 2.2.6 on 2019-11-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='media/noimage/noimage.jpg', upload_to='media/'),
        ),
    ]
