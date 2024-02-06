from django.shortcuts import render

# Create your views here.


def stockPicker(request):
    return render(request, 'main/stockpicker.html')


def stockTracker(request):
    return render(request, 'main/stocktracker.html')
