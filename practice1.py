def main():
    N = str(input("N: ")) # Takes input for test case N
    P = int(input("P: ")) # Takes input for test case P

    length = len(N) # Stores length of number as variable length
    num = length    # copy of variable length
    number = []     # list to store individual digits of N

    for i in range(0, num):   # Takes all the characters from the string N and adds to the list 'number'
        number.append(N[i])

    for i in range(0, num): # Changes every character in list 'number' from a string to an int
        number[i] = int(number[i])

    index = length - P   # Takes the length and subtracts P to get the index of the Pth number from the right
    digit = number[index]   # Saves the Pth digit from the right as 'digit'

    i = 0 # Iteration variable 'i'
    while i < index:                            # For every number left of index
        if (number[i] + digit) > 9:             # If the digits are greater than 9 only uses the ones place digit
            number[i] = (number[i] + digit) % 10
        else:                                   # Else it just adds digit to that number
            number[i] += digit
        i += 1                                                 

    i += 1 # i + 1 to move past index digit

    while i > index and i < length: # For every number right of index
        number[i] = abs(number[i] - digit)  # Takes the absolute value of the difference and sets that to number at that index
        i += 1

    final = "" # String to hold final answer

    for i in range(0, num): # Goes through the list converting all of the updated numbers back to strings
        number[i] = str(number[i]) 
        final += number[i] # Strings together all of the individual digits
    
    final = int(final) # Converts final string back into an int
    print(final) # Prints final answer


main()
