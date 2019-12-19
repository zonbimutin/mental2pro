# Generated by Django 3.0 on 2019-12-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('ville', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('longitud', models.DecimalField(decimal_places=50, max_digits=50)),
                ('latitud', models.DecimalField(decimal_places=50, max_digits=50)),
                ('zipe_code', models.IntegerField()),
            ],
        ),
    ]
