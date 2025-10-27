# Pixel Cat's End is an online pet game in which players manage a slowly growing village of "not-cats".
# Players can use their not-cats as characters in a small turn-based strategy RPG.
# As of 27/10/2025, the game is in early development and some features are incomplete.

class NotCat:
    
    def __init__(self, name_string):
        self.name = name_string
    
    def set_name(self, name_string):
        self.name = name_string

    def set_personality(self, personality_dict):
        # the personality of a cat is 5 values representing bravery, benevolence, energy, extroversion, and dedication.
        # they should be in the range 0-10 inclusive.
        self.personality = personality_dict

    def set_stats(self, stats_dict):
        # the stats of a cat are 7 values representing strength, agility, health, finesse, cleverness, perception, and luck.
        # they should be in the range 0-40 inclusive (though currently base stats cannot go above 24)
        self.stats = stats_dict
        self.stat_total = sum(x for x in self.stats.values())
        
    def set_levels(self, levels_dict):
        # for a given cat, each role can be levelled from the starting level of 1 up to 4.
        # role levels determine available moves.
        self.levels = levels_dict

    def set_active_role(self, role_string):
        # currently implemented adventuring classes are: fighter, thief, guardian, ranger, medic, scout, bard
        # due to potential confusion with python classes, adventuring classes will be referred to as roles
        # the active role gains exp and gives a buff to certain actions.
        self.active_role = role_string

    def set_trinket(self, trinket_tuple_string_integer):
        # Each cat can hold one trinket, which modifies one stat. The trinket is represented as a tuple (stat_string, modifier_integer)
        self.trinket = trinket_tuple_string_integer

    def create_adventure_dice(self):
        statstodice = { 0: 1,  1: 1,  2: 1,  3: 1,  4: 1,  5: 1,  6: 1,  7: 2,  8: 2,  9: 2, 10: 2, 11: 2, 12: 2, 13: 3,
                       14: 3, 15: 3, 16: 3, 17: 4, 18: 4, 19: 4, 20: 4, 21: 5, 22: 5, 23: 5, 24: 5, 25: 6, 26: 6, 27: 6,
                       28: 6, 29: 7, 30: 7, 31: 7, 32: 7, 33: 8, 34: 8, 35: 8, 36: 8, 37: 9, 38: 9, 39: 9, 40: 9}