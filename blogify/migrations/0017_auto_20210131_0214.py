# Generated by Django 2.2.1 on 2021-01-30 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogify', '0016_auto_20210131_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blogs_connected',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
    ]
