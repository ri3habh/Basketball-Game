import random
import time
import turtle
print("Welcome to NBA My Player")
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
print("Your coming off a great high school career, but you still have to choose whether you want to go to college, the G League, or overseas to start your carrer.")
time.sleep(2.1)
print("")
first = int(input("Type 1 to go to college, or 2 to go to the G-League"))
randint = random.randint(1, 28)
if randint == 1:
    GLeagueteam = "Maine Red Claws"
elif randint == 2:
    GLeagueteam = "South Bay Lakers"
elif randint == 3:
    GLeagueteam = "Raptors 905"
elif randint == 4:
    GLeagueteam = "Santa Cruz Warriors"
elif randint == 5:
    GLeagueteam = "Delaware Blue Coats"
elif randint == 6:
    GLeagueteam = "Iowa Wolves"
elif randint == 7:
    GLeagueteam = "Fort Wayne Mad Ants"
elif randint == 8:
    GLeagueteam = "Oklahoma City Blue"
elif randint == 9:
    GLeagueteam = "Texas Legends"
elif randint == 10:
    GLeagueteam = "Rio Grande Valley Vipers"
elif randint == 11:
    GLeagueteam = "Austin Spurs"
elif randint == 12:
    GLeagueteam = "Westcester Knicks"
elif randint == 13:
    GLeagueteam = "Windy City Bulls"
elif randint == 14:
    GLeagueteam = "Canton Charge"
elif randint == 15:
    GLeagueteam = "Stockton Kings"
elif randint == 16:
    GLeagueteam = "Grand Rapids Drive"
elif randint == 17:
    GLeagueteam = "Lakeland Magic"
elif randint == 18:
    GLeagueteam = "Salt Lake City Stars"
elif randint == 19:
    GLeagueteam = "Northern Arizona Suns"
elif randint == 20:
    GLeagueteam = "Sioux Falls Skyforce"
elif randint == 21:
    GLeagueteam = "College Park Skyhawks"
elif randint == 22:
    GLeagueteam = "Long Island Nets"
elif randint == 23:
    GLeagueteam = "Wisconsin Herd"
elif randint == 24:
    GLeagueteam = "Agua Caliente Clippers"
elif randint == 25:
    GLeagueteam = "Capital City Go-Go"
elif randint == 26:
    GLeagueteam = "Erie Bayhawks"
elif randint == 27:
    GLeagueteam = "Greensboro Swarm"
elif randint == 28:
    GLeagueteam = "Mephis Hustle"
#Add overseas option eventually

if first == 1:
    print("College it is! You have offers from Ohio State, Alabama University, and Baylor.")
    college = input("Which college will you like to go to?")
    
    if college == "Ohio" or college == "Ohio State" or college == "ohio" or college == "ohio state":
        print(name, " has commited to Ohio State! Buckeyes for life!")
        time.sleep(1)
        print("There will be 32 games in the season, the first of which is against Cincinaati Bearcats!")
        time.sleep(2)
        print("")
        print("It's the first game of the season, and coach Holtmann puts you in with 5 minutes left in the 1st half, when your down 45-43")
        score = 43
        opp_score = 45
        print("Then, you get the ball, right outside the 3 point line, with a defender straight on you. Do you...")
        time.sleep(1)
        choice1 = int(input("Shoot the ball (Press 1), \n Pass it inside (Press 2), \n or drive into the paint (Press 3)"))
        if choice1 == 1:
            if build == "PG" or build == "SG":
                print("You Score! Three points to your team, you guys are up 46-45!")
                score = 46
                opp_score = 45
            else:
                print("Miss, they get the rebound, and score again! Score: 47-43!")
                score = 43
                opp_score = 47
        elif choice1 == 2:
            if build == "C" or build == "PF" or build == "PG":
                print("You pass it to your teammate, who scores an easy basket. Tied game, 45-45!")
                score = 45
                opp_score = 45
            else:
                print("You pass gets intercepted! The Bearcats go to the other end and score! The score is 43-47")
                score = 43
                opp_score = 47
    
        elif choice1 == 3:
            if build == "C" or build == "PF":
                print("You drive into the paint easily and go for the layup. Easy points! Score: 45-45")
                score = 45
                opp_score = 45
            else:
                print("You try driving into the paint, but you miss the layup. The other team gathers the rebound, and goes to the other side to score!")
                score = 43
                opp_score = 47
        else:
            print("You miss completly, and the ball goes out of bounds!")
            print("The other team goes to the other side and scores! Score: 43-47")
            score = 43
            opp_score = 47
    elif college == "Alabama University" or college == "Alabama" or college == "alabama" or college == "alabama univeristy":
        print("Alabama it is! Let's go Crimson Tide!")
        time.sleep(1)
        print("")
        print("There will be 32 games in the season, the first of which is against Cincinaati Bearcats!")
        time.sleep(2)
        print("")
        print("It's the first game of the season, and coach Oats puts you in with 5 minutes left in the 1st half, when your down 45-43")
        score = 43
        opp_score = 45
        print("Then, you get the ball, right outside the 3 point line, with a defender straight on you. Do you...")
        time.sleep(1)
        choice1 = int(input("Shoot the ball (Press 1), /Pass it inside (Press 2), /or drive into the paint (Press 3)"))
        if choice1 == 1:
            if build == "PG" or build == "SG":
                print("You Score! Three points to your team, you guys are up 46-45!")
                score = 46
                opp_score = 45
            else:
                print("Miss, they get the rebound, and score again! Score: 47-43!")
                score = 43
                opp_score = 47
        elif choice1 == 2:
            if build == "C" or build == "PF" or build == "PG":
                print("You pass it to your teammate, who scores an easy basket. Tied game, 45-45!")
                score = 45
                opp_score = 45
            else:
                print("You pass gets intercepted! The Bearcats go to the other end and score! The score is 43-47")
                score = 43
                opp_score = 47
    
        elif choice1 == 3:
            if build == "C" or build == "PF":
                print("You drive into the paint easily and go for the layup. Easy points! Score: 45-45")
                score = 45
                opp_score = 45
            else:
                print("You try driving into the paint, but you miss the layup. The other team gathers the rebound, and goes to the other side to score!")
                print("Score = 47-43")
                score = 43
                opp_score = 47
        else:
            print("You miss completly, and the ball goes out of bounds!")
            print("The other team goes to the other side and scores! Score: 43-47")
            score = 43
            opp_score = 47
    else:
        print("Baylor it is! Let's go Bears!")
        time.sleep(1)
        print("")
        print("There will be 32 games in the season, the first of which is against Cincinaati Bearcats!")
        time.sleep(2)
        print("")
        print("It's the first game of the season, and coach Drew puts you in with 5 minutes left in the 1st half, when your down 45-43")
        score = 43
        opp_score = 45
        print("Then, you get the ball, right outside the 3 point line, with a defender straight on you. Do you...")
        time.sleep(1)
        choice1 = int(input("Shoot the ball (Press 1), /Pass it inside (Press 2), /or drive into the paint (Press 3)"))
        if choice1 == 1:
            if build == "PG" or build == "SG":
                print("You Score! Three points to your team, you guys are up 46-45!")
                score = 46
                opp_score = 45
            else:
                print("Miss, they get the rebound, and score again! Score: 47-43!")
                score = 43
                opp_score = 47
        elif choice1 == 2:
            if build == "C" or build == "PF" or build == "PG":
                print("You pass it to your teammate, who scores an easy basket. Tied game, 45-45!")
                score = 45
                opp_score = 45
            else:
                print("You pass gets intercepted! The Bearcats go to the other end and score! The score is 43-47")
                score = 43
                opp_score = 47
    
        elif choice1 == 3:
            if build == "C" or build == "PF":
                print("You drive into the paint easily and go for the layup. Easy points! Score: 45-45")
                score = 45
                opp_score = 45
            else:
                print("You try driving into the paint, but you miss the layup. The other team gathers the rebound, and goes to the other side to score!")
                print("Score = 47-43")
                score = 43
                opp_score = 47
        else:
            print("You miss completly, and the ball goes out of bounds!")
            print("The other team goes to the other side and scores! Score: 43-47")
            score = 43
            opp_score = 47
    if score > opp_score:
        print("You have won the very first game of the season! Congratulations!")
    else:
        print("Oh no! You have lost your very first game of the season!")

    print("Now, 32 games later, its time for March Madness to Begin!")
    
    

else:
    print("The G-League! In the draft, if seems that you are in going 3rd in the second round, 31st overall!")
    time.sleep(1)
    print("")
    print("'After much careful consideration, the.....'")
    time.sleep(2)
    print(GLeagueteam, " has chosen", name, ", Congratulations!")
    print("")
    time.sleep(1)
    print("In a G-League Reguar Season, there are 50 regular season games, followed by the playoffs.")
    time.sleep(1)
    print("")
    print("The first game of the season is against the Raptors 905!")
    time.sleep(1)
    print("The coach puts you in with 2 minutes remaining in the game, your team down 73-70!")
    score = 70
    opp_score = 73
    choice1 = int(input("Shoot the ball (Press 1), \n Pass it inside (Press 2), \n or drive into the paint (Press 3)"))
    if choice1 == 1:
        if build == "PG" or build == "SG":
           print("You Score! Three points to your team, the game is tied 73-73!")
           score = 73
           opp_score = 73
        else:
            print("Miss, they get the rebound, and score again! Score: 75-70")
            score = 70
            opp_score = 75
    elif choice1 == 2:
        if build == "C" or build == "PF" or build == "PG":
            print("You pass it to your teammate, who scores an easy basket. They are still winning though, 73-72!")
            score = 72
            opp_score = 73
        else:
            print("You pass gets intercepted! The Bearcats go to the other end and score! The score is 75-70")
            score = 75
            opp_score = 70
    
    elif choice1 == 3:
        if build == "C" or build == "PF":
            print("You drive into the paint easily and go for the layup. Easy points! Score: 73-72")
            score = 72
            opp_score = 73
        else:
            print("You try driving into the paint, but you miss the layup. The other team gathers the rebound, and goes to the other side to score!")
            print("Score = 75-70")
            score = 70
            opp_score = 75
    else:
        print("You miss completly, and the ball goes out of bounds!")
        print("The other team goes to the other side and scores! Score: 75-70")
        score = 70
        opp_score = 75


    
        
