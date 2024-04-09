class jewelry:
    def __init__(self, hp_rate = 1, intelligence_rate = 1, strength_rate = 1, defense_rate = 1, speed_rate = 1, luck_rate = 1):
        self.hp_rate = hp_rate
        self.intelligence_rate = intelligence_rate
        self.strength_rate = strength_rate
        self.defense_rate = defense_rate
        self.speed_rate = speed_rate
        self.luck_rate = luck_rate

    def rate(self):
        return [self.hp_rate, self.intelligence_rate, self.strength_rate, self.defense_rate, self.speed_rate, self.luck_rate]
        