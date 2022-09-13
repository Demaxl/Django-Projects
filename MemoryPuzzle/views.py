import os

from django.shortcuts import render
from django.http import HttpResponse


IMAGES_BASE_PATH = './MemoryPuzzle/static/MemoryPuzzle/images/'

board = []
images_path = [path for path in os.listdir(IMAGES_BASE_PATH)]

def index(request):
    print(images_path)
    return render(request, "MemoryPuzzle/index.html", {
        "images": images_path
    })
