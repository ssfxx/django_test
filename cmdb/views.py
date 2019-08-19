from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template

from datetime import datetime
from .models import Post
# Create your views here.
def header(requets):
    return render('header1.html')


def index(request):
    return render_to_response('index.html', )


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    #post_lists = list()
    #for count, post in enumerate(posts):
    #    post_lists.append(str(post.title) + "<br />")
    #    post_lists.append("<small>" + str(post.body) + "</small><br /><br />")
    #return HttpResponse(post_lists)
    return HttpResponse(html)


def showpost(requets,slug):
    template = get_template('post.html') #加载页面模板
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return HttpResponseRedirect('/')
