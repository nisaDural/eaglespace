# Generated by Django 5.0.6 on 2024-06-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_merge_0011_auto_20210524_2200_0012_auto_20210515_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(blank=True, to='social.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(blank=True, to='social.image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='threadmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
