from django.shortcuts import render

def home(request):
    template_name = "home.html"  
    context = {
        'title': 'Selamat Datang di halaman home', 
        'umur': 20,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"  
    context = {
        'title': 'Selamat Datang di halaman about', 
        'umur': 20,
    }
    return render(request, template_name, context)