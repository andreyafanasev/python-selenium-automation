"""
Write a function to convert a name into initials.
This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
Patrick Feeney => P.F

"""


def abbrevName(name):
    name_1 = list(name)
    ind = name_1.index(' ')
    a = name_1[0].upper()
    b = name_1[ind+1].upper()
    return (a + '.' + b)

abbrevName("Patrick Feenan")
