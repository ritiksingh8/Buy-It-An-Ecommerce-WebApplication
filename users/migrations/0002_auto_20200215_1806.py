# Generated by Django 2.2.6 on 2020-02-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]