import matplotlib.pyplot as plt

def make_a_graph():
    nums = []
    squares = []
    doubles = []

    for i in range(-15,15):
        nums.append(i)
        squares.append(i*i)
        doubles.append(2*i)
    
    plt.plot(nums, squares)
    plt.plot(nums, doubles)
    plt.legend(['y = x^2', 'y = 2x'])
    plt.savefig("my_first_graph")

make_a_graph()