# Generated by Django 4.1.5 on 2023-02-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_kiosco', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
