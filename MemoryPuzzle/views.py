import os, random

from django.shortcuts import render
from django.http import HttpResponse


IMAGES_BASE_PATH = './MemoryPuzzle/static/MemoryPuzzle/images/'
BOARDWIDTH = 6
BOARDHEIGHT = 5

BOX_NUM = BOARDWIDTH * BOARDHEIGHT


def prepare():
    images_path = [path for path in os.listdir(IMAGES_BASE_PATH)]

    random.shuffle(images_path)
    images = images_path[:BOX_NUM]

    return images

def index(request):

    return render(request, "MemoryPuzzle/index.html", {
        "images": prepare()
    })
