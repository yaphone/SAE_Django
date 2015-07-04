# -*- coding=utf-8 -*-

import sys, urllib, urllib2, json
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def get_busline(request):	
    appkey = 'ebe44ee7130cc7fcc443079f15a0f165' #您申请到的数据的APPKEY
    url = 'http://op.juhe.cn/189/bus/busline' #数据API请求URL
    paramsData = {'key':appkey, 'city':"重庆", 'bus':"346"} #需要传递的参数
    params = urllib.urlencode(paramsData)
    
    req = urllib2.Request(url, params)
    #req.add_header('Content-Type', "application/x-www-form-urlencoded")
    
    resp = urllib2.urlopen(req)
    content = resp.read()
    
    if(content):
        result = json.loads(content, 'utf-8')
        error_code = result['error_code']
        if(error_code == 0):
            data = result['result'] #接口返回结果数据
#            print data
            return HttpResponse(result)
        else:
            errorinfo = str(error_code)+":"+result['reason'] #返回不成功，错误码:原因
            print(errorinfo)

if __name__ == '__main__':
    get_busline()