import json
from botocore.vendored import requests
import pymysql
import json

def lambda_handler(event, context):
    # TODO implement
    
    conn = pymysql.connect(host='multicampus.clhnj2zwdisk.eu-west-2.rds.amazonaws.com', user='admin',
                           passwd='master123', db='multicampus', port=3306, charset='utf8')
    cursor = conn.cursor()
    
    success_flag = 1
    
    
    storageInfo = event['Records'][0].get('s3')
    fileName = storageInfo['object']['key']
    
    url = "https://yangjae-team07-bucket.s3.eu-west-2.amazonaws.com/"
    url += fileName
    
    
    
    
    if '_' in fileName:
        fileName = fileName[:-4]
        nameArr = fileName.split('_')
        if 'fail' in nameArr:
            success_flag = 0
        id = int(nameArr[0])
        sql = "INSERT INTO Item_image (Item_id, Img_url, Judgement_img) VALUES(%s,%s,%s)"
        
        var = (id, url, success_flag)
        cursor.execute(sql, var)
        conn.commit() 
        result = cursor.fetchall()
        
        if success_flag == 0:
            sql = "INSERT INTO Error_detection (Wrong_item_id, Errorimg_id) VALUES(%s,%s)"
            cursor.execute("select LAST_INSERT_ID()")
            conn.commit() 
            result = cursor.fetchall()
            var = (id, result)
            cursor.execute(sql, var)
            conn.commit() 
            result = cursor.fetchall()
            
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }