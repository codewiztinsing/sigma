from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'active_page': 'home'})


def about(request):
    return render(request, 'about.html', {'active_page': 'about'})


def what_we_do(request):
    return render(request, 'what-we-do.html', {'active_page': 'what_we_do'})


def impact(request):
    return render(request, 'impact.html', {'active_page': 'impact'})


