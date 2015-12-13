# Create your views here.
'''
from django.http import HttpResponse
from django.template import Context,loader

def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))
'''

from django.shortcuts import render_to_response
from django.http import HttpResponse
from blog.models import Person

def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        person = Person(username=username,password=password)
        person.save()
        return render_to_response('login.html')
    except:
        return render_to_response('login.html')

def register(request):
    return render_to_response('register.html')

def submit(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        Person.objects.get(username=username,password=password)
        return render_to_response('index.html')
    except:
        return HttpResponse(r'<html><script type="text/javascript">alert("Error!Please check again!"); window.location="/"</script></html>')

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')