# Generated by Django 3.0 on 2021-05-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('foto', models.TextField()),
                ('educacion', models.CharField(max_length=100)),
                ('experiencia', models.TextField()),
            ],
        ),
    ]