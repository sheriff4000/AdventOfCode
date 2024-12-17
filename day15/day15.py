

def move(grid, position, direction):
    match direction:
        case '^':
            delta = (-1, 0)
        case 'v':
            delta = (1, 0)
        case '<':
            delta = (0, -1)
        case '>':
            delta =  (0, 1)

    curr = (position[0] + delta[0], position[1] + delta[1])
    block_size = 0
    while grid[curr[0]][curr[1]] == 'O':
        x, y = curr
        block_size += 1
        curr = (x + delta[0], y + delta[1]) 

    if grid[curr[0]][curr[1]] == '#':
        return grid, position
    else:
        new_grid = grid
        new_grid[position[0]][position[1]] = '.'
        new_position = (position[0] + delta[0], position[1] + delta[1])
        new_grid[new_position[0]][new_position[1]] = '@'
        box_position = (new_position[0] + delta[0], new_position[1] + delta[1])
        for _ in range(block_size):
            x, y = box_position
            new_grid[x][y] = 'O'
            box_position = (x + delta[0], y + delta[1])
        return new_grid, new_position
    
def scaled_move(grid, position, direction):
    match direction:
        case '^':
            delta = (-1, 0)
        case 'v':
            delta = (1, 0)
        case '<':
            delta = (0, -1)
        case '>':
            delta =  (0, 1)    

    curr = (position[0] + delta[0], position[1] + delta[1])
    if grid[curr[0]][curr[1]] == '#':
        return grid, position
    if direction in ['<', '>']:
        block_size = 0
        while grid[curr[0]][curr[1]] in ['[', ']']:
            x, y = curr
            block_size += 1
            curr = (x + delta[0], y + delta[1]) 

        if grid[curr[0]][curr[1]] == '#':
            return grid, position
        else:
            new_grid = grid
            new_grid[position[0]][position[1]] = '.'
            new_position = (position[0] + delta[0], position[1] + delta[1])
            new_grid[new_position[0]][new_position[1]] = '@'
            box_position = (new_position[0] + delta[0], new_position[1] + delta[1])
            edge = '[' if direction == '>' else ']'
            for _ in range(block_size):
                x, y = box_position
                new_grid[x][y] = edge
                edge = '[' if edge == ']' else ']'
                box_position = (x + delta[0], y + delta[1])
            return new_grid, new_position
    else:
        positions_to_move = [position]
        stack = [curr]
        visited = set()
        while stack:
            x, y = stack.pop(0)
            if not (0 < x < len(grid) - 1) or not (1 < y < len(grid[0]) - 2) or (x, y) in visited:
                continue
            visited.add((x, y))
            if grid[x][y] == '[':
                positions_to_move.append((x, y))
                stack.append((x, y + 1))
            elif grid[x][y] == ']':
                positions_to_move.append((x, y))
                stack.append((x, y - 1))
            else:
                continue
            next_position = (x + delta[0], y + delta[1])
            if 0 < next_position[0] < len(grid)-1 and 1 < next_position[1] < len(grid[0])-2:
                if grid[next_position[0]][next_position[1]] == '#':
                    return grid, position
                elif grid[next_position[0]][next_position[1]] == '[':
                    stack.append(next_position)
                    stack.append((next_position[0], next_position[1] + 1))
                elif grid[next_position[0]][next_position[1]] == ']':
                    stack.append(next_position)
                    stack.append((next_position[0], next_position[1] - 1))
            else:
                return grid, position

        robot_position = positions_to_move.pop(0)
        new_robot_position = (robot_position[0] + delta[0], robot_position[1] + delta[1])
        new_grid = grid
        if direction == '^':
            sorted_positions = sorted(positions_to_move, key=lambda x: x[0])
        elif direction == 'v':
            sorted_positions = sorted(positions_to_move, key=lambda x: x[0], reverse=True)

        sorted_positions.append(robot_position)
        for i, j in sorted_positions:
            new_grid[i + delta[0]][j + delta[1]] = new_grid[i][j]
            new_grid[i][j] = '.'
        
        return new_grid, new_robot_position



def scale_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for char in row:
            if char == 'O':
                new_row.append('[')
                new_row.append(']')
            elif char != '@':
                new_row.append(char)
                new_row.append(char)
            else:
                new_row.append(char)
                new_row.append('.')
        new_grid.append(new_row)
    return new_grid

def part1(grid, position, moves):
    new_grid = grid
    for direction in moves:
        new_grid, position = move(new_grid, position, direction)
    total = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == 'O':
                total += 100*i + j
    return total

def part2(grid, position, moves):
    new_grid = grid
    new_position = position
    for direction in moves:
        new_grid, new_position = scaled_move(new_grid, new_position, direction)
    total = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == '[':
                total += 100*i + j
    return total

with open("day15/real.txt") as f:
    input_grid = [list(line.strip()) for line in f]
    empty_line = input_grid.index([])
    original_grid = input_grid[:empty_line]
    moves = input_grid[empty_line + 1:]
    moves = "".join([item for sublist in moves for item in sublist])

for i in range(len(original_grid)):
    for j in range(len(original_grid[i])):
        if original_grid[i][j] == '@':
            position = (i, j)
            break

grid = original_grid
scaled_grid = scale_grid(original_grid)

p1 = part1(grid, position, moves)
print(p1)

for i in range(len(scaled_grid)):
    for j in range(len(scaled_grid[i])):
        if scaled_grid[i][j] == '@':
            scaled_position = (i, j)
            break

for row in original_grid:
    print("".join(row))

for row in scaled_grid:
    print("".join(row))

p2 = part2(scaled_grid, scaled_position, moves)
print(p2)
