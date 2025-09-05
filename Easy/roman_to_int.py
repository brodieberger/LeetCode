romans = {
    'I':1,
    'IV':4,
    'V':5,
    'IX':9,
    'X':10,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'CD':400,
    'D':500,
    'CM':900,
    'M':1000
}

numeral = "MMMCDXC"

final = 0
i = len(numeral) - 1

while i >= 0:
    if i == 0:
        final += romans[numeral[i]]
        break
    if numeral[i] == "X" and numeral[i-1] == "I":
        final += 9
        i -= 2
    elif numeral[i] == "V" and numeral[i-1] == "I":
        final += 4
        i -= 2
    elif numeral[i] == "L" and numeral[i-1] == "X":
        final += 40
        i -= 2
    elif numeral[i] == "C" and numeral[i-1] == "X":
        final += 90
        i -= 2
    elif numeral[i] == "D" and numeral[i-1] == "C":
        final += 400
        i -= 2
    elif numeral[i] == "M" and numeral[i-1] == "C":
        final += 900
        i -= 2
    else:
        final += romans[numeral[i]]
        i -= 1

print(final)