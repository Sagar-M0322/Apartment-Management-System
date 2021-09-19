# Generated by Django 3.1.4 on 2021-05-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart', '0027_auto_20210501_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aptno', models.CharField(max_length=10)),
                ('area', models.IntegerField(max_length=10)),
                ('Bathroom', models.IntegerField(max_length=12)),
                ('Bedroom', models.IntegerField(max_length=12)),
                ('parking', models.IntegerField(max_length=12)),
            ],
        ),
    ]
