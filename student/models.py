from django.db import models


# Create your models here.

class Student(models.Model):
    sex_choice = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
    )
    name = models.CharField(max_length=32, null=False, verbose_name='姓名')
    age = models.SmallIntegerField(default=18, verbose_name='年龄')
    sex = models.SmallIntegerField(choices=sex_choice, verbose_name='性别')
    birthday = models.DateField(verbose_name='生日')
    tel = models.CharField(max_length=11, null=True, verbose_name='电话号码')
    addr = models.CharField(max_length=64, null=True, verbose_name='家庭住址')

    # 建立一对多关系：数据库关联字段 clas_id
    clas = models.ForeignKey(to='Clas', on_delete=models.CASCADE, related_name='student_list')

    # 建立多对多关系：创建第三张关系表
    course = models.ManyToManyField('Course', db_table='db_student2course', related_name='students')

    # 一对一的关系：建立关联字段
    # stu_detail = models.OneToOneField('StudentDetail', on_delete=models.CASCADE, related_name='stu')

    class Meta:
        db_table = 'db_student'


class Clas(models.Model):
    name = models.CharField(max_length=32, null=False, verbose_name='班级名称')

    class Meta:
        db_table = "db_class"


class Course(models.Model):
    title = models.CharField(max_length=48, null=False, verbose_name='课程名称')
    credit = models.IntegerField(verbose_name='学分', default=3)
    teacher = models.CharField(max_length=32, verbose_name='教师', null=True)
    classTime = models.CharField(max_length=32, verbose_name='上课时间', null=True)
    classAddr = models.CharField(max_length=32, verbose_name='上课地点', null=True)

    class Meta:
        db_table = "db_course"


class StudentDetail(models.Model):
    tel = models.CharField(max_length=11, verbose_name='电话号码')
    addr = models.CharField(max_length=64, verbose_name='地址')

    class Meta:
        db_table = 'db_stu_detail'


from django.contrib.auth.models import AbstractUser


class AdminUser(AbstractUser):
    pass

    class Meta:
        db_table = 'db_admin_user'
