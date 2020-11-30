from django.shortcuts import get_object_or_404
from courses.models import Course
from courses.serializers import CourseSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def courses(req):
    if req.method == 'GET':
        courses = Course.objects.all()
        serialized = CourseSerializer(courses, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if req.method == 'POST':
        course = CourseSerializer(data=req.data)
        print(course)
        if course.is_valid():
            course.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400, data=course.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def course(req,course_id):
    course_obj = get_object_or_404(Course, id=course_id)
    if req.method == 'GET':
        serialized = CourseSerializer(course_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if req.method == 'PUT':
        serialized = CourseSerializer(instance=course_obj, data=req.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if req.method == 'DELETE':
        course_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)