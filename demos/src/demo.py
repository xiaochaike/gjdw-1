#!/usr/bin/python3
import urllib.parse  
import urllib.request  
import threading as thd
import time
def hello() :
    url = 'http://127.0.0.1:8083/DataCheck/post'  
    values = {  
        'parameter': "6/60/ISC_PMS_DEPT/12/MC/ISC_PMS_IS_USER/LSBM"
    }  
    data = urllib.parse.urlencode(values)  
    # that params output from urlencode is encoded to bytes before it is sent to urlopen as data  
    data = data.encode('utf-8')  
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    response = urllib.request.urlopen(req)  
    html = response.read()  
    print(html.decode('utf-8'))
    
   
   
   
def fn():
    hello()
    thd.Timer(1,fn).start()
    
fn()
