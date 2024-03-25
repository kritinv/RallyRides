from django.shortcuts import render, redirect
from django.db.models import Q  # Import Q object
from .models import Person
from .forms import RideForm, NewRideForm


def index(request):

  context = {}
  context["form"] = RideForm()

  # Initialize an empty queryset
  filtered_people = Person.objects.all()

  print(filtered_people)
  print(request.GET)

  if "stateSearch" in request.GET:
    print("hi")
    context["inputExists"] = True
    stateSearch = request.GET["stateSearch"]
    citySearch = ""

    if "citySearch" in request.GET:
      citySearch = request.GET["citySearch"]

    # Apply filtering using Q objects and logical OR
    filtered_people = filtered_people.filter(
        Q(origination_city__icontains=citySearch) |
        Q(destination_city__icontains=citySearch),
        Q(destination_state__icontains=stateSearch) )
    
    context["people"] = filtered_people

    ('filtered people')
    
  if "city_search" in request.GET and "state_search" in request.GET:
    city_search = request.GET["city_search"]
    state_search = request.GET["state_search"]

    print(city_search)
    print(state_search)

    # Assign filtered queryset to context
    context["people"] = filtered_people

  context["new_ride_form"] = NewRideForm()

  return render(request, "index_view.html", context)

def create(request):
  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()
    print(new_ride)
    print(Person.objects.all())

    return redirect("/rides")
  
def form(request):
  context = {}
  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  return render(request, "form.html", context)