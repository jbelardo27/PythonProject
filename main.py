print("Hello World")

character_job = "pirate"
character_ride = "ship"
character_souvenir = "gold"
character_pet = "parrot"


print("There was once a " + character_job + " who loved adventure.")
print("The " + character_job + " would take her " + character_ride + " to unknown places.")
print("She brings home a lot of " + character_souvenir + ".")
print("Then she goes home to her pet " + character_pet + ", Chuckles.")


print("Roses are red, violets are blue")


if 10 > 7:
    print("Ten is greater than seven!")
if 16 < 42:
    print("Sixteen is less than forty-two!")
print("A long time ago in a galaxy far, far away...")


def hand_function(name):
    print("Have a nice day, " + name +"!")
hand_function("Coleen")


name = input("Name: ")
age = int(input("Age: "))
favorite_color = input("Favorite Color: ")
favorite_movie = input("Favorite Movie: ")
mobile_number = int(input("Mobile Number:" ))
motto = input("Motto in Life: ")


print(10 > 7)
print(str(73911))
print(tuple("Thank God it's Friday!"))
print(float(4302))
print(int(3299.35640))


class Customers:
    greeting = "Welcome to Coffee Palace!"

c1 = Customers()
c1name = "Samirah"
c1beverage = "Iced Coffee Latte"
c1food = "Cinnamon Roll"
c1total = 225

c2 = Customers()
c2name = "Jerry"
c2beverage = "Caramel Macchiato"
c2food = "Glazed Doughnut"
c2total = 230

print(Customers.greeting)
print(c1beverage)
print(c2food)


print(217 * 6)
print(600 + 35234)
print(67 // 12)
print(56329 % 982)
print(34 ** 5)


myage = 22
momage = 61
sisterage = 29

print(momage < sisterage and myage)
print(momage == 61)
print(momage > 34 or sisterage == 22)
print(momage >= 54)
print(not(sisterage <= 400 and myage))


x = 332
y = 2031

if x >= y:
    print("X is greater than or equal to Y.")
elif x == y:
    print("X is equal to Y")
else:
    print("X is less than Y")


furniture = ["table", "chair", "desk", "couch"]
for x in furniture:
    if x == "cabinet":
        continue
    print(x)

i = 1
while i <15:
    print(i)
    i += 1
else:
    print("i is no longer less than 15")


