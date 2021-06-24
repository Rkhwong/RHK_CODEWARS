# write the function is_anagram
def is_anagram(test, original):
    # Compare if STRING SIZE is the SAME
    if (len(test) == len(original)):
        # Make Sure Upper and Lower Case does not Matter
        test = test.lower()
        original = original.lower()
        #SORTED() function returns a sorted list of the specified iterable object.
        if( sorted(test) == sorted(original)):
            return True
        else:
            return False
    return False
# RW - 28/05/2021