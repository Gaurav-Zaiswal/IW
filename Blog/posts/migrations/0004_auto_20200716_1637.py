# Generated by Django 3.0.8 on 2020-07-16 10:52

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200716_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_img',
            field=models.ImageField(max_length=52, upload_to=posts.models.thumbnail_path),
        ),
    ]