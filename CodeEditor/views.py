from django.shortcuts import render
import sys
from django.http import request,HttpResponse,Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Code
import coderunner
import codesnippets
import tokengenerator

# Create your views here.

def index(request):

    token_unique = False
    token = ""
    while not token_unique:
        token = tokengenerator.generate_token(6)

        try:
            r = Code.objects.get(token=token)
        except Code.DoesNotExist:
            token_unique = True

    #got unique token insert into db
    r = Code(token=token,language="JAVA",code=codesnippets.CODE_SNIPPETS['JAVA'],shared_code='')
    r.save()

    return redirect("/"+token+"/")

def serve_token_url(request,token):
    try:
        c = Code.objects.get(token=token)
        language  = c.language
        code = c.code

        context = {
            'token' :token,
            'language':language,
            'code':code
        }
        return render(request,"codeeditor.html",context=context)

    except Code.DoesNotExist:
        return render(request,"error.html")



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
        except:
            pass
        finally:
            return HttpResponse("Saved")

@csrf_exempt
def run(request):
    if request.method == "GET":
        HttpResponse("Forbidden")
    else:
        try:
            token = request.POST.get('token','')
            inp = request.POST.get('input','')
            if token != '':
                try:
                    r = Code.objects.get(token=token)
                    language = r.language
                    code = r.code


                    jsonopt = coderunner.run(code=code,language=language,inp=inp)
                    opt =  jsonopt['run_status']
                    print opt
                    if(opt['status_detail']=="NA"):
                        print "compiled successfully and ran successfully",r.token
                        return HttpResponse(opt['output_html'])
                    elif opt['status_detail']=='NZEC':
                        return HttpResponse(opt['stderr'])
                    else:
                        return HttpResponse(opt['status_detail'])


                except Code.DoesNotExist:
                    print "Compilation Failed"
                    return HttpResponse("Error: Some big bloody error")
        except Exception as e:
            return HttpResponse("Error: Some error " + str(e))


@csrf_exempt
def lang_change(request):
    if request.method == "GET":
        HttpResponse("Forbidden")
    else:
        token = request.POST.get('token','')
        language = request.POST.get('language','')

        if token != '' and language != '':
            try:
                r = Code.objects.get(token=token)
                r.language = language
                r.code = codesnippets.CODE_SNIPPETS[language]
                r.save();
                return HttpResponse(str(r.code))
            except Code.DoesNotExist:
                return HttpResponse(str(''))
        else:
            return HttpResponse(str(''))