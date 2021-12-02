import data

sums = [sum(data.task1[x-2:x+1]) for x in range(2, len(data.task1))]
count = 0
for i in range(1, len(sums)):
    if sums[i-1] < sums[i]:
        count += 1
print(count)
