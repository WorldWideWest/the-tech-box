# Generated by Django 4.0.5 on 2022-06-26 12:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cover_image', models.ImageField(upload_to='media/cover_images/')),
            ],
        ),
    ]
