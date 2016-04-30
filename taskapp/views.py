import console

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .app.PostManager import *

def index(request):  #BREAK THIS THE FUCK UP!!!!!!!!!
    
    status = "Make a post!" #Eventually add an account status marker here too
    post_frame = "<br/><h3>{title}</h3><p>{post_body}</p><br/>"
    post_info = ''

    pm = PostManager()

    #pm.create_post('test_name2')
    #Instantiate post and fetch depickle using username hash
    my_post = pm.fetchPost('test_name2') # eventually will be the signed in username
    prev_posts = pm.displayPosts(my_post)
    
    print pm.stat_post(my_post)

    payability = pm.payable(my_post)
    if payability == True:
        payability = "Yes"
    else:
        payability = "No"

    

    for post in pm.displayPosts(my_post):
        print post
        post_info = post_info + post_frame.format(title = post[0], post_body = post[1])
    
    if request.POST:
        status = pm.makeSubmission(my_post,request.POST["idea_title"],request.POST["idea"])
 
    templates = "index.html"

    templates = loader.get_template(templates)
        
    context = {
        "payability" : payability,
        "status" : status,
        "previous_posts" : post_info,
        "post_info" : request.POST}
    return HttpResponse(templates.render(context,request))

# Create your views here.
