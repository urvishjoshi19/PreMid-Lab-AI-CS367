from collections import deque

# Define the initial, goal, and forbidden states
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

# Check if a state is valid
def is_valid(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    if missionaries < 3 and missionaries > cannibals:
        return False
    return True

# Get all possible states
def get_successors(state):
    missionaries, cannibals, boat = state
    possible_moves = [
        (1, 0), (2, 0), (0, 1), (0, 2), (1, 1)  # Different boat capacities
    ]
    successors = []
    if boat == 1:
        for m, c in possible_moves:
            new_state = (missionaries - m, cannibals - c, 0)
            if is_valid(new_state):
                successors.append(new_state)
    else:
        for m, c in possible_moves:
            new_state = (missionaries + m, cannibals + c, 1)
            if is_valid(new_state):
                successors.append(new_state)
    return successors

# BFS implementation
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path + [goal]
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    return None

# DFS implementation
def dfs(start, goal):
    stack = [(start, [])]
    visited = set()
    visited.add(start)
    while stack:
        current_state, path = stack.pop()
        if current_state == goal:
            return path + [goal]
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                stack.append((successor, path + [current_state]))
    return None

# Compare BFS and DFS solutions
bfs_solution = bfs(initial_state, goal_state)
dfs_solution = dfs(initial_state, goal_state)

print("BFS Solution:", bfs_solution)
print("DFS Solution:", dfs_solution)
