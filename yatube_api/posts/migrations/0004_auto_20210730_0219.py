# Generated by Django 2.2.6 on 2021-07-29 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_auto_20210729_2356"),
    ]

    operations = [
        migrations.RenameField(
            model_name="follow",
            old_name="author",
            new_name="following",
        ),
    ]
