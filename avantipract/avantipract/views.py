from django.shortcuts import render


def inicio(request):
    return render(request, "index.html")
def acerca(request):
    return render(request, "acerca.html")

def login(request):
    return render(request, "login.html")

