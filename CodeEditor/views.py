from django.shortcuts import render
import sys
from django.http import request,HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Code

# Create your views here.

def index(request):
    print "index",request.body
    return render(request,"codeeditor.html")



@csrf_exempt
def save(request):
    opt = ""
    #if tried to access using GET, confuse them
    if request.method == "GET":
        return Http404
    else:
        try:
            token = request.POST.get('token','')
            language = request.POST.get('language','')
            code = request.POST.get('code','')
            opt = "adad"+token+" "+language+" "+code

            if token != '' and language !='':
                try:

                    r = Code.objects.get(token=token)
                    r.language = language
                    r.code = code
                    r.save()
                except Code.DoesNotExist:

                    r = Code(token=token,language=language,code=code,shared_code='')
                    r.save()
                    print "save",opt
        except:
            pass
        finally:
            return HttpResponse("Saved")

@csrf_exempt
def run(request):
    if request.method == "GET":
        return Http404
    else:
        try:
            token = request.POST.get('token','')


            if token != '':
                try:
                    r = Code.objects.get(token=token)
                    print "compiled successfully",r.token

                except Code.DoesNotExist:
                    print "Compilation Failed"
        except:
            pass
        finally:
            return HttpResponse("ran")

