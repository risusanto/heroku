from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import numpy as np
import cv2
import os
import time

from food_ai.utils import recognize

def api_check(request):
    data = {
        'status': 'ok',
        'method': request.method
    }
    return JsonResponse(data)

def recognize_food(request):
    data = {
        'status': 'ok',
        'method': request.method
    }
    if request.method == 'POST' and request.FILES['img_data']:
        start_time = time.time()
        img_data = request.FILES['img_data']
        cls_name, acc = recognize(img_data)

        cls_name = cls_name.replace('_',' ')
        cls_name = ' '.join(word[0].upper() + word[1:] for word in cls_name.split())

        data['cls_name'] = cls_name
        data['acc'] = acc
        data['time'] = "%.2f" % (time.time() - start_time)

        return JsonResponse(data)
    
    return JsonResponse(data)


