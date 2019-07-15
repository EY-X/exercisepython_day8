# ----------- EXERCISE ------------ 0-1 

# These are lists

fav_colours = ["blue", "purple", "green"]
age = [25, 35, 40]
coin = ["heads", "tails", "heads", "heads", "tails"]
artists = ["drake", "RHCP", "Eminem"]

# These are dictionaries

dictionary = {
    'hot': 'having a high degree of heat or a high temperature.',
    'cold': 'low or relatively low temperature',
    'freezing-point': 'the temperature at which a liquid turns into a solid when cooled.'
}

dictionary2 = {
    'pulp fuction': '1994',
    'wolf of wall street': '2013',
    '2 fast 2 furious': '2003'
}
dictionary3 = {
    'new-york': 12000000,
    'toronto': 5000000,
    'los-angeles': 40000000
}
dictionary4 = {
    'me': 25,
    'sister': 35,
    'brother': 40
}

print(coin) 
print(fav_colours[0]) # printing 0 index of LIST
age.sort() # sorting LIST 
print(age) 
age.append(0) # adding
print(age)
print(dictionary4['sister'])

# EXERCISE 2

print(fav_colours[-1])

dictionary3['miami'] = 12000000

coin.reverse()

print(dictionary3.get("toronto", None))

for artist_name in artists:
  print("I think {} is amazing!".format(artist_name))

# EXERCISE 3

print(artists[0:2])

for movie, year in dictionary2.items():
    print(f"{movie} came out in {year}.")

age.sort()
age.reverse()
print(age)  # list(reversed(sorted(age))) {ONE LINE}

dictionary2['beauty and the beast'] = ['1991', '2017']
print(dictionary2)

# Exercise 4

for age_order in age:
    if age_order < 25:
        print(f"{age_order} IS WAY TOO YOUNG FOR ME")
    else:
        print(f"YOU'RE {age_order}! THATS OLD SCHOOL!")

age.sort()
print(age[-1]) #oldest age

print(coin.count('heads'))

artists.pop(0)
print(artists)

dictionary3['toronto'] = 4000000
print(dictionary3)

# Exercise 5

total_population =  sum(dictionary3.values())
print(total_population)

for name, age in dictionary4.items():
    if age > 26: 
        print(f"{name} is old!")
    else:
        print(f"{name} is young!")


print(fav_colours[-2:])

for add_age in age:
    add_age += 1 
    print(add_age)

fav_colours.extend(['black', 'pink'])
print(fav_colours)

Exercise 6

movies_dict = {
    '1999': ['The Matrix', 'Star Wars(Episode 1)', 'The Mummy'],
    '2009': ['Avatar', 'Star Trek', 'District 9'],
    '2019': ['How to train your dragon 3' 'Toy Story 4', 'District 9']
}

phone_buttons_rows = ['123', '456', '789', '*0#']

countries = [
    {
        'name': 'Canada', 
        'continent': 'North America',
        'island': False
    },
    {
        'name': 'Brazil',
        'continent': 'South America',
        'island': False
    },
    {  
        'name': 'Philippines',
        'continent': 'Asia',
        'island': True
    }
]
# Exercise 7

# for detention in range(20):
#     print('I will not skateboard in the halls')

# detention2 = ['I will not skateboared in the halls' * 20]  # Creats list with 20 times the item

# # Create a list consisting of the numbers between 1 and 50.

numbers = []
for x in range(1,51):
    numbers.append(x)
print(numbers)

# use loop to find the sum of the numbers in the lost above
numbers_sum = 0
for x in numbers:
    numbers_sum += x
print(numbers_sum)

# Create a new list which has three of each number up to 50.

new_number_list = []
for number in numbers:
    inner_range = range(1,4)
    for n in inner_range:
        new_number_list.append(number)
print(new_number_list)

# make new list with countries with value island

island_countries = []
for country in countries:
    if country["island"] == True:
        island_countries.append(country)

print(island_countries)

# Exercise 8

# SUMS INT IN LIST TOGETHER

expenses = [50, 100, 200, 175]
total_expenses = sum(expenses)
print(total_expenses)



