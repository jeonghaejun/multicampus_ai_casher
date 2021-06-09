#-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread
from keras import models
from tensorflow.image import resize
from keras.preprocessing.image import load_img, img_to_array
import time
import random
import json 
import cv2
import net2
import boto3
from PIL import ImageFont, ImageDraw, Image
import requests
import warnings
import asyncio
import websockets
import threading
from socket import *


#IP_ADDRESS_PC = '3.35.202.158'
IP_ADDRESS_PC = '172.31.4.72'
PORT = 8902
MODEL_PATH = 'models/Xception_99.h5'
MODEL = models.load_model(MODEL_PATH)
    
    

indicate_key = {0: '11340',
 1: '11512',
 2: '11722',
 3: '11723',
 4: '11749',
 5: '11751',
 6: '11791',
 7: '11850',
 8: '11933',
 9: '11945',
 10: '11956',
 11: '11957',
 12: '11967',
 13: '11973',
 14: '11978',
 15: '11994',
 16: '12014',
 17: '13733',
 18: '13861',
 19: '13909'}


indicate = {0: '농심_츄파춥스',
 1: '롯데_칸쵸컵95g',
 2: '롯데_아몬드빼빼로1500',
 3: '롯데_초코빼빼로1500',
 4: '롯데_허쉬밀크초콜릿',
 5: '롯데_씨리얼오트컵',
 6: '오리온_다이제초코',
 7: '프링글스_오리지날53g',
 8: '매일_페레로로쉐5구',
 9: '롯데_드림카카오56%',
 10: '롯데_크런키더블크런치바',
 11: '마즈_스니커즈땅콩',
 12: '서영_홀스레몬맛',
 13: '롯데_허쉬쿠앤크초콜릿',
 14: '크라운_마이쮸딸기',
 15: '롯데_쥬시후레쉬스틱팩껌',
 16: '롯데_자일리톨용기껌52g',
 17: '코카_코카콜라제로캔250ml',
 18: '코카_코카콜라캔250ml',
 19: '롯데_칠성사이다캔250ml'}

DF = pd.read_csv("infos_2.csv" , encoding = "cp949")




FAIL_IOT = True

if FAIL_IOT:
  PORT_2 = 8898
  serverSock = socket(AF_INET, SOCK_STREAM)
  serverSock.bind((IP_ADDRESS_PC, PORT_2))
  serverSock.listen(1)
  print('%d  ...'%PORT_2)
  connectionSock, addr = serverSock.accept()
  print(str(addr), 'finish.')





async def connect(json_input):
    # 웹 소켓에 접속을 합니다.
    async with websockets.connect("ws://18.169.67.45:8000/ws/chat/1234/") as websocket:
        # 10번을 반복하면서 웹 소켓 서버로 메시지를 전송합니다.
        # await websocket.send('{message: {0}}'.format(json));
        send_msg = {"message": json_input}
        await websocket.send(json.dumps(send_msg));


# 웹 소켓 서버로 부터 메시지가 오면 콘솔에 출력합니다.
# 비동기로 서버에 접속한다.




## REST_API 송신 함수
def send_REST_API(result_dict):
    print("Start send REST-API server")
    url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev/judgement"
    response = requests.post(url, data=json.dumps(result_dict))
    return response

## S3 송신 함수
def send_S3(file_name):
    print("Start send S3 server")
    s3 = boto3.client('s3',aws_access_key_id= "key_id",
                    aws_secret_access_key='secret_access_key') 
    
    #key_name = "test_dsadasdasdadasdasda.jpg"
    bucket_name = 'yangjae-team07-bucket'
    s3.upload_file('./History/' + file_name, bucket_name, file_name)
  
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object_acl
    response = s3.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=file_name)
    
    
