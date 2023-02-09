from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def product(request):
    
    return render(request, 'product.html')

def putcharse(request):
    return render(request, 'putcharse.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')