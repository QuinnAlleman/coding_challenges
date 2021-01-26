"""
Problem:
A clock smith must convert power between two gears on a giant clock.
Admittedly, the engineer isn't concerned with efficiency and insists on using other gears to
fill the space without using any type of belt or chain. In his supply, he has an unlimited number
of gears that measure: 1cm, 2cm, 3cm, 5cm, 7cm, and 8cm in diameter.
Any two gears fit perfectly together, for example: a 3cm gear right next to a 7cm gears will measure
10 cm all together.
The distance between the two ends is exactly 1 meter across. The centers of the gears must be 
attached along a line between the Blue and Red gears.

How many combinations of gears can the clock smith connect so that the Blue Gear will rotate in the
same direction as the Red Gear?
For instance, he could use twelve 8cm gears, with one 2cm gears and two 1 cm gears for a total of 15.
(This specific set only counts as 1 solution. Ignore the different arrangements these gears could be in.)

Bonus Question:
Suppose we do care about the number of arrangements of each set. How many ways can the clock smith arrange
gears so that the Blue and Read gear will rotate in the same direction?

FINAL ANSWER:
Order does not matter: 44,958
Order does matter (Bonus Question): 2,937,844,727,743,166,753,554,825,216

"""

gearOptions = [1,2,3,5,7,8] # Diameter of the various available gears. Units are in cm. None of these should repeat.
distance = 100 # Distance between the two gears. Units are in cm

# If you want to test the for the normal rules where the arrangement doesn't matter, set normalQuestion to True. False if you don't want to run it.
# If you want to test for the bonus question requirements, set bonusQuestion to True. False if you don't want to run it.
normalQuestion = True
bonusQuestion = True

# Set printOut to True if you want a printout of each combination for debugging. False if you don't.
printOut = False

# If you want the gears to spin the same way, set this variable to 0. If the opposite, set to 1.
rotation = 0

# Testing possible issues for the input into gearOptions and D.
if not(all(i>0 for i in gearOptions)):
    raise ValueError('Non-positive values listed in gearOptions')
if distance<= 0:
    raise ValueError('Distance between gears should be greater than 0')

def factorial(x): # I know there is a builtin factorial function in math, but I didn't want to use any libraries in case it was against the rules.
    ans = 1
    if x > 0:
        if isinstance(x, int):
            for i in range(1,x+1):
                ans = ans * i
            return ans
        else:
          raise ValueError('I didn\'t want to code factorials for decimal points, so stop')  
    elif x == 0:
        return ans
    else:
        raise ValueError('You are trying to find the factorial of a negative value. You shouldn\'t have to do that here.')

def permutation(comboSet, possibleValues):
    # comboSet is the array  of the combination that needs the permutation found without unique repeating variables.
    # possibleValues is a list of the unique values that could be in comboSet 
    # This is done by taking the permutation and dividing by the factorial of how many times 
        # each variable is repeated. Since the number of elements is equal to the number of 
        # selected elements, then the permutation of an array with x elements is x!. Then this
        # value is divided by the factorial of each element's number of repeated values.
    ans = factorial(len(comboSet))
    for i in range(len(possibleValues)):
        ans = ans / factorial(comboSet.count(possibleValues[i]))
    return ans

def fitGears(remainingDistance, gearNumber, arrangement, modeBQ):
    # remainingDistance is the remainder as you take away a "Gear" from the total length
    # gearNumber is the position in the array of gears. It is the location of the size of gear currently being used.
    # arrangement is the possible solution array. This gives you the option of making sure the 
        # number of gears is odd and finding the permutations of a specific combination of gears.
    # modeBQ This is set to true if you are wanting to test for the arrangements of each combination.   
    if remainingDistance < 0 or gearNumber < 0: # If the gears have taken up too much room, or there are no more gears to try.
        return 0
    if remainingDistance == 0: # If the specific combination of gears in "arrangement" add up to D perfectly.
        if len(arrangement)%2==rotation: # This checks for whether the gears are spinning in the correct orientation relative to each other.
            return 0
        else:
            if printOut: # If the printOut variable is set to 1, it will print out each combination that satisfies the dimensional requirement.
                print(arrangement)
            if modeBQ:
                # This condition checks for if the user cares about the order of the gears.
                # If so, it calls the permutation function to find how many non-unique type permutations there are for "arrangement"
                return(permutation(arrangement, gearOptions))
            else:
                # If the order does not matter, then this combination of gears only counts as 1, instead of the number of permutations.
                return 1
    if remainingDistance > 0:
        # If there is still a remainder, the algorithm will do two things.
        # 1. It will check for arrangements for the remainder minus the gear size with another of the same size taken away.
        # 2. It will check for arrangements with the same remainder but with the next gear size.
        # Doing both of these will make sure that for each combination that still has a positive remainder left, both situations will be tested.
        # This algorithm uses recursion and sums up the possible arrangements and combinations.
        return fitGears(remainingDistance-gearOptions[gearNumber],gearNumber,arrangement + [gearOptions[gearNumber]], modeBQ)\
             + fitGears(remainingDistance, gearNumber-1,arrangement, modeBQ)


def run(): # All this is doing is printing out either/both of the cases for if arrangement matters or not.
    if normalQuestion:
        print("Number of Combinations (Order Doesn't Matter): %d" % fitGears(distance , len(gearOptions)-1 , [], False))
    if bonusQuestion:
        print("Number of Combinations (Order Does Matter - Bonus Question): %d" % fitGears(distance , len(gearOptions)-1 , [], True))

run()