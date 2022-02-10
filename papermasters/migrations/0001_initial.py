# Generated by Django 4.0.1 on 2022-02-10 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_text', models.CharField(max_length=100)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('content_two', models.TextField(blank=True)),
                ('lower_content', models.TextField(blank=True)),
                ('old_url', models.URLField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='subtopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic_text', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('content_two', models.TextField(blank=True)),
                ('lower_content', models.TextField(blank=True)),
                ('old_url', models.URLField(blank=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papermasters.subject')),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_text', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('related', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
                ('image_url', models.URLField(blank=True)),
                ('lower_content', models.TextField(blank=True)),
                ('old_url', models.URLField(blank=True)),
                ('update_date', models.DateTimeField(default='2022-01-31T15:58:44.767594-06:00', verbose_name='Last Updated')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papermasters.subject')),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papermasters.subtopic')),
            ],
        ),
    ]
