# Generated by Django 3.2.5 on 2021-07-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=20)),
                ('description', models.TextField(default='', max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]