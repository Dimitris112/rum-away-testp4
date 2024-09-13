from django.shortcuts import render

def index(request):
    context = {
        'page_title': 'Home',
    }
    return render(request, 'bar/index.html', context)

def reservations(request):
    context = {
        'page_title': 'Reservations',
    }
    return render(request, 'bar/reservations.html', context)

def profile(request):
    context = {
        'page_title': 'Profile',
    }
    return render(request, 'bar/profile.html', context)

def orders(request):
    context = {
        'page_title': 'Orders',
    }
    return render(request, 'bar/orders.html', context)

def comments(request):
    context = {
        'page_title': 'Comments',
    }
    return render(request, 'bar/comments.html', context)  
