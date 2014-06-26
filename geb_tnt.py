from encoding import *

output_file = open("output.txt", "r+")

axiom_1 = "Aa:~Sa=0" 	#[forall, var_a, colon, not_, succ, var_a, equal, zero]
axiom_2 = "Aa:(a+0)=a" 	#[forall, var_a, colon, l_para, var_a, add, zero, r_para, equal, var_a]
axiom_3 = "Aa:Ab:(a+Sb)=S(a+b)"
axiom_4 = "Aa:(a.0)=0"
axiom_5 = "Aa:Ab:(a.Sb)=((a.b)+a)"

# Merges elements of a listed formula into one string
# list -> string
def truncate (lst):
	return "".join(lst)

# Produces a listed formula from a stringed formula
# string -> list 
def expand (formula):
	return list(formula)

# Predicate to determine if string is a numeral or not
# string -> Boolean
def isNumeral (pot_Numeral):
	if pot_Numeral == "":
		return False
	elif pot_Numeral == "0":
		return True
	elif pot_Numeral[0] == "S":
		return isNumeral(pot_Numeral[1:])
	else: 
		return False

# Predicate to determine if string is a Variable or not
# string -> Boolean
def isVariable (pot_Variable):
	if pot_Variable == "":
		return False
	elif pot_Variable in ["a","b","c","d","e"]:
		return True
	elif pot_Variable[len(pot_Variable)-1] == "'":
		return isVariable(pot_Variable[:(len(pot_Variable)-1)])
	else:
		return False
