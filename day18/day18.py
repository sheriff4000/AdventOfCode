def shortest_path(blocked, dims=(70, 70)):
    stack = [(0, 0, 0)]
    # visited = set()
    step_map = {}
    while stack:
        x, y, steps = stack.pop(0)
        if (x, y) in step_map and step_map[(x, y)] <= steps:
            continue
        step_map[(x, y)] = steps

        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < dims[0]+1 and 0 <= ny < dims[1]+1 and (nx, ny) not in blocked:
                stack.append((nx, ny, steps+1))
    return step_map.get(dims, None)

def min_obstacles(ordered_blocks):
    l = 0
    r = len(ordered_blocks)-1
    while l < r:
        print(l, r)
        m = (l + r) // 2
        if shortest_path(set(ordered_blocks[:m])) is not None:
            l = m+1
        else:
            r = m-1

    return ordered_blocks[l]

with open('day18/real.txt') as f:
    lines = f.read().splitlines()

blocked_points = set()
for line in lines:
    x, y = tuple(map(int, line.split(",")))
    blocked_points.add((x, y))   
    
ordered_blocks = [tuple(map(int, line.split(","))) for line in lines]


print(shortest_path(blocked_points))
print(min_obstacles(ordered_blocks))