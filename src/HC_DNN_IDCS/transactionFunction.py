import random as rand

def transaction(solution, upper, hiddenLayer):
    r1 = rand.randint(0,hiddenLayer-1) # choice revise layer or neuron
    r2 = rand.randint(-10,10) # choice revise number

    solution[r1] += r2
    if solution[r1] > upper:
        solution[r1] = upper
    elif solution[r1] <= 0:
        solution[r1] = 1
    return solution