###############################################################################
#                           ADVENT OF CODE 2018                               #
#                                  DAY 2                                      #
###############################################################################
from collections import Counter
########
# INIT #
########

FP = "Day2/Day2_input.txt"
candidates = []
with open(FP, 'r') as inputFile:
    # Start with initializing the data
    for item in inputFile.readlines():
        candidates.append(item.strip())


# #########
# Part 1 #
# #########

doubles = 0
triples = 0
for candidate in candidates:
    letter_counts = dict(Counter(candidate))
    if 2 in letter_counts.values():
        doubles += 1
    if 3 in letter_counts.values():
        triples += 1

print(f"Found {doubles} ID's that countained double characters, and {triples} ID's that had triple characters.")

checksum = doubles*triples
print(f"The checksum is {doubles} * {triples} = {checksum}.")

# #########
# Part 2  #
# #########

for index, candidate_1 in enumerate(candidates):
    for candidate_2 in candidates[index+1::]:
        try:
            matches = [i for i in range(len(candidate_1))
                       if candidate_1[i] != candidate_2[i]]
        except IndexError as e:
            ""

        if len(matches) == 1:
            sharedCharacters = candidate_1[:matches[0]
                                           ]+candidate_1[matches[0]+1:]
            print(
                f"Candidates:\n{candidate_1} and \n{candidate_2} \n{sharedCharacters} are the shared characters. they differ on {matches[0]}")
