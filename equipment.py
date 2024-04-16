import time
import random
import hashlib
import random
import pickle
import os

sword_name = ["God_bless","God_curse","God_sword","God_axe","God_bow","God_staff","God_wand","God_knife","God_spear","God_shield"]
sword_base_damage = [10,10,10,10,10,10,10,10,10,10]
sword_attribute = ["light","dark","light","dark","light","dark","light","dark","light","dark"]
sword_critical_damage_percentage = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]

# 生成随机攻击数值
def weapon_random_rate(i, luck):
    base = sword_base_damage[i]
    rate = random.randint(luck, 100+luck)/100
    return base * rate 

# 将数据保存到文件中
def save_items_to_file(filename, items):
    directory = 'data'
    filename = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 将数据保存到文件中
    with open(filename, 'wb') as f:
        pickle.dump(items, f)
    print(f"Items saved to {filename}.")

# 从文件中加载数据
def load_items_from_file(filename):
    directory = 'data'
    filename = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 如果文件存在则加载数据
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            items = pickle.load(f)
        print(f"Items loaded from {filename}.")
        return items
    # 如果文件不存在则创建一个新文件
    else:
        print(f"File {filename} does not exist. Creating a new file.")
        items = []
        with open(filename, 'wb') as f:
            pickle.dump(items, f)
        print(f"New file {filename} created.")
        return items

# 遍历inventory的items字典，打印每个物品的信息
def print_weapons_hash():
    for id in weapon_hash.items:
        print(weapon_hash.get_item(id))
    print("\n")

# 遍历weapons列表，打印每个物品的信息
def print_weapons():
    for i in weapons:
        print(i)
    print("\n")

def get_weapon_id(position_id):
    if len(weapons) > position_id:
        return weapons[position_id].id
    else:
        print("Error: The position_id is out of range.")
        return None

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

# 定义库存类，用于管理物品
class Inventory:
    def __init__(self):
        self.items = {}  # 用字典作为哈希表存储物品

    def generate_unique_id(self, name):
        """
        生成一个基于当前时间、物品名称和随机数的独一无二的ID。
        使用SHA1哈希算法来确保ID的唯一性。
        """
        unique_string = f"{name}_{time.time()}_{random.randint(1, 10000)}"
        unique_id = hashlib.sha1(unique_string.encode()).hexdigest()
        return unique_id

    def add_item(self, weapon_type_id, luck):
        # 生成物品的ID并添加到库存
        id = self.generate_unique_id(sword_name[weapon_type_id])
        if id not in self.items:
            damage = weapon_random_rate(weapon_type_id, luck)
            self.items[id] = Weapon(id, sword_name[weapon_type_id], damage, sword_attribute[weapon_type_id], "sword", sword_critical_damage_percentage[weapon_type_id])
            weapons.append(self.items[id])
            print(f"Item {sword_name[weapon_type_id]} with ID {id} added.")
        else:
            print(f"Item ID {id} already exists.")
        save_items_to_file("weapon_hash.pkl", weapon_hash)

    def remove_item(self, id):
        # 根据ID移除物品
        if id in self.items:
            del self.items[id]
            print(f"Item ID {id} removed.")
        else:
            print(f"Item ID {id} not found.")
        save_items_to_file("weapon_hash.pkl", weapon_hash)

    def get_item(self, id):
        # 根据ID获取物品
        return self.items.get(id, None)

    def update_item(self, id, **kwargs):
        """
        根据ID更新物品的信息。
        kwargs 可用于传递希望更新的属性值，如名称或描述。
        """
        weapon = self.get_item(id)
        if weapon:
            weapon.name = kwargs.get('name', weapon.name)
            weapon.damage = kwargs.get('damage', weapon.damage)
            weapon.attribute = kwargs.get('attribute', weapon.attribute)
            weapon.type = kwargs.get('type', weapon.type)
            weapon.critical_damage_percentage = kwargs.get('critical_damage_percentage', weapon.critical_damage_percentage)
            print(f"Item ID {id} updated.")
        else:
            print(f"Item ID {id} not found.")

    


#武器排序以及保存
def sort_weapon():
    weapons.sort(key=lambda x: x.damage, reverse=True)
    # 将 weapons 列表保存到文件中
    with open(os.path.join('data', 'weapons.pkl'), 'wb') as f:
        pickle.dump(weapons, f)

# 生成武器
def generate_weapon(i, luck):
    weapon_hash = load_items_from_file("weapon_hash.pkl")
    weapon_hash.add_item(i, luck)
    save_items_to_file("weapon_hash.pkl", weapon_hash)
    sort_weapon()

#删除武器
def delete_weapon(id_to_remove):
    global weapons
    if id_to_remove != None:
        weapon_hash = load_items_from_file("weapon_hash.pkl")
        weapons = [weapon for weapon in weapons if weapon.id != id_to_remove]
        weapon_hash.remove_item(id_to_remove)
        sort_weapon()
        save_items_to_file("weapon_hash.pkl", weapon_hash)
        save_items_to_file("weapons.pkl", weapons)
    
# 测试    
weapons = load_items_from_file("weapons.pkl")
print_weapons()
weapon_hash = Inventory()
weappon_hash = load_items_from_file("weapon_hash.pkl")

generate_weapon(0, 10)
print_weapons()
#delete_weapon(get_weapon_id(0))

save_items_to_file("weapons.pkl", weapons)
save_items_to_file("weapon_hash.pkl", weapon_hash)