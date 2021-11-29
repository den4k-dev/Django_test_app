from django.shortcuts import render


def index(request):
    content = {
        'title': 'Stuff list',
    }
    return render(request, 'index.html', context=content)
