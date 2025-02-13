from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0010_messagemodel_threadmodel'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Image',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('image', models.ImageField(blank=True, null=True, upload_to='uploads/post_photos')),
        #     ],
        # ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on', '-shared_on']},
        ),
        migrations.AddField(
            model_name='notification',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.threadmodel'),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        # migrations.AddField(
        #     model_name='post',
        #     name='image',
        #     field=models.ManyToManyField(blank=True, to='social.Image'),
        # ),
    ]
