# Generated by Django 3.1 on 2020-08-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_petstore_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstore',
            name='latitude',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='petstore',
            name='longitude',
            field=models.CharField(default='', max_length=12),
        ),
    ]
