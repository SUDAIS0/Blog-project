# Generated by Django 5.0.2 on 2024-09-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='captions',
            field=models.ManyToManyField(null=True, to='blog.tag', verbose_name='blogs'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='imageName',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
