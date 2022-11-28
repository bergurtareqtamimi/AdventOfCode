file1 = open('inp.txt', 'r')
count = 0
 
x = 0
aim = 0
y = 0
while True:
    count += 1

    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break

    line = line.strip()
    line = line.split()
    for i, e in enumerate(line):
        if i == 1:
            line = [line[i-1], int(e)]
    
    if line[0] == 'up':
        aim -= line[1]
    elif line[0] == 'down':
        aim += line[1]
    elif line[0] == 'forward':
        x += line[1]
        y += aim * line[1]
    

    print("Line{}: {}".format(count, line))
 
file1.close()

print(f"Answer: {x*y}")