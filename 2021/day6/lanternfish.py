def breed(state):
    baby_count = 0

    for i, e in enumerate(state):
        if e == 0:
            baby_count += 1
            state[i] = 6
        else:
            state[i] -= 1
        
    for _ in range(baby_count):
        state.append(8)
    
    return state

def read_input():
    file1 = open('inp.txt', 'r')
    coll = []
    while True:
        # Get next line from file
        line = file1.readline()

        if not line:
            break

        line = line.strip().split(",")
        coll.extend(line)

    file1.close()
    
    for i, e in enumerate(coll):
        coll[i] = int(e)
    
    return coll

# solution 1
# state = read_input()
# days = 256

# for i in range(days + 1):
#     print(f"After {i} days size: {len(state)}")
#     state = breed(state)


def update_dict(di):
    new_dict = {}
    for i in range(9):
        new_dict[i] = 0
    for day, count in di.items():
        if day == 0:
            new_dict[6] += count
            new_dict[8] += count
        else:
            new_dict[day-1] += count
    
    return new_dict

# solution 2
state = read_input()
days = 256
state_dict = dict()

for i in range(9):
    state_dict[i] = 0

for i in state:
    state_dict[i] += 1

for i in range(days + 1):
    print(f"After {i} days size: {sum(state_dict.values())}")
    state_dict = update_dict(state_dict)



