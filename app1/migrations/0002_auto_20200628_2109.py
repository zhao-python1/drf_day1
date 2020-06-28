# Generated by Django 2.0.6 on 2020-06-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'other')], default=0)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'me_user',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
