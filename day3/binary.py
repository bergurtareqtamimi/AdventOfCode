def b_to_d(binary):
    b = []
    for i in binary:
        b.append(int(i))    

    a_sum = 0
    b.reverse()

    for i, e in enumerate(b):
        a_sum += e*2**i
    
    return a_sum

def binary_search(a_list, binary):
    for i, e  in enumerate(binary):
        if len(a_list) == 1:
            break
        r = []
        for bin in a_list:
            if bin[i] != e:
                r.append(bin)
        for i in r:
            a_list.remove(i)
    
    return a_list[0]

counter = [0,0,0,0,0,0,0,0,0,0,0,0]

file1 = open('inp.txt', 'r')
count = 0
bine_list = []
while True:

    # Get next line from file
    line = file1.readline()

 
    # if line is empty
    # end of file is reached
    if not line:
        break

    binary = line.strip()
    #print("Line{}: {}".format(count, line.strip()))

    # count
    for i, e in enumerate(binary):
        counter[i] += int(e)
    
    bine_list.append(binary)

    count += 1
 

file1.close()
print(counter)
for i, e in enumerate(counter):
    counter[i] = round(e/count)
print(counter)

b = ""
r = ""

for i in counter:
    b += str(i)

for i in counter:
    if i == 1:
        r += "0"
    else:
        r += "1"


print(b)
print(r)

print(b_to_d(b)*b_to_d(r))

b1 = bine_list.copy()
b2 = bine_list.copy()

ox = binary_search(b1, b)
print(ox)
co = binary_search(b2, r)
print(co)


print(b_to_d(ox)*b_to_d(co))



    





