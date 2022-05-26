# Generated by Django 4.0.4 on 2022-05-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Name of food')),
                ('author', models.CharField(max_length=35, verbose_name='from author')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='food/%Y/%m')),
            ],
        ),
    ]