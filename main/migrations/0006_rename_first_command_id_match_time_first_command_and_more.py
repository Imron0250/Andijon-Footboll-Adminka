# Generated by Django 4.1.7 on 2023-04-02 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_first_command_match_time_first_command_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match_time',
            old_name='first_command_id',
            new_name='first_command',
        ),
        migrations.RenameField(
            model_name='match_time',
            old_name='second_command_id',
            new_name='second_command',
        ),
    ]
