    # INSTRUCTIONS

    # In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

    # <QUESTION>

    # <EXAMPLES>

    # <HINT>

    # You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

    # Access Python from you CLI

    # Type help() or for example help(str)



    # <QUESTION 1>    
    
    # Given a string, return a string where for every char in the original string, there are three chars.
    
    # <EXAMPLES>

    # one("The") → "TTThhheee"
    # one("AAbb") → "AAAAAAbbbbbb"
    # one("Hi-There") → "HHHiii---TTThhheeerrreee"

    # <HINT>
    # How does a for loop iterate through a string?

def one(string):
    result = ""
    for letter in string:
        char = chr[letter]
    return result == result + char + char
    # for str(char) in string:
    #     return result += char
# I practiced this one, but I can't remember how to iterate strings properly, can't believe I can't answer this off the top of my head.
    
    









    # <QUESTION 2>

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.
    
    # The function should return the boolean False if not.

    # <EXAMPLES>

    # two(3) → True
    # two(8) → False

    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(num):
    # for x in range(abs(num), 0, -1):
    #     # while num % num == 0 and num % 1 == 0:
    #     if num/x != 1:
    #         return False
    #     else: 
    #         return True
    pass
# I KNOW I know how to do this, but I can't put my nloody finger on it, how irksome.
    








    # <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

    # So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

    # <EXAMPLES>

    # three(9) → 11106
    # three(5) → 6170

    # <HINT>
    # What happens if you multiply a string by a number?

def three(a):
    result = ""
    return 1
# ran out of time








    # <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.
    
    # <EXAMPLES>

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee" 
    # four("return","letter") → "rleettutrenr"

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?

def four(string1, string2):
    result = ''.join(''.join(f for f in tup) for tup in zip(string1, string2))

    return result
# looks good









    # <QUESTION 5>

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    
    # <EXAMPLES>
    
    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]
    
    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.

def five():
    # from random import randint
    # randomlist = []
    # for i in range(0, 5):
    #     numb = randint(100, 200)
    #     if numb % 2 == 0:
    #         randomlist.append(numb)
    pass
# This LOOKS like it's correct but i'm missing something, and i can't figure out what. How upsetting, I need more practice.
    











    # <QUESTION 6>

    # Given a string, return the boolean True if it ends in "py", and False if not. 
    
    # Ignore Case.

    # For Example:

    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

    # <HINT>
    # There are no hints for this question.
    
def six(string):
    return string.casefold().endswith("py")

# looks good











    # <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large. 
    
    # Return the boolean True if the three values are evenly spaced, so the
    # difference between small and medium is the same as the difference between
    # medium and large. 
    
    # Do not assume the ints will come to you in a reasonable order.
    
    # <EXAMPLES>

    # seven(2, 4, 6) → True
    # seven(4, 6, 2) → True
    # seven(4, 6, 3) → False
    # seven(4, 60, 9) → False

    # <HINT>
    # There is a function for lists called sort.
    # Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
    return False
#ran out of time








    # <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
    
    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)

def eight(string, num):
    num = int
    new_string = string.replace(""[0:num])
    return new_string






    # <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT> 
    # There are no hints for this question.

def nine(string1, string2):
#     if string1 in string2:
#         return True
#     elif string2 in string1:
#         return True
#     else:
#         return False
#The command is not (in), but the logic should be true, i've forgotten it... cant even google it cause i cant remember what to google...
    pass







    # <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
    
    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.

def ten(a, b):
    pass
    # numberlist = []
    # for i in range(0, a):
    #     for j in range(0, b):
    #        numberlist = i*j
    # return numberlist
    #Why doesn't it work!?