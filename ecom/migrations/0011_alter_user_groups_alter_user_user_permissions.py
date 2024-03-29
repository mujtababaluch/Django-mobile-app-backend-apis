# Generated by Django 4.2.2 on 2023-07-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ecom', '0010_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='custom_users_group', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='custom_users_permission', to='auth.permission'),
        ),
    ]
