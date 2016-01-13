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
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Person,Article

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
        p = Person.objects.get(username=username,password=password)
        request.session['person_id'] = p.id
        articles = Article.objects.filter(usernameid=p.id)
        return render_to_response('index.html',{'username':username,'articles':articles})
    except:
        if request.session['person_id']:
            perid = request.session['person_id']
            username = Person.objects.get(id=perid).username
            articles = Article.objects.filter(usernameid=perid)
            return render_to_response('index.html',{'username':username,'articles':articles})
        else:
            return HttpResponse(r'<html><script type="text/javascript">alert("Error!Please check again!"); window.location="/"</script></html>')

def about(request):
    if request.session['person_id']:
        perid = request.session['person_id']
        username = Person.objects.get(id=perid).username
        return render_to_response('about.html',{'username':username})
    else:
        return HttpResponse(r'<html><script type="text/javascript">alert("Login again!"); window.location="/"</script></html>')

def add(request):
    if request.session['person_id']:
        perid = request.session['person_id']
        username = Person.objects.get(id=perid).username
        return render_to_response('add.html',{'username':username})
    else:
        return HttpResponse(r'<html><script type="text/javascript">alert("Login again!"); window.location="/"</script></html>')

def article(request):
    title = request.POST['title']
    author = request.POST['author']
    body = request.POST['body']
    usernameid = request.session['person_id']
    art = Article(title=title,author=author,body=body,usernameid=usernameid)
    art.save()
    return HttpResponseRedirect('/blog/')

def logout(request):
    del request.session['person_id']
    return render_to_response('login.html')

def single(request,num):
    if request.session['person_id']:
        perid = request.session['person_id']
        username = Person.objects.get(id=perid).username
        body = Article.objects.get(id=num).body
        return render_to_response('single.html',{'username':username,'body':body,'num':num})
    else:
        return HttpResponse(r'<html><script type="text/javascript">alert("Login again!"); window.location="/"</script></html>')

def delete(request):
    if request.session['person_id']:
        perid = request.session['person_id']
        username = Person.objects.get(id=perid).username
        value = request.POST['value']
        deletearticle = Article.objects.get(id=value)
        deletearticle.delete()
        return render_to_response('index.html',{'username':username})
    else:
        return HttpResponse(r'<html><script type="text/javascript">alert("Login again!"); window.location="/"</script></html>')

def toedit(request,num):
    if request.session['person_id']:
        getarticle = Article.objects.get(id=num)
        title = getarticle.title
        author = getarticle.author
        body = getarticle.body
        return render_to_response('edit.html',{'num':num,'title':title,'author':author,'body':body})


def edit(request,num):
    if request.session['person_id']:
        updatearticle = Article.objects.get(id=num)
        updatearticle.title = request.POST['title']
        updatearticle.author = request.POST['author']
        updatearticle.body = request.POST['body']
        updatearticle.save()
        return HttpResponseRedirect('/blog/')
    else:
        return HttpResponse(r'<html><script type="text/javascript">alert("Login again!"); window.location="/"</script></html>')


def consult(request):
    if request.session['person_id']:
        perid = request.session['person_id']
        username = Person.objects.get(id=perid).username
        title = request.POST['title']
        result = Article.objects.filter(title__icontains=title)
        return render_to_response('index.html',{'username':username,'articles':result})
    else:
        return HttpResponse(r'<html><script type="text/javascript">alert("Login again!"); window.location="/"</script></html>')

