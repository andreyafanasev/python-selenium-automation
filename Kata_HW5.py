"""
Welcome to the Codewars Bar!
Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.

Your fellow coders have bought you several drinks tonight in the form of a string.
Return a string suggesting how many glasses of water you should drink to not be hungover.

Examples
"1 beer"  =>  "1 glass of water"
"1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water"
Notes
To keep the things simple, we'll consider that anything with a number in front of it is a drink:
"1 bear" => "1 glass of water" or "1 chainsaw and 2 pools" => "3 glasses of water"
The number in front of each drink lies in range [1; 9]


hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"), "10 glasses of water"

"""

def hydrate(drink_string):
    summ = 0
    for i in drink_string:
        if i.isdigit() == True:
            summ += int(i)
    if summ == 1:
        return f'{summ} glass of water'
    else:
        return f'{summ} glasses of water'

print(hydrate("1 shot"))