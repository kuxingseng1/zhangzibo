# Generated by Django 3.0.8 on 2020-09-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rookie', '0003_remove_custom_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='user',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
