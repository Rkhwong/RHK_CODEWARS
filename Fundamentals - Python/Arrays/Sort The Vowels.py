
vowels = ['a','A','e','E','i','I','o','O','u','U']

def cat(s):
    string = ""
    print(s)
    for x in s:
        string = string + x
    return string

def sort_vowels(s):
    if(type(s) == int or type(s) == float or s == None):
        return
    newlist = []
    for x in range(len(s)):
        if ( s[x] in vowels):
            y = "|" + s[x]
            newlist.append(y)
            if( x < len(s)-1):
                newlist.append("\n")
        else:
            y = s[x] + "|"
            newlist.append(y)
            if( x < len(s)-1):
                newlist.append("\n")
    return cat(newlist)

print( sort_vowels("rnD Test") )

#RW 14/06/2021