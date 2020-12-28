from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django import forms


class addSchoolForm(forms.Form):
    CHOICES = [
        ('r','Restaurant'),
        ('d','Dining Hall')
    ]
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    schoolName = forms.CharField(max_length=128)
    R_or_D = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    eateryName = forms.CharField(max_length=128)
    rating = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect)
    comment = forms.CharField(widget = forms.Textarea)

class selectSchoolForm(forms.Form):
    schools = []
    for school in School.objects.all():
        choice = (school.name, school.name)
        schools.append(choice)
    dropdown = forms.ChoiceField(choices=schools, widget=forms.Select)

# Create your views here
def index(request):
    if request.method == 'POST':
        query = request.POST["q"]
        schools = School.objects.filter(name__icontains=query)
        return render(request, "rmd/searchResults.html", {
            'searchResult':schools,
            'query':query
        })
    return render(request, "rmd/index.html")

def write(request):
    if request.method == 'POST':
        school = request.POST['dropdown']
        return redirect("write/"+school)
    form = selectSchoolForm()
    return render(request, "rmd/write.html", {
        'schools':form,
    })

def addSchool(request):
    
    if request.method == 'POST':
        form = addSchoolForm(request.POST)
        if form.is_valid():

            #get info out of form
            schoolName = form["schoolName"].value()
            R_or_D = form["R_or_D"].value()
            eateryName = form["eateryName"].value()
            rating = form["rating"].value()
            comment = form["comment"].value()
            urlName = schoolName
            urlName = urlName.split(" ")
            urlName = "".join(urlName)

            #put info to databases and save
            newSchool = School(name=schoolName, urlName=urlName)
            newSchool.save()

            if R_or_D=='r':
                newE = Restaurant(name=eateryName, school=newSchool, urlName=urlName)
                newE.save()
                newR = restaurantReview(rating=rating, comment=comment, restaurant=newE)
            else:
                newE = diningHall(name=eateryName, school=newSchool, urlName=urlName)
                newE.save()
                newR = diningHallReview(rating=rating, comment=comment, diningHall=newE)
            newR.save()

            return render(request, "rmd/thanks.html")
        else:
            return render(request, "rmd/failure.html")
    form = addSchoolForm()
    return render(request, "rmd/addSchool.html", {
        'form':form
    })

def school(request, schoolName):
    school = School.objects.get(urlName=schoolName)
    restaurants = Restaurant.objects.filter(school=school)
    diningHalls = diningHall.objects.filter(school=school)
    
    return render(request, "rmd/school.html", {
        'school':school.name,
        'restaurants':restaurants,
        'diningHalls':diningHalls
    })
