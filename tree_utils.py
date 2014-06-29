class Term(value, children, enclose):
    def __init__(self, value = None, children = None, enclose = None):
    	self.value = value
    	self.children = children
    	if enclose:
    	    self.paren, self.opp = enclose
    	else:
    		self.paren, self.opp = None, None

    def add_child(self, new_children):
        self.children.append(new_children)

    def print_term(self, start = ""):
    	if self.value:
    		if self.value == "S":
    








a = node("a")
b = node("S", [a])

test = node(None, [a, b], ["()", "+"])

term_1 =  
