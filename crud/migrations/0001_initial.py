# Generated by Django 3.2.9 on 2021-12-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rn', models.IntegerField()),
                ('username', models.CharField(default='none', max_length=64, null=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
