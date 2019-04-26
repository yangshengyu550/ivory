# Generated by Django 2.1.7 on 2019-04-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doubanmovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('actor', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('rate', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'doubanmovie',
                'managed': True,
            },
        ),
    ]