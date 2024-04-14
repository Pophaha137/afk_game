import random
import pickle
import os

sword_name = ["God_bless","God_curse","God_sword","God_axe","God_bow","God_staff","God_wand","God_knife","God_spear","God_shield"]
sword_base_damage = [10,10,10,10,10,10,10,10,10,10]
sword_attribute = ["light","dark","light","dark","light","dark","light","dark","light","dark"]
sword_critical_damage_percentage = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]

weapons = []

# 生成随机攻击数值
def weapon_random_rate(i, luck):
    base = sword_base_damage[i]
    rate = random.randint(luck, 100+luck)/100
    return base * rate 

#武器排序以及保存
def sort_weapon():
    weapons.sort(key=lambda x: x.damage, reverse=True)
    # 将 weapons 列表保存到文件中
    with open(os.path.join('data', 'weapons.pkl'), 'wb') as f:
        pickle.dump(weapons, f)

# 生成武器
def generate_weapon(i, luck):
    name = sword_name[i]
    damage = weapon_random_rate(i, luck)
    attribute = sword_attribute[i]
    type = "sword"
    critical_damage_percentage = sword_critical_damage_percentage[i]
    weapon = Weapon(name, damage, attribute, type, critical_damage_percentage)
    weapons.append(weapon)
    # 将 weapons 列表保存到文件中
    sort_weapon()

#删除武器
def delete_weapon(i):
    weapons.pop(i)
    # 将 weapons 列表保存到文件中
    sort_weapon()




class Weapon:
    def __init__(self, name, damage, attribute, type, critical_damage_percentage):
        self.name = name
        self.damage = damage
        self.attribute = attribute
        self.type = type
        self.critical_damage_percentage = critical_damage_percentage
        self.percentage = 0

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

    
    
def load_weapons():
    # 检查文件是否存在，如果存在则加载，否则生成新的武器
    if os.path.exists(os.path.join('data', 'weapons.pkl')):
        # 从文件中加载 weapons 列表
        with open(os.path.join('data', 'weapons.pkl'), 'rb') as f:
            weapons = pickle.load(f)

generate_weapon(1,10)
generate_weapon(2,10)

# 打印 weapons 列表中的所有武器
def show_weapon():
    for i in weapons:
        print(i)