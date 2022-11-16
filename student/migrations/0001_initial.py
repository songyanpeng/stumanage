# Generated by Django 3.2 on 2022-10-07 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='班级名称')),
            ],
            options={
                'db_table': 'db_class',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48, verbose_name='课程名称')),
            ],
            options={
                'db_table': 'db_course',
            },
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=11, verbose_name='电话号码')),
                ('addr', models.CharField(max_length=64, verbose_name='地址')),
            ],
            options={
                'db_table': 'db_stu_detail',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('age', models.SmallIntegerField(default=18, verbose_name='年龄')),
                ('sex', models.SmallIntegerField(choices=[(0, '女'), (1, '男'), (2, '保密')], verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_list', to='student.clas')),
                ('course', models.ManyToManyField(db_table='db_student2course', related_name='students', to='student.Course')),
                ('stu_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stu', to='student.studentdetail')),
            ],
            options={
                'db_table': 'db_student',
            },
        ),
    ]
