from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from students.models import Student
from django.views import View
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from students.serializers import StudentSerializer
 


@api_view(['GET', 'POST'])
def students(req):
    if req.method == 'GET':
        
        students = Student.objects.all()
        
        serialized= StudentSerializer(students, many=True) 
    
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    
    if req.method == 'POST':
        
        student = StudentSerializer(data=req.data)
        
        
        if student.is_valid():
            student.save()
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=student.errros)
        
@api_view(['GET', 'PUT', 'DELETE'])
def student(req, student_id):
    
    student_obj = get_object_or_404(Student, id=student_id)
    
    if req.method == 'GET':
        
        serialized = StudentSerializer(student_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    
    if req.method == 'PUT':
        
         serialized = StudentSerializer(instance = student_obj, data= req.data, partial=True)
         
         if serialized.is_valid():
             
             serialized.save()
             return Response(status=status.HTTP_200_OK)
         
         else:
             
             return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
         
    if req.method == 'DELETE':
        
        student_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# def home(req):
#     return render(req, 'index/index.html', {})


# def get_student(req, id):
#     student = Student.objects.get(id=id)
#     classes = student.classes.all()
#     context = {
#         'student': student,
#         'classes': classes,
#     }
#     return render(req, 'students/student_single.html', context)

# template_form= 'students/student_form.html'
# http_method_names = ['get', 'post']

# class StudentView(View):
#     template_name=''
#     all_students = 'students/index.html'

#     def get(self, req):

#         students = Student.objects.all()
#         context = {
#             'students': students
#         }
#         print(req)
#         return render(req, self.all_students, context)


#     def post(self, req):
#         student_data={
#             'name' : req.POST['name'],
#             'last_name' : req.POST['lastname'],
#             'age' : int(req.POST['age']),
#             'email' : req.POST['email']
#         }
#         print(student_data)
#         Student.objects.create(**student_data)
#         return render(req, self.all_students,{})

# class StudentFormView(View):

#     def get(self, req):
#        return render(req, template_form, {})
