from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(request):
    if request.method == 'POST':
        return render(request, "rmd/searchResult.html")
    return render(request, "rmd/index.html")

def write(request):
    return render(request, "rmd/write.html")