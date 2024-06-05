from django.shortcuts import render
from .models import Jobs

# Create your views here.
def home(request):
    images = Jobs.objects.all()
    return render(request, 'portfolio/home.html', {'images': images})