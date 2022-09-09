from django.shortcuts import render
from django import forms


class SurveyForm(forms.Form):
    pass

def index(request):
    if request.method == 'POST':
        print('-'*50)
        print(dict(request.POST))

        form_msg = 'Thank you for taking time to help me improve the platform'
        color = "red"

        print('_'*50)

    else:
        form_msg = "Please fill in the survey"
        color = "f3f3f3"


    return render(request, "survey_form/index.html", {
        "form_msg": form_msg,
        "color": color,
        "form": SurveyForm()
    })
