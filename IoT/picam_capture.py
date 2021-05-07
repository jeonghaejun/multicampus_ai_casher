from io import BytesIO
from time import sleep
from picamera import PiCamera

project_stream = open('test.jpg', 'wb')

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

camera.capture(project_stream) # 포맷 지정 필요


