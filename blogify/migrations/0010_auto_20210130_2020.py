# Generated by Django 2.2.1 on 2021-01-30 14:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogify', '0009_auto_20210130_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
