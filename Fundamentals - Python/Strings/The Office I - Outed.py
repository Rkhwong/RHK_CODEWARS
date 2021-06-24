#https://www.codewars.com/kata/the-office-i-outed
"""Your colleagues have been looking over you shoulder.

When you should have been doing your boring real job, you've been using the
work computers to smash in endless hours of codewars.

In a team meeting, a terrible, awful person declares to the group that you aren't working.
You're in trouble. You quickly have to gauge the feeling in the room to decide whether or not you should gather your things and leave.

Given an object (meet) containing team member names as keys, and their happiness rating out of 10 as the value,
 you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.

Happiness rating will be total score / number of people in the room.

Note that your boss is in the room (boss), their score is worth double it's face value (but they are still just one person!)."""

def outed(meet, boss):
    rating = 0
    for x in meet:
        if( x == boss):
            rating = rating + meet[x]*2
        else:
            rating = rating + meet[x]
    if ( rating / len(meet) <= 5):
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"

#test.assert_equals(, 'Get Out Now!')

outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura')

#RW 21/06/2021

#Other Solutions
def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'