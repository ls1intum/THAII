# Generated by Django 5.0.4 on 2024-05-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_page_parent_page_alter_page_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
