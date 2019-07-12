from django.shortcuts import render
#from django.views.generic import TemplateView
from django.views.generic.list import ListView
import json
#from django.http import HttpResponseRedirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .models import Cat


#def mysite1(request):
    #return render(request, 'mysite1/index.html')

#def index(request):
    #queryset = Cat.objects.all()
    #queryset = serializers.serialize('json', queryset)
    #return HttpResponse(queryset, content_type='application/json')

# получение данных из бд
def index(request):
   cat = Cat.objects.all()
   return render(request, "mysite1/index.html", locals())


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Cat()
        tom.name = request.POST.get("name")
        tom.gender = request.POST.get("gender")
        tom.age = request.POST.get("age")
        tom.lotok = request.POST.get("lotok")
        tom.med_pasport = request.POST.get("med_pasport")
        tom.save()
    return HttpResponse("/".format())

    dump = json.dumps(cat)
    return HttpResponse(cat, content_type='json/cats.json')

class CatView(ListView):
    model = Cat
    template_name = 'mysite1/index.html'
    context_object_name = 'cats'


# Create your views here.

#with open('C:/Users/User/Downloads/cat.json') as d:
    #data = json.load(d)


#def load_json_table_format(request):
    #print(data)
    #html = render_to_string()
    #return HttpResponse({'d':data}, 'mysite1/index.html', content_type="application/html")
    #return JsonResponse(data, safe=False,content_type="application/html")
    #return render(request, 'mysite1/index.html', {'d': data}, content_type="text/html")
