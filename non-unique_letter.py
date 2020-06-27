"""
Amazon interview question:
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?

"""

def non_unique_letter(string):
    for i in range(len(string)):
        if string.lower()[i] not in string.lower().replace(string[i],'',1):
            return string[i]
    else:
        return ''

print(non_unique_letter('Amazon'))