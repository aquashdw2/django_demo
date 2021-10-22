from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, "base.html", context=context)


def inherited(request):
    return render(request, "base_ih.html",)
