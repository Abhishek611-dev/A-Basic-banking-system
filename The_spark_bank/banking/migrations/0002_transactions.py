# Generated by Django 3.1.4 on 2021-08-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('sender', models.CharField(max_length=300)),
                ('receiver', models.CharField(max_length=300)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
