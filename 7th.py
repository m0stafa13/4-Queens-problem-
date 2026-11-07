numberQ =4
#*function to check if the new place is empty
def isSave(state, column):
    row = len(state)
    for old_row in range(len(state)):
        old_column = state[old_row]
        if old_column == column:
            return False
        if abs(old_column - column) == abs(old_row - row):
            return False
    return True

    #!printing tha matrix
def print_board(state):
    for row in range(numberQ):
        for column in range(numberQ):
            if state[row] == column:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()

# DFS with Backtracking
def dfs(state):
    print("Visit:", state)
    if len(state) == numberQ:
        return state
    for column in range(numberQ):
        if isSave(state, column):
            new_state = state + [column]
            result = dfs(new_state)
            if result is not None:
                return result
            print("Backtrack:", new_state)
    return None

# A* Heuristic
def checkQueenNumber(state):
    return numberQ - len(state)

# A* Search
def a_star():
    aStarInitial = [[]]
    while aStarInitial:
        best_state = min(
            aStarInitial,
            key=lambda state: (
                #role f(n)=g(n)+h(n)
                len(state) + checkQueenNumber(state),
                -len(state)
            )
        )
        aStarInitial.remove(best_state)
        print("Expand:", best_state)
        # Goal state
        if len(best_state) == numberQ:
            return best_state
        # Generate new states
        for column in range(numberQ):
            if isSave(best_state, column):
                new_state = best_state + [column]
                aStarInitial.append(new_state)
    return None

# Main Program
print("DFS")
dfsInitialState = dfs([])
print("DFS Solution:", dfsInitialState)
if dfsInitialState is not None:
    print_board(dfsInitialState)
print("\nA*")
aStarSolution = a_star()
print("A* Solution:", aStarSolution)
if aStarSolution is not None:
    print_board(aStarSolution)
