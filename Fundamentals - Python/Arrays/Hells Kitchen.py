"""Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.

Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.

Rules:

Obviously the words should be Caps, Every word should end with '!!!!',
 Any letter 'a' or 'A' should become '@', Any other vowel should become '*'."""

def gordon(a):
    new_list = []
    a = a.upper()
    a = a.replace("A","@").replace("E","*").replace("I","*").replace("O","*").replace("U","*")
    a = a.split()
    for x in a:
        x = x + "!!!!"
        new_list.append(x)

    new_list = " ".join(new_list)
    return new_list

a = "What feck damn cake"

print( gordon(a) )

#RW 02/06/2021