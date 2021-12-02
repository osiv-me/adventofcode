import data

depth = 0
distance = 0
for input in data.data:
    if input[:-2] == "forward":
        distance += int(input[-2:])
    elif input[:-2] == "down":
        depth += int(input[-2:])
    elif input[:-2] == "up":
        depth -= int(input[-2:])

print(f"distance: {distance}")
print(f"depth: {depth}")
print(f"answer: {distance*depth}")
