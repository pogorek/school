# Generated by Django 4.0.1 on 2022-02-25 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='author',
        ),
        migrations.RemoveField(
            model_name='like',
            name='posts',
        ),
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]