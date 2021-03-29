
from picamera import PiCamera
from time import sleep
import requests
camera = PiCamera()
code = 'ВАШ СЕКРЕТНЫЙ КОД КАМЕРЫ'

# Запускаем предпросмотр сигнала с камеры на экране поверх всех окон
#camera.start_preview()
camera.resolution = (1920, 1080) # тут можно скорректировать разрешение снимка
camera.exposure_mode = 'auto'
#camera.shutter_speed = 70000 # если снимать в сложных условиях, то можно скорректировать вручную вермя выдержки
#camera.rotation = 180 # поворот картинки с камеры
# Даём камере три секунды на автофокусировку и установку баланса белого
sleep(1)
i = 0
n = 1

str1 = 'image' + '.jpg'
#print(str1)
# Делаем снимок и сохраняем его на рабочий стол с именем image.jpg, тут не факт, что на рабочий стол, скорее в каталог /
camera.capture(str1)
#print(str1)
foto = open(str1, 'rb')  # some file on local disk
headers = {}
url = 'http://narodmon.ru/post'
files = {code: (code, foto, "image/jpeg")}

r = requests.post(url, files=files, headers=headers)

print(r.text)
# Выключаем режим предпросмотра
#camera.stop_preview()
