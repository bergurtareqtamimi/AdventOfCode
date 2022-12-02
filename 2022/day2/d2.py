file1 = open('input.txt', 'r')

lines = file1.readlines()

my_mapper = {'X': 1, 'Y': 2, 'Z': 3}

def result_points(opp:str , me:str) -> int:
    if opp == 'A':
        if me == 'X':return 3
        if me == 'Y':return 6
        if me == 'Z':return 0
    if opp == 'B':
        if me == 'X':return 0
        if me == 'Y':return 3
        if me == 'Z':return 6
    if opp == 'C':
        if me == 'X':return 6
        if me == 'Y':return 0
        if me == 'Z':return 3

my_score = 0

for line in lines:
    line = line.strip().split()
    my_score += result_points(line[0], line[1]) + my_mapper[line[1]]

print("Solution 1: ", my_score)

#########################################
my_mapper = {'X': 0, 'Y': 3, 'Z': 6}


def result_points(opp:str , me:str) -> int:
    if opp == 'A': # rock
        if me == 'X':return 3
        if me == 'Y':return 1
        if me == 'Z':return 2
    if opp == 'B': # paper
        if me == 'X':return 1
        if me == 'Y':return 2
        if me == 'Z':return 3
    if opp == 'C': # scissor
        if me == 'X':return 2
        if me == 'Y':return 3
        if me == 'Z':return 1



my_score = 0

for line in lines:
    line = line.strip().split()
    my_score += result_points(line[0], line[1]) + my_mapper[line[1]]

print("Solution 2: ", my_score)










