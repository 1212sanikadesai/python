# Generated by Django 4.2.1 on 2024-11-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_customuser_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="profile_pictures\\default-avatar.jpeg",
                null=True,
                upload_to="profile_pictures/",
            ),
        ),
    ]
