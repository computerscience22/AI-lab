# Given two jugs, one with a capacity of x litres and the other with a capacity of 5 litres. you need to measure exactly z litres of water using these 2 jugs.
# Allowed operations are:
# 1. Fill one of the jugs.
# 2. Empty one of the jugs.
# 3. Pour water from one jug to the other until one of the jugs is either full or empty.

from collections import deque

def water_jug_solver_bfs(x, y, z):
    if z > max(x, y):  
        return "Not possible"

    visited = set()  # To track visited states
    queue = deque()  # BFS queue
    queue.append((0, 0))  # Initial state (both jugs empty)
    
    while queue:
        jug1, jug2 = queue.popleft()  # Current state

        # If we measure exactly z liters, return success
        if jug1 == z or jug2 == z:
            return f"Possible to measure {z} liters!"

       
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

       
        queue.append((x, jug2))  # Fill Jug 1
        queue.append((jug1, y))  # Fill Jug 2
        queue.append((0, jug2))  # Empty Jug 1
        queue.append((jug1, 0))  # Empty Jug 2

        # Pour water from Jug 1 -> Jug 2
        pour1 = min(jug1, y - jug2)  
        queue.append((jug1 - pour1, jug2 + pour1))

        # Pour water from Jug 2 -> Jug 1
        pour2 = min(jug2, x - jug1)  
        queue.append((jug1 + pour2, jug2 - pour2))

    return "Not possible"


print(water_jug_solver_bfs(6, 7, 5)) 
