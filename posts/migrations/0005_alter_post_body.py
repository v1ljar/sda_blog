# Generated by Django 4.2.7 on 2023-11-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_created_at_post_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, default=''),
        ),
    ]
