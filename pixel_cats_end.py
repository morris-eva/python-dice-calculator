# Pixel Cat's End is an online pet game in which players manage a slowly growing village of "not-cats".
# Players can use their not-cats as characters in a small turn-based strategy RPG.
# As of 27/10/2025, the game is in early development and some features are incomplete.

class NotCat:
    
    def __init__(self, name_string):
        self.name = name_string
    
    def set_name(self, name_string):
        self.name = name_string

    def set_personality(self, personality_tuple):
        # Using a tuple makes it easier to copy in stats from a spreadsheet
        personality_names = ("Bravery", "Benevolence", "Energy", "Extroversion", "Dedication")
        self.personality = {personality_names[x]: personality_tuple[x] for x in range(5)}

    def set_basestats(self, basestats_tuple):
        # Using a tuple makes it easier to copy in stats from a spreadsheet
        self.basestat_total = sum(basestats_tuple)
        stats_names = ("Strength", "Agility", "Health", "Finesse", "Cleverness", "Perception", "Luck")
        self.basestats = {stats_names[x]: basestats_tuple[x] for x in range(7)}
        
    def set_level(self, levels_dict):
        # Levels will need to be updated. This method should only update specified roles.
        # It should also alert in case of mispelling.
        # The default value is 1. Use the .get() method
        allowed_roles = ("Fighter", "Thief", "Guardian", "Ranger", "Medic", "Scout", "Bard")
        self.levels = {}
        for role, level in levels_dict.items():
            if role in allowed_roles:
                self.levels[role] = level
            else:
                raise NameError("Did not understand " + str(role) + ". Roles are Fighter, Thief, Guardian, Ranger, Medic, Scout, Bard")


    def set_active_role(self, role_string):
        self.active_role = role_string

    def set_trinket(self, trinket_tuple_string_integer):
        # Each cat can hold one trinket, which modifies one stat. The trinket is represented as a tuple (stat_string, modifier_integer)
        self.trinket = trinket_tuple_string_integer

    def create_adventure_dice(self):
        statstodice = { 0: 1,  1: 1,  2: 1,  3: 1,  4: 1,  5: 1,  6: 1,  7: 2,  8: 2,  9: 2, 10: 2,
                        11: 2, 12: 2, 13: 3, 14: 3, 15: 3, 16: 3, 17: 4, 18: 4, 19: 4, 20: 4, 21: 5,
                        22: 5, 23: 5, 24: 5, 25: 6, 26: 6, 27: 6, 28: 6, 29: 7, 30: 7, 31: 7, 32: 7,
                        33: 8, 34: 8, 35: 8, 36: 8, 37: 9, 38: 9, 39: 9, 40: 9}
        