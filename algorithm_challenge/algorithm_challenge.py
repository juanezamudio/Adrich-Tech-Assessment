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


def print_directions(initial, target):
    """
    
    
    Arguments:
        initial {[type]} -- [description]
        target {[type]} -- [description]
    """
    if (check_if_empty_input(initial, target)):
        print("\nNo initial or target positions inputted. Please input two lists.")
        return
    else:
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
    of swaps and runs in O(n) time

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
        empty = initial.index(0)
        initial[len(initial)/2] = initial[empty]
        initial[empty] = temp

        print("Move car from space " + str(temp_spot) + " to space " + str(empty))


    values = hashtable.values()
    i = 0
    while i < len(initial):
        
        if (hashtable[0] == initial.index(0) and i < len(initial)-1):
            counter = i
            check_spot = True
            
            while check_spot:
                empty = initial.index(0)
                temp = initial[counter]
                temp_spot = initial.index(initial[counter])

                if (temp_spot != hashtable[temp]):
                    check_spot = False

                counter -= 1
            else:
                initial[temp_spot] = initial[empty]
                initial[empty] = temp

            i+=1

            print("Move car from space " + str(temp_spot) + " to space " + str(empty))
        else:
            temp = initial[initial.index(values.index(initial.index(0)))]
            temp_spot = initial.index(temp)
            counter = 1
            check_spot = True

            if (temp_spot == hashtable[0] and i < len(initial)-2):
                
                while check_spot:
                    empty = initial.index(0)
                    temp = initial[len(initial)-counter]
                    temp_spot = initial.index(temp)
                    
                    if (temp_spot != hashtable[temp] and temp != 0):
                        check_spot = False

                    counter += 1
                else:
                    initial[temp_spot] = initial[empty]
                    initial[empty] = temp
            else:
                empty = initial.index(0)
                initial[temp_spot] = initial[empty]
                initial[empty] = temp

                i+=1
                
            
            print("Move car from space " + str(temp_spot) + " to space " + str(empty))
    
        if (check_correct(initial, target)):
            print("\nCars in target position!")
            print(initial)
            print(target)
            break
    
    if (not check_correct(initial, target)):
        print("\nCars not in target position!")
        print(initial)
        print(target)