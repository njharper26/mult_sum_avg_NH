for i in range (1, 1001):
    if i % 2 != 0:
        print i

for i in range (5, 1000001):
    if i % 5 == 0:
        print i

x = [1, 2, 5, 10, 255, 3]
sum = 0
for i in x:
    sum += i  
avg = sum / len(x)
print "sum =", sum, ";  avg =", avg
