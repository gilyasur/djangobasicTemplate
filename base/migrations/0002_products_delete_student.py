# Generated by Django 4.2.6 on 2023-10-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
