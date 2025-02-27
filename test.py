pre = 0
for i in range(10):
    sum = i + pre
    print("Current Number ",i,"Previous Number ",pre,"sum :",sum)
    pre = i
print("we done")