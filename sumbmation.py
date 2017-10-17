a = [1,2,3,4,5]
def custom_sumbmation():
    sum = 0
    for i in a:
        sum += i
    print(sum)

def recursion_sumbmation(l):
    if not l:
        return 0
    return l[0]+recursion_sumbmation(l[1:])

def ternary_sumbmation(l):
    return 0 if not l else l[0]+ternary_sumbmation(l[1:])

def ternary_sumbmation1(l):
    return l[0] if not l[1] else l[0]+ternary_sumbmation(l[1:])


def while_sumbmation(l):
    sum = 0
    while l:
        sum += l[0]
        l = l[1:]
    print(sum)

def comprehension_test(l):
    b = [x*x for x in l]
    print(b)

def function_map_test(l):
    s = list(map(lambda x:x*x,l))
    print(s);

def function_filter_test(l):
    s = list(filter(lambda x:x%2==0,l))
    print(s)

# custom_sumbmation()
# print(recursion_sumbmation(a))
# print(ternary_sumbmation(a))
# print(ternary_sumbmation1(a))
print(function_filter_test(a))
