from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import Http404, HttpResponseRedirect, HttpRequest, HttpResponse
from .models import Employee, Company


# Create your views here.
# a = Employee.objects.create(name="uday", email="uday@321", password="uday@132", salary="24000", company_id=4).save()
# Employee.objects.get(id=5).delete()
# Employee.objects.order_by("name")

def home(request):
    # if "vishal" in Employee.objects.all():
    #     return HttpResponse("name not found")
    # else:
        return render(request, "base.html")
    #     return HttpResponse("hello world")
    #     return HttpResponse(Http404("Page not found"))

def show(request):
    compdata = Company.objects.all()
    Empdata = Employee.objects.all()
    return render(request, "show.html", {'compdata': compdata, 'empdata': Empdata})


def showdata(request, id):
    compdata = Company.objects.get(id=id)
    print(compdata)
    emp = Employee.objects.filter(company__id=id)
    print(emp)
    return render(request, "comdata.html", {'empdata': emp})


def showcomp(request, id):
    cdata = Employee.objects.filter(company=id)
    print(cdata)
    return render(request, "com_emp.html", {'com_emp': cdata})


def responce(request):
    return ValidationError("This field accepts valid input")
