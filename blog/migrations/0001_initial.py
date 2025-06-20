# Generated by Django 5.1.1 on 2025-05-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('published_date', models.DateField()),
                ('summary', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
            ],
        ),
    ]
