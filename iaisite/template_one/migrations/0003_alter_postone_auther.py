# Generated by Django 5.0.6 on 2024-06-08 11:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_one', '0002_rename_post_postone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='postone',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post_one', to=settings.AUTH_USER_MODEL),
        ),
    ]
