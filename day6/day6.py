
with open('real_input6.txt') as f:
    grid = f.read().splitlines()


def find_guard():
    for idx, line in enumerate(grid):
        if '^' in line:
            return (idx, line.index('^'))
        
start_pos = find_guard()
def find_path(start, lines=grid, new_obs=None):
    stack = [(start, "up")]
    visited = set()
    visited_directions = set()
    while stack:
        curr, curr_dir = stack.pop()
        # print(curr, curr_dir)
        if new_obs is not None and (curr[0], curr[1], curr_dir) in visited_directions:
            return True

        x, y = curr

        if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[0]):
            continue

        if lines[x][y] == '#' or (x, y) == new_obs:
            if curr_dir == "up":
                new_dir = "right"
                next_pos = (x+1, y+1)
            elif curr_dir == "right":
                new_dir = "down"
                next_pos = (x+1, y-1)
            elif curr_dir == "down":
                new_dir = "left"
                next_pos = (x-1, y-1)
            elif curr_dir == "left":
                new_dir = "up"
                next_pos = (x-1, y+1)
            # print("facing: ", curr_dir, "new_dir: ", new_dir)
        else:
            if curr_dir == "up":
                next_pos = (x-1, y)
            elif curr_dir == "right":
                next_pos = (x, y+1)
            elif curr_dir == "down":
                next_pos = (x+1, y)
            elif curr_dir == "left":    
                next_pos = (x, y-1)

            new_dir = curr_dir
            visited.add((x, y))
            visited_directions.add((x, y, curr_dir))

        if next_pos is not None:
            stack.append((next_pos, new_dir))

    if new_obs is not None:
        return False
    return visited

def part1():
    points = find_path(start_pos)
    return len(points)

def part2():
    # _, directions, is_loop  = find_path_iterative(start_pos)
    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                print("looking at point: ", i, j)
                is_loop = find_path(start_pos, new_obs=(i,j))
                res += 1 if is_loop else 0
    return res

# print(part1())
print(part2())