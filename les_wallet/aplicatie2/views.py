from django.shortcuts import render


def wallet(request):
    return render(request, 'wallet.html')