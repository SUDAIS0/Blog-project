# Generated by Django 5.0.2 on 2024-09-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_about_alter_post_captions_alter_post_excerpt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(null=True),
        ),
    ]
