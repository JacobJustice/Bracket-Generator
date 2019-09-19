import match
import competitor
#
# Bracket class
# Contains the bracket_file, list of competitors in the bracket,
# 	list of incomplete matches, and list of complete matches
# Contains helper methods for generating these attributes
# Contains methods allowing you to interact with these attributes in
# 	various ways
#

class Bracket:
    bracket_file = None
    competitor_list = []
    incomplete_matches = []
    complete_matches = []

    def __init__(self, filename):
        #open bracket file
        bracket_file = open(filename, "r")
        bracket_file_lines = bracket_file.readlines()

        #making competitor_list from the bracket file
        match_count = 1
        for i in range(len(bracket_file_lines)):
            bracket_file_lines[i] = bracket_file_lines[i][:-1]		# remove \n
            comp = competitor.Competitor(bracket_file_lines[i], i+1)	# make new competitor object
            self.competitor_list.append(comp)		#append that competitor to the list

        num_comps = len(self.competitor_list)

        #figure out the greatest power of 2 that is <= the number of competitors
        base_rounds = 0
        while (2**base_rounds <= num_comps):
            base_rounds+=1
        base_rounds-=1

        #figure out how many outlier matches there are
        num_outlier_matches = num_comps - 2**base_rounds
        #figure out how many byes there are
        byes = 2**base_rounds - num_outlier_matches

        #for every bye set the next top competitors bye to true
        for i in range(byes):
            self.competitor_list[i].bye = True
            print(self.competitor_list[i], self.competitor_list[i].bye)

            
    def __str__(self):
        return "Bracket"

    def generate_match(self, m_no,  comp_1, comp_2):
        return match.Match(m_no, comp_1, comp_2)

    def user_complete_match(self, match):
        print(match)
        winner = input("Who is the winner?\ninput 1 or 2:")


#br = Bracket(input("filename: "))
br = Bracket("bracket.txt")

