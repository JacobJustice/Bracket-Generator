#
# Match Class
# Contains two Competitor objects go head to head
# Contains methods allowing the user to fight those competitors in
# 	various ways
#

class Match:
    next_match = None
    match_number = None
    competitor_1 = None
    competitor_2 = None

    def __init__(self, match_number, comp_1, comp_2):
#        if comp_1 != None comp_2 != None:
#            self.next_match = Match(None, None, None)
        self.match_number = match_number
        self.competitor_1 = comp_1
        self.competitor_2 = comp_2

    def __str__(self):
        return "Match Number: " + str(self.match_number) + "\nCompetitor 1: " + str(self.competitor_1) + "\nCompetitor 2: " + str(self.competitor_2)

    def predict_winner(self):
        if self.competitor_1.seed > self.competitor_2.seed:
            return competitor_2
        else:
            return competitor_1

