name = input("Hi! What's your name?")

print(f"Hey {name}. Let's make a fill in the blank story today.")
print("You will have to complete a cooking challenge")
food1 = input("Pick a main to start with")
print(f"Alright, {food1} sounds good")
foodvessel1 = input("What would you like to cook in? A pot? Pan? Oven? Something else?")
time1 = input("Ok, now that you've picked a vessel for your main, how long would you like to cook for")
if time1 == "1 hour":
    print("You sure that won't burn?")
    print("Seems awfully long")
else:
    print(f"Ok,{time1} seems ok")
cookingoil1 = input("What cooking oil do you want to use - vegetable oil, olive oil, canola oil, or none?")
print("Next up, you're gonna want a side to go with your main")
food2 = input(f"Pick something small that would taste good with {food1}")
print("Now that you have your side, you're going to need a vessel for it.")
foodvessel2 = input("What will you cook your side in?")
cookingoil2 = input("With what oil?")
time2 = input("And for how long")
if time2 == "30 minutes": 
    print("Maybe a little long, but ok")
else:
    print("Ok then")
print(f"Here's your meal: {food1}, in a {foodvessel1}, made with {cookingoil1}, cooked for {time1}.")
print(f"To go with that, you have {food2}, in a {foodvessel2}, with {cookingoil2}, cooked for {time2}.")
print("Bon appetit!")



    