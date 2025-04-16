from django.shortcuts import render

def home(request):
    template_name = 'halaman/index.html'
    context = {
        'title': '-HOMEPAGE-',
        'description': 'web portfolio saya',
        'body': 'Halaman home'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title': '-ABOUT PAGE-',
        'description': 'web portfolio saya',
        'body': 'Halaman about'
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'contact.html'
    context = {
        'title': '- CONTACT -',
        'description': 'Contact',
        'body': 'Contact Page'
    }
    return render(request, template_name, context)