import data

li = data.task1
count = 0
for i in range(1, len(li)):
    if li[i-1] < li[i]:
        count += 1

print(count)

# uno linerrr
print(sum([1 for i in range(1, len(li)) if li[i-1] < li[i]]))
