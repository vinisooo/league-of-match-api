# Generated by Django 4.2 on 2023-05-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_discord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
