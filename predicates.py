# This is my Predicate module
# Importing the regular expressions module
import regex

# Defining the regular expressions
Numeral = r"S*0"
Variable = r"[abcde]'*?"

def Term(index = 1):
	return regex.sub(r"Term", "Term" + str(index), "(?P<Term>S*(?:\(((?&Term))[.+]((?&Term))\)" + "|" + Numeral + "|" + Variable + "))")  


def wfs(index = 1):
	return regex.sub(r"wfs", "wfs" + str(index), "(?P<wfs>" + "(?:~|E"+ Variable + ":" + "|A" + Variable + ":" + ")*" + "(?:<((?&wfs))[&V-]((?&wfs))>" + "|" + Term(2*index-1) + "=" + Term(2*index) + "))") #wfs(1) has term(1) and term(2).... wfs(2) has term(3) and term(4)..........

# Predicate to determine if string matches desired regular expression
# regex string -> Boolean
def isType (exp, string):
	return True if regex.match((r"^" + exp + r"$"), string) else False
		