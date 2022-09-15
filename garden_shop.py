'''
# Riddle 2: Magic Grass.

1. "Super Grass" doubles in size each day
2. One patch cover's Peter's garden in 10 days
3. He wants to cover the garden much quicker and 
   buys 2 patches
4. How many days until Peter's garden is covered?


#1 Garden is covered by Patch #1: 

Patch #1: Cover's the garden in 10 days
          1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8: 128, 9:256, 10:512

#2 Garden is covered by Patch #1 and Patch #2:

Patch #1: 
          1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8: 128, 9:256, 10:512
Patch #2: 
          1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8: 128, 9:256, 10:512

Garden is covered by day 9.


DIY:

Build an implementation for x patches and calculate in how many days
garden will be covered.
'''
from exceptions import ValueNotANumberError

GRASS_SIZE = 512

# get the days it takes to cover a garden withn x patches (p)
def get_days(p):
    days = 1
    grassSize = 1
    grassCovered = False
    while (not grassCovered):
        if ((grassSize * p) >= GRASS_SIZE):
            grassCovered = True
        else:
            days += 1
            grassSize += grassSize
    return days

# print the days taken to cover the garden for n patches (p).
def print_days_taken(p):    
    days = get_days(p)
    print(f"Total time to cover the garden with {p} patches: {days} days.")

def main():
    print("Garden shop (calculator):")
    question_p = "How many patches would you like to buy? "
    question = "Quit the program (q) or do another calculation (y)? [q/y] "
    valid_choice = {"yes": False, "y": False, "ye": False, "quit": True, "q": True}
    quit = False
    while quit == False:
        try:        
            p = input(question_p)
            if not p.isnumeric(): raise ValueNotANumberError()     
            print_days_taken(int(p))
            choice = input(question).lower()
            if (choice in valid_choice):
                quit = valid_choice[choice]    
            else:
                raise ValueError("Error: Invalid answer: '%s'." % choice)
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()