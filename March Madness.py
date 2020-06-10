#March Madness Sim
import random
import time
import turtle
print("Welcome to The March Madness Simulator!")
name = input("To begin, what is your name?")
weight = int(input("Please enter your player's weight(in lbs). Note, this will impact what position you play at, and will affect gameplay."))
height = int(input("Please also enter your player's height (in cm). Note, this also impacts gameplay."))

if height <= 190:
    if weight < 175:
        print("You have chosen a lightweight Point Guard!")
        build = "PG"
        time.sleep(2)
        print("Your primary job is to facilitate scoring opportunities for your team, or sometimes for yourselves.")
    else:
        print("You have chosen a heavyweight Point Guard!")
        build = "PG"
        time.sleep(2)
        print("Your primary job is to facilitate scoring opportunities for your team, or sometimes for yourselves.")
elif height > 191 and height < 200:
    if weight < 195:
        print("You have chosen a lightweight Shooting Guard!")
        build = "SG"
        time.sleep(2)
        print("A shooting guard's main objective is to score points for their team and steal the ball on defense.")
    else:
        print("You have chosen a heavyweight Shooting Guard!")
        build = "SG"
        time.sleep(2)
        print("A shooting guard's main objective is to score points for their team and steal the ball on defense.")
elif height > 201 and height < 210:
    if weight < 225:
        print("You have chosen a lightweight Small Forward")
        build = "SF"
        time.sleep(2)
        print("Small forwards are responsible for scoring points, defending and often as secondary or tertiary rebounders behind the power forward and center, although a few have considerable passing responsibilities.")
    else:
        print("You have chosen a heavyweight Small Forward")
        build = "SF"
        time.sleep(2)
        print("Small forwards are responsible for scoring points, defending and often as secondary or tertiary rebounders behind the power forward and center, although a few have considerable passing responsibilities.")
elif height > 211 and height < 215:
    if weight < 230:
        print("You have chosen a lightweight Power Forward")
        build = "PF"
        time.sleep(2)
        print("They play close to the basket, fighting for rebounds and posting up on offense.")
    else:
        print("You have chosen a heavyweight Power Forward")
        build = "PF"
        time.sleep(2)
        print("They play close to the basket, fighting for rebounds and posting up on offense.")
else:
    if weight < 250:
        print("You have chosen a lightweight Center")
        build = "C"
        time.sleep(2)
        print("Defensively, the two main responsibilites of a center is to defend the basket and rebound the basketball. Offensively, Centers are good in the paint")
    else:
        print("You have chosen a heavyweight Center")
        build = "C"
        time.sleep(2)
        print("Defensively, the two main responsibilites of a center is to defend the basket and rebound the basketball. Offensively, Centers are good in the paint")
print("")
time.sleep(2.121)
print("Now,", name, " you are coming off an impressive high school career, but now need to choose your college")
print("You have gotten four offers, from the: \n University of Virginia, \n University of Oklahoma, \n Louisiana State University, \n and Iowa State University")
print("")
time.sleep(2)
team = input("Which team would you like to commit to?")
if team == "virginia" or team == "University of Virginia" or team == "univeristy of virginia" or team == "Virginia" or team == "VIRGINIA":
    print("The University of Virginia! Let's go Cavaliers!")
    print("Your team went 35-3 all season, securing you a place in the March Madness Tournament!")
elif team == "oklahoma" or team == "University of Oklahoma" or team == "university of oklahoma" or team == "Oklahoma" or team == "OKLAHOMA":
    print("The University of Oklahoma! Let's go Sooners!")
    print("Your team went 20-14 all season, securing a place in the March Madness Tournament!")
elif team == "louisiana" or team == "Louisiana State University" or team == "louisiana state university" or team == "Louisiana" or team == "LOUISIANA":
    print("Louisiana State University! Let's go Tigers!")
    print("Your team went 27-7 all season, securing a place in the March Madness Tournament!")
else:
    print("Iowa State University! Cyclones For the Win!")
    print("Your team went 23-12 all season, securing a place in the March Madness Tournament!")
    
s = turtle.getscreen()
t = turtle.Turtle()
turtle.title("March Madness Simulator")
t.penup()



    

