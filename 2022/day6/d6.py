
file1 = open('input.txt', 'r')



def process(line:str) -> int:
    a0 = set()
    a1 = set()
    a2 = set()
    a3 = set()

    for i in range(len(line)):
        if i <= 3:
            if i % 4 == 0:
                a0.add(line[i])
            if i % 4 == 1:
                a1.add(line[i])
            if i % 4 == 2:
                a2.add(line[i])
            if i % 4 == 3:
                a3.add(line[i])
        else:
            if i % 4 == 0:
                a0.clear()
                a0.add(line[i])
            if i % 4 == 1:
                a1.clear()
                a1.add(line[i])
            if i % 4 == 2:
                a2.clear()
                a2.add(line[i])
            if i % 4 == 3:
                a3.clear()
                a3.add(line[i])

        if len(a0.union(a1.union(a2.union(a3)))) == 4: return i + 1

text = file1.readlines()[0]

print("Solutions 1: ", process(text))

def process(line:str) -> int:
    a0 = set()
    a1 = set()
    a2 = set()
    a3 = set()
    a4 = set()
    a5 = set()
    a6 = set()
    a7 = set()
    a8 = set()
    a9 = set()
    a10 = set()
    a11 = set()
    a12 = set()
    a13 = set()

    for i in range(len(line)):
        if i <= 13:
            if i % 14 == 0:
                a0.add(line[i])
            if i % 14 == 1:
                a1.add(line[i])
            if i % 14 == 2:
                a2.add(line[i])
            if i % 14 == 3:
                a3.add(line[i])
            if i % 14 == 4:
                a4.add(line[i])
            if i % 14 == 5:
                a5.add(line[i])
            if i % 14 == 6:
                a6.add(line[i])
            if i % 14 == 7:
                a7.add(line[i])
            if i % 14 == 8:
                a8.add(line[i])
            if i % 14 == 9:
                a9.add(line[i])
            if i % 14 == 10:
                a10.add(line[i])
            if i % 14 == 11:
                a11.add(line[i])
            if i % 14 == 12:
                a12.add(line[i])
            if i % 14 == 13:
                a13.add(line[i])
        else:
            if i % 14 == 0:
                a0.clear()
                a0.add(line[i])
            if i % 14 == 1:
                a1.clear()
                a1.add(line[i])
            if i % 14 == 2:
                a2.clear()
                a2.add(line[i])
            if i % 14 == 3:
                a3.clear()
                a3.add(line[i])
            if i % 14 == 4:
                a4.clear()
                a4.add(line[i])
            if i % 14 == 5:
                a5.clear()
                a5.add(line[i])
            if i % 14 == 6:
                a6.clear()
                a6.add(line[i])
            if i % 14 == 7:
                a7.clear()
                a7.add(line[i])
            if i % 14 == 8:
                a8.clear()
                a8.add(line[i])
            if i % 14 == 9:
                a9.clear()
                a9.add(line[i])
            if i % 14 == 10:
                a10.clear()
                a10.add(line[i])
            if i % 14 == 11:
                a11.clear()
                a11.add(line[i])
            if i % 14 == 12:
                a12.clear()
                a12.add(line[i])
            if i % 14 == 13:
                a13.clear()
                a13.add(line[i])

        if len(a0.union(a1.union(a2.union(a3.union(a4.union(a5.union(a6.union(a7.union(a8.union(a9.union(a10.union(a11.union(a12.union(a13)))))))))))))) == 14: return i + 1



print("Solutions 2: ", process(text))