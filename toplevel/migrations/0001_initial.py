# Generated by Django 4.0.1 on 2022-01-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.CharField(max_length=400)),
                ('content', models.TextField(blank=True)),
                ('old_url', models.URLField(blank=True)),
                ('lower_content', models.TextField(blank=True)),
                ('type_of_resource', models.CharField(choices=[('E', 'Elements of a Paper'), ('R', 'Type of Research'), ('P', 'Type of Paper')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('meta_description', models.CharField(max_length=400)),
                ('content', models.TextField(blank=True)),
                ('old_url', models.URLField(blank=True)),
                ('lower_content', models.TextField(blank=True)),
            ],
        ),
    ]
