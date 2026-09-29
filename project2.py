print("Your mission to a strange planet has gone horribly wrong. Your crew left you after you crashed, and you are stranded.")
print("\nYou only have 10 days' worth of food and water, but you have shelter in the wreck of your spaceship")
print("\nYou don't know much about the planet. It could sustain life, and has small amounts of water, but aside from that it's a mystery.")
stayorgo = input("Do you stay in place?")
if stayorgo == "Yes" or stayorgo == "yes" or stayorgo == "yeah":
    print("You choose to await a rescue mission. After 3 days, your supplies are depleted.")
    rescue = input("Do you settle in and start rationing, leave and try to find more food, or give it another day? Respond with 'another day,' 'ration,' or 'search.'")
    if rescue == "search":
        oasis = input("You encounter a safe haven. It has water, but it is purple and bubbling. Do you drink?")
        if oasis == "yes" or oasis == "Yes" or oasis == "yeah":
            print("The water was toxic. You try to survive, but cannot. You lose.")
        elif oasis == "no" or oasis == "No":
            thirsty = input("After a day looking, you can't find any other water. Do you try to return to the haven and drink?")
            if thirsty == "yes" or thirsty == "yeah" or thirsty == "Yes":
                print("You can't find the oasis again. After a day, you run out of water. You lose.")
            elif thirsty == "No" or thirsty == "no":
                print("You keep walking. Within a few hours, you see a light in the distance. It is a town of humanoid aliens.")
                print("They welcome you in and offer food and drink. You live happily for the rest of your days.")
            else:
                print("Wrong input. Say 'yes' or 'no' with no space.")
        else:
            print("Wrong input. Say 'yes' or 'no' with no space.")
    elif rescue == "another day":
        print("You continue as normal for another day, but now have almost no supplies and no rescue arrives.")
        leave = input("You have to leave. Do you go east or west?")
        if leave == "west" or leave == "West":
            print("You head west. Eventually, you reach a tropical beach. There is plenty of food and shelter, and you can live there as long as you need.")
        elif leave == "east" or leave == "East":
            print("You head east. Quickly, you run into the barren desert. There is no water or food, only long-forgotten fossils. You lose.")
    elif rescue == "ration":
        timeuse = input("You decide to ration your remaining food. In your spare time, do you try to establish communication with your crew or conserve energy? Respond with 'conserve' or 'comms.' ")
        if timeuse == "comms" or timeuse == "Comms":
            print ("You are able to hot-wire a radio and reach your crew.")
            print ("They pick you up within a few days. You are heading home.")
        elif timeuse == "conserve" or timeuse == "Conserve":
            print("After ten days you run out of food and water. You lose.")
        else:
            print("Wrong input. Say 'yes' or 'no' with no space.")
    else:
        print("Wrong input. Say 'ration,' 'search,' or 'another day' with no space.")
elif stayorgo == "No" or stayorgo == "no":
    alien = input("You see a strange grey blob moving quickly towards you. Do you run?")
    if alien == "yes" or alien == "Yes" or alien == "yeah":
        walk = input("You turn to run, but fall down a sinkhole into a deep pit. It is dark, and you cannot see. Do you try to walk forward?")
        if walk == "Yes" or walk == "yes" or walk == "yeah":
            print("You fall down into deep water, with no way out. You lose.")
        elif walk == "no" or walk == "No":
            run = input("After a few minutes, you are surrounded by a bright light. You can make out bug-like aliens. Do you run?")
            if run == "no" or run == "No":
                print("You cannot communicate with them, and eventually they leave you. You are stuck. You lose.")
            elif run == "Yes" or run == "yes" or run == "yeah":
                print("You run, and they don't give chase. You see a set of stairs going up, and take it.")
                print("You find yourself inside a well-stocked cave, with food and water, as well as a working communication device.")
                print()
                print("You reach out to your space agency, and they pick you up and bring you home.")
            else:
                print("Wrong input. Say 'yes' or 'no' with no space.")
        else:
            print("Wrong input. Say 'yes' or 'no' with no space.")
    elif alien == "no" or alien == "No":
        follow = input("The aliens seem friendly. They motion for you to follow them. Do you?")
        if follow == "yes" or follow == "Yes" or follow == "yeah":
            print("They take you to a shelter, and give you food and water. You live peacefully with them for the rest of your life.")
        elif follow == "no" or follow == "No":
            print("You are alone in the dark, with no supplies. You lose.")
        else: 
            print("Wrong input. Say 'yes' or 'no' with no space.")
    else:
        print("Wrong input. Say 'yes' or 'no' with no space.")
else:
    print("Wrong input. Say 'yes' or 'no' with no space.")
        
