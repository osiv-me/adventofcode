import data

li = data.task1
sums = [sum(li[x-2:x+1]) for x in range(2, len(li))]
count = 0
for i in range(1, len(sums)):
    if sums[i-1] < sums[i]:
        count += 1
print(count)


# refactored one liner
print(sum([1 for i in range(3, len(li)) if li[i-3] < li[i]]))
