file1 = open('input.txt', 'r')

lines = file1.readlines()

def process_sections(line:str) -> tuple[int]:
    a, b = line.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    return int(a1), int(a2), int(b1), int(b2)

count = 0

for line in lines:
    line = line.strip()
    a1, a2, b1, b2 = process_sections(line)
    
    if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
        count += 1

print("Solution 1: ",count)

count = 0
for line in lines:
    line = line.strip()
    a1, a2, b1, b2 = process_sections(line)

    if (a1 <= b2 and a1 >= b1) or (b1 <= a2 and b1 >= a1):
        count += 1

print("Solution 2: ",count)