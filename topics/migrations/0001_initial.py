# Generated by Django 4.0.1 on 2022-03-07 13:47

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='topics.category')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('topic_text', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('related', models.TextField(blank=True)),
                ('old_url', models.CharField(blank=True, max_length=255)),
                ('new_url', models.CharField(blank=True, max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('categories', mptt.fields.TreeManyToManyField(to='topics.Category')),
            ],
        ),
    ]
