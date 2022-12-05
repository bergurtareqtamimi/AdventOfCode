
file1 = open('input.txt', 'r')

crates = [[],[],[],[],[],[],[],[],[]]

index_mapper = {0:1, 1:5, 2:9, 3:13, 4:17, 5:21, 6:25, 7:29, 8:33}

lines = file1.readlines()

def move(quant, fro, to):
    for _ in range(quant):
        crates[to].append(crates[fro].pop())

for number, line in enumerate(lines):
    if number < 8:
        for key in index_mapper:
            if line[index_mapper[key]] != " ":
                crates[key].append(line[index_mapper[key]])
    if number == 8:
        for i, column in enumerate(crates):
            crates[i].reverse()
    if number >= 10:
        _, quant, _, fro, _, to = line.split()
        quant = int(quant)
        fro = int(fro) - 1
        to = int(to) - 1
        move(quant, fro, to)



answer = ""
for i in crates:
    answer += i[-1]

print("Solution 1: ", answer)


crates = [[],[],[],[],[],[],[],[],[]]
def move(quant, fro, to):
    temp = []
    for _ in range(quant):
        temp.append(crates[fro].pop())
    for _ in range(quant):
        crates[to].append(temp.pop())

for number, line in enumerate(lines):
    if number < 8:
        for key in index_mapper:
            if line[index_mapper[key]] != " ":
                crates[key].append(line[index_mapper[key]])
    if number == 8:
        for i, column in enumerate(crates):
            crates[i].reverse()
    if number >= 10:
        _, quant, _, fro, _, to = line.split()
        quant = int(quant)
        fro = int(fro) - 1
        to = int(to) - 1
        move(quant, fro, to)

answer = ""
for i in crates:
    answer += i[-1]
print("Solution 2: ", answer)




