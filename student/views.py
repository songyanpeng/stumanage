from django.shortcuts import render, HttpResponse, redirect
from .models import Student, Clas, Course, StudentDetail, AdminUser
from django.contrib import auth


# Create your views here.


def index(request):
    if request.user.username:
        # 获取所有学生数据
        student_list = Student.objects.all()

        return render(request, 'student/index.html', {'student_list': student_list})
    else:
        return redirect('/login')


def add_student(request):
    if request.method == 'GET':
        class_list = Clas.objects.all()
        course_list = Course.objects.all()

        return render(request, 'student/add_stu.html', {'class_list': class_list, 'course_list': course_list})
    else:
        # 获取客户端数据
        # name = request.POST.get('name')
        # age = request.POST.get('age')
        # sex = request.POST.get('sex')
        # birthday = request.POST.get('birthday')
        # clas_id = request.POST.get('clas_id')
        # tel = request.POST.get('tel')
        # addr = request.POST.get('addr')

        stu = Student.objects.create(**request.POST.dict())

        # <QueryDict: {'name': ['小明'], 'age': ['23'], 'sex': ['1'], 'birthday': ['2022-10-11'], 'tel': ['1212'], 'addr': ['河北'], 'clas_id': ['1']}>
        # 添加到数据库
        return redirect('/index')


def delete_student(request, del_id):
    student = Student.objects.get(id=del_id)

    if request.method == "GET":
        return render(request, 'student/delete_stu.html', {'student': student})
    else:

        Student.objects.get(id=del_id).delete()

        return redirect('/index')


def edit_student(request, edit_id):
    edit_stu = Student.objects.get(id=edit_id)
    if request.method == 'GET':

        class_list = Clas.objects.all()
        course_list = Course.objects.all()

        return render(request, "student/edit_stu.html",
                      {'edit_stu': edit_stu, 'course_list': course_list, 'class_list': class_list})
    else:
        data = request.POST.dict()

        Student.objects.filter(id=edit_id).update(**data)

        return redirect('/index')


def eletive(request):
    if request.method == 'GET':
        course_list = Course.objects.all()
        return render(request, 'student/course.html', {'course_list': course_list})
    else:

        course_id_list = request.POST.getlist('course_id_list')
        stu_id = 9
        stu = Student.objects.get(id=stu_id)
        stu.course.set(course_id_list)
        # print(course_id_list)

        return redirect('/student/index')


def search(request):
    student_list = []
    keyword = request.GET.get('keyword')
    cate = request.GET.get("cate")

    if cate == 'name':
        student_list = Student.objects.filter(name__contains=keyword)
    elif cate == 'class':
        student_list = Student.objects.filter(clas__name=keyword)

    return render(request, "student/search.html", {'student_list': student_list, 'keyword': keyword, "cate": cate})


def login(request):
    erro_msg = ''
    if request.method == 'GET':
        return render(request, 'student/login.html', {'erro_msg': erro_msg})

    else:
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        user = auth.authenticate(username=username, password=password)
        if user:

            auth.login(request, user)
            return redirect('/index')
        else:
            erro_msg = '用户名或密码错误'
            return render(request, 'student/login.html', {'erro_msg': erro_msg})


def register(request):
    if request.method == 'GET':
        return render(request, 'student/register.html')
    else:
        username = request.POST.get('registerUsername')
        password = request.POST.get('registerPassword')
        email = request.POST.get('registerEmail')
        AdminUser.objects.create_user(username=username, password=password, email=email)
        return redirect('/login')


def logout(request):
    auth.logout(request)

    return redirect('/login')


def edit_admin(request, admin_id):
    user = AdminUser.objects.get(id=admin_id)
    if request.method == 'GET':

        return render(request, 'student/edit_admin.html', {'username': user})
    else:
        user = request.user
        new_password = request.POST.get('newPassword')
        user.set_password(new_password)
        user.save()

        return redirect('/index')
