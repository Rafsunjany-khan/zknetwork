from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def package(request):
    return render(request, 'package.html')
def airlince(request):
    return render(request, 'airlince.html')
def blog(request):
    return render(request, 'blog.html')
def carrier(request):
    return render(request, 'carrier.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'index-2.html')
def visa(request):
    return render(request, 'visa.html')
def airticket(request):
    return render(request, 'airticket.html')
def hotel(request):
    return render(request, 'hotel.html')