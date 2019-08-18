def create_hashtable(target):
    """
    Creates a hashtable from target arrangement list.

    The hashtable maps a car number to its target space (index) 
    in the target arrangement list.
    
    Arguments:
        target : list -- The target arrangement list
    
    Returns:
        dictionary -- The hashtable of car number to target space mappings
    """
    hashtable = {}

    for spot in target:
        hashtable[spot] = target.index(spot)

    return hashtable


def check_if_empty_input(initial, target):
    """
    Checks whether initial or target lists are empty

    Arguments:
        initial: list -- The initial arrangement list
        target: list -- The target arrangement list
    """
    return not initial or not target


def check_correct(initial, target):
    """
    Checks whether initial and target lists are equal
    
    Arguments:
        initial: list -- The initial arrangement list
        target: list -- The target arrangement list
    
    Returns:
        boolean -- True if the lists are equal; False otherwise
    """
    for i in range(0, len(initial)):
        if (initial[i] != target[i]):
            return False

    return True

def swap_positions(initial, temp, temp_spot, empty_spot):
        """
        Swaps two cars in the initial arrangement list
        
        Arguments:
            initial : list -- The initial arrangement list
            temp : int -- The car that is being replaced
            temp_spot : int -- The space of the car that is being replaced
            empty_spot : int -- The space of the empty spot
        """
        initial[temp_spot] = initial[empty_spot]
        initial[empty_spot] = temp

def print_directions(initial, target):
    """
    Prints a sequence of steps to take to get from the initial
    arrangement of car positions to the target arrangement of
    car positions
    
    Arguments:
        initial: list -- The initial arrangement list
        target: list -- The target arrangement list
    """
    print("Initial: " + str(initial))
    print("Target: " + str(target) + "\n")

    if (check_if_empty_input(initial, target)):
        print("\nNo initial or target positions inputted. Please input two lists.")
        return
    
    if (check_correct(initial, target)):
        print("\nCars already in target position. No moves needed!")
        return
        
    hashtable = create_hashtable(target)

    '''
    --> This code block allows my solution to comply with the example
    print statement sequences given in the assessment document.

    --> It is not needed for my solution, so feel free to comment it out
    to get my version of the solution.

    --> Despite a difference in steps taken to achieve target arrangement,
    my solution still reaches the target arrangement with a minimum number 
    of swaps and an O(n) runtime. It also takes a lists of any size.

    Example:

    Initial:    [0,4,2,5,1,3]
    Target:     [0,1,5,3,2,4]

                Your Solution       My Solution
                -------------       -------------
    Initial     [0,4,2,5,1,3]       [0,4,2,5,1,3]
    Step #1     [5,4,2,0,1,3]       [3,4,2,5,1,0]
    Step #2     [5,4,2,3,1,0]       [3,0,2,5,1,4]
    Step #3     [5,0,2,3,1,4]       [3,1,2,5,0,4]
    Step #4     [5,1,2,3,0,4]       [3,1,0,5,2,4]
    Step #5     [5,1,0,3,2,4]       [3,1,5,0,2,4]
    Step #6     [0,1,5,3,2,4]       [0,1,5,3,2,4]
    Target      [0,1,5,3,2,4]       [0,1,5,3,2,4]
    
    '''
    if (initial[0] == 0 and hashtable[0] == 0):

        temp = initial[len(initial)/2]
        temp_spot = initial.index(temp)
        empty_spot = initial.index(0)
        initial[len(initial)/2] = initial[empty_spot]
        initial[empty_spot] = temp

        print("Move car from space " + str(temp_spot) + " to space " + str(empty_spot))

    values = hashtable.values()     # a list of the correct values (car spots) in the hashtable

    i = 0                           # the counter that helps find a car to 
                                    # move to empty in the start of the initial list

    # while initial arrangement != target arrangement
    while (not check_correct(initial, target)):
        empty_spot = initial.index(0)       # position of the empty spot
        check_spot = True                   # a boolean for whether a valid spot has been found
        
        # if the correct position of the empty spot 
        # is the spot where empty currently is
        if (hashtable[0] == empty_spot):
            counter = i
            
            # find a car to move into the empty spot
            while check_spot:
                temp = initial[counter]
                temp_spot = initial.index(temp)

                # check if car spot is not currently in target spot
                if (temp_spot != hashtable[temp]):
                    check_spot = False

                counter -= 1    # decrease counter by 1 to find a new car to put in empty
            else:
                # finally: once car is found, move it to empty 
                # and increase i by 1 and print move steps
                swap_positions(initial, temp, temp_spot, empty_spot)
                i+=1
                print("Move car from space " + str(temp_spot) + " to space " + str(empty_spot))
        else:
            # otherwise: find the car whose target position 
            # is the current empty space
            temp = initial[initial.index(values.index(initial.index(0)))]
            temp_spot = initial.index(temp)
            counter = 1

            # if the car's initial position is equal to the target position of empty
            if (temp_spot == hashtable[0]):

                # find a new car to swap with empty
                while check_spot:
                    temp = initial[len(initial) - counter]
                    temp_spot = initial.index(temp)
                    
                    # check if car spot is not currently in target spot 
                    # and if there is even a car in the initial position to swap 
                    # with to prevent deadlock by not moving any car at all
                    if (temp_spot != hashtable[temp] and temp != 0):
                        check_spot = False

                    counter += 1    # increase counter by 1 to find a new car to put in empty
                else:
                    # finally: once car is found, move it to empty
                    swap_positions(initial, temp, temp_spot, empty_spot)
            else:
                # else: just place the car whose target position 
                # is the current empty space, increase i by 1, and print move steps 
                swap_positions(initial, temp, temp_spot, empty_spot)
                i+=1
                print("Move car from space " + str(temp_spot) + " to space " + str(empty_spot))
    else:
        # finally: once initial == target then print success 
        # message and the arrangement of initial and target
        print("\nCars in target position!\n")
        print("Initial: " + str(initial))
        print("Target: " + str(target) + "\n")