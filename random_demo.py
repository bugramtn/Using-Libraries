import random

def do_random_stuff():
    a_random_number = random.random()
    print(a_random_number)

    a_random_integer = random.randint(1, 100)
    print(a_random_integer)

    options = ["The Brothers Karamazov", "Rashomon", "Steppenwolf", "Journey to the End of the Night"]
    a_random_string = random.choice(options)
    print(a_random_string)
    
do_random_stuff()