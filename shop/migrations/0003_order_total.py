# Generated by Django 2.2.6 on 2019-12-21 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]