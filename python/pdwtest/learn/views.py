#coding:utf-8
#声明编编码格式
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'good by python!!!')
#引入HttpRespones,用来向网页返回内容，类似print
# Create your views here.
