from django.shortcuts import render

def complete(request):
    return render(request, 'chat/complete.html', {
    })
