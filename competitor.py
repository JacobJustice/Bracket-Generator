#
# Competitor Class
# Contains a name and a seed for a competitor in the bracket
#
class Competitor:
    name = None
    seed = None
    bye = False
    matched = False
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed

    def __str__(self):
        return self.name + ": " + str(self.seed)



