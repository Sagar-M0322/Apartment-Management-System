# Generated by Django 3.1.4 on 2021-04-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='flatownerinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doorno', models.CharField(max_length=19, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phono', models.CharField(default='SOME STRING', max_length=10)),
                ('name', models.CharField(default='SOME STRING', max_length=30)),
                ('faltno', models.CharField(default='SOME STRING', max_length=10)),
            ],
        ),
    ]
