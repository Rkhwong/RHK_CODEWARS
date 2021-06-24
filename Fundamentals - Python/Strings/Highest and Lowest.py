"""
https://www.codewars.com/kata/554b4ac871d6813a03000035

In this little assignment you are given a string of space separated numbers,
 and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first."""


def high_and_low(string):
    string_split = string.split()
    if len(string_split) == 1:
        high = string_split[0]
        low = string_split[0]
    else:
        if (int(string_split[0]) > int(string_split[1]) or int(string_split[0]) == int(string_split[1]) ):
            high = string_split[0]
            low = string_split[1]
        else:
            high = string_split[1]
            low = string_split[0]
        for x in range (2,len(string_split)):
            if int(string_split[x]) > int(low):
                if int(string_split[x]) > int(high):
                    high = string_split[x]
            else:
                 low = string_split[x]
    result = high+" "+ low
    return(result)

print( high_and_low("1 1 0") )

#RW 21/06/2021

#Others Solutions
def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))