import random
import os
os.system('cls')

# Function to initialize the chessboard with N queens randomly placed
def initial_state(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    queens = random.sample(range(N), N) #returns a list of N random integers from the population of range(N)
    for i in range(N):
        board[i][queens[i]] = 1
    # board=[ [0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 1, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 1, 0, 0, 0],
    #         [0, 1, 0, 0, 0, 1, 0, 1],
    #         [0, 0, 1, 0, 0, 0, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0] ]
    return board

# Function to calculate the number of attacking pairs.
def evaluation_function(board,n)->int:

    pairs=0 # no.of attacking pairs
    k=0 #for indexing of diagonals

    for i in range(n):
        one_count=0
        for j in range(n):
            if board[i][j]==1:
                one_count+=1
        if(one_count>=2):
            pairs+=one_count-1

    for i in range(n):
        one_count=0
        for j in range(n):
            if board[j][i]==1:
                one_count+=1
        if(one_count>=2):
            pairs+=one_count-1

    for i in range(n):
        k=0
        one_count=0
        for j in range(n-i-1,n,1):
            if board[k][j]==1:
                one_count+=1
            k+=1
        if(one_count>=2):
            pairs+=one_count-1

    for i in range(1,n):
        k=i
        one_count=0
        for j in range(n-i):
            if board[k][j]==1:
                one_count+=1
            k+=1
        if(one_count>=2):
            pairs+=one_count-1
         
    for i in range(n):
        k=0
        one_count=0
        for j in range(i,-1,-1):
            if board[k][j]==1:
                one_count+=1
            k+=1
        if(one_count>=2):
            pairs+=one_count-1

    for i in range(1,n):
        k=n-1
        one_count=0
        for j in range(i,n):
            if board[k][j]==1:
                one_count+=1
            k-=1
        if(one_count>=2):
            pairs+=one_count-1
    
    return pairs


#* Generate Succesors
def generate_successors(board):
    successors = []

    # Iterate through each column
    for col in range(len(board)):
        # Iterate through each row in the column
        for row in range(len(board)):
            # If there is a queen in the current position, consider moving it
            if board[row][col] == 1:
                # Generate successor states by moving the queen to an empty space in the same column
                for new_row in range(len(board)):
                    if new_row != row:
                        # Create a new board by copying the current state
                        new_board = [row[:] for row in board]
                        # Move the queen to the new position
                        new_board[row][col] = 0
                        new_board[new_row][col] = 1
                        # Add the new state to the list of successors
                        successors.append(new_board)

    return successors


#* Basic Hill-Climbing algorithm(Steepest Ascent)

def hill_climbing(N):
    current_state = initial_state(N) #choosing a random initial state
    current_value = evaluation_function(current_state,len(current_state))
    steps = 0
    while True:
        successors = generate_successors(current_state)
        if not successors: #if no succcessors can be generated
            break
        best_successor = min(successors, key=lambda x: evaluation_function(x,len(x)))
        best_value = evaluation_function(best_successor,len(best_successor))
        if best_value >= current_value: # if all the next generated has evaluation value greater than the current state
            break
        current_state = best_successor
        current_value = best_value
        steps += 1
    return current_state, current_value, steps



#* Hill-Climbing algorithm with sideways moves (100 maximum)

def hill_climbing_sideways_moves(N):
    current_state = initial_state(N)
    current_value = evaluation_function(current_state,len(current_state))
    steps = 0
    sideways_moves = 0
    while sideways_moves < 100:
        successors = generate_successors(current_state)
        if not successors:
            break
        best_successor = min(successors, key=lambda x: evaluation_function(x,len(x)))
        best_value = evaluation_function(best_successor,len(best_successor))
        if best_value > current_value:
            break
        if best_value == current_value:
            sideways_moves += 1
        else:
            sideways_moves = 0
        current_state = best_successor
        current_value = best_value
        steps += 1
    return current_state, current_value, steps

#* Queens Problem
N = 8  # Change N to the desired size of the board
initial_board = initial_state(N)
initial_value = evaluation_function(initial_board,len(initial_board))

#Printing the initial state and  initial heuristic value
print("Initial State:")
for row in initial_board:
    print(row)
print("Initial Heuristic Value:", initial_value)

#* Steepest Ascent Hill Climbing
solution_hill_climbing, solution_value_hc, steps_hc = hill_climbing(N)

print("\nSolution State (Hill Climbing):")
for row in solution_hill_climbing:
    print(row)
print("Heuristic Value of Solution:", solution_value_hc)
print("Number of Steps:", steps_hc)

#* Hill Climbing (Sideways Movement)
solution_sideways, solution_value_sideways, steps_sideways = hill_climbing_sideways_moves(N)

print("\nSolution State (Hill Climbing with Sideways Moves):\n")
for row in solution_sideways:
    print(row)
print("Heuristic Value of Solution:", solution_value_sideways)
print("Number of Steps:", steps_sideways)



