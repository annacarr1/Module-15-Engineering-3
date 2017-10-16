def sum_of_squares(limit): # makes function for the squares #limit we are setting is 100
    total = 0 #to start at 0
    for i in range (limit+1): #limit 10 and is +1 because we want to include 10
        total += i**2 # makes total add each number squared
    return total # returning the answer

def square_of_sum(limit): # squaring the sum
    total = 0
    for i in range(limit+1):
        total += i # we're only adding
    return total**2 # going through every #, adding together, returning & squaring it

s1 = sum_of_squares(100) #simple variable
s2 = square_of_sum(100) #simple variable

print ("Answer: " + str(s2-s1)) # printing answer in a string
