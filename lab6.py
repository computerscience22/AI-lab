import heapq
import math

def astar(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0 + h(start), 0, start))  # (f, g, node)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current == goal:
            # reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor, cost in graph.get(current, []):
            new_cost = g + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + h(neighbor)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    return None  # no path found

# Example heuristic: Euclidean distance
def heuristic(n):
    goal_x, goal_y = 5, 5
    x, y = n
    return math.sqrt((goal_x - x)**2 + (goal_y - y)**2)

# Example graph as adjacency list
example_graph = {
    (0, 0): [((1, 0), 1), ((0, 1), 1)],
    (1, 0): [((1, 1), 1), ((2, 0), 1)],
    (0, 1): [((0, 2), 1), ((1, 1), 1)],
    (1, 1): [((1, 2), 1), ((2, 1), 1)],
    (2, 0): [((3, 0), 1)],
    (0, 2): [((0, 3), 1)],
    (1, 2): [((1, 3), 1)],
    (2, 1): [((3, 1), 1)],
    (3, 0): [((4, 0), 1)],
    (0, 3): [((0, 4), 1)],
    (1, 3): [((1, 4), 1)],
    (3, 1): [((4, 1), 1)],
    (4, 0): [((5, 0), 1)],
    (0, 4): [((0, 5), 1)],
    (1, 4): [((1, 5), 1)],
    (4, 1): [((5, 1), 1)],
    (5, 0): [((5, 1), 1)],
    (0, 5): [((1, 5), 1)],
    (1, 5): [((2, 5), 1)],
    (5, 1): [((5, 2), 1)],
    (2, 5): [((3, 5), 1)],
    (5, 2): [((5, 3), 1)],
    (3, 5): [((4, 5), 1)],
    (5, 3): [((5, 4), 1)],
    (4, 5): [((5, 5), 1)],
    (5, 4): [((5, 5), 1)],
    (5, 5): []
}

# Example usage
path = astar(example_graph, (0, 0), (5, 5), heuristic)
print(path)
