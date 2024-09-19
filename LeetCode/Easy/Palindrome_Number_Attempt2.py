def palindrome(x):
    xcopy = x #x will need to be modified.
    stringx = str(x) #x is converted to a string so we can get its length

    length = 10 ** (len(stringx)-1) #Get the length of the number, and use that number to the power of 10. For example 1234 becomes 1000
    reversedinteger = 0 #This value will have numbers added to it. It is the reversed form of X
    integervariable = 10

    for i in range (len(stringx)):
        #print(f"{reversedinteger} = ({reversedinteger}/10) + ({xcopy} // {length})") 
        #Take the number and floor divide it by its length. This gives the first digit of the number. For example (1234 // 1000) becomes 1
        #Then add it to the start of the empty int (reversedinteger). Put this number in the previous digits place by dividing the number first. ((1 / 10 = 0.1)+(0.1 + 2)) = 2.1. This is 12 reversed.
        reversedinteger = ((reversedinteger/10) + (xcopy // length))
        xcopy = (xcopy % length) #Now that the first number in the integer is reversed, it can be removed from the given integer. 1234 % 1000 = 234
        length /= 10 #Divide the length by 10. For example, the 1000 now becomes 100. 

        #Debug code
        #print(f"reversedinteger:  {reversedinteger}")
        #print(f"xcopy: {xcopy}")
        #print(f"length {length}")

    print(f"finalnumber = int(round(({reversedinteger} * (10 ** (len({stringx})-1)))))")
    finalnumber = int(round((reversedinteger * (10 ** (len(stringx)-1))))) #The final number would be returned as 5.4321. So it needs to be multiplied back up to 54321

    print(f"x: {x} \nfinalnumber: {finalnumber}")
    return (finalnumber == x) #Simply compare if the reversed number is the same as the original number.


    #operations

    #x % 10 GETS LAST DIGIT
    #x // length RETURNS FIRST DIGIT
    #x % length REMOVES FIRST DIGIT

print(palindrome(1234))
print("")
print(palindrome(1331))
