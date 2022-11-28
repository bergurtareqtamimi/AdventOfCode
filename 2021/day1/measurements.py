file1 = open('inp.txt', 'r')
count = 0
 
depts = []
while True:
    count += 1
    # Get next line from file
    line = file1.readline()

 
    # if line is empty
    # end of file is reached
    if not line:
        break
    depts.append(int(line.strip()))
    print("Line{}: {}".format(count, line.strip()))
 
file1.close()

dept_sum = []

incr= 0
for i in range(len(depts)-2):
    dept_sum.append(depts[i]+depts[i+1]+depts[i+2])

for i in range(len(dept_sum)-1):
    if dept_sum[i] < dept_sum[i+1]:
        incr += 1

print(incr)
