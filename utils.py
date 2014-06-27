class String_Processor:
    def __init__(self, string):
        self.string = string
        self.paren_stack = list()
        self.opp_stack = list()

    def add_paren(self, s):
        pass

    def add_opp(self, s):
        pass

    def pop_paren(self):
        return self.paren_stack.pop()

    def pop_opp(self):
        return self.opp_stack.pop()
