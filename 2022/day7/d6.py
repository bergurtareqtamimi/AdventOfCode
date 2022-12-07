from collections import defaultdict


file1 = open("input.txt")
cleaned_file = file1.read().strip()
lines = ("\n" + cleaned_file).split("\n$ ")[1:]


current_path = []
children = defaultdict(list)
directory_size = defaultdict(int)


def process_input(block):
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    commands = command.split(" ")

    if commands[0] == "cd":
        if commands[1] != "..":
            current_path.append(commands[1])
        else:
            current_path.pop()

        return

    absolute_current_path = "/".join(current_path)

    size_collector = []
    for line in outputs:
        if line.startswith("dir"):
            dir_name = line.split(" ")[1]
            children[absolute_current_path].append(f"{absolute_current_path}/{dir_name}")
        else:
            size_collector.append(int(line.split(" ")[0]))

    directory_size[absolute_current_path] = sum(size_collector)


for line in lines:
    process_input(line)


def dfs(absolute_current_path):
    size = directory_size[absolute_current_path]
    for child in children[absolute_current_path]:
        size += dfs(child)
    return size


solution = 0
for absolute_current_path in directory_size:
    if dfs(absolute_current_path) <= 100000:
        solution += dfs(absolute_current_path)

print("Solution 1: ", solution)

required = 30000000 - (70000000 - dfs("/"))

solution = 10000000000000 # some hich number
for absolute_path in directory_size:
    size = dfs(absolute_path)
    if size >= required:
        solution = min(solution, size)

print("Solution 2: ", solution)