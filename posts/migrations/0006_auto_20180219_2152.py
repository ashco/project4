# Generated by Django 2.0.2 on 2018-02-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20180219_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
