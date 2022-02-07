# Generated by Django 4.0.1 on 2022-02-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papermasters', '0005_topic_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='subject',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='subject',
            name='old_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='related',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='subject',
            name='update_date',
            field=models.DateTimeField(default='2022-01-31T15:58:44.767594-06:00', verbose_name='Last Updated'),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='old_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='related',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='subtopic',
            name='update_date',
            field=models.DateTimeField(default='2022-01-31T15:58:44.767594-06:00', verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
