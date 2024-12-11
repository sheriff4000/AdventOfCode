with open("day9/real.txt") as f:
    data = f.read().replace("\n", "")

def part1(data):
    # build disk
    disk = []
    for idx, num in enumerate(data):
        index = idx // 2
        if idx % 2 == 0:
            disk.extend([index] * int(num))
        else:
            disk.extend([None] * int(num))

    # reorder disk
    
    left_ptr = 0
    while left_ptr < len(disk):
        while left_ptr < len(disk) and disk[left_ptr] is not None:
            left_ptr += 1
        if left_ptr >= len(disk):
            break
        while disk[-1] is None:
            disk.pop()
        disk[left_ptr] = disk.pop()
        
    # calculate score

    return sum(i * x for i, x in enumerate(disk))

# PART 2

class DLL:
    def __init__(self, value, size=0, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt
        self.size = size

    def insert_before(self, node):
        assert node is not self and node is not None
        node.prev = self.prev
        node.next = self
        self.prev = node
        if node.prev is not None:
            node.prev.next = node

    def replace(self, node):
        assert node is not self and node is not None
        node.prev = self.prev
        node.next = self.next
        self.prev = None
        self.next = None
        if node.prev is not None:
            node.prev.next = node
        if node.next is not None:
            node.next.prev = node

def print_dll(head):
    node = head
    while node is not None:
        print(node.value, node.size)
        node = node.next

def part2(data):
    # build disk
    head = tail = None
    data_blocks = []
    for idx, num in enumerate(data):
        if num == 0:
            continue
        index = idx // 2
        if idx % 2 == 0:
            new_node = DLL(index, int(num))
            data_blocks.append(new_node)
        else:
            new_node = DLL(None, int(num))

        if head is None:
            head = tail = new_node
        else:
            tail.next = new_node
            new_node.prev = tail
            tail = new_node

    # reorder disk
    for data_node in reversed(data_blocks):
        curr = head
        while curr.value is not None or curr.size < data_node.size:
            if curr is data_node:
                break
            curr = curr.next
        else:
            new_node = DLL(None, data_node.size)
            data_node.replace(new_node)
            curr.size -= data_node.size
            if curr.size == 0:
                curr.replace(data_node)
            else:
                curr.insert_before(data_node)
    
    curr = head
    total = index = 0
    while curr is not None:
        for _ in range(curr.size):
            if curr.value is not None:
                total += index * curr.value
            index += 1
        curr = curr.next
    return total

print(part1(data))
print(part2(data))