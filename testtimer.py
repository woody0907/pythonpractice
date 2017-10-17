import timer
__author__ = 'woody'

print(timer.total(1000,pow,2,1000)[0])
print(timer.bestof(1000,str.upper,'spam')[0])
print(timer.bestoftotal(50,1000,str.upper,'spam'))