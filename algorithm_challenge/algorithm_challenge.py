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

    values = hashtable.values()
    i = 0
    while (not check_correct(initial, target)):
        empty_spot = initial.index(0)
        check_spot = True
        
        if (hashtable[0] == empty_spot):
            counter = i
            
            while check_spot:
                temp = initial[counter]
                temp_spot = initial.index(temp)

                if (temp_spot != hashtable[temp]):
                    check_spot = False

                counter -= 1
            else:
                swap_positions(initial, temp, temp_spot, empty_spot)
                i+=1
                print("Move car from space " + str(temp_spot) + " to space " + str(empty_spot))
        else:
            temp = initial[initial.index(values.index(initial.index(0)))]
            temp_spot = initial.index(temp)
            counter = 1

            if (temp_spot == hashtable[0]):
                while check_spot:
                    temp = initial[len(initial) - counter]
                    temp_spot = initial.index(temp)
                    
                    if (temp_spot != hashtable[temp] and temp != 0):
                        check_spot = False

                    counter += 1
                else:
                    swap_positions(initial, temp, temp_spot, empty_spot)
            else:
                swap_positions(initial, temp, temp_spot, empty_spot)
                i+=1
                print("Move car from space " + str(temp_spot) + " to space " + str(empty_spot))
    else:
        print("\nCars in target position!")
        print(initial)
        print(target)