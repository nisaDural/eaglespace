# Generated by Django 5.0.6 on 2024-06-08 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_comment_tags_post_image_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
