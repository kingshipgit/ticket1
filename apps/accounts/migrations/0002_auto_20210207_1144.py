# Generated by Django 3.1.6 on 2021-02-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='first_name'),
        ),
    ]
