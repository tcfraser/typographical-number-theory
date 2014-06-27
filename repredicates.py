# This is my Predicate module

# Importing the regular expressions module
import re

# Defining the regular expressions
Numeral = "S*0"
Variable = "[abcde]'*"
Base_Term = "S*" + "(" + Numeral +  "|" + Variable + ")" 
Term = "S*" + "(" + Base_Term + "|" + "\(" + Base_Term + "[.+]" + Base_Term + "\)" +x



# Predicate to determine if string matches desired regular expression
# REGEX string -> Boolean
def isType (exp, string):
	if not re.match(("^" + exp + "$"), string):
		return False
	else:
		return True

# Predicate to determine if string is a numeral or not
# string -> Boolean
def isNumeral (pot_Numeral):
	if not re.match(Numeral, pot_Numeral):
		return False	
	else:
		return True		

# Predicate to determine if string is a Variable or not
# string -> Boolean
def isVariable (pot_Variable):
	if not re.match(Variable, pot_Variable):
		return False
	else:
		return True
	
# Predicate to determine if a string is a string is a Term or not
# string -> Boolean
def isTerm (pot_Term):
	if pot_Term == "":
		return False
	elif isNumeral(pot_Term) or isVariable(pot_Term):
		return True	
	elif pot_Term[0] == "S":
		return isTerm(pot_Term[1:])
	elif not re.match(r"^(.*)$", pot_Term):
		return False
	else:
		return isTerm_helper(pot_Term[1:-1])

# Predicate to determine if the string is of a form (s+t) or (s.t) where s and t are terms
# *Only used when borrowed by isTerm
# string -> Boolean
def isTerm_helper (pot_Term):
	for i in range(0,len(pot_Term)):
		if pot_Term[i] in [".", "+"]:
			if (isTerm(pot_Term[:i]) and isTerm(pot_Term[i+1:])):
				return True
			else:
				pass 
	return False
				
# Predicate to determine if the string is a Formula or Not
# string -> Boolean
def isFormula (pot_Formula):
	if pot_Formula == "":
		return False
	elif pot_Formula[0] == "~":
		return isFormula(pot_Formula[1:])
	elif pot_Formula[0] in ["E","A"]:
		return "banananana"
				