# Generated by Django 4.1.5 on 2023-02-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='article_pics'),
        ),
    ]
