# Generated by Django 3.2.16 on 2022-11-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.FileField(upload_to='Pictures/'),
        ),
    ]
