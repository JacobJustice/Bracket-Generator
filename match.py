#
# Match Class
# Contains two Competitor objects go head to head
# Contains methods allowing the user to fight those competitors in
# 	various ways
#

class Match:
    round = 0
    next_match = None
    match_number = None
    com_1 = None
    com_2 = None


    def __init__(self, match_number, comp_1, comp_2, round):
#        if comp_1 != None comp_2 != None:
#            self.next_match = Match(None, None, None)
        self.match_number = match_number
        self.comp_1 = comp_1
        self.comp_2 = comp_2
        self.round = round


    def __str__(self):
        if self.next_match !=  None:
            return "Match Number: " + str(self.match_number) + "\nRound Number: " + str(self.round) + "\nCompetitor 1: " + str(self.comp_1) + "\nCompetitor 2: " + str(self.comp_2) + "\nNext Match comp_1" + str(self.next_match.comp_1) + "\n"
        else:
            return "Match Number: " + str(self.match_number) + "\nRound Number: " + str(self.round) + "\nCompetitor 1: " + str(self.comp_1) + "\nCompetitor 2: " + str(self.comp_2) + "\n"

    def predict_winner(self):
        if self.comp_1.seed > self.comp_2.seed:
            return comp_2
        else:
            return comp_1


    def fill_comp(self, comp):
        if comp_1 == None:
            comp_1 = comp
            return True
        elif comp_2 == None:
            comp_2 = comp
            return True
        else:
            return False


    def decide_winner(self, winner):
        if winner == 1:
            next_match.fill_comp(comp_1)
        elif winner == 2:
            next_match.fill_comp(comp_2)

