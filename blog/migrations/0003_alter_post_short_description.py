# Generated by Django 5.1.1 on 2024-12-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short_description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
