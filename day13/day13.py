import re

def solve_linear_system(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p

    n1 = (px*by - py*bx) / (ax*by - ay*bx)
    n2 = (py*ax - px*ay) / (ax*by - ay*bx)

    return n1, n2

def min_cost(A, B, prize):
    
    na, nb = solve_linear_system(A, B, prize)
    if na >= 0 and nb >= 0 and na % 1 == 0 and nb % 1 == 0:
        return na*3 + nb
    else:
        return 0


print(min_cost((94,34), (22,67), (8400,5400))) #



def part1(machines):
    tokens = 0
    for machine in machines:
        tokens += min_cost(machine[0], machine[1], machine[2])
    return tokens

def part2(machines):
    tokens = 0
    for machine in machines:
        tokens += min_cost(machine[0], machine[1], (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000))
    return tokens

with open('day13/real.txt') as f:
    lines = f.read().split("\n\n")
machines = []
for machine_def in lines:
    m = list(map(int, (re.findall(r"\d+", machine_def))))
    machines.append(((m[0], m[1]), (m[2], m[3]), (m[4], m[5])))
    

    
print(part1(machines)) # 0
print(part2(machines)) # 0