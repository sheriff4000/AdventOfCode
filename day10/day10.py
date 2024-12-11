with open('day10/real.txt') as f:
    data = f.read().splitlines()

grid = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[i])):
        grid[i][j] = int(data[i][j])

def get_zeros(grid):
    zeros = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                zeros.append((i, j))
    return zeros

def get_score(grid, start_point, is_rating=False):
    score = 0
    stack = [start_point]
    visited = set()
    while stack:
        x, y = stack.pop()
        if grid[x][y] == 9 and (x, y) not in visited:
            if not is_rating:
                visited.add((x, y))
            score += 1
            continue
        new_points = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for new_x, new_y in new_points:
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == grid[x][y]+1:
                stack.append((new_x, new_y))
    return score

def part1(grid):
    zeros = get_zeros(grid)
    total_score = 0
    for zero in zeros:
        total_score += get_score(grid, zero)

    return total_score

def part2(grid):
    zeros = get_zeros(grid)
    total_score = 0
    for zero in zeros:
        total_score += get_score(grid, zero, is_rating=True)

    return total_score

# print(get_zeros(grid))
# print(grid)
# print(get_rating(grid, (0, 2)))
print(part1(grid))
print(part2(grid))