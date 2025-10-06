from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord,Persons
# Create your views here.
def help(request):
    return render(request, 'first_app/help.html')

def user(request):
    return render(request, 'first_app/users.html')


def index(request):
    users_list = Persons.objects.all()
    user_data = {'users_list': users_list}
    return render(request, 'first_app/users.html', context=user_data)