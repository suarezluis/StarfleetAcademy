#The Starfleet Academy Program
# Luis Suarez

name = input("Applicant name: ")
age = int(input("Age: "))
gpa = float(input("GPA: "))
sat = int(input("SAT: "))
race = input("Race: ")

#variables to act as flags where 1 is aproved and 0 is rejected

ggpa = 0
gsat = 0
gage = 0
grace = 0

# basic qualifications

if(gpa >= 2):
    ggpa = 1
if(sat >= 800):
    gsat = 1
if(age >= 17):
    gage = 1
if(race != "Romulan"):
    grace = 1

# special situations and wavers

if(race == "Vulcan" and age >= 16): #Vulcans minimum age is 16
    gage = 1

if(gpa >= 3.5): # a GPA higher or equal to 3.5 waves SAT requirements
    gsat = 1

if(sat >= 1100): # a SAT higher or equal to 3.5 waves GPA requirements
    ggpa = 1

if(sat >= 1500): # a SAT higher or equal to 3.5 waves Age requirements
    gage = 1

#final decision

if( ggpa + gsat + gage + grace == 4): # all conditions must meet
    print("Congratulations", name, ", you have been accepted into Starfleet Academy")

else: # rejection and identifying reasons for rejection
    print("We are sorry to informe you that at this time you are not accepted into Starfleet Academy,")
    print("due to the following reason(s):")
    if(ggpa == 0):
        print("Your GPA,", gpa, "is too low")
    if (gsat == 0):
        print("Your SAT,", sat, "is too low")
    if (gage == 0):
        print(age, " years old is too young, please try again in the future")
    if (grace == 0):
        print("Romulans can not be accepted at this time")
    print("Rejection code:", ggpa, gsat, gage, grace)

print("Thank you for your interest")
