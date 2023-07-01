# Generated by Django 4.0.2 on 2023-06-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('user', models.CharField(max_length=255)),
                ('upload_rate', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(max_length=20)),
                ('extension', models.CharField(max_length=10)),
                ('duration', models.FloatField()),
                ('is_song', models.BooleanField()),
            ],
        ),
    ]
