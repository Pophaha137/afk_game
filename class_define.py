import pygame
# 定义武器类
class Weapon:
    def __init__(self, id, name, damage, attribute, type, critical_damage_percentage):
        self.id = id
        self.name = name
        self.damage = damage
        self.attribute = attribute
        self.type = type
        self.critical_damage_percentage = critical_damage_percentage
        self.percentage = 0
        self.img = self.get_img()

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.damage:.2f} {self.attribute} damage, {self.critical_damage_percentage:.1f}% critical damage"
    
    def weapon_damage(self):
        return self.damage
    
    def weapon_attribute(self):
        return self.attribute
    
    def weapon_type(self):
        return self.type

    def weapon_critical_damage_percentage(self):
        return self.critical_damage_percentage

    def get_img(self):
        img = pygame.image.load(f"./resource/weapon/{self.name}.png")
        img = pygame.transform.scale(img, (89, 91))
        return img
    
    def to_dict(self):
        return {
            "Name": f"{self.name}",
            "Damage": f"{self.damage:.2f}",
            "Attribute": f"{self.attribute}",
            "Type": f"{self.type}",
            "Critical Damage Percentage": f"{self.critical_damage_percentage}"
        }
    
class Armor:
    def __init__(self, id, name, defense, attribute):
        self.id = id
        self.name = name
        self.defense = defense
        self.attribute = attribute
        self.img = self.get_img()

    def __str__(self):
        return f"{self.name} - {self.defense:.2f} {self.attribute} defense"
    
    def armor_defense(self):
        return self.defense
    
    def armor_attribute(self):
        return self.attribute
    
    def get_img(self):
        img = pygame.image.load(f"./resource/armor/{self.name}.png")
        img = pygame.transform.scale(img, (89, 91))
        return img

    def to_dict(self):
        return {
            "Name": f"{self.name}",
            "Defense": f"{self.defense:.2f}",
            "Attribute": f"{self.attribute}"
        }
    
class Jewelry:
    def __init__(self, id, name, hp, intelligence, strength, speed, luck, defense):
        self.id = id
        self.name = name
        self.hp = hp
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.luck = luck
        self.defense = defense
        self.img = self.get_img()

    def __str__(self):
        return f"{self.name} - {self.hp:.2f} hp, {self.intelligence:.2f} intelligence, {self.strength:.2f} strength, {self.speed:.2f} speed, {self.luck:.2f} luck, {self.defense:.2f} defense"
    
    def jewelry_hp(self):
        return self.hp
    
    def jewelry_intelligence(self):
        return self.intelligence
    
    def jewelry_strength(self):
        return self.strength
    
    def jewelry_speed(self):
        return self.speed
    
    def jewelry_luck(self):
        return self.luck
    
    def jewelry_defense(self):
        return self.defense
    
    def get_img(self):
        img = pygame.image.load(f"./resource/jewelry/{self.name}.png")
        img = pygame.transform.scale(img, (89, 91))
        return img
    
    def to_dict(self):
        return {
            "Name": f"{self.name}",
            "Hp": f"{self.hp}",
            "Intelligence": f"{self.intelligence}",
            "Strength": f"{self.strength}",
            "Speed": f"{self.speed}",
            "Luck": f"{self.luck}",
            "Defense": f"{self.defense}"
        }
    


class Items:
    def __init__(self, id, name, number = 0):
        self.name = name
        self.id = id
        self.number = number
        self.img = self.get_img()
    
    def get_img(self):
        img = pygame.image.load(f"./resource/item/{self.name}.png")
        img = pygame.transform.scale(img, (90, 107))
        return img
    
    def to_dict(self):
        return {
            "Name": f"{self.name}",
            "Number": f"{self.number}"
        }
    
    def add_item(self, number):
        self.number += number

    def reduce_item(self, number):
        if self.number >= number:
            self.number -= number
        else:
            return False
        
    def __str__(self):
        return f"{self.name} - {self.number}"
    
    def show_number(self):
        return self.number