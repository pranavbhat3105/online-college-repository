from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

def staff_home(request):
    return render(request, "staff_templates/home_content.html")

#def staff_take_attendace(request):
 #   return render(request,"staff_template/staff_take_attendance.html")