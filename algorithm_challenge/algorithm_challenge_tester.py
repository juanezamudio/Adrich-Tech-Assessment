import unittest
import random
import algorithm_challenge as file

print_directions = file.print_directions
check_correct = file.check_correct
check_if_empty_input = file.check_if_empty_input

class TestPrintDirections(unittest.TestCase):

    def test_print_directions_empty_start(self):
        print("\n")
        initial = [0,4,2,5,1,3]
        target = [0,1,5,3,2,4]

        print_directions(initial, target)

        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")

        initial = [0,3,5,4,2,1]
        target = [0,4,1,3,5,2]

        print_directions(initial, target)
        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")

    def test_print_directions_equal(self):
        print("\n")
        initial = [0,1,5,3,2,4]
        target = [0,1,5,3,2,4]

        print_directions(initial, target)

        self.assertTrue(check_correct(initial,target))

        print("-------------------------------------")

        initial = [0,1,5,3,2,4]
        random.shuffle(initial)
        target = initial

        print_directions(initial, target)

        self.assertTrue(check_correct(initial,target))

        print("-------------------------------------")

    def test_print_directions_empty_middle(self):
        print("\n")
        initial = [5,2,1,0,3,4]
        target = [3,5,4,2,0,1]

        print_directions(initial, target)

        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")

        initial = [3,5,0,4,2,1]
        target = [4,1,3,0,5,2]

        print_directions(initial, target)
        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")


    def test_print_directions_no_input(self):
        print("\n")
        initial = []
        target = []

        print_directions(initial, target)

        self.assertTrue(check_if_empty_input(initial, target))

        print("-------------------------------------")

        initial = []
        target = [4,2,1,0,3,5]

        print_directions(initial, target)

        self.assertTrue(check_if_empty_input(initial, target))

        print("-------------------------------------")

        initial = [4,2,1,0,3,5]
        target = []

        print_directions(initial, target)

        self.assertTrue(check_if_empty_input(initial, target))

        print("-------------------------------------")
        

    def test_print_directions_reverse(self):
        print("\n")
        initial = [0,1,2,3,4,5]
        target = [5,4,3,2,1,0]

        print_directions(initial, target)
        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")
        
        initial = [5,4,3,2,1,0]
        target = [0,1,2,3,4,5]

        print_directions(initial, target)
        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")

    def test_print_directions_empty_middle_start(self):
        print("\n")
        initial = [2,1,0,3,5,4]
        target = [3,5,0,1,2,4]

        print_directions(initial, target)

        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")

        initial = [3,5,4,0,2,1]
        target = [4,1,3,0,5,2]

        print_directions(initial, target)
        self.assertTrue(check_correct(initial, target))

        print("-------------------------------------")

    def test_print_directions_random_one(self):
        print("\n")
        initial = [5,4,3,2,1,0]
        random.shuffle(initial)

        target = [0,1,2,3,4,5]
        random.shuffle(target)

        print(initial)
        print(target)

        print_directions(initial, target)

        self.assertTrue(check_correct(initial,target))

        print("-------------------------------------")

    def test_print_directions_random_two(self):
        print("\n")
        initial = [2,4,5,0,1,3]
        random.shuffle(initial)

        target = [0,1,2,3,4,5]
        random.shuffle(target)

        print(initial)
        print(target)

        print_directions(initial, target)

        self.assertTrue(check_correct(initial,target))

        print("-------------------------------------")

    def test_print_directions_random_three(self):
        print("\n")
        initial = [1,3,5,4,0,2]
        random.shuffle(initial)

        target = [0,1,2,3,4,5]
        random.shuffle(target)

        print(initial)
        print(target)

        print_directions(initial, target)

        self.assertTrue(check_correct(initial,target))

        print("-------------------------------------")

    def test_print_directions_random_four(self):
        print("\n")
        initial = [1,4,2,0,3,5]
        random.shuffle(initial)

        target = [0,1,2,3,4,5]
        random.shuffle(target)

        print(initial)
        print(target)

        print_directions(initial, target)

        self.assertTrue(check_correct(initial,target))

        print("-------------------------------------")

    if __name__ == '__main__':
        unittest.main()