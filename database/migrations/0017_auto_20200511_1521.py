# Generated by Django 2.2.10 on 2020-05-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20200511_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='headline',
            field=models.BooleanField(default=True),
        ),
    ]
