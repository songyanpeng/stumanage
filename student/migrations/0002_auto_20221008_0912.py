# Generated by Django 3.2 on 2022-10-08 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stu_detail',
        ),
        migrations.AddField(
            model_name='student',
            name='addr',
            field=models.CharField(max_length=64, null=True, verbose_name='家庭住址'),
        ),
        migrations.AddField(
            model_name='student',
            name='tel',
            field=models.CharField(max_length=11, null=True, verbose_name='电话号码'),
        ),
    ]
