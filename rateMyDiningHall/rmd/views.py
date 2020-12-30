from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django import forms
from django.db.models import Avg
from django.template.defaulttags import register

class addReviewForm(forms.Form):
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    rating = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect)
    comment = forms.CharField(widget = forms.Textarea)

class addEateryForm(addReviewForm):
    eateryName = forms.CharField(max_length=128)

class addSchoolForm(addEateryForm):
    CHOICES = [
        ('r','Restaurant'),
        ('d','Dining Hall')
    ]
    schoolName = forms.CharField(max_length=128)
    R_or_D = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class selectSchoolForm(forms.Form):
    schools = []
    for school in School.objects.all():
        choice = (school.urlName, school.name)
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

            urlEName = eateryName
            urlEName = urlEName.split(" ")
            urlEName = "".join(urlName)

            #put info to databases and save
            newSchool = School(name=schoolName, urlName=urlName)
            newSchool.save()

            if R_or_D=='r':
                newE = Restaurant(name=eateryName, school=newSchool, urlName=urlEName)
                newE.save()
                newR = restaurantReview(rating=rating, comment=comment, restaurant=newE)
            else:
                newE = diningHall(name=eateryName, school=newSchool, urlName=urlEName)
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

@register.filter
def getAvgRating(dic, key):
    return dic.get(key).get('rating__avg')

def school(request, schoolName):
    if request.method =='POST':
        if 'dininghalls' in request.POST:
            return redirect(schoolName+"/dininghalls")
        else:
            return redirect(schoolName+"/restaurants")

    school = School.objects.get(urlName=schoolName)
    return render(request, "rmd/school.html", {
        'school':school.name
    })

def dininghalls(request, schoolName):
    school = School.objects.get(urlName=schoolName)
    dininghalls = diningHall.objects.filter(school=school)

    avgDRatings={}
    for dininghall in dininghalls:
        rating = diningHallReview.objects.filter(diningHall=dininghall).aggregate(Avg('rating'))
        avgDRatings[dininghall.name]=rating
    print(avgDRatings)

    return render(request, "rmd/dininghalls.html", {
        'school':school.name,
        'diningHalls':dininghalls,
        'avgDRatings':avgDRatings
    })


def restaurants(request, schoolName):
    school = School.objects.get(urlName=schoolName)
    restaurants = Restaurant.objects.filter(school=school)

    avgRRatings={}
    for restaurant in restaurants:
        rating = restaurantReview.objects.filter(restaurant=restaurant).aggregate(Avg('rating'))
        avgRRatings[restaurant.name]=rating
    print(avgRRatings)

    return render(request, "rmd/restaurants.html", {
        'school':school,
        'restaurants':restaurants,
        'avgRRatings':avgRRatings
    })


def addDiningHall(request, schoolName):
    school = School.objects.get(urlName=schoolName)

    if request.method == 'POST':
        form = addEateryForm(request.POST)
        if form.is_valid():
            eateryName = form["eateryName"].value()
            rating = form["rating"].value()
            comment = form["comment"].value()

            urlName = eateryName
            if " " in urlName:
                urlName = urlName.split(" ")
                urlName = urlName.join("")

            diningHallNew = diningHall(name=eateryName, school=school, urlName=urlName)
            diningHallNew.save()

            diningHallNewReview = diningHallReview(rating=rating, comment=comment, diningHall=diningHallNew)
            diningHallNewReview.save()

            return render(request, "rmd/thanks.html")
        else:
            return render(request, "rmd/failure.html")
    form = addEateryForm()
    return render(request, "rmd/addDiningHall.html", {
        'school':school.name,
        'form':form
    })

def addRestaurant(request, schoolName):
    school = School.objects.get(urlName=schoolName)
    if request.method == 'POST':
        form = addEateryForm(request.POST)
        if form.is_valid():
            eateryName = form["eateryName"].value()
            rating = form["rating"].value()
            comment = form["comment"].value()

            urlName = eateryName
            if " " in urlName:
                urlName = urlName.split(" ")
                urlName = urlName.join("")

            restaurantNew = Restaurant(name=eateryName, school=school, urlName=urlName)
            restaurantNew.save()

            restaurantNewReview = restaurantReview(rating=rating, comment=comment, restaurant=restaurantNew)
            restaurantNewReview.save()

            return render(request, "rmd/thanks.html")
        else:
            return render(request, "rmd/failure.html")
    form = addEateryForm()
    return render(request, "rmd/addRestaurant.html", {
        'school':school.name,
        'form':form
    })


def addDiningHallReview(request, schoolName, diningHallName):
    school = School.objects.get(urlName=schoolName)
    dininghall = diningHall.objects.get(urlName=diningHallName)

    if request.method == 'POST':
        form = addReviewForm(request.POST)
        if form.is_valid():
            rating = form["rating"].value()
            comment = form["comment"].value()
            newDHR = diningHallReview(diningHall=dininghall, rating=rating, comment=comment)
            newDHR.save()
            return render(request, 'rmd/thanks.html')
        else:
            return render(request, 'rmd/failure.html')

    form = addReviewForm()
    return render(request, "rmd/addReview.html", {
        'school':school,
        'eatery':dininghall,
        'form':form
    })


def addRestaurantReview(request, schoolName, restaurantName):
    school = School.objects.get(urlName=schoolName)
    restaurant = Restaurant.objects.get(urlName=restaurantName)

    if request.method == 'POST':
        form = addReviewForm(request.POST)
        if form.is_valid():
            rating = form["rating"].value()
            comment = form["comment"].value()
            newRR = restaurantReview(restaurant=restaurant, rating=rating, comment=comment)
            newRR.save()
            return render(request, 'rmd/thanks.html')
        else:
            return render(request, 'rmd/failure.html')

    form = addReviewForm()
    return render(request, "rmd/addReview.html", {
        'school':school,
        'eatery':restaurant,
        'form':form
    })
