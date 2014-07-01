from predicates import *
import regex

axiom_1 = "Aa:~Sa=0"    #[forall, var_a, colon, not_, succ, var_a, equal, zero]
axiom_2 = "Aa:(a+0)=a"  #[forall, var_a, colon, l_para, var_a, add, zero, r_para, equal, var_a]
axiom_3 = "Aa:Ab:(a+Sb)=S(a+b)"
axiom_4 = "Aa:(a.0)=0"
axiom_5 = "Aa:Ab:(a.Sb)=((a.b)+a)"


# takes in a regex match and returns a list of groups matched is there are any, and an empty list if no matches are made.
# regexmatch -> [matched groups]
def groups (match):
    if match == None:
        return []
    else:
        return match.groupdict()

# This function replaces all instances of A with wfs(1) and B with wfs(2) for later use in checking
# string -> string
def AB_wfs (general_string, template):
    if template:
        return general_string.replace("A",wfs([1])).replace("B", wfs([2]))
    elif not template:
        return general_string.replace("A","\g<wfs_1>").replace("B", "\g<wfs_2>")

# interchange is meant to handle DeMorgan, Contrapostive, and Switheroo by taking in a string, and returning a list of strings that correspond to all possible modifications that could be made to the string that are valid under the respective rule.
# wfs -> [wfs,wfs,wfs...]

def interchange (string, form1, form2):
    one_to_two = regex.match(AB_wfs(form1, True), string)
    two_to_one = regex.match(AB_wfs(form2, True), string)
    # *************************** one_to_two.expandf(AB_wfs(form2, False))
    return [["1->2",groups(one_to_two)],["2->1",groups(two_to_one)]]
    # Possibilities = [(string != one_to_two),(string != two_to_one)]
    # if Possibilities == [False, False]:
    #     return "Can't be Modified."
    # elif Possibilities == [True, False]:
    #     return one_to_two
    # elif Possibilities == [False, True]:
    #     return two_to_one
    # elif Possibilities  == [True, True]:
    #     return one_to_two if reverse == False else two_to_one
    # else:
    #     return "Error"

def DeMorgan (string):
    return interchange(string, "<~A&~B>", "~<AVB>")

def Contrapositive (string, reverse = False):
    return interchange(string, "<A-B>", "<~B-~A>")

def Switcheroo (string, reverse = False):
    return interchange(string, "<AVB>", "<~A-B>")

# -----------------
# Tests
# -----------------
# print(AB_wfs("<~A&~B>", True))
# print("\n")
print(groups(regex.fullmatch(AB_wfs("A", True), "~a=b"))["wfs_1"])
# print("\n")
print(DeMorgan("<<~a=b&~~b=d>V<~~a=a'&~Sb=SSb>>"))
print(groups(regex.fullmatch(wfs(), "a=b")))
print(groups(regex.fullmatch(wfs(), "<a=b-b=c>")))
print(groups(regex.fullmatch(wfs(), "Ea''':<a=b-b=Sc'>")))
print(groups(regex.fullmatch(wfs(), "~Aa:a=SSSS0'''''")))
print(groups(regex.fullmatch(wfs(), "~Aa:<<a=a'-b=b'>&<c=c'Vd=d'>>")))
print(groups(regex.fullmatch(Modifiers + AB_wfs("<A[&V-]B>", True), "~Aa:<<a=a'-b=b'>&~Aa:<c=c'Vd=d'>>")))
