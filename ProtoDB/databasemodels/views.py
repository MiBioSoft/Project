from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from databasemodels.forms import UserForm, ProtocolForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from databasemodels.models import *
import itertools
from django.utils.text import slugify
from django.core import serializers
from django.template import RequestContext
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            ref = user_form.save(commit=False)
            #saves as hashed so that authenticate will work
            ref.set_password(request.POST['password'])
            ref.save()
            reft = authenticate(username=request.POST['username'],
                               password=request.POST['password'])
            
            login(request, reft)
            return HttpResponseRedirect('/home/')
        else:
            pass


    else:
        user_form = UserForm()
        
   # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form,},
            context_instance=RequestContext(request))
def user_login(request):

    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        #authenticates username and pwd
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                #send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/home/')

        else:
            
            return HttpResponse("Invalid login details supplied.")


    else:
        return render_to_response('login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')
#This function is only to validate if user is logged in.   
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

def home(request):
    home_template = get_template('home.html')
    return render(request, 'home.html')
    return HttpResponse(html)


@login_required
def create_protocol(request, **kwargs):
    context = RequestContext(request)

    created = False
    
    if request.method == 'POST':
        
        
        protocol_form = ProtocolForm(data=request.POST)
  
        if protocol_form.is_valid():

            #commit = False doesn't save, but still creates instance.
            bbb = protocol_form.save(commit=False)
            #makes the publisher equal the current user
            bbb.publisher = request.user
            #slugifys the title (adds "-" instead of spaces)
            bbb.slug = orig = slugify(bbb.title)
            # if the slug doesnt exist, do nothing. if it does, add number to it
            for x in itertools.count(1):
                if not Protocol.objects.filter(slug=bbb.slug).exists():
                    break
                bbb.slug = '%s-%d' % (orig, x)
            bbb.save()

            created = True
        else:
            
            pass

    else:
        
        protocol_form = ProtocolForm()


    
    
    return render_to_response(
        'create_protocol.html',
        {'protocol_form': protocol_form, 'created': created},
        context)




def protocol(request, slug):
     #render protocol, allow deletion if logged in (thru template)   
    protocol = get_object_or_404(Protocol, slug=slug)
    if request.POST.get('delete'):
        protocol.delete()
        return redirect('/protocol_list/')
    return render(request, 'protocol.html', {
        'protocol': protocol,
    })
   

#creates a list of all protocols
def protocol_list(request):
    all_entries = Protocol.objects.all()
    slug_tuple = Protocol.objects.values_list('slug')
    items = []
    url = ""
    title = ""
    #takes slug and title, creates url /view/slug.html, appends to list. list is read in template
    for each in Protocol.objects.all():
        slug = each.slug
        title = each.title
        url = "/view/" + slug + ".html"
        inner_item = []
        inner_item.append(title)
        inner_item.append(url)
        items.append(inner_item)
        
    return render_to_response('protocol_list.html', {'items':items})

