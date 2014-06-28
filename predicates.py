# This is my Predicate module
# Importing the regular expressions module
import regex

# Defining the regular expressions
Numeral = r"S*0"
Variable = r"[abcde]'*?"
Term = "(?P<Term>S*(?:\(((?&Term))[.+]((?&Term))\)" + "|" + Numeral + "|" + Variable + "))" 
# The Term[9:] is to remove the double reference on the ?P<Term> group.
Well_Formed_String = "(?P<wfs>" + "(?:~|E"+ Variable + ":" + "|A" + Variable + ":" + ")*" + "(?:<((?&wfs))[&V-]((?&wfs))>" + "|" + Term + "=" + "(" + Term[9:] + "))" 
wfs = Well_Formed_String

# Predicate to determine if string matches desired regular expression
# regex string -> Boolean
def isType (exp, string):
	return True if regex.match((r"^" + exp + r"$"), string) else False
		