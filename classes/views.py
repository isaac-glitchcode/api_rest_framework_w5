from django.shortcuts import render
from classes.models import Class

def get_classes(req):
    classes = Class.objects.all()
    context = {
        'classes' : classes
    }
    return render(req,'classes/index.html', context)

def get_class(req, id):
    class_ = Class.objects.get(id=id)
    students = class_.students.all()
    context = {
        'class_' : class_,
        'students':students
    }
    return render(req,'classes/class_students.html', context)
