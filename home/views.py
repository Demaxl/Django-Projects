from django.shortcuts import render
from django.http import HttpResponse



APP_LIST = [
    ["Survey Form", "survey_form"],
    ["Memory Puzzle", "memorypuzzle"]
]

def index(request):
    return render(request, "home/index.html", {
        "apps": APP_LIST
    })
