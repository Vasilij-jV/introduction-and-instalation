# Generated by Django 5.0.6 on 2024-06-08 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_one', '0003_alter_postone_auther'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='postone',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_one', to=settings.AUTH_USER_MODEL),
        ),
    ]
