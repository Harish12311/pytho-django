from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'templet.html')


def my_view(request):
    if request.method == 'POST':
        username1 = request.POST.get('username', '')
        email1 = request.POST.get('email', '')
        password1 = request.POST.get('password', '')
        # Process the data as needed
      
    else:
        return render(request, 'my_template.html')

