# Generated by Django 4.1.5 on 2023-02-07 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpart', '0004_tags_alter_post_image_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='name',
            new_name='category',
        ),
    ]