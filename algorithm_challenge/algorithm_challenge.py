def create_hashtable(target):
    hashtable = {}

    for spot in target:
        hashtable[spot] = target.index(spot)

    return hashtable

def check_correct(initial, target):
    for i in range(0, len(initial)):

        if (initial[i] != target[i]):
            return False

    return True

def print_directions(initial, target):

    if (not initial or not target):
        print("\n")
        print("No initial or target positions inputted. Please input two lists.")
        return

    if (initial == target):
        print("No moves needed!")
        check_correct(initial, target)
        return

    hashtable = create_hashtable(target)

    if (initial[0] == 0 and hashtable[0] == 0):

        temp = initial[len(initial)/2]
        temp_spot = initial.index(temp)
        empty = initial.index(0)
        initial[len(initial)/2] = initial[empty]
        initial[empty] = temp

        print("Move car from space " + str(temp_spot) + " to space " + str(empty))
        print(initial)

    values = hashtable.values()
    i = 0

    while i < len(initial):
        
        if (hashtable[0] == initial.index(0) and i < len(initial)-1):
            empty = initial.index(0)
            temp = initial[i]
            temp_spot = initial.index(initial[i])
            initial[temp_spot] = initial[empty]
            initial[empty] = temp

            i+=1

            print("Move car from space " + str(temp_spot) + " to space " + str(empty))
            print(initial)
        else:
            temp = initial[initial.index(values.index(initial.index(0)))]
            temp_spot = initial.index(temp)

            if (temp_spot == hashtable[0] and i < len(initial)-2):
                empty = initial.index(0)
                temp = initial[len(initial)-1]
                temp_spot = len(initial)-1
                initial[temp_spot] = initial[empty]
                initial[empty] = temp
            else:
                empty = initial.index(0)
                initial[temp_spot] = initial[empty]
                initial[empty] = temp

                i+=1
                
            
            print("Move car from space " + str(temp_spot) + " to space " + str(empty))
            print(initial)
    
        if (check_correct(initial, target)):
            print("\n")
            print("Cars in target position!")
            print(initial)
            print(target)
            break
    
    if (not check_correct(initial, target)):
        print("\n")
        print("Cars not in target position!")
        print(initial)
        print(target)

print_directions([0,4,2,5,1,3], [0,1,5,3,2,4])
print("-------------------------------------\n")
print_directions([0,1,5,3,2,4], [0,1,5,3,2,4])
print("-------------------------------------\n")
print_directions([5,2,1,0,3,4], [3,5,4,2,0,1])
print("-------------------------------------\n")
print_directions([],[])
print("-------------------------------------\n")
print_directions([0,1,2,3,4,5], [5,4,3,2,1,0])
print("-------------------------------------\n")
print_directions([0,3,5,4,2,1],[0,4,1,3,5,2])
print("-------------------------------------\n")
print_directions([2,1,0,3,5,4],[3,5,0,1,2,4])