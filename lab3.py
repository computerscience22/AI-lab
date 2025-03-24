def solve(c1, c2, tgt):
    v = set()
    
    def dfs(j1, j2, path=[]):
        if (j1, j2) in v: 
            return None
        
        v.add((j1, j2))
        current_path = path + [(j1, j2)]

        if j1 == tgt or j2 == tgt: 
            return current_path
        
        result = dfs(c1, j2, current_path)
        if result: return result

        result = dfs(j1, c2, current_path)
        if result: return result

        result = dfs(0, j2, current_path)
        if result: return result

        result = dfs(j1, 0, current_path)
        if result: return result

        result = dfs(max(0, j1 - (c2 - j2)), min(c2, j1 + j2), current_path)
        if result: return result

        result = dfs(min(c1, j1 + j2), max(0, j2 - (c1 - j1)), current_path)
        if result: return result
        
        return None
    
    return dfs(0, 0)

def print_solution(steps, c1, c2):
    if not steps:
        print("Not possible")
        return
    
    print(f"Solution to measure {tgt} liters using jugs of capacity {c1} and {c2}:")
    
    for i in range(len(steps) - 1):
        curr_j1, curr_j2 = steps[i]
        next_j1, next_j2 = steps[i+1]
        
        if next_j1 == c1 and curr_j1 < c1:
            print(f"Fill jug 1: ({curr_j1}, {curr_j2}) -> ({next_j1}, {next_j2})")
        elif next_j2 == c2 and curr_j2 < c2:
            print(f"Fill jug 2: ({curr_j1}, {curr_j2}) -> ({next_j1}, {next_j2})")
        elif next_j1 == 0 and curr_j1 > 0:
            print(f"Empty jug 1: ({curr_j1}, {curr_j2}) -> ({next_j1}, {next_j2})")
        elif next_j2 == 0 and curr_j2 > 0:
            print(f"Empty jug 2: ({curr_j1}, {curr_j2}) -> ({next_j1}, {next_j2})")
        elif next_j1 < curr_j1 and next_j2 > curr_j2:
            print(f"Pour from jug 1 to jug 2: ({curr_j1}, {curr_j2}) -> ({next_j1}, {next_j2})")
        elif next_j1 > curr_j1 and next_j2 < curr_j2:
            print(f"Pour from jug 2 to jug 1: ({curr_j1}, {curr_j2}) -> ({next_j1}, {next_j2})")
    
    last_j1, last_j2 = steps[-1]
    if last_j1 == tgt:
        print(f"Target achieved: {tgt} liters in jug 1")
    else:
        print(f"Target achieved: {tgt} liters in jug 2")

c1, c2, tgt = 2, 6, 5
solution_steps = solve(c1, c2, tgt)
if solution_steps:
    print_solution(solution_steps, c1, c2)
else:
    print("Not possible")