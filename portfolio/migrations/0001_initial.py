# Generated by Django 3.2.7 on 2021-10-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
