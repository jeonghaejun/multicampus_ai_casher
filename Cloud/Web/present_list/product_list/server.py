# websocket client로부터 문자열로 된 json 데이터 업로드
data = await websocket.recv();

# json.loads에서 마지막 s는 string을 의미
jd = json.loads(data)

# type 확인
print(type(data))
print(type(jd))

# 결과 확인
print('{}'.format(data))
json_string = jd["info"]
print(json_string)