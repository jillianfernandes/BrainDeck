from card import card

class deck:
    def init(self):
        self.name = "untitled deck"
        self.terms = []
        self.count = 0
        self.first = None
        self.last = None

        
    def add_term(self, card):
        if self.first == None:
            self.first == card
            self.last == card
        else:
            self.last.next = card
        self.terms.append(card)
        self.last = card
        self.count +=1

    def remove_term(self, card):
        i = 0
        removed = False
        while((i< self.count) & (removed == False)):
            if (self.terms[i].equals(card) == False):
                i +=1
            else:
                self.terms.remove(self.term[i])
                removed = True
        return
    




    
