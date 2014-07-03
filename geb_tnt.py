from predicates import *
import regex 

# Temporary documentation for the list of theorems
theorems = open("theorems.txt", "w+")

# apply_rules takes in a list of the rules from TNT/Propositional Calc and applies them to a list of known theorems and puts them in the file of theorems.
def apply_rules(rules, strings):
	pass

# takes in a regex match and returns a list of groups matched is there are any, and an empty list if no matches are made.
# regexmatch -> [matched groups]
def groups (match):
    if match == None:
        return []
    else:
        return match.capturesdict()

# takes in a regex match and a replacment regex and applies it. If the regex match was none, it will return an empty list
# regexmatch format -> list of things
def replace (match, newform):
    if match == None:
        return []
    else:
        return [match.expandf(newform)]

# This function replaces all instances of A with wfs(1) and B with wfs(2) for later use in checking
# string -> string
def AB_wfs (general_string, template):
    if template:
        return general_string.replace("A",wfs([1])).replace("B", wfs([2]))
    elif not template:
        return general_string.replace("A","{wfs_1}").replace("B", "{wfs_2}")

# interchange is meant to handle DeMorgan, Contrapositive, and Switheroo by taking in a string, and returning a list of strings that correspond to all possible modifications that could be made to the string that are valid under the respective rule.
# wfs -> [wfs,wfs,wfs...]

def interchange (string, form1, form2):
    if isType(Modifiers([0]) + Term([1]) + "=" + Term([2]),string):
        return []
    else:
        one_to_two = regex.fullmatch(Modifiers([0]) + AB_wfs(form1, True), string)  # I can be more efficient and remove these with a regex.subf below. 
        two_to_one = regex.fullmatch(Modifiers([0]) + AB_wfs(form2, True), string)  ## ^^^^^
        deep = regex.fullmatch(general, string)
        left = []
        for lstring in interchange (deep.group("wfs_1"), form1, form2):
            left.extend(replace(deep, "{Modifiers_0}{lbra}" + lstring + "{opperator}{wfs_2}{rbra}"))
        right = []
        for rstring in interchange (deep.group("wfs_2"), form1, form2):
            right.extend(replace(deep, "{Modifiers_0}{lbra}{wfs_1}{opperator}" + rstring + "{rbra}"))
        return replace(one_to_two, "{Modifiers_0}" + AB_wfs(form2, False)) + replace(two_to_one, "{Modifiers_0}" + AB_wfs(form1, False)) + left + right

def DeMorgan (string):
    return interchange(string, "<~A&~B>", "~<AVB>")

def Contrapositive (string):
    return interchange(string, "<A-B>", "<~B-~A>")

def Switcheroo (string):
    return interchange(string, "<AVB>", "<~A-B>")




# This is the list of all the applicable rules to well formed strings 
rules = {
DeMorgan.__name__: DeMorgan,
Contrapositive.__name__: Contrapositive,
Switcheroo.__name__: Switcheroo
}

# List of the common TNT axioms expressed in custom theorem notation
axioms = {
1: [1, "axiom_1", "Aa:~Sa=0"],
2: [2, "axiom_2", "Aa:(a+0)=a"], 
3: [3, "axiom_3", "Aa:Ab:(a+Sb)=S(a+b)"],
4: [4, "axiom_4", "Aa:(a.0)=0"],
5: [5, "axiom_5", "Aa:Ab:(a.Sb)=((a.b)+a)"]
} 





# -----------------
# Tests
# -----------------
# DeMorgan_Test_1 = "~<Ab:<~a=b&~~b=d>V<~~a=a'&~Sb=SSb>>"
# DeMorgan_Test_2 = "Ab:<~a=b&~c=d>"
# Contrapositive_Test_1 = "<~a=b-~c=d>"
# Switcheroo_Test_1 = "<a=b'Vc=SSSSSd''>"
# Contrapositive_Test_2 = "<~a=(S0.a''')-~c=d>"

# print(DeMorgan(DeMorgan_Test_1))
# print(DeMorgan(DeMorgan_Test_2))
# print(Contrapositive(Contrapositive_Test_1))
# print(Switcheroo(Switcheroo_Test_1))
# print(Contrapositive(Contrapositive_Test_2))
# print(Switcheroo(Contrapositive_Test_1))
# print(Switcheroo(DeMorgan_Test_1))


# -----------------
# Archived Tests
# -----------------

# print(AB_wfs("<~A&~B>", True))
# print("\n")
# print(groups(regex.fullmatch(AB_wfs("A", True), "~a=b"))["wfs_1"])
# print("\n")
#test = regex.fullmatch(general, "Ab:<~a=b&~~b=d>")
#print(groups(test))
#print(test.group("Modifiers_0"))
#print(DeMorgan(test.group("wfs_1")))
#print(DeMorgan("Ab:<~a=b&~~b=d>"))
# print(groups(regex.fullmatch(wfs(), "a=b")))
# print(groups(regex.fullmatch(wfs(), "<a=b-b=c>")))
# print(groups(regex.fullmatch(wfs(), "Ea''':<a=b-b=Sc'>")))
# print(groups(regex.fullmatch(wfs(), "~Aa:a=SSSS0'''''")))
# print(groups(regex.fullmatch(wfs(), "~Aa:<<a=a'-b=b'>&<c=c'Vd=d'>>")))
# print(groups(regex.fullmatch(Modifiers + AB_wfs("<A[&V-]B>", True), "~Aa:<<a=a'-b=b'>&~Aa:<c=c'Vd=d'>>")))
