from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from databasemodels.forms import UserForm, ProtocolForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from databasemodels.models import UserDescription, Protocol

from django.template import RequestContext
# Create your views here.

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of UserForm
        user_form = UserForm(data=request.POST)
        

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            ref = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            ref.set_password(ref.password)
            ref.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            pass

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        
    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
           # print "Invalid login details"
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')
    
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

def home(request):
    home_template = get_template('home.html')
    return render(request, 'home.html')
    return HttpResponse(html)


@login_required
def create_protocol(request):
    context = RequestContext(request)

    created = False

    if request.method == 'POST':
        
        protocol_form = ProtocolForm(data=request.POST)
        print(request.user.id)
        
        print(protocol_form) #= UserDescription.objects.get(id = request.user.id)
        if protocol_form.is_valid():
            #Protocol.publisher = request.user.id
            #print(Protocol.objects.all())
            #print(protocol_form)
            protocol = protocol_form.save()
            
            #protocol.save()
            #protocol.publisher = 
            created = True
        else:
            #do protocol_form.errors
            pass

    else:
        #created = False
        protocol_form = ProtocolForm()
        #print(request.user.id)

    return render_to_response(
        'create_protocol.html',
        {'protocol_form': protocol_form, 'created': created},
        context)

#def about(request):
    
