# Generated by Django 2.2.1 on 2019-05-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
            ],
        ),
    ]
