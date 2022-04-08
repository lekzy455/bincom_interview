from django.shortcuts import render

def poll_results(request):
    return render(request, "poll.html")

def lga_results(request):
    return render(request, "lga.html")