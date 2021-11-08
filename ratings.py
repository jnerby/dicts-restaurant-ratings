"""Restaurant rating lister."""


file = open("scores.txt")
ratings = {}

for line in file:
    line = line.strip().split(":")
    restaurant = line[0]
    rating = line[1]
    ratings[restaurant] = rating

print(ratings)