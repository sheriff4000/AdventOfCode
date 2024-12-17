from collections import defaultdict 

with open('day11/real.txt') as f:
    data = f.read().split(" ")

data = [int(x) for x in data]

stones = defaultdict(int)
for stone in data:
    stones[stone] += 1

def step(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        half = len(str_stone) // 2
        return [int(str_stone[:half]), int(str_stone[half:])]
    else:
        return [stone * 2024]
    
def fast_step(stones):
    new_stones = defaultdict(int)
    for s in stones:
        for new_stone in step(s):
            new_stones[new_stone] += stones[s]
    return new_stones
    

def blink_once(data):
    global results
    new_data = []
    for num in data:
        if num in results:
            if type(results[num]) == list:
                new_data.extend(results[num])
            else:
                new_data.append(results[num])
            continue
        str_num = str(num)
        if num == 0:
            new_data.append(1)
            results[num] = new_data[-1]
        elif len(str_num) % 2 == 0:
            half = len(str_num) // 2
            new_data.append(int(str_num[:half]))
            new_data.append(int(str_num[half:]))
            results[num] = new_data[-2:]
        else:
            new_data.append(num * 2024)
            results[num] = new_data[-1]

    return new_data

def part1(data):
    for _ in range(25):
        data = blink_once(data)

    return len(data)

def part2(stones):
    for _ in range(75):
        stones = fast_step(stones)

    total = 0
    for s in stones:
        total += stones[s]
    return total

# print(data)
# print(blink_once(data))
if __name__ == '__main__':
    results = {}
    print(part1(data))
    print(part2(stones))