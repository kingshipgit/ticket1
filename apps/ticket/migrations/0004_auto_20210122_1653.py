# Generated by Django 3.1.5 on 2021-01-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_remove_comment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='ticket',
        ),
    ]
