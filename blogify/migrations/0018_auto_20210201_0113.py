# Generated by Django 2.2.1 on 2021-01-31 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogify', '0017_auto_20210131_0214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
