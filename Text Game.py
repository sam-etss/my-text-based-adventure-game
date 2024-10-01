inventory=[]
options = ["north", "south", "east", "west", "grab", "use"]
def text_game():
    print("You wake up in the middle of a bustling cafeteria you must have dozed off during lunch break you look at timetable and realize\nenglish starts in 3 minutes.")
    print("The only thing is you have alot to do before you can go to class you must: Get Macbeth from your locker, fill up your water, get your copy. And remember you must not get caught by the janitor on your way to class.")
    print("You are in the cafeteria on the ground floor, sitting at a table infront of you is a empty water bottle.\n{possible exits} east")
    while True:
        move=input ("Enter your move: ")
        if move=="grab" and "grab" in options:
             inventory.append("water bottle *empty*")
             print("You pick up the water bottle")
             options.remove("grab")
        elif move=="east":
          print("You are now in a long hallway with hundreds of lockers and kids racing to class.\n {possible exits} north, south, west")
          break
        else:
            print("Not a valid move")
      
    








text_game()