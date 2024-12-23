# Generated by Django 5.1.3 on 2024-12-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'film',
                'managed': False,
            },
        ),
    ]
