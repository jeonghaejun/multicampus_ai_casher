# -*- coding: utf-8 -*-

import net2
import pandas as pd
import cv2
import numpy as np
import boto3
import time
import json 
from matplotlib.image import imread
import matplotlib.pyplot as plt 
from PIL import ImageFont, ImageDraw, Image
import requests
import warnings
import random
import os
import requests
import json
import asyncio
import threading
import websockets
from socket import *
from time import localtime, strftime
import time
from datetime import timedelta , datetime
    
#IP_ADDRESS_PC = '18.169.67.45'
IP_ADDRESS_PC = '172.31.1.75'
PORT = 8902



################################## # IOT ADDRESS

PORT_2 = 8898
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((IP_ADDRESS_PC, PORT_2))
#serverSock.listen(1)
#print('%d  ...'%PORT_2)
#connectionSock, addr = serverSock.accept()
#print(str(addr), 'finish.')

##################################    


YOLO_CONVERT_INDICATOR = {
"13861" : "13733" ,
"11957" : "13861" , 
"11512" : "13909" , 
"13909" : "11722" ,
"12014" : "11956" ,
"11967" : "11945" , 
"11933" : "11957" ,
"11978" : "11340" , 
"11751" : "11967" ,
"11850" : "11933" ,
"11722" : "11978" ,
 
"11749" : "11512" ,
"11956" : "11751" , 
"11994" : "11973" , 
"11723" : "11723" ,
"11340" : "11791" ,

"11973" : "11850" , 
"11749" : "11512" , 
"11945" : "11749" , 
"11791" : "12014" 
}

DF = pd.read_csv("infos_2.csv" , encoding = "cp949")

# CONNECT
async def connect(json_input):
    # �� ���Ͽ� ������ �մϴ�.
    async with websockets.connect("ws://18.169.67.45:8000/ws/chat/1234/") as websocket:
        # 10���� �ݺ��ϸ鼭 �� ���� ������ �޽����� �����մϴ�.
        # await websocket.send('{message: {0}}'.format(json));
        send_msg = {"message": json_input}
        print(send_msg)
        await websocket.send(json.dumps(send_msg));


## REST_API �۽� �Լ�
def send_REST_API(result_dict):

    print("Start send REST-API server")
    url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev/judgement"
    response = requests.post(url, data=json.dumps(result_dict))
    return response


## S3 �۽� �Լ�
def send_S3(file_name , key_name):
    
    s3 = boto3.client('s3',aws_access_key_id='key_Id',
                    aws_secret_access_key='secret_key') 
  
    bucket_name = 'yangjae-team07-bucket'
    s3.upload_file(file_name, bucket_name, key_name)
  
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object_acl
    response = s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=key_name)

    return response


def show_image(data):
   
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    key = cv2.waitKey(1)  # �̹��� ������ �Ͼ�� ��
    
    return (image, key)

def show_window(item_image , df_info , prob , show_option = False):
    
    img = np.zeros((600,500,3),np.uint8)
    b,g,r,a = 255,255,255,0

    item_pred = str(prob*100) + " %"
    item_id = df_info[0]
    item_name = df_info[1]
    item_price = df_info[2]
    item_Qty = df_info[3]
    item_Category = df_info[4] 

    fontpath = "./font/NanumGothic.ttf"
    font = ImageFont.truetype(fontpath, 20)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    draw.text((60, 70),  "Prediction_Prob  :  {}".format(item_pred) , font = font , fill=(b,g,r,a))
    draw.text((60, 140),  "Item_ID :  {}".format(item_id), font = font , fill=(b,g,r,a))
    draw.text((60, 210),  "Item_Name  :   {}".format(item_name), font = font ,  fill=(b,g,r,a))
    draw.text((60, 280),  "Item_Price  :  {}".format(item_price) , font = font  , fill=(b,g,r,a))
    draw.text((60, 350),  "Item_Qty  :  {}".format(item_Qty) , font = font  , fill=(b,g,r,a))
    draw.text((60, 420),  "Item_Category  :  {}".format(item_Category) , font = font  , fill=(b,g,r,a))

    img_text = np.array(img_pil)
    resize_text = cv2.resize(img_text , (600 , 600))
    resize_pic =cv2.resize(item_image , (600 ,600))
    addh = np.hstack([resize_pic , resize_text])
    return addh


