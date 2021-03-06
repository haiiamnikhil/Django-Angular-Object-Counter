from django.shortcuts import render
from django.http import JsonResponse
from .models import Reports, UploadData, UserModel
from .detector import detector
import os
import cv2 as cv
from PIL import Image
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from .serializer import CsvSerializer, DetectionSerializer, UserSerializer
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password


@csrf_exempt
def single_image_processor(request):
    if request.method == 'POST':
        mode = 'single_object_detection'
        detectType = request.POST.get('detectType')
        file = request.FILES.get('image')
        
        data = UploadData.objects.create(user=request.user,image=file)
        filename = data.image.name.split('/')[1]
        
        count, count_objects = detector.detect(filename,detectType,mode)
        
        cv.imwrite(os.path.join('media/singledetection',f'{filename}'),count_objects)
        
        name = filename.split('.')[0]
        data.filename=name 
        data.singledetection = f"singledetection/{filename}"
        data.save()
        
        processed_data = UploadData.objects.filter(filename=name)
        
        try:
            serializer = DetectionSerializer(processed_data,many=True)
            return JsonResponse({'data':serializer.data,'status':True,'count':count},safe=False,status=200)
        except:
            return JsonResponse({'status':False},safe=False,status=200)


@csrf_exempt
def multi_image_processor(request):
    filenames = []
    count = []
    detected_details = []
    if request.method == 'POST':
        mode = 'multi_object_detection'
        
        for file in request.FILES.getlist('imagefiles'):
            # original_file_name.append(file._name)
            dataType = request.POST.get('detection_type')
            data = UploadData.objects.create(user=request.user,image=file)
            filename = data.image.name.split('/')[1]
            
            getCount, getDetection = detector.detect(filename,dataType,mode)
            
            cv.imwrite(os.path.join('media/multidetection',filename),getDetection)
            
            name = filename.split('.')[0]
            data.filename = name
            data.multidetection = f"multidetection/{filename}"
            data.count = getCount
            data.save()
        
            filenames.append(name)
            count.append(getCount)

        
        for data in filenames:
            getDetails = UploadData.objects.filter(filename = data)
            imageSerilaizer = DetectionSerializer(getDetails,many=True)
            detected_details.append(imageSerilaizer.data)
            
        
        data = {'Files':filenames,'Count':count}
        df = pd.DataFrame(data)
        
        try:os.mkdir(os.path.join('./media','reports'))
        except:pass
        
        df.to_csv(os.path.join('media/reports',f"{name}.csv"),index=None)
        
        csv_name = f"reports/{name}.csv"
        reports = Reports.objects.get_or_create(filename=name,report=csv_name)
        
        serializer = CsvSerializer(reports,many=True)

        return JsonResponse({"status":True,"csv":serializer.data,"data":detected_details},safe=False,status=200)


@csrf_exempt
def registerAuth(request):
    if request.method == 'POST':
        credentials = JSONParser().parse(request)
        
        if UserModel.objects.filter(username=credentials['username']).exists() or UserModel.objects.filter(email=credentials['email']).exists():
            return JsonResponse({"status":False,"message":"User With Same Username or Email Exists"},safe=False,status=200)
        
        else:
            user = UserModel.objects.create(
            username=credentials['username'],
            password=make_password(credentials['password']),
            email=credentials['email'],
            full_name = f"{credentials['first_name'] } {credentials['last_name']}",
            organisation_name=credentials['organisation_name'],
            organisation_strength = credentials['organisation_strength'],
            organisation_type = credentials['organisation_type'],
            organisation_email = credentials['organisation_email']
            )
            return JsonResponse({'status':True,"message":"User Created"},safe=False,status=200)


@csrf_exempt
def loginAuth(request):
    if request.method == 'POST':
        auth = JSONParser().parse(request)
        user = authenticate(username=auth['username'],password=auth['password'])
        if user:
            login(request,user)
            return JsonResponse({'status':True},safe=False,status=200)
        else:
            return JsonResponse({'status':False},safe=False,status=200)


@csrf_exempt
def isLoggedIn(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return JsonResponse({'status':True,'message':'User Alredy Logged In'})
        else:
            return JsonResponse({'status':False})


@csrf_exempt
def userDetails(request):
    if request.method == 'GET':
        user = UserModel.objects.filter(username=request.user)
        getCount = UploadData.objects.filter(user=request.user).count()
        serializer = UserSerializer(user,many=True)
        return JsonResponse({'status':True,'message':serializer.data},safe=False,status=200)


@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'status':True},safe=False,status=200)
    
    
def home(request):
    return render(request,"demo.html")


def singledetector(request):
    return render(request, 'upload.html')


def showimage(request):
    return render(request, 'showimage.html')


def multi_detector(request):
    return render(request, 'multidetector.html')


def multi_detector_processor(request):
    return render(request, 'detector.html')


@csrf_exempt
def loginView(request):
    return render(request, 'login.html')


@csrf_exempt
def registerView(request):
    return render(request, 'register.html')


def userProfileView(request):
    return render(request, 'profile.html')