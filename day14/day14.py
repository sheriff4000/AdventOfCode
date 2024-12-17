from collections import defaultdict
import re
from operator import mul
from functools import reduce

def end_point(position, velocity, seconds, max_x, max_y):
    x, y = position
    x_v, y_v = velocity
    return ((x + x_v * seconds) % max_x, (y + y_v * seconds) % max_y)

def robot_count(robots, seconds, max_x, max_y):
    quad_counts = defaultdict(int)
    pos_counts = defaultdict(int)
    for robot in robots:
        x, y = end_point(robot[0], robot[1], seconds, max_x, max_y)
        if 0 <= x < max_x and 0 <= y < max_y:
            if x < (max_x // 2) and y < (max_y // 2):
                quad_counts[(0, 0)] += 1
            elif x > (max_x // 2) and y < (max_y // 2):
                quad_counts[(1, 0)] += 1
            elif x < (max_x // 2) and y > (max_y // 2):
                quad_counts[(0, 1)] += 1
            elif x > (max_x // 2) and y > (max_y // 2):
                quad_counts[(1, 1)] += 1
            pos_counts[(x, y)] += 1
    return quad_counts, pos_counts

def part1(robots, seconds=0):
    max_x = 101
    max_y = 103

    counts, _ = robot_count(robots, seconds, max_x, max_y)
    print(counts)
    return reduce(mul, counts.values())

def part2(robots):
    seconds = 0
    _, pos_counts = robot_count(robots, seconds, 101, 103)
    while not all(val == 1 for val in pos_counts.values()):
        seconds += 1
        _, pos_counts = robot_count(robots, seconds, 101, 103)

    return seconds


with open('day14/real.txt') as f:
    data = f.read().splitlines()
robots = []
for line in data:
    pos, vel = tuple(re.findall(r'(-?\d+),(-?\d+)', line))
    pos = tuple(map(int, pos))
    vel = tuple(map(int, vel))
    robots.append((pos, vel))

print(part1(robots, 100))
print(part2(robots))