# Generated by Django 4.1 on 2022-09-01 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("society_app", "0002_rename_msg_message_message"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message", old_name="Message", new_name="Msg",
        ),
    ]
