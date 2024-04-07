import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from dbManager import DbManager

# Create your views here.
def index(request):
    return HttpResponse("Hi")
# def my_view(request):
#   if request.method == 'Get':
#     data = json.loads(request.body) # parse the JSON data into a dictionary
#     # Get the ingridients array

#     # USE Food Processor class and add all th recipies into a json object
    
#     # Get user's id ("id" :"xyz")
#     # Check the previous used ingridients with the new ones[Using MongoDB]



#     return JsonResponse(data) # Change this with the Recipies object made
def my_view(request):
   if request.method == 'POST':
    data = json.loads(request.body) # parse the JSON data into a dictionary
    # do something with the data
    if data['username'] is None or data['password'] is None :
        raise TypeError
    else:
        username = data['username']
        password = data['password']
        DbManager.add(username,password)
        print("test")
        return JsonResponse({
           "request": True
        }) # return the data as a JSON response

def getRecipe(request):
   if request.method == 'POST':
    data = json.loads(request.body) # parse the JSON data into a dictionary
    # do something with the data
    if data['Ingredient'] is None :
        raise TypeError
    else:
        username = data['username']
        ingredient = data['password']
        DbManager.addUserIngridients(username,ingredient)
        food = FoodProcessor()
        food.generateRecipes()
        names = food.getNameList()
        urls = food.getNameList()
        combine_list = []
        for food1, url1 in zip(names, urls):
           combine_list.append(food1)
           combine_list.append(url1)

        return JsonResponse(combine_list) # return the data as a JSON response

    
    

    
    
