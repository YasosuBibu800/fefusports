# Generated by Django 4.2.7 on 2024-01-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_ref_vk'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='ref_tg',
            field=models.URLField(blank=True),
        ),
    ]
