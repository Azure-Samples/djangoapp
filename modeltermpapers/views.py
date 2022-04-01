from django.shortcuts import render

def home(request):
    return render(request, 'modeltermpapers/home.html') 

def prices(request):
    return render(request, 'modeltermpapers/prices.html') 