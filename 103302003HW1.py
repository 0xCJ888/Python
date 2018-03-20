#find prime nmber
import math

def isPrime(num):
    for x in range(2,num):
        if(num % x == 0):
            return False
    return True

count = 0
for i in range(100, 1001):
    if(isPrime(i)):
        print(i)
        count += 1    
print("Total count = ", count)