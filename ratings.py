"""Restaurant rating lister."""
from random import choice

# initialize empty directory
ratings = {}

def add_rating():
    """Ask user to add new restaurant and rating"""
    # asking user for new restaurant and rating
    new_restaurant = input("Restaurant name: ")
    # initialized new_score at integer that forces into while loop
    new_score = 0
    # Validate score between 1 and 5
    while new_score < 1 or new_score > 6:
        new_score = int(input("Rating: "))

    # insert user entry into dictionary
    ratings[new_restaurant] = new_score

# def main():
#     view_ratings = input("Would you like to view all ratings? (Y/N) ")
#     if view_ratings == "Y":
#         print_ratings()
#     elif view_ratings == "N":
#         add_new = input("Enter new restaurant? (Y/N) ")
#         if add_new == "Y":
#             add_rating()
#         else:
#             qt = input("Quit? (Y/N) ")
#             if qt == "Y":
#                 quit()

def main():
    """Gives users choices to view, add or quit"""
    answer = ""
    while answer not in ["View", "Add"]:
        answer = input("What would you like to do? View/Add/Quit? ")
    if answer == "View":
        print_ratings()
        main()
    elif answer == "Add":
        add_rating()
        main()
    elif answer == "Quit":
        quit()


def print_ratings():
    """"Print all restaurants and ratings"""
    file = open("scores.txt")

    # loop through scores.txt file to create dictionary
    for line in file:
        # strip and split at colon
        line = line.strip().split(":")
        # variable assignment
        restaurant = line[0]
        rating = line[1]
        # insert into dictionary
        ratings[restaurant] = rating

    # sorting and printing for each key-value pair
    for restaurant, rating in sorted(ratings.items()):
        print(f"{restaurant} is rated at {rating}.")

    file.close()

def random_restaurant():
    chosen_rest = random.choice(ratings.keys())
    print(f"The chosen restaurant is {chosen_rest}.")



# main()