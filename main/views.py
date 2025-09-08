from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        "npm": "2406428781",
        "name": "Kevin Cornellius Widjaja",
        "class": "PBP E",
    }

    return render(request, "main.html", context)
