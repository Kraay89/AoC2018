###############################################################################
#                           ADVENT OF CODE 2018                               #
#                                  DAY 1                                      #
###############################################################################
import itertools

########
# INIT #
########

FP = "Day1/Day1_input.txt"
instructions = []
with open(FP, 'r') as inputFile:
    for instruction in inputFile.readlines():
        instructions.append(int(instruction))


##########
# Part 1 #
##########

f_start = 0
f_result = f_start

for instruction in instructions:
    f_result += int(instruction)

print(f_result)

##########
# Part 2 #
##########
frequencies = set([0])

f_result = f_start
for instruction in itertools.cycle(instructions):
    f_result += instruction
    if f_result in frequencies:
        print(
            f"The frequency {f_result} is the first frequency to apear twice.")
        break
    else:
        frequencies.add(f_result)
