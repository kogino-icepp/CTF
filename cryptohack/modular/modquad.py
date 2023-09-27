p = 29
ints = [14,6,11]
for i in range(1,29,1):
    x = (i*i)%p
    for j in range(0,3,1):
        if x == ints[j]:
            print(i)