# Generated by Django 5.1.1 on 2024-11-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_user_options_user_date_joined_user_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='role',
            field=models.CharField(default='Physiotherapist', max_length=60),
            preserve_default=False,
        ),
    ]
