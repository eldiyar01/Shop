# Generated by Django 3.1.3 on 2020-11-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0003_auto_20201127_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]