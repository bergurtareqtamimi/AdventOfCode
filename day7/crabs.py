
file1 = open('inp.txt', 'r')

numbers = [int (i) for i in file1.readline().strip().split(",")]


# part 1
# mininum_fuel = 100000000000
# for pos in range(len(numbers)):
#     fuel = 0
#     for dude in numbers:
#         fuel += abs(dude - numbers[pos])
    
#     if fuel < mininum_fuel:
#         mininum_fuel = fuel

# print(mininum_fuel)


def average(x):
    return (x * (x + 1)) // 2


# part 2
mininum_fuel = 100000000000
for pos in range(len(numbers)):
    fuel = 0
    for dude in numbers:
        fuel += average(abs(dude - numbers[pos]))
    
    if fuel < mininum_fuel:
        mininum_fuel = fuel

print(mininum_fuel)

