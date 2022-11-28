file1 = open('inp.txt', 'r')
count = 0
 
coll = []

def process_input(line):
    line = line.strip().split("->")
    n1 = line[0].split(",")
    n1 = (int(n1[0]),int(n1[1]))
    n2 = line[1].split(",")
    n2 = (int(n2[0]),int(n2[1]))

    return [n1, n2]

def set_direction(p1, p2):
    if p1 < p2:
        return 1
    return -1

def produce_points(point_list: list[tuple[int,int], tuple[int,int]]):
    points = []
    direction = 1
    
    x1 = point_list[0][0]
    y1 = point_list[0][1]
    x2 = point_list[1][0]
    y2 = point_list[1][1]

    # case 1 (if lines are not diagonal)
    if x1 == x2:
        direction = set_direction(y1, y2)
        for i in range(y1, y2+1, direction):
            points.append((x1, i))
        if direction == -1:
            points.append((x1, y2))
    elif y1 == y2:
        direction = set_direction(x1, x2)
        for i in range(x1, x2, direction):
            points.append((i, y1))
        if direction == -1:
            points.append((x2, y1))
    
    return points





while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    if not line:
        break

    line = process_input(line)


    coll.append(line)
    print("Line{}: {}".format(count, line))
 
file1.close()

grid = [[0] * 1000 for _ in range(1000)]


for points in coll:
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]

    # chase 1: if lines are not diagonal
    if x1 == x2:
        # we want to get the larger and smaller y for our for-loop to work
        a = min(y1, y2)
        b = max(y1, y2)
        for y in range(a, b+1):
            grid[y][x1] += 1
    elif y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        for x in range(a, b+1):
            grid[y1][x] += 1
    else:
        # line is diagonal
        if x1 < x2 and y1 < y2:
            x_step = 1
            y_step = 1
        elif x1 < x2 and y1 > y2:
            x_step = 1
            y_step = -1
        elif x1 > x2 and y1 > y2:
            x_step = -1
            y_step = -1
        elif x1 > x2 and y1 < y2:
            x_step = -1
            y_step = 1
        
        current_pos = [x1, y1]

        while current_pos != [x2, y2]:
            grid[current_pos[1]][current_pos[0]] += 1
            current_pos = [current_pos[0] + x_step, current_pos[1] + y_step]
        grid[x2][y2] += 1



count = 0
for row in grid:
    for value in row:
        if value > 1:
            count += 1
print(count)

    



