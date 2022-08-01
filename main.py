from urllib import request
from datetime import datetime

import schedule
import time

every = "01:00"
steps = 80000
distance = 50000
date = datetime.today().strftime('%Y-%m-%d')
access_token = 'vk1.a.ApmaRc5SLlwcc_VnIqQMIwTgfcoXRQqx1fHAVEk2WHkORUggVVZG9Jt7ViMOirRLf1hfYK4xSnVG3wEWSudWOcIRWP-Uj2sVz6tUJZh5K2xGmXynSP2K0mNiURj53LQsb-38D4dxFrJDG71Wxdk9rntWMFwvt0Gc4yqPuvCwbpILpGXeWBqFaavn_mECTk8t'
user_agent = 'VKAndroidApp/7.7-10445 (Android 11; SDK 30; arm64-v8a; Xiaomi M2003J15SC; ru; 2340x1080)'

def script():
	print(request.urlopen(request.Request('https://api.vk.com/method/vkRun.setSteps?steps='+str(steps)+'&distance='+str(distance)+'&date='+date+'&access_token='+access_token+'&v=5.131', headers={'User-Agent': user_agent})).read().decode('utf-8'))

schedule.every().day.at(every).do(script)
print("Каждый день в "+every+" я буду накручивать "+str(steps)+" ("+str(distance)+" метров)")

while True:
    schedule.run_pending()
    time.sleep(60)
