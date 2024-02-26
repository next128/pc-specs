from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def index_page(request: WSGIRequest):
    context = {

    }
    return render(request, 'pages/index.html', context)
