# Generated by Django 2.2.6 on 2019-11-06 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191105_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, default='img/noimage/noimage.jpg', null=True, upload_to='c_img/'),
        ),
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
