# Generated by Django 3.0 on 2019-12-31 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='需求')),
                ('tool', models.CharField(max_length=20, verbose_name='工具')),
                ('url', models.URLField(verbose_name='参考地址')),
            ],
        ),
    ]
