# Generated by Django 3.1.3 on 2020-12-07 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201206_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='purchases',
            field=models.IntegerField(default=0),
        ),
    ]
