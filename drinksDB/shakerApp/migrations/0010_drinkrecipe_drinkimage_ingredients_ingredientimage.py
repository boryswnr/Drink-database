# Generated by Django 4.0.4 on 2022-06-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakerApp', '0009_rename_drinkname_drinkrecipe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkrecipe',
            name='drinkImage',
            field=models.ImageField(default='no-photo.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='ingredientImage',
            field=models.ImageField(default='no-photo.png', upload_to=''),
        ),
    ]
