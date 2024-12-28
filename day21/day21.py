

class Node:
    def __init__(self, value, children={}):
        self.value = value
        self.children = children
        
    def add_child(self, child, direction):
        self.children[direction] = child

class Keypad:
    def __init__(self, keypad, type='numeric'):
        self.paths = {}
        self.nodes = {}
        self.type = type
        directions = [(-1, 0, '^'), (1, 0, 'v'), (0, -1, '<'), (0, 1, '>')]

        for i, row in enumerate(keypad):
            for j, value in enumerate(row):
                if value is not None:
                    node = self.nodes.setdefault(value, Node(value, {}))
                    for di, dj, direction in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(keypad) and 0 <= nj < len(row) and keypad[ni][nj] is not None:
                            child_value = keypad[ni][nj]
                            child = self.nodes.setdefault(child_value, Node(child_value, {}))
                            node.add_child(child, direction)  
                            
    def find_path(self, start_val, end_val, start_direction=None):
        if start_val == end_val:
            return [], start_direction

        if (start_val, end_val, start_direction) in self.paths:
            return self.paths[(start_val, end_val, start_direction)], start_direction

        queue = [(start_val, [], start_direction)]
        visited = set()

        while queue:
            current_val, path, curr_dir = queue.pop(0)
            if current_val in visited:
                continue

            visited.add(current_val)
            current_node = self.nodes[current_val]
            
            if self.type == 'numeric':
                check = '^'
            else:
                check = 'v'
            
            for direction, child in sorted(current_node.children.items(), key=lambda x: (x[0]==curr_dir), reverse=True):
                if child.value == end_val:
                    self.paths[(start_val, end_val, direction)] = path + [direction]
                    return path + [direction], direction
                if child.value not in visited:
                    queue.append((child.value, path + [direction], direction))
        return None

    def enter_code(self, code, start='A'):
        curr_pos = start
        direction = None
        path = []
        for val in code:
            next_path, direction = self.find_path(curr_pos, val, direction)
            path.extend(next_path)
            path.extend('A')
            curr_pos = val
            # print("".join(path))
        return "".join(path)

numeric_keypad = [
    ['7','8' ,'9'],
    ['4','5','6'],
    ['1','2','3'],
    [None, '0', 'A']
]

directional_keypad= [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

main_keypad = Keypad(numeric_keypad, type='numeric')
sub_keypad1 = Keypad(directional_keypad, type='directional')
sub_keypad2 = Keypad(directional_keypad, type='directional')

def part1(codes):
    total = 0
    for code in codes:
        main_code = main_keypad.enter_code(code)
        sub_code1 = sub_keypad1.enter_code(main_code)
        sub_code2 = sub_keypad2.enter_code(sub_code1)
        print(len(sub_code2), int(code[:-1]))
        total += (len(sub_code2)) * int(code[:-1])
    return total

with open('day21/test.txt') as f:
    codes = f.read().splitlines()
print(part1(codes[-1:]))
