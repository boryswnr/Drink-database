# Generated by Django 4.0.4 on 2022-05-31 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakerApp', '0006_drinkrecipe_utensil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkrecipe',
            name='preparation',
            field=models.TextField(max_length=1000),
        ),
    ]
