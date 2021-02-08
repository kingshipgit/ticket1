# Generated by Django 3.1.6 on 2021-02-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210207_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('last_name',)},
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together={('id', 'slug')},
        ),
        migrations.AlterIndexTogether(
            name='profile',
            index_together={('id', 'slug')},
        ),
    ]