from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/',postStudent),
    path('add-teacher/',postTeacher),
    path('get-student/',getStudent),
    path('get-teacher/',getTeacher),
    path('edit-student/<id>',editStudentData),
    path('update-student/<id>',updateStudentData),
    path('delete-student/<id>',deleteStudentData)
]