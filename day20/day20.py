from collections import defaultdict

def cheats_from_point(grid, point, cheat_size, cheat_set=set()):
    stack = [(point, 0)]
    visited = set()
    visited.add(point)
    while stack:
        (x, y), depth = stack.pop(0)
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            new_depth = depth + 1
            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and ((nx, ny) not in visited) and (new_depth <= cheat_size):
                stack.append(((nx, ny), new_depth))
                visited.add((nx, ny))
                if grid[nx][ny] != "#":
                    cheat_set.add(((point, (nx, ny)), new_depth))
    return cheat_set

def find_cheats(grid, start_point, cheat_size=2):
    stack = [start_point]
    path = {}
    path_count = 0
    cheat_set = set()
    while stack:
        x, y = stack.pop()
        if (x, y) in path:
            continue
        path[(x, y)] = path_count
        path_count += 1
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and (grid[nx][ny] != "#"):
                stack.append((nx, ny))
        cheats_from_point(grid, (x, y), cheat_size=cheat_size, cheat_set=cheat_set)
    cheat_sizes = defaultdict(int)
    for cheat, dist in cheat_set:
        time_save = path[cheat[1]] - path[cheat[0]] - dist
        cheat_sizes[time_save] += 1
        
    return cheat_sizes


def part1(grid, start_point):
    cheats = find_cheats(grid, start_point)
    total = 0
    for (time_save, count) in cheats.items():
        if time_save >= 100:
            total += count
    return total

def part2(grid, start_point):
    cheats = find_cheats(grid, start_point, cheat_size=20)
    total = 0
    for time_save, count in cheats.items():
        if time_save >= 100:
            total += count
            
    return total

with open('day20/real.txt') as f:
    grid = f.read().splitlines()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start_point = (i, j)
            break

print(part1(grid, start_point))
print(part2(grid, start_point))