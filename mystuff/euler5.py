#start = 2520 must be even
def check(n):
    for i in range(11, 21): #doesn't include 21
        if n % i == 0: #if n is divisible evenly by current number in range, then continue
            continue
        else:
            return False # if n is not evently divisible, return False
    return True

x = 2520

while not check(x):
    x += 2520 #if returning false, we are adding 2520

print(x)
