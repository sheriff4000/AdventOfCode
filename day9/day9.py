
with open ('day9/real.txt') as f:
    data = f.read().replace("\n", "")

def build_disk(input_data):
    disk = []
    index = 0
    for i in range(len(input_data)):
        if i %2 == 0:
            disk.extend([index] * int(input_data[i]))
            index += 1
        else:
            disk.extend(["."] * int(input_data[i]))
    
    return disk, index-1

def reorder_disk(disk):
    out = []
    idx = -1
    dots = disk.count(".")
    disk_size = len(disk)
    for i in range(len(disk)):
        if disk[i] == '.':
            val = disk[idx]
            while val == '.' and idx > -disk_size:
                idx -= 1
                val = disk[idx]
            out.append(val)
            disk[idx] = '.'
        else:
            out.append(disk[i])
    return out[:-dots]

def reorder_disk_whole(disk, max_index):
    # print(disk)
    out = []
    blocks = []
    current_block = []
    for i in range(len(disk)):
        if i == 0 or disk[i] == disk[i-1]:
            current_block.append(disk[i])
        else:
            blocks.append(current_block)
            current_block = [disk[i]]
    blocks.append(current_block)  # Append the last block
    # print(blocks)
    def place_block(block_list, block_to_place):
        idx = block_list.index(block_to_place)
        for i in range(idx):
            if len(block_list[i]) > 0 and block_list[i][0] == '.' and len(block_list[i]) >= len(block_to_place):
                block_list.insert(i, block_to_place)
                block_list[i+1] = block_list[i+1][len(block_to_place):]
                if i+2 < len(block_list) and len(block_list[i+2]) > 0 and block_list[i+2][0] == '.':
                    block_list[i+1] = block_list[i+1] + block_list[i+2]
                    block_list.pop(i+2)

                block_list[idx+1] = ['.'] * len(block_to_place)
                if idx+2 < len(block_list) and len(block_list[idx+2]) > 0 and block_list[idx+2][0] == '.':
                    block_list[idx+1] = block_list[idx+1] + block_list[idx+2]
                    block_list.pop(idx+2)
                return block_list
        return block_list
    
    # print(place_block(blocks, blocks[-2]))

    for i in range(max_index, 1, -1):
        # print(i)
        for block in reversed(blocks):
            if len(block) > 0 and block[0] == i:
                blocks = place_block(blocks, block)
                break
        # print(blocks)
        

    return [val for block in blocks for val in block]


def part1(data):
    disk, _ = build_disk(data)
    total = 0
    for i, val in enumerate(reorder_disk(disk)):
        total += i * val

    return total

def part2(data):
    disk, max_idx = build_disk(data)
    total = 0
    for i, val in  enumerate(reorder_disk_whole(disk, max_idx)):
        if val == '.':
            continue
        total += i * val
    return total
# print(build_disk(data)) 

# print(part1(data))
# disk, max_idx = build_disk(data)
# print(reorder_disk_whole(disk, max_idx))
print(part1(data))
print(part2(data))