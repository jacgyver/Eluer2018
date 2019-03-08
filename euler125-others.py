import time

start = time.time()
data = []
Max = 100000000
for i in range(1, 10000):
    num = i*i
    while num < Max:
        i = i+1
        num += i*i
        if num < Max and str(num) == str(num)[::-1]:
            data.append(num)


print(sum(set(data)))
print(time.time()-start)


