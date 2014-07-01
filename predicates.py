# This is my Predicate module
# Importing the regular expressions module
import regex
# I should really do regex.compile on these to enable it much faster so that I do not have to create them each time


# Defining the regular expressions
Numeral = r"S*0"
Variable = r"[abcde]'*?"
Modifiers = "(?:"+ "~|E"+ Variable + ":" + "|A" + Variable + ":" + ")*" 

def indices(listofints):
    return "_" + "_".join(str(i) for i in listofints)

def Term(i = [0]):
    return regex.subf(r"Term", "Term" + indices(i), "(?P<Term>S*(?:\(((?&Term))[.+]((?&Term))\)" + "|" + Numeral + "|" + Variable + "))")  

def wfs(i = [0]):
    return regex.subf(r"wfs", "wfs" + indices(i), "(?P<wfs>" +  Modifiers + "(?:<((?&wfs))[&V-]((?&wfs))>" + "|" + Term([i[0],1]) + "=" + Term([i[0],2]) + "))")

# Predicate to determine if string matches desired regular expression
# regex string -> Boolean
def isType (exp, string):
    return True if regex.fullmatch(exp, string) else False
        