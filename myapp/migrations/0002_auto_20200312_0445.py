# Generated by Django 3.0.3 on 2020-03-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]