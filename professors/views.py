from django.shortcuts import get_object_or_404
from professors.models import Professor
from professors.serializers import ProfessorSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def professors(req):
    if req.method == 'GET':
        professors = Professor.objects.all()
        serialized = ProfessorSerializer(professors, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if req.method == 'POST':
        professor = ProfessorSerializer(data=req.data)
        if professor.is_valid():
            professor.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=professor.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def professor(req, professor_id):
    professor_obj = get_object_or_404(Professor, id=professor_id)
    
    if req.method == 'GET':
        serialized = ProfessorSerializer(professor_obj)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if req.method == 'PUT':
        serialized = ProfessorSerializer(instance=professor_obj, data=req.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized.errors)
    if req.method == 'DELETE':
        professor_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)