# Generated by Django 4.2 on 2023-12-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("destinations", "0009_destinationcomment_delete_destination_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="destination",
            name="image",
            field=models.ImageField(
                default="staticfiles/img/dest/no_image.jpg",
                upload_to="static/img/dest/",
            ),
        ),
    ]