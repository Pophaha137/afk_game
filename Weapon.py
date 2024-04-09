class Weapon:
    def __init__(self, name, damage, attribute, type, critical_damage_percentage):
        self.name = name
        self.damage = damage
        self.attribute = attribute
        self.type = type
        self.critical_damage_percentage = critical_damage_percentage

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.damage} {self.attribute} damage, {self.critical_damage_percentage}% critical damage"