# Generated by Django 2.2.3 on 2019-07-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('driver', models.CharField(choices=[('ORACLE', 'ORACLE_DB'), ('SYBASE', 'SYBASE_DB')], max_length=20)),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
