from django.shortcuts import render
from django.http import HttpResponse
from test1 import test_ansible
from django.core.urlresolvers import reverse

# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     c = int(a)+int(b)
#     return HttpResponse(str(c))
# Create your views here.

# def add2(request, a, b):
#     c = int(a) + int(b)
#     return HttpResponse(str(c))
# def redis_status(request):
#     test1 = test_ansible(module='shell',args='hostname',host='test')
#     return HttpResponse(test1)
def  index(request):
    return render(request, 'home.html')
# def old_add2_redirect(request ,a , b):
#     return HttpResponseRedirect(
#         reverse('add2', args=(a, b))
#     )
def home(request):
    return render(request, 'home.html')
