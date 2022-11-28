
def read_input():
    coll = []
    with open("inp2.txt") as file:
        line = file.readline()
        while line:
            left = sorted(["".join(sorted(x)) for x in line.strip().split("|")[0].split()])
            right = ["".join(sorted(x)) for x in line.strip().split("|")[1].split()]
            coll.append([left, right])
            line = file.readline()
    return coll


def segment_to_possible_numbers(segment):
    if len(segment) == 2:
        return 1
    if len(segment) == 4:
        return 4
    if len(segment) == 3:
        return 7
    if len(segment) == 7:
        return 8
    if len(segment) == 5:
        return 2, 3, 5
    if len(segment) == 6:
        return 6, 9, 0


def number_to_segments(number):
    if number == 0:
        return "a","b","c","e","f","g"
    if number == 1:
        return "c", "f"
    if number == 2:
        return "a", "c", "d", "e", "g"
    if number == 3:
        return "a", "c", "d", "f", "g"
    if number == 4:
        return "b", "c", "d", "f"
    if number == 5:
        return "a", "b","d", "f","g"
    if number == 6:
        return "a", "b", "d", "f", "g", "e"
    if number == 7:
        return "a", "c", "f"
    if number == 8:
        return "a", "b","c", "d", "f", "g", "e"
    if number == 9:
        return "a", "b","c", "d", "f", "g"

def get_mapper():
    d = dict()
    for i in ["a", "b", "c","d","e","f","g"]:
        d[i] = []
    return d

data = read_input()
print(data)
counter = 0
for case in data:
    mapper = get_mapper()
    for number in case[0]:
        p_number = segment_to_possible_numbers(number)

        if p_number in [1,4,7,8]:
            counter += 1

print(counter)


# take in each segment (before pipe) and convert them into possible numbers
# convert each possible number into possible segments
# the goal is to map each broken segment to its real segment









