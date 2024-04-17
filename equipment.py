import time
import random
import hashlib
import random
import pickle
import os

#武器数据
sword_name = ["God_bless","God_curse","God_sword","God_axe","God_bow","God_staff","God_wand","God_knife","God_spear","God_shield"]
sword_base_damage = [10,10,10,10,10,10,10,10,10,10]
sword_attribute = ["light","dark","light","dark","light","dark","light","dark","light","dark"]
sword_critical_damage_percentage = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]

def generate_unique_id(name):
        """
        生成一个基于当前时间、物品名称和随机数的独一无二的ID。
        使用SHA1哈希算法来确保ID的唯一性。
        """
        unique_string = f"{name}_{time.time()}_{random.randint(1, 10000)}"
        unique_id = hashlib.sha1(unique_string.encode()).hexdigest()
        return unique_id


# 生成随机攻击数值
def weapon_random_rate(i, luck):
    base = sword_base_damage[i]
    rate = random.randint(luck, 100+luck)/100
    return base * rate 

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



# 将数据保存到文件中
def save_items_to_file(filename, items):
    directory = 'data'
    file = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 将数据保存到文件中
    with open(file, 'wb') as f:
        pickle.dump(items, f)
    print(f"Items saved to {file}.")
    items = load_items_from_file(filename)


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


# 遍历weapons列表，打印每个物品的信息
def print_weapons():
    for i in weapons:
        print(i)
    print("\n")


# 根据位置获取武器的ID
def get_weapon_id(position_id):
    if len(weapons) > position_id:
        return str(weapons[position_id].id)
    else:
        print("Error: The position_id is out of range.")
        return None

def print_weapon_hash():
    for i in weapon_hash:
        print(i)
    print("\n")

#武器排序以及保存
def sort_weapon():
    weapons.sort(key=lambda x: x.damage, reverse=True)
    # 将 weapons 列表保存到文件中
    with open(os.path.join('data', 'weapons.pkl'), 'wb') as f:
        pickle.dump(weapons, f)

# 生成武器
def generate_weapon(i, luck):
    global weapon_hash
    id = generate_unique_id(sword_name[i])
    for id in weapon_hash:
        if id == id:
            id = generate_unique_id(sword_name[i])
    weapons.append(Weapon(id, sword_name[i], weapon_random_rate(i, luck), sword_attribute[i], "sword", sword_critical_damage_percentage[i]))
    sort_weapon()
    weapon_hash.append(id)
    save_items_to_file("weapon_hash.pkl", weapon_hash)
    weapon_hash = load_items_from_file("weapon_hash.pkl")

#删除武器
def delete_weapon(id_to_remove):
    global weapons
    global weapon_hash
    if id_to_remove != None:
        print(f"Removing weapon with ID {id_to_remove}...")
        weapons = [weapon for weapon in weapons if weapon.id != id_to_remove]
        weapon_hash = [id for id in weapon_hash if id != id_to_remove]
        save_items_to_file("weapon_hash.pkl", weapon_hash)
        weapon_hash = load_items_from_file("weapon_hash.pkl")
        sort_weapon()

# 测试    
weapons = load_items_from_file("weapons.pkl")
weapon_hash = load_items_from_file("weapon_hash.pkl")


#generate_weapon(0, 10)
delete_weapon(get_weapon_id(0))
print_weapons()
print_weapon_hash()



save_items_to_file("weapons.pkl", weapons)
save_items_to_file("weapon_hash.pkl", weapon_hash)