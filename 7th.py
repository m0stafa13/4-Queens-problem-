N = 4
#*function to check if the new place is empty
def is_safe(state, column):
    row = len(state)
    for old_row in range(len(state)):
        old_column = state[old_row]
        if old_column == column:
            return False
        if abs(old_column - column) == abs(old_row - row):
            return False
    return True

    #!printing tha atrix
def print_board(state):
    for row in range(N):
        for column in range(N):
            if state[row] == column:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


        
# DFS with Backtracking
def dfs(state):
    print("Visit:", state)
    if len(state) == N:
        return state
    for column in range(N):
        if is_safe(state, column):
            new_state = state + [column]
            result = dfs(new_state)
            if result is not None:
                return result
            print("Backtrack:", new_state)
    return None


# A* Heuristic
def checkQueenNumber(state):
    return N - len(state)


# A* Search
def a_star():
    open_list = [[]]
    while open_list:
        best_state = min(
            open_list,
            key=lambda state: (
                #role f(n)=g(n)+h(n)
                len(state) + checkQueenNumber(state),
                -len(state)
            )
        )
        open_list.remove(best_state)
        print("Expand:", best_state)
        # Goal state
        if len(best_state) == N:
            return best_state
        # Generate new states
        for column in range(N):
            if is_safe(best_state, column):
                new_state = best_state + [column]
                open_list.append(new_state)
    return None


# Main Program
print("DFS")
dfs_solution = dfs([])
print("DFS Solution:", dfs_solution)
if dfs_solution is not None:
    print_board(dfs_solution)
print("\nA*")
astar_solution = a_star()
print("A* Solution:", astar_solution)
if astar_solution is not None:
    print_board(astar_solution)
