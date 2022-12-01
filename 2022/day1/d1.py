
file1 = open('input.txt', 'r')

collector = []
current_sum = 0


lines = file1.readlines()

for line in lines:
    if line.strip() == "": 
        collector.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(line.strip())



print("Solution 1: ", max(collector))

collector = sorted(collector)
print("Solution 2: ", sum(collector[-3:]))



