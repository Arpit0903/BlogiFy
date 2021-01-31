# Generated by Django 2.2.1 on 2021-01-28 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogify', '0005_auto_20210128_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
