from django.shortcuts import render, redirect
from django.db.models import Q  # Import Q object
from .models import Person
from .forms import RideForm, NewRideForm


def index(request):

  context = {}
  context["form"] = RideForm()

  # Initialize an empty queryset
  filtered_people = Person.objects.all()

  if "stateSearch" in request.GET:
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

  if not filtered_people:
    print("bye")
    user_input = request.GET.get("query", "")  # Example of getting a general query input
    ai_response = generate_ai_response(user_input)
    context["ai_text"] = ai_response
  else:
    print("hi")
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

import os
from transformers import pipeline
from .models import Person

def generate_ai_response(user_input):
    # Adjust the prompt to suggest the user is looking for help with searching
    if user_input.strip() == "":
        # Default prompt if the user input is empty or just whitespace
        prompt = "The user is trying to find a ride but isn't sure what to search for. How should they refine their search query. The search is only for cities and states."
    else:
        # Craft a prompt that includes the user's input and asks the AI for help
        prompt = f"The user entered '{user_input}' in the search but didn't find what they were looking for. How can they refine their search query to find a ride more effectively? The search is only for cities and states."

    # Initialize the text generation pipeline with the desired model
    generator = pipeline("text-generation", model="openai-community/gpt2")
    # Generate text based on the crafted prompt
    ai_text = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    # Extract the final AI response
    final_ai_text = ai_text.split("AI:")[-1].strip()
    return final_ai_text

