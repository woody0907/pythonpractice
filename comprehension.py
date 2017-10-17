__author__ = 'woody'


print([x ** 2 for x in range(10) if x % 2 == 0])

print(list(map((lambda x: x ** 2),filter((lambda x : x % 2 == 0),range(10)))))

res = [x + y for x in [0, 1, 2]
             for y in [100,200,300]]
print(res)
