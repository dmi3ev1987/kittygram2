# Generated by Django 3.2.3 on 2024-03-31 12:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0002_cat_unique_name_owner'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='cat',
            name='unique_name_owner',
        ),
        migrations.AlterUniqueTogether(
            name='cat',
            unique_together={('name', 'owner')},
        ),
    ]
