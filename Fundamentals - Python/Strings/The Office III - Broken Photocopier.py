#https://www.codewars.com/kata/57ed56657b45ef922300002b/train/python

"""The bloody photocopier is broken... Just as you were sneaking around the office to print off your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string."""

tests =     [
        ['001111110011001110101111101001', '110000001100110001010000010110'],
        ['00110100110010011100110010100111100000011', '11001011001101100011001101011000011111100']
    ]

binary_dict = { '0':'1', '1':'0'}
result = []

def broken(inp):
        new_value = ""
        for index, value in enumerate(inp):
                for x in range ( len(value)):
                        new_value += value[x].replace('1','2').replace('0','1').replace('2','0')
                        new_value = new_value+""
        return new_value

print( broken(tests) )
