# Write a program for hopfield network.

import numpy as np

def compute_next_state(state, weights):
  
    next_state = np.where(weights @ state >= 0, +1, -1)
    return next_state

def compute_final_state(initial_state, weights, max_iter=1000):
  
    previous_state = initial_state
    next_state = compute_next_state(previous_state, weights)
    is_stable = np.all(previous_state == next_state)
    n_iter = 0

    while not is_stable and n_iter <= max_iter:
        previous_state = next_state
        next_state = compute_next_state(previous_state, weights)
        print("Iteration:", n_iter)
        print("Previous State:", previous_state)
        print("Next State:", next_state)
        is_stable = np.all(previous_state == next_state)
        n_iter += 1

    return previous_state, is_stable, n_iter

# Initialize the initial state and weight matrix
initial_state = np.array([+1, -1, -1, -1])
weights = np.array([[0, -1, -1, +1], 
                    [-1, 0, +1, -1], 
                    [-1, +1, 0, -1], 
                    [+1, -1, -1, 0]])

# Compute the final state
final_state, is_stable, n_iter = compute_final_state(initial_state, weights)

# Print the results
print("Final State:", final_state)
print("Is Stable:", is_stable)
print("Number of Iterations:", n_iter)
