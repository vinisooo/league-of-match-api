# Generated by Django 4.2 on 2023-05-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='user',
            name='route',
            field=models.TextField(blank=True, choices=[('Toplane', 'Toplane'), ('Jungle', 'Jungle'), ('Midlane', 'Midlane'), ('Adc', 'Adc'), ('Support', 'Support')], max_length=10, null=True),
        ),
    ]