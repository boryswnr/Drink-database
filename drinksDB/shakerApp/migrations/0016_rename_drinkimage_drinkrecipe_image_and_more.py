# Generated by Django 4.0.4 on 2022-06-06 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shakerApp', '0015_alter_drinkrecipe_drinkimage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinkrecipe',
            old_name='drinkImage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='ingredients',
            old_name='ingredientImage',
            new_name='image',
        ),
    ]
