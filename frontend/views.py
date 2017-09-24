from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import NewAccount
from django.views.decorators.csrf import csrf_exempt
from django.views import generic


# Create your views here.
def home(request):
    return render_to_response("Project Mahrabani -FrontEnd/index.html")
    #contax = {'result': objects,} #contax = is a dictionary contains results etc
    #return render_to_response(request,template,contax)

#
# def about(request):
#     return render_to_response("frontend-templates/index.html" + "#about")
#
# def work(request):
#     return render_to_response("frontend-templates/index.html")
#
#
# def team(request):
#     return render_to_response("frontend-templates/index.html")
#
#
# def contact(request):
#     return render_to_response("frontend-templates/index.html")
#
#
# def login(request):
#     return render_to_response("frontend-templates/login.html")
#
#
# def signup(request):
#     return render_to_response("frontend-templates/signup.html")
#
#
#
# @csrf_exempt
# def saveaccount(request):
#     rname = request.POST['user_name']
#     email = request.POST['email']
#     d = request.POST['password-input']
#     address = request.POST['address']
#     city = request.POST['city']
#     photographs = request.POST['files']
#     new_add_account = NewAccount(username = rname,email= email, drowssap= d, address= address, city = city, photograph=photographs)
#     new_add_account.save()
#     return render_to_response("frontend-templates/login.html")
