from random import choice
from app import ai

# Asking the user for 2 questions 
# 1. Consult the book
# 2. Create a new recipe

choice = input("1. Consult the book\n2. Create a new recipe\nCoose an action 1 or 2: ")
print(choice) 

if choice == "2":
    ingredients = input("What are the ingredients do you want ")
    recipe_type = input("What kind of food do you want ")
    chatgpt_response = ai.recipe([ingredients], recipe_type)
    print(chatgpt_response)
    print(ai) 
# Do the project here
# New line 

if choice == "1":
    choose = input("kind of recipe do you want to consult: ")
    level_type = input("easy or difficult ")
    chatgpt_response = ai.recipe([choose], level_type)
    print(chatgpt_response)
    print(ai)
decision = input("What do you want to do with your recipe\n edit or delete ")
if decision == "delete": 
     print("Now is eliminated ")
     delete = "recipe"
if decision == "edit": 
        edit = input("What do you want to edit ")
        print("Now you have a new recipe ")
