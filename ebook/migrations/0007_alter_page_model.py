# Generated by Django 4.2 on 2023-04-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ebook", "0006_rename_swiftxr_link_page_site_url_page_site_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="model",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
