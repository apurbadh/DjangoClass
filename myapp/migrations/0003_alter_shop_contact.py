# Generated by Django 3.2.6 on 2021-09-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210910_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]