import random

class character:
    def __init__(self, HP, Intelligence, Strength, Defense, Speed, Luck, x, y, Jewelry = None, Weapon = None ):
        self.hp = HP
        self.intelligence = Intelligence
        self.strength = Strength
        self.defense = Defense
        self.speed = Speed
        self.luck = Luck
        self.x = x
        self.y = y
        self.jewelry = Jewelry
        self.damage_type = None
        self.attack_hurt = None
       
        if Weapon != None:
            self.weapon_damage = Weapon.damage
            self.weapon_attribute = Weapon.attribute
            self.weapon_type = Weapon.type
            self.critical_damage_percentage = Weapon.critical_damage_percentage
        else:
            self.weapon_damage = 0
            self.weapon_attribute = None
            self.weapon_type = None
            self.critical_damage_percentage = 1.2

    
    def damage_type_func(self):
        if self.weapon_type == "close combat":
            return "physical"
        elif self.weapon_type == "long-range attack":
            return "physical"
        elif self.weapon_type == "magic":
            return "magical"
        else:
            return "physical"
        
    def attack_hurt_func(self):
        if self.damage_type == "magical":
            return self.intelligence + self.weapon_damage
        else:
            return self.strength + self.weapon_damage
        
    def critical_damage(self): 
        if random.randint(1, 100) >= self.luck:
            # 暴击发生，伤害值增加
            return self.attack_hurt * self.critical_damage_percentage
        else:
            # 未发生暴击，返回基础伤害
            return self.attack_hurt
        

