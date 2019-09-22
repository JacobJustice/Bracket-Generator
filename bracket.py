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

        #figure out the smallest power of 2 that is >= the number of competitors
        rounds = 0
        while (2**rounds <= num_comps):
            rounds+=1
        #rounds-=1
        print("rounds", rounds)

        base_rounds = rounds-1

        #figure out how many outlier matches there are
        num_outlier_matches = num_comps - 2**base_rounds
        #figure out how many byes there are
        byes = 2**(base_rounds) - num_outlier_matches

        #for every bye set the next top competitors bye to true
        for i in range(byes):
            self.competitor_list[i].bye = True
            #print(self.competitor_list[i], self.competitor_list[i].bye)

        #the number of base matches you have is equal to one power of two less than the
        # maximum power of two that is less than the number of matches, that
        # occur plus the number of outlier matches 
        base_matches_starting_seed = 2**(base_rounds) + num_outlier_matches - 1
        #print(2**base_rounds)
        #print(base_matches_starting_seed)

        #the number of competitors who don't have to wait on another match to start after their first match
        #is equal to base_matches_starting_seed - num_outlier_matches
        #this will leave the top seeds as people who do have to wait on another match before their first match
        match_number = 1
        print("num_outlier_matches", num_outlier_matches)
        max_match_number = 2**(base_rounds-1) + num_outlier_matches
        print("asdf",max_match_number)

        print("len of competitor_list",len(self.competitor_list))
        outliers = num_outlier_matches
        for i in range(base_matches_starting_seed,num_outlier_matches-1,-1):
            if match_number > max_match_number:
                print("hello world")
                break

            #print(i)
            if outliers > 0:
                second_competitor_i = 2**rounds - i
                outliers -= 1
            else:
                second_competitor_i = 2**base_rounds - i

            second_competitor_i -= 1
            #print("second i: ",second_competitor_i)

            if self.competitor_list[i].matched == False:
                competitor1 = self.competitor_list[i]
            else:
                competitor1 = None

            if self.competitor_list[second_competitor_i].matched == False:
                competitor2 = self.competitor_list[second_competitor_i]
            else:
                competitor2 = None

            if competitor2.bye:
                new_match = self.generate_match(match_number, competitor1, competitor2, 2)
            else:
                new_match = self.generate_match(match_number, competitor1, competitor2, 1)

            round_2_matches = []
            self.incomplete_matches.append(new_match)
            if new_match.round == 2:
                round_2_matches.append(new_match)

            match_number+=1

        print(round_2_matches)
        for match in self.incomplete_matches:
            if match.round == 1:
                print('yeey')
                next_match_num = 2**base_rounds + 1
                next_match_comp = next_match_num - match.comp_2.seed
                print("next_match_comp", next_match_comp)
                for r2_match in round_2_matches:
                    if r2_match.comp_2.seed == next_match_comp:
                        match.next_match = r2_match
            print(match)

    def generate_next_match(self):
        return None
            
    def __str__(self):
        return "Bracket"

    def generate_match(self, m_no,  comp_1, comp_2, r_no):
        if comp_1 != None:
            comp_1.matched = True

        if comp_2 != None:
            comp_2.matched = True
        return match.Match(m_no, comp_1, comp_2, r_no)

    def user_complete_match(self, match):
        print(match)
        winner = input("Who is the winner?\ninput 1 or 2:")


#br = Bracket(input("filename: "))
br = Bracket("bracket.txt")