def receiver(client, addr , model):
    print('\n\n\n#####################################################\n')
    asyncio.set_event_loop(asyncio.new_event_loop())

    # �ð� �������� ��������
    current_time = datetime.now() + timedelta(hours=9)
    current_time = current_time.strftime("%m%d%H%M%S.%f")[:-3]
    current_time = current_time.replace("." , "")


    print("#####################")
    print(current_time)
    print("#####################")
    ###############################
    # 1. �̹��� ���� �� ����      #
    ###############################
    

    print("="*40)
    print('Receiver start')
    print("="*40)

    reader = client.makefile('rb')
    data, data_len = net2.receive(reader)
    if not data_len:
        return
    image, key = show_image(data)
    
    # ī�޶� �׽�Ʈ �̹���
    file_name = "test"
    cv2.imwrite("./" + file_name + ".jpg" , image)

    
    ###############################
    # 2. AI - �з�                #
    ###############################


    
    
    ## YOLO ����
    NAME_CFG = "yolov4_CASHER_v6.cfg"
    NAME_WEIGHT = "yolov4_CASHER_v6_best.weights"
    os.system('./darknet detector test data/obj.data ' + NAME_CFG + " " + NAME_WEIGHT + " test.jpg"  + " -thresh 0.5 -out result.json")
    os.system('mv predictions.jpg ./predictions/' + "result_" + current_time + ".jpg")
    os.system('mv result.json ./predictions/' + "result_" + current_time + ".json")

    
    ## OBJECT DETECTION ���
    json_file_name = "result_" + current_time + ".json"
    with open('./predictions/' + json_file_name , 'r') as f:
      json_data = json.load(f)
    print(json_data)
    
    THRESHOLD = 0.7   
    ITEM_LST = []
    RESULT = 1
    
    for item_data in json_data[0]["objects"]:
      item_dict = {}
      item_dict["id"] = item_data["name"]
      item_dict["prob"] = item_data["confidence"]
      item_dict["outcome"] = 1 
      if item_dict["prob"] > THRESHOLD :
        item_dict["outcome"] = 1
      else:
        item_dict["outcome"] = 0
        RESULT = 0
      ITEM_LST.append(item_dict)
      


#     ###############################
#     # 3. Ŭ���� ���� �۽�       #
#     ###############################       
                 
    print("="*40)
    print('Send Server start')
    print("="*40)
    
    

    

    
    ## 1. REST_API >> S3 ���
    REST_API_DICT = {}
    REST_API_DICT["result"] = RESULT
    REST_API_DICT["time"] = current_time
    REST_API_DICT["item"] = ITEM_LST
    response_1 = send_REST_API(REST_API_DICT)
    print("REST-API SERVER")
    print(response_1)
    
    ## 3. BOTO3 >> S3 ���
    if RESULT == False:
      response_2 = send_S3( "./predictions/" + "result_" + current_time + ".jpg" , "result_" + current_time + ".jpg" )
      print("BOTO3 SERVER")
      print(response_2)
    
    
    ## 4. WEBSOCKET >> WEB ���
    WEB_DICT = {}
    WEB_LST = []
    
    for item in ITEM_LST:
      item_dict = {}
      
      item_dict["id"] = YOLO_CONVERT_INDICATOR[item["id"]]  
      item_dict["name"] = DF[DF["Item_id"]==int(item_dict["id"])]["Product_name"].values[0]
      item_dict["price"] = int(DF[DF["Item_id"]==int(item_dict["id"])]["Price"].values[0])
      item_dict["Qty"] = 1
      WEB_LST.append(item_dict)
      
    WEB_DICT["item"] = WEB_LST
    asyncio.get_event_loop().run_until_complete(connect(WEB_DICT))
    
#     # Ŭ���� ������ �۽��� ������ ����
#     item_lst = []
#     item_dic = {'result' :  result , "time" : time_log , "item" : item_lst }

#     result_item =  {
#           "outcome": result,
#           "id": primary_key,
#           "prob": int(prob*100)
#         }

#     item_lst.append(result_item)


#     # ���� �۽� (�з� ���� >> REST-API , �з� ���� >> REST-API / S3)
#     if result == 1:
#         response = send_REST_API(item_dic)
#         print("Detect Success")

#     else:
#         response = send_REST_API(item_dic)
#         send_S3(image , file_name)
#         print("Detect Fail")
             
#     print(" ")
#     print("���� �۽� ��� ")
#     print(response)
#     print(" ")
    

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # �н� �Ķ���� �ҷ��� �� ����
    print('\n\nProgram Start!!!!\n\n')
    model = 10
    while(1):
        # ī�޶� ���ؼ� �̹��� ������ �޾ƿ���
        net2.server(IP_ADDRESS_PC, PORT, receiver, model)



    

