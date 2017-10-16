def sum_of_squares(limit): # makes function for sthe squares
    total = 0
    for i in range (limit+1): #limit is +1 because we want to include 10
        total += i**2 # squaring i
    return total # returning the square

def square_of_sum(limit): # squaring the sum
    total = 0
    for i in range(limit+1):
        total += i # we want to add to i
    return total**2 # returning the square of the total

s1 = sum_of_squares(100)
s2 = square_of_sum(100)

print ("Answer: " + str(s2-s1)) # printing answer in a string, answer appears rounded
