from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory


def home(request):
    return render(request, "app/home.html")

@login_required
def tests(request):
    context = {
        "tests": Test.objects.all(),
        'reports': Report.objects.filter(user__id=request.user.id),
    }
    return render(request, "app/tests.html", context)

@login_required
def attend(request, pk):
    context = {
        "test": Test.objects.get(id=pk)
    }
    return render(request, "app/test.html", context)

@login_required
def submit(request, pk):
    obj = Test.objects.get(id=pk)
    count = int(request.POST.get("qcount")) + 1
    val = ''
    for x in range(1, count):
        if request.POST.get("choice-" + str(x)) != None :
            val = val + request.POST.get("choice-" + str(x))
        else:
            val = val + '0'
    marks = ''
    mark = 0
    for question in obj.questions.all():
        if question.answer  == request.POST.get("choice-"+str(count-1)):
            marks = marks + '1'
            mark += 1
            count += -1
        else:
            marks = marks + '0'
            count +=-1
    report = Report()
    report.user = User.objects.get(id=request.user.id)
    report.test = obj
    report.choices = val[::-1]
    report.marklist = marks[::-1]
    report.marks = mark
    report.save()
    test = Test.objects.get(id=pk)
    test.students.add(User.objects.get(id=request.user.id))
    return redirect("home")

@login_required
def report(request, pk):
    report = Report.objects.get(id=pk)
    context = {
        "reports": Report.objects.get(id=pk),
        "test": Test.objects.get(id=report.test.id)
    }
    return render(request, "app/report.html", context)
