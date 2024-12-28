from math import trunc
from collections import deque

def execute_command(instr_idx, command, operand, curr_output, registers):
    match operand:
        case 4:
            combo_op = registers[0]
        case 5:
            combo_op = registers[1]
        case 6:
            combo_op = registers[2]
        case 7:
            combo_op = None
        case _:
            combo_op = operand
    match command:
        case 0:
            registers[0] = trunc(registers[0] / (2 ** combo_op))
            return instr_idx+2, curr_output, registers
        case 1:
            registers[1] = registers[1] ^ operand
            return instr_idx+2, curr_output, registers
        case 2:
            registers[1] = combo_op % 8
            return instr_idx+2, curr_output, registers
        case 3:
            if registers[0] == 0:
                return instr_idx+2, curr_output, registers
            else:
                return operand, curr_output, registers
        case 4:
            registers[1] = registers[1] ^ registers[2]
            return instr_idx+2, curr_output, registers
        case 5:
            out = combo_op % 8 
            curr_output.append(out)
            return instr_idx+2, curr_output, registers
        case 6:
            registers[1] = trunc(registers[0] / (2 ** combo_op))
            return instr_idx+2, curr_output, registers
        case 7:
            registers[2] = trunc(registers[0] / (2 ** combo_op))
            return instr_idx+2, curr_output, registers         
        

def run_program(program, registers):
    instr_idx = 0
    curr_output = []
    curr_reg = registers
    while 0 <= instr_idx < len(program):
        instr = program[instr_idx]
        if instr_idx+1 < len(program):
            instr_idx, curr_output, curr_reg = execute_command(instr_idx, instr, program[instr_idx+1], curr_output, curr_reg)
        else:
            print(instr_idx, instr, curr_output, curr_reg)
            instr_idx, curr_output, curr_reg = execute_command(instr_idx, instr, None, curr_output, curr_reg)
    return curr_output

def find_quine_iterative_backtrack(prog):
    queue = deque()
    queue.append((0, 1))

    while queue:
        a, n = queue.popleft()
        if n > len(prog):  # Base
            return a

        for i in range(8):
            a2 = (a << 3) | i
            out = run_program(prog, [a2, 0, 0])
            target = prog[-n:]

            # save correct partial solutions
            if out == target:
                queue.append((a2, n + 1))
    return False

with open('day17/real.txt') as f:
    lines = f.read().split("\n\n")
    reg_def = lines[0].split("\n")
    registers = [int(reg.split(": ")[1]) for reg in reg_def]
    program = list(map(int, lines[1].split(": ")[1].split(",")))
    
# print(registers, program)

test_program = [2, 6]
test_registers = [0, 0, 9]
output = run_program(program, registers)
print(",".join(list(map(str,output))))

print(find_quine_iterative_backtrack(program))

