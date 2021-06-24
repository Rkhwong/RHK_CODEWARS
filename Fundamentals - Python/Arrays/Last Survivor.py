# https://www.codewars.com/kata/609eee71109f860006c377d1

"""You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.

Example:

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'
Notes
The given string will never be empty.
The length of the array is always one less than the length of the string.
All numbers are valid.
There can be duplicate letters and numbers.
"""
"""     test.assert_equals(last_survivor('abc', [1, 1]), 'a')
        test.assert_equals(last_survivor('kbc', [0, 1]), 'b')
        test.assert_equals(last_survivor('zbk', [2, 1]), 'z')
        test.assert_equals(last_survivor('c', []), 'c')"""

def last_survivor(letters, coords):
    print(letters,coords,"\n")
    word = list(letters.strip())
    for x in range (len(coords)):
        print("Interation {} | Coord [{}] = {}: {}".format(x,coords[x],word[coords[x]],word))
        if ( len(coords) == 1):
            print("Removed : ", coords[0])
            word.pop(coords[0])
        else:
            print("Removed : ", word[coords[x]])
            word.pop(coords[x])
    letter = "".join(word)
    print("Result",letter)
    return letter

#RW 02/06/2021