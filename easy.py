import requests
import sys
import pytz
import pyttsx3
while True:
        a=input()
        url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
        te=requests.get(url).json()
        data=te['data']['info']['text']
        print(data)
        #下面三行会输出语音
        #pt = pyttsx3.init()
        #pt.say(data)
        #pt.runAndWait()
