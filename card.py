
class card:
    def init(self):
        self.term = ""
        self.definition = ""
        self.next = None

    def edit_term(self, new_name):
        self.term = new_name

    def edit_definition(self, new_defintion):
        self.definition = new_defintion

    def equals(self, target):
        if ((self.term == target.term) & (self.definition == target.definition)):
            ans = True
        else:
            ans = False 
        return ans
        
    def get_term(self):
        return self.term
    
    def get_definition(self):
        return self.definition 
