file1 = open('input.txt', 'r')

lines = file1.readlines()

def priority(char: str) -> int:
    if char.isupper():
        return ord(char) - 38
    if char.islower():
        return ord(char) - 96
    print("Something is wrong with: ", char)

total_priority = 0

for line in lines:
    line = line.strip()
    part_a = line[:len(line)//2]
    part_b = line[len(line)//2:]
    
    #compairing two strings
    already_common = set()
    for char_a in part_a:
        for char_b in part_b:
            if char_a == char_b and char_a not in already_common:
                total_priority += priority(char_a)
                already_common.add(char_a)

print("Solution 1: ",total_priority)

total_priority = 0
s1 = ""
s2 = ""
s3 = ""

count = 0

for index, line in enumerate(lines):
    count += 1
    line = line.strip()

    if index % 3 == 0:
        s1 = line

    if index % 3 == 1:
        s2 = line
    
    if index % 3 == 2:
        s3 = line

        already_common = set()
        for a in s1:
            for b in s2:
                if b == a:
                    for c in s3:
                        if b == c and b not in already_common:
                            total_priority += priority(c)
                            already_common.add(b)

print("Solution 2: ",total_priority)


