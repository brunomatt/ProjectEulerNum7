#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
import time
import math
start = time.time() #this program takes about 80 seconds to run.

primes = [2]

def prime_check(int):
    possible_factors = []
    for k in range(2, math.ceil(int/2) + 1):
        possible_factors.append(k)
    if all(int % k for k in possible_factors) == 0:
        return False
    else:
        return True

def odd_check(int):
    if int % 2 == 0:
        return False
    else:
        return True

for i in range(3,105000):
    if odd_check(i) is True: #cuts prime check calculations in half
        if prime_check(i) is True:
            primes.append(i)

print(primes[10000]) #prints 10,001 prime, ie our answer.

stop = time.time()

print('Time: ', stop - start)