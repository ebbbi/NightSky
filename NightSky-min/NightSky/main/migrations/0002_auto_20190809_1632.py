# Generated by Django 2.2.3 on 2019-08-09 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]