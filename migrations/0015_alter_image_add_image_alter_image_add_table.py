# Generated by Django 4.1 on 2022-09-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("society_app", "0014_alter_image_add_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image_add",
            name="image",
            field=models.ImageField(upload_to="image"),
        ),
        migrations.AlterModelTable(name="image_add", table="image_add",),
    ]
