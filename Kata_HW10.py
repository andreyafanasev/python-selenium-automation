"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""


def find_it(seq):
    a = {}
    for i in seq:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    for s in a:
        if a[s]%2!=0:
            return s


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))