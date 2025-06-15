import math

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to build distance matrix
def build_distance_matrix(points):
    n = len(points)
    return [[distance(points[i], points[j]) for j in range(n)] for i in range(n)]

# Function to calculate mean distance for each point
def mean_distances(matrix):
    return [sum(row)/len(row) for row in matrix]

# Main function to plan robot path
def robo_path_mean_heuristic(points):
    n = len(points)
    matrix = build_distance_matrix(points)
    means = mean_distances(matrix)
    
    visited = [False] * n
    path = []

    current = means.index(min(means))  # Start from the most central point
    path.append(current)
    visited[current] = True

    for _ in range(n - 1):
        next_city = None
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and matrix[current][j] < min_dist:
                min_dist = matrix[current][j]
                next_city = j
        path.append(next_city)
        visited[next_city] = True
        current = next_city

    return path, matrix

# Function to calculate total path distance
def total_path_distance(path, matrix):
    dist = 0
    for i in range(len(path) - 1):
        dist += matrix[path[i]][path[i + 1]]
    dist += matrix[path[-1]][path[0]]  # Return to start
    return dist

# --- User Input Section ---
points = []
n = int(input("Enter number of waypoints: "))

for i in range(n):
    x = float(input(f"Enter x coordinate of point {i + 1}: "))
    y = float(input(f"Enter y coordinate of point {i + 1}: "))
    points.append((x, y))

# Run the path planner
path, matrix = robo_path_mean_heuristic(points)
total = total_path_distance(path, matrix)

# Output Results
print("\nWaypoints (index: x, y):")
for i, p in enumerate(points):
    print(f"{i}: {p}")

print("\nRobot visiting order (by index):", path)
print("Total distance travelled by robot:", round(total, 2))
