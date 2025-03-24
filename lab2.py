# Given two jugs, one with a capacity of x litres and the other with a capacity of 5 litres. you need to measure exactly z litres of water using these 2 jugs.
# Allowed operations are:
# 1. Fill one of the jugs.
# 2. Empty one of the jugs.
# 3. Pour water from one jug to the other until one of the jugs is either full or empty.

from collections import defaultdict, deque

def water_jug_solver_graph(x, z):
    # Graph to represent states and transitions
    class Graph:
        def __init__(self):
            self.graph = defaultdict(list)
        
        def add_edge(self, u, v):
            self.graph[u].append(v)
        
        def bfs(self, start, target_check):
            visited = set([start])
            queue = deque([start])
            
            # Dictionary to store parent of each state for path reconstruction
            parent = {start: None}
            
            while queue:
                current = queue.popleft()
                
                # Check if current state satisfies our goal
                if target_check(current):
                    # Reconstruct the path
                    path = []
                    while current is not None:
                        path.append(current)
                        current = parent[current]
                    path.reverse()  # Reverse to get path from start to goal
                    return True, path
                
                # Visit all adjacent states
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        parent[neighbor] = current
            
            return False, []
    
    # Create graph
    g = Graph()
    
    # Create nodes and edges - using BFS to build the graph
    build_queue = deque([(0, 0)])
    visited_states = set([(0, 0)])
    
    while build_queue:
        a, b = build_queue.popleft()
        state = (a, b)
        w = 5
        
        # Generate all next states
        next_states = [
            (x, b),  # Fill jug 1
            (a, w),  # Fill jug 2
            (0, b),  # Empty jug 1
            (a, 0),  # Empty jug 2
            (a - min(a, w- b), b + min(a, w - b)),  # Pour jug 1 to jug 2
            (a + min(b, x - a), b - min(b, x - a))   # Pour jug 2 to jug 1
        ]
        
        for next_state in next_states:
            g.add_edge(state, next_state)
            
            if next_state not in visited_states:
                visited_states.add(next_state)
                build_queue.append(next_state)
    
    # Check if a state satisfies our goal
    def is_goal(state):
        a, b = state
        return a == z or b == z or a + b == z
    
    # Start BFS from initial state (0, 0)
    return g.bfs((0, 0), is_goal)

# Example usage
x = 3  # Capacity of the first jug
z = 4  # Desired amount of water

result, path = water_jug_solver_graph(x, z)
print(f"Solution exists: {result}")

if result:
    print("\nPath to solution:")
    print("----------------")
    for i, state in enumerate(path):
        a, b = state
        print(f"Step {i}: Jug 1 = {a} liters, Jug 2 = {b} liters")
        if a == z or b == z or a + b == z:
            print(f"Goal reached! We have {z} liters of water.")
            break
else:
    print(f"It's not possible to measure exactly {z} liters with these jugs.")