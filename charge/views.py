from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from paking.models import *
from paking.models import *
from .paytime import ShouldToPay
# Create your views here.
import numpy as np
import cv2
import time
import os
from .predict import get_result as gs
from .kears_vgg import get_result as gp
import json
from PIL import Image
import datetime
__author__ = 'Haiy'
## This example create by Haiy in 2019-03-18
## It includes some basic function about the Parking lot
## PLEASE NOTE: This example maybe have some bug
## If you have trouble installing it, try any of the other demos
## that don't require it instead.


def Carinprot(request):
    folder_path = 'images'
    # 捕捉帧，笔记本摄像头设置为0即可
    capture = cv2.VideoCapture(0)
    # 循环显示帧
    while (capture.isOpened()):
        ret, frame = capture.read()
        # 显示窗口第一个参数是窗口名，第二个参数是内容
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            timestr = time.strftime('%Y%m%d%H%M%S', time.localtime())
            capture.release()
            cv2.destroyAllWindows()
            isExists = os.path.exists(folder_path)
            if not isExists:
                os.mkdir(folder_path)
            # cv2.imwrite(os.path.join(folder_path, timestr+'.jpg'), frame)
            # car_type = gp(frame)
            # if car_type == "未找到匹配车型":
            #     return False
            # else:
            #     car_sign = gs(frame)
            #     car_sign = ''.join(car_sign)
            #     data = {'car_type':car_type,'car_sign':car_sign, 'time':timestr}
            #     return data
            car_type = '小型车'
            car_sign = '川AA662F'
            data = {'car_type': car_type, 'car_sign': car_sign, 'time': timestr}
            return data
        elif k == ord('q'):
            break
    return HttpResponse('')


def car_in(request):
    data = Carinprot(request)
    if data is False:
        return HttpResponse(json.dumps({"result":False, "data":"", "error":"未找到匹配车型"}))
    else:
        car_type = data["car_type"]
        if car_type == "小型车":
            car = 0
        elif car_type == '中型车':
            car = 1
        elif car_type == '大型车':
            car = 2
        car_sign = data["car_sign"]
        car_in_time = data["time"]
        for root, dirs, files in os.walk('images'):
            for file in files:
                if os.path.splitext(file)[0] == car_in_time:
                    car_in_picture = file
        dt = datetime.datetime.strptime(car_in_time, "%Y%m%d%H%M%S")
        # Car.objects.create(type=car, carplate=car_sign, inimg=car_in_picture,in_time=dt)
        Car.objects.filter(carplate=car_sign).update(in_time=dt)
        return HttpResponse("{0}在{1}成功驶入".format(car_sign, dt))


def Caroutprot(request):
    folder_path = 'images'
    # 捕捉帧，笔记本摄像头设置为0即可
    capture = cv2.VideoCapture(0)
    # 循环显示帧
    while (capture.isOpened()):
        ret, frame = capture.read()
        # 显示窗口第一个参数是窗口名，第二个参数是内容
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            timestr = time.strftime('%Y%m%d%H%M%S', time.localtime())
            capture.release()
            cv2.destroyAllWindows()
            isExists = os.path.exists(folder_path)
            if not isExists:
                os.mkdir(folder_path)
            cv2.imwrite(os.path.join(folder_path, timestr+'.jpg'), frame)
            # car_type = gp(frame)
            # if car_type == "未找到匹配车型":
            #     return False
            # else:
            # car_sign = gs(frame)
            # car_sign = ''.join(car_sign)
            data = {'car_sign':'川AA662F', 'time':timestr}
            return data
        elif k == ord('q'):
            break
    return HttpResponse('')


def car_out(request):
    data = Caroutprot(request)
    # if data is False:
    #     return HttpResponse(json.dumps({"result":False, "data":"", "error":"未找到匹配车型"}))
    car_sign = data["car_sign"]
    car_out_time = data["time"]
    for root, dirs, files in os.walk('images'):
        for file in files:
            if os.path.splitext(file)[0] == car_out_time:
                car_out_picture = file
    dt = datetime.datetime.strptime(car_out_time, "%Y%m%d%H%M%S")
    car = Car.objects.filter(carplate=car_sign)
    car_type = car[0].type
    car_stad = Standard.objects.filter(cartype=car_type)
    f_time = car_stad[0].start_time
    f_time = f_time.strftime("%H%M%S")
    s_time = car_stad[0].end_time
    s_time = s_time.strftime("%H%M%S")
    early_money = car_stad[0].night_money
    day_money = car_stad[0].day_money
    night_money = car_stad[0].night_money
    all_day_money = car_stad[0].all_day_money
    per_se_money = car_stad[0].time_unit
    if car:
        car.update(outimg=car_out_picture, out_time=dt)
        # car.update(out_time=dt)
        out_time = car[0].out_time
        in_time = car[0].in_time
        out_time_str = datetime.datetime.strftime(out_time, "%Y%m%d%H%M%S")
        in_time_str = datetime.datetime.strftime(in_time, "%Y%m%d%H%M%S")
        day = (out_time-in_time).days
        second = (out_time-in_time).seconds
        minute = second
        result = ShouldToPay(in_time_str, out_time_str, f_time, s_time, early_money, day_money, night_money, all_day_money, per_se_money)
        total_money = result.get_money()["total_money"]
        car.update(cost=total_money)
        return HttpResponse("{0}在{1}成功驶出, 共计消费{2}元".format(car_sign, dt, total_money))
    else:
        return HttpResponse('未检测到该车辆')