def cv2_plot(file_name, result) :
    file_name = './History/' + 'result_0601205613_4891.jpg'
    img = np.zeros((600,500,3),np.uint8)
    b,g,r,a = 255,255,255,0

    pred = 0.8
    item_pred = str(pred*100) + " %"
    item_id = 10010
    item_name = "해태_포도봉봉캔340ml"
    item_price = 1200
    item_Qty = 105
    item_Category = "drink" 


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
    
    img_pic = cv2.imread(file_name)
    
    
    resize_text = cv2.resize(img_text , (600 , 600))
    resize_pic =cv2.resize(img_pic , (800 ,600))
    
    #addv = np.vstack([img1 , img2])
    addh = np.hstack([resize_pic , resize_text])


    cv2.imshow("Test", addh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_image(data):
   
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_COLOR)
    key = cv2.waitKey(1)  # 이미지 갱신이 일어나는 곳
    
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
    #print('\n\n\n#####################################################\n')

    asyncio.set_event_loop(asyncio.new_event_loop())
    ###############################
    # 1. 이미지 수신 및 저장      #
    ###############################
    print('\n\n\n')
    print("="*100)
    print('Receiver start')
    print("="*100)
    
    reader = client.makefile('rb')
    data, data_len = net2.receive(reader)
    if not data_len:
        return
    image, key = show_image(data)
    
    # 현재 시간 기준으로 파일명 저장
    current_time = time.time()
    current_ms = str(int(round(current_time * 1000)))[-3:]
    current_time = time.strftime(f'%m%d%H%M%S{current_ms}', time.localtime(current_time))

    file_name = "result_"  + current_time + '.jpg' # result_0601135334123.jpg (6월 1일 13시 53분 34.123초)
    print(f'\n#\n# File Name : {file_name}\n#\n')
    cv2.imwrite("./History/" + file_name, image)
    
    
    ###############################
    # 2. AI - 분류                #
    ###############################

    THRESHHOLD = 0.9
    
    
    # 이미지 Resize
    
    input_arr = resize(image, (200,200)) / 255
    input_arr = np.array([input_arr]) # Convert single image to a batch.
    input_arr = input_arr[:,:,:,::-1] # GBR to RGB
    

    
    
    # Model predict
    prob = MODEL.predict(input_arr)[0]
    pred = prob.argmax()
    prob = prob[pred]
    
    # 더미값
    primary_key = int(indicate_key[pred])
    
    result = 1 if prob > THRESHHOLD else 0
    
    print('\n#\n# 예측 결과\n#\n')
    print(f'Predict Index : {pred}    name : {indicate[pred]}')
    print(f'Probability : {prob}')
    print(f'Primary Key : {primary_key}\n')

          
    ###############################
    # 3. 클라우드 서버 송신       #
    ###############################       
            
    ## 1. SOCKET >> IOT 통신
    
    if FAIL_IOT:
      print('Start IoT socket...')
      sendData = str(result)
      connectionSock.send(sendData.encode('utf-8'))
      connectionSock.send(sendData.encode('utf-8'))

    
    # 클라우드 서버에 송신할 데이터 생성
    send_data = {'result' :  result , 'time' :  current_time , 'item' : [] }
        
    result_item =  {
          "outcome": result,
          "id": str(primary_key), # Type : string
          "prob": int(prob*100)
        }

    ## REST-API 보내는 데이터
    send_data['item'].append(result_item)
    
    
    
    ITEM_DICT = {'item' : []}
    
    item_info = DF[DF['Item_id'] == primary_key] # SELECT * FROM table WHERE Item_id = primary_key
    
    temp_dict = {
        'id' : primary_key,
        'name' : item_info['Product_name'].values[0],
        'price' : int(item_info['Price'].values[0]),
        'Qty' : 1
    }
    
    ITEM_DICT['item'].append(temp_dict)
    
    if result :
        asyncio.get_event_loop().run_until_complete(connect(ITEM_DICT))


    # 서버 송신 (분류 성공 >> REST-API , 분류 실패 >> REST-API / S3)
    response = send_REST_API(send_data)
    if not result : send_S3(file_name) # 분류 실패 시 S3에 이미지파일도 전송

    print(f'서버 송신 결과 : {response}')
    #cv2_plot(None, None)
    

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # 학습 파라미터 불러서 모델 생성
    print('\n\nProgram Start!!!!\n\n')
 
    
    while(1):
        # 카메라 통해서 이미지 데이터 받아오기
        net2.server(IP_ADDRESS_PC, PORT, receiver)



    

