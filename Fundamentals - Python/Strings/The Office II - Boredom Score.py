#https://www.codewars.com/kata/the-office-ii-boredom-score
"""Every now and then people in the office moves teams or departments.
Depending what people are doing with their time they can become more or less boring. Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.

Each department has a different boredom assessment score, as follows:

accounts = 1
finance = 2
canteen = 10
regulation = 3
trading = 6
change = 6
IS = 8
retail = 5
cleaning = 4
pissing about = 25

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'
< 100 & > 80: 'i can handle this'
100 or over: 'party time!!'"""

score_values = {  'accounts' : 1,
            'finance' : 2,
            'canteen' : 10,
            'regulation' : 3,
            'trading' : 6,
            'change' : 6,
            'IS' : 8,
            'retail' : 5,
            'cleaning' : 4,
            'pissing about' : 25}

def boredom(staff):
    resultado = 0
    for x in staff:
        resultado += score_values[staff[x]]
    if resultado <= 80 :
        return "Kill me now"
    elif resultado < 100 and resultado > 80:
        return "i can handle this"
    else:
        return "party time!!"



boredom({"tim": "change", "jim": "accounts",
             "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
             "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
             "mr": "finance"})

#rw 22/06/2021
#Other Solutions
"""    
    n = sum(lookup[s] for s in staff.values())
    if n <= 80:
        return "kill me now"
    if n < 100:
        return "i can handle this"
    return "party time!!
    
"""