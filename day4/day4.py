with open("real_input4.txt") as f:
    lines = lines = f.read().splitlines()
    

def check_horizontal(input):
    count = 0
    for row in input:
        count += row.count('XMAS')
        count += row.count('SAMX')
    return count

def check_vertical(input):
    count = 0
    for col in range(len(input[0])):
        column = ''.join(row[col] for row in input)
        count += column.count('XMAS')
        count += column.count('SAMX')
    return count
    
def check_diagonal(input):
    count = 0
    for start in range(len(input)):
        # idx = start
        diag_str = ''.join(input[start+idx][idx] for idx in range(0, min(len(input)-start, len(input[0]))))
        count += diag_str.count('XMAS')
        count += diag_str.count('SAMX')
        # print(diag_str)
        # idx += 1
    for start in range(1,len(input[0])):
        diag_str = ''.join(input[idx][start+idx] for idx in range(0, min(len(input[0])-start, len(input))))
        count += diag_str.count('XMAS')
        count += diag_str.count('SAMX')
        # print(diag_str)
        
    for start in range(len(input)):
        diag_str = ''.join(input[start+idx][-(idx+1)] for idx in range(0, min(len(input)-start, len(input[0]))))
        count += diag_str.count('XMAS')
        count += diag_str.count('SAMX')
        
    for start in range(1, len(input[0])):
        diag_str = ''.join(input[idx][-(start+idx+1)] for idx in range(0, min(len(input[0])-start, len(input))))
        count += diag_str.count('XMAS')
        count += diag_str.count('SAMX')
        
    return count

def check_x_str(input):
    str1 = ''.join([input[x][x] for x in range(len(input))])
    str2 = ''.join([input[-(x+1)][x] for x in range(len(input))])

    options = {'SAM', 'MAS'}
    if (str1 in options) and (str2 in options):
        return True
    return False
    

def part1():
    return check_horizontal(lines) + check_vertical(lines) + check_diagonal(lines)
        
def part2():
    count = 0
    for i in range(len(lines) - 2):
        for j in range(len(lines[0]) - 2):
            submatrix = [lines[i+k][j:j+3] for k in range(3)]
            if check_x_str(submatrix):
                count += 1

    return count

print(part1())
print(part2())
