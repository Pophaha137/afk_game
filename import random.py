import random

class enemy:
    def __init__(self, name, level, hp, intelligence, strength, luck, speed, defense, exp, damage_type , attribute = None):
        self.name = name
        self.level = level
        self.hp = hp
        self.intelligence = intelligence
        self.strength = strength
        self.luck = luck
        self.speed = speed
        self.defense = defense
        self.attribute = attribute
        self.damage_type = damage_type
        self.exp = exp
        self.critical_damage_percentage = 1.2
        self.base_damage = self.base_damage_func()

    #伤害类型判断
    def damage_type_func(self):
        if self.damage_type == "magical":
            return self.intelligence
        else:
            return self.strength

    #暴击伤害判断    
    def critical_damage(self): 
        if random.randint(1, 100) >= self.luck:
            # 暴击发生，伤害值增加
            return self.base_damage * self.critical_damage_percentage
        else:
            # 未发生暴击，返回基础伤害
            return self.base_damage
        
    #伤害计算
    def damage(self):
        if self.damage_type == "magical":
            return [self.critical_damage(),self.attribute]
        else:
            return [self.critical_damage(),None]
        
