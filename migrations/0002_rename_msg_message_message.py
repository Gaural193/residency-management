# Generated by Django 4.1 on 2022-08-30 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("society_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message", old_name="msg", new_name="Message",
        ),
    ]
