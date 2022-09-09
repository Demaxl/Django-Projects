from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage


board = []

def index(request):
    return render(request, "MemoryPuzzle/index.html", {})
