from predicates import *
import regex

axiom_1 = "Aa:~Sa=0"	#[forall, var_a, colon, not_, succ, var_a, equal, zero]
axiom_2 = "Aa:(a+0)=a"	#[forall, var_a, colon, l_para, var_a, add, zero, r_para, equal, var_a]
axiom_3 = "Aa:Ab:(a+Sb)=S(a+b)"
axiom_4 = "Aa:(a.0)=0"
axiom_5 = "Aa:Ab:(a.Sb)=((a.b)+a)"

DR_ts = "<~a=b&~~b=d>"


# This function replaces all instances of A with wfs(1) and B with wfs(2) for later use in checking
# string -> string
def AB_wfs (general_string, template):
	if template:
		return general_string.replace("A",wfs(1)).replace("B", wfs(2))
	elif not template:
		return general_string.replace("A","\g<wfs1>").replace("B", "\g<wfs2>")

def interchange (string, form1, form2, reverse = False):
	one_to_two = regex.sub(AB_wfs(form1, True), AB_wfs(form2, False), string, 1)
	two_to_one = regex.sub(AB_wfs(form2, True), AB_wfs(form1, False), string, 1)
	Possibilities = [(string != one_to_two),(string != two_to_one)]
	if Possibilities == [False, False]:
		return "Can't be Modified."
	elif Possibilities == [True, False]:
		return one_to_two
	elif Possibilities == [False, True]:
		return two_to_one
	elif Possibilities	== [True, True]:
		return one_to_two if reverse == False else two_to_one
	else:
		return "Error"

def DeMorgan (string, reverse = False):
	return interchange(string, "<~A&~B>", "~<AVB>", reverse)

def Contrapositive (string, reverse = False):
	return interchange(string, "<A-B>", "<~A-~B>", reverse)

def Switcheroo (string, reverse = False):
	return interchange(string, "<AVB>", "<~A-B>", reverse)
