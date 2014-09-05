from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse

def testview(request):
    teststring = "teststring"
    html = "<html><body>This is displaying the test string: %s" % teststring
    return HttpResponse(html)


