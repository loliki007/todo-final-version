from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("hellooou everybody")

def test(request):
    return render(request, "test.html")


# Create your views here.
