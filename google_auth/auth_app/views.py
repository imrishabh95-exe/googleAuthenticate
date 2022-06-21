from django.shortcuts import render

# Create your views here.
def home_page(request):
    #Home Page
    return render(request, 'index.html')