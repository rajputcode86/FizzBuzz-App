

def dessert (sweet):
    print("I love " + sweet)

dessert ("jamun")


def home (name, age):

    greeting = "Hello, %s! You are %s years old." % (name, age)
    print(greeting)

home ("rakesh", 45)

def summer (age, school, character):
    greet = "My daughter summer is %s year old, goes to %s school and has a %s character" % (age, school, character)
    print (greet)

summer (6, "Sæhæj", "Good")

'|'


def num  (num1, num2, num3):
    
    if (num1 > num2) & (num1 > num3):
        greater_num = "%s is the greatest number" % (num1)
        print (greater_num)

    elif (num2 > num1) & (num2 > num3):
        greater_num = "%s is the greatest number" % ( num2)
        print (greater_num)

    else: 
        print ( " %s is the greate number" %(num3))


num (3, 4, 5)



import project3

print (project3.namer ("bob"))



class Home:
    def __init__(self, area, rooms, beds):
        self.area = area
        self.rooms = rooms
        self.beds = beds

    
my_home = Home (10, 120, 4)
print (my_home.area, my_home.rooms, my_home.beds)



age = 25

if age >= 65:
    print("You are a senior citizen.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


def calculatePerc( marks):
    
    perc = marks /100 *100

    if perc >= 90 :
        print("Grade A")

    elif perc >= 80 :
        print ("Grade B")
    elif perc >= 70 :
        print ("Grade C")
    elif perc >60 :
        print ("Grade D")
    else :
        print ("Grade E")

calculatePerc(70)


def salarycalc (salary):
    if salary <= 10000:
        print ("HRA = 20%, DA = 80%")

    elif salary <= 20000:
        print ("HRA = 25%, DA = 90%")

    else:
        print ("HRA = 30%, DA = 95%")

 
salarycalc (30000)


def elecunit (units):
    if units <= 50:
        print ("Rs. 0.50/unit")
    
    elif units >= 150:
        print ("Rs. 0.75/unit")
    
    elif units >= 200:
        print ("Rs. 1.20/unit")
    
    else:
        print ("Rs. 2.50/unit")

    elecunit (150)


