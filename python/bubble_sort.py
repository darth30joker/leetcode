a = [5, 1, 6, 3, 4]

for j in range(len(a) - 1):
    for i in range(len(a) - j - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

print(a)
