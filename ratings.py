"""Restaurant rating lister."""


file = open("scores.txt")

# initialize empty directory
ratings = {}

# asking user for new restaurant and rating
new_restaurant = input("Restaurant name: ")
# initialized new_score at integer that forces into while loop
new_score = 0
# Validate score between 1 and 5
while new_score < 1 or new_score > 6:
    new_score = int(input("Rating: "))


# insert user entry into dictionary
ratings[new_restaurant] = new_score

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