from django.shortcuts import render

from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers,TeacherSerializers
#Create your views here
@api_view(['POST'])
def postStudent(request):
     try:
          request_data= request.data
          serializer = StudentSerializers(data=request_data,many= False)
          if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response({'message':"student added sucessfully"}) 
     except Exception as e:
          return Response(e)
     
@api_view(['POST'])
def postTeacher(request):
     try:
          request_data= request.data
          serializer = TeacherSerializers(data=request_data,many= False)
          if serializer.is_valid(raise_exception=True):
               serializer.save()
               return Response({'message':"Teacher added sucessfully"}) 
     except Exception as e:
          return Response({"err":e})
     
@api_view(['GET'])
def getStudent(request):
     try:
          students = Student.objects.all()
          serialized_data = StudentSerializers(students, many=True)  
          return Response(serialized_data.data)
     except Exception as e:
         return Response({"err":e})
     
@api_view(['GET'])
def getTeacher(request):
     try:
          teacher = Teacher.objects.all()
          serialized_data = TeacherSerializers(teacher, many=True)  
          return Response(serialized_data.data)
     except Exception as e:
         return Response({"err":e})
     
@api_view(['GET'])
def editStudentData(request,id):
     try:
          student=Student.objects.get(id=id)
          serialized_data = StudentSerializers(student, data=request.data,many=False,partial = True)
     except Exception as e:
          return Response([serialized_data.data])

@api_view(['post'])
def updateStudentData(request, id):
     try:
          student= Student.objects.get(id=id)
          serialized_data= StudentSerializers(student,data=request.data,many =False,partial=True)
          if serialized_data.is_valid(raise_exception=True):
               serialized_data.save()
               return Response({"message":"data updated sucessfully","data":serialized_data.data}) 
     except Exception as e:
          return Response({"err":e}) 

@api_view(['GET'])
def deleteStudentData(request, id):
     try:
          student=Student.objects.get(id=id)
          student.delete()
          return Response({"message":"data deleted sucessfully"})
     except Exception as e:
          return Response({'err':e})

     
          



     
             

     