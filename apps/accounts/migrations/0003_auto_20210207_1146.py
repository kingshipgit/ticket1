# Generated by Django 3.1.6 on 2021-02-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210207_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ext',
            field=models.CharField(max_length=50, null=True, verbose_name='extension'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=200, null=True, verbose_name='last_name'),
        ),
    ]
