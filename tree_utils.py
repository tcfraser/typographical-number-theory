class Term(value, children, enclose):
    def __init__(self, value = None, children = None, enclose = None):
    	self.value = value
    	self.children = children
    	if enclose = None:
    		self.paren, self.opp = None
    	else:
    		self.paren = enclose[0]
    		self.opp = enclose[1]

    def add_child(self, new_children):
        self.children.append(new_children)

    def print_term(self, start = ""):
    	if self.value != None:
    		if self.value == "S":







a = node("a")
b = node("S", [a])

test = node(None, [a,b], ["()", "+"])

term_1 =  