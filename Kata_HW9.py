"""
Santa's elves are boxing presents, and they need your help!
Write a function that takes two sequences of dimensions of the present and the box,
respectively, and returns a Boolean based on whether or not the present will fit in the box provided.
The box's walls are one unit thick, so be sure to take that in to account.

Examples: Present and box respectively

[10, 7, 16], [13, 32, 10] --> true, box is bigger than present
[5, 7, 9], [9, 5, 7]      --> false, present and box are same size
[17, 22, 10], [5, 5, 10]) --> false, box is too small

"""


def will_fit(present, box):
    answ = True
    for i in range(len(present)):
        if sorted(present)[i] >= sorted(box)[i]-1:
            answ = False
    return answ


print(will_fit((10, 2, 4), (6, 4, 12)))