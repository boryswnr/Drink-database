# Generated by Django 4.0.4 on 2022-06-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakerApp', '0013_alter_drinkrecipe_drinkimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkrecipe',
            name='drinkImage',
            field=models.ImageField(default='no-photo.png', upload_to='static/shakerApp/media'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ingredientImage',
            field=models.ImageField(default='no-photo.png', upload_to='static/shakerApp/media'),
        ),
    ]