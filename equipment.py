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


# 打印武器ID列表
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

armor_name = ["God_armor","God_helmet","God_gloves","God_boots","God_ring","God_necklace","God_belt","God_cloak","God_bracelet","God_earring"]
armor_base_defense = [10,10,10,10,10,10,10,10,10,10]
armor_attribute = ["light","dark","light","dark","light","dark","light","dark","light","dark"]

# 生成随机防御数值
def armor_random_rate(i, luck):
    base = armor_base_defense[i]
    rate = random.randint(luck, 100+luck)/100
    return base * rate

# 防具排序以及保存
def sort_armor():
    armors.sort(key=lambda x: x.defense, reverse=True)
    # 将 armors 列表保存到文件中
    with open(os.path.join('data', 'armors.pkl'), 'wb') as f:
        pickle.dump(armors, f)

# 打印防具列表
def generate_armor(i, luck):
    global armor_hash
    id = generate_unique_id(armor_name[i])
    for id in armor_hash:
        if id == id:
            id = generate_unique_id(armor_name[i])
    armors.append(armor(id, armor_name[i], armor_random_rate(i, luck), armor_attribute[i]))
    sort_armor()
    armor_hash.append(id)
    save_items_to_file("armor_hash.pkl", armor_hash)
    armor_hash = load_items_from_file("armor_hash.pkl")

# 删除防具
def delete_armor(id_to_remove):
    global armors
    global armor_hash
    if id_to_remove != None:
        print(f"Removing armor with ID {id_to_remove}...")
        armors = [armor for armor in armors if armor.id != id_to_remove]
        armor_hash = [id for id in armor_hash if id != id_to_remove]
        save_items_to_file("armor_hash.pkl", armor_hash)
        armor_hash = load_items_from_file("armor_hash.pkl")
        sort_armor()

# 打印防具列表
def print_armors():
    for i in armors:
        print(i)
    print("\n")

# 根据位置获取防具的ID
def get_armor_id(position_id):
    if len(armors) > position_id:
        return str(armors[position_id].id)
    else:
        print("Error: The position_id is out of range.")
        return None
    
# 打印防具ID列表
def print_armor_hash():
    for i in armor_hash:
        print(i)
    print("\n")

# 定义防具类
class armor:
    def __init__(self, id, name, defense, attribute):
        self.id = id
        self.name = name
        self.defense = defense
        self.attribute = attribute

    def __str__(self):
        return f"{self.name} - {self.defense:.2f} {self.attribute} defense"
    
    def armor_defense(self):
        return self.defense
    
    def armor_attribute(self):
        return self.attribute

jewelry_name = ["God_ring","God_necklace","God_belt","God_cloak","God_bracelet","God_earring"]
jewelry_hp =            [10,10,10,10,10,10]
jewelry_intelligence =  [10,10,10,10,10,10]
jewelry_strength =      [10,10,10,10,10,10]
jewelry_speed =         [10,10,10,10,10,10]
jewelry_luck =          [10,10,10,10,10,10]
jewelry_defense =       [10,10,10,10,10,10]


class jewelry:
    def __init__(self, id, name, hp, intelligence, strength, speed, luck, defense):
        self.id = id
        self.name = name
        self.hp = hp
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.luck = luck
        self.defense = defense

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
    


# 首饰排序以及保存
def sort_jewelry():
    jewelrys.sort(key=lambda x: x.hp, reverse=True)
    # 将 jewelrys 列表保存到文件中
    with open(os.path.join('data', 'jewelrys.pkl'), 'wb') as f:
        pickle.dump(jewelrys, f)


# 生成首饰    
def generate_jewelry(i, luck):
    global jewelry_hash
    if random.randint(0, 1000) <= luck:
        id = generate_unique_id(jewelry_name[i])
        for id in jewelry_hash:
            if id == id:
                id = generate_unique_id(jewelry_name[i])
        jewelrys.append(jewelry(id, jewelry_name[i], jewelry_hp[i], jewelry_intelligence[i], jewelry_strength[i], jewelry_speed[i], jewelry_luck[i], jewelry_defense[i]))
        sort_jewelry()
        jewelry_hash.append(id)
        save_items_to_file("jewelry_hash.pkl", jewelry_hash)
        jewelry_hash = load_items_from_file("jewelry_hash.pkl")


# 删除首饰
def delete_jewelry(id_to_remove):
    global jewelrys
    global jewelry_hash
    if id_to_remove != None:
        print(f"Removing jewelry with ID {id_to_remove}...")
        jewelrys = [jewelry for jewelry in jewelrys if jewelry.id != id_to_remove]
        jewelry_hash = [id for id in jewelry_hash if id != id_to_remove]
        save_items_to_file("jewelry_hash.pkl", jewelry_hash)
        jewelry_hash = load_items_from_file("jewelry_hash.pkl")
        sort_jewelry()


# 打印首饰列表
def print_jewelrys():
    for i in jewelrys:
        print(i)
    print("\n")


# 根据位置获取首饰的ID
def get_jewelry_id(position_id):
    if len(jewelrys) > position_id:
        return str(jewelrys[position_id].id)
    else:
        print("Error: The position_id is out of range.")
        return None
    

# 打印首饰ID列表
def print_jewelry_hash():
    for i in jewelry_hash:
        print(i)
    print("\n")


    

# 从文件中加载数据    


#武器测试
"""
generate_weapon(0, 10)
#delete_weapon(get_weapon_id(0))
print_weapons()
print_weapon_hash()


#防具测试

generate_armor(0, 10)
#delete_armor(get_armor_id(0))
print_armors()
print_armor_hash()


#首饰测试

generate_jewelry(0, 10)
#delete_jewelry(get_jewelry_id(0))
print_jewelrys()
print_jewelry_hash()

"""

weapons = load_items_from_file("weapons.pkl")
weapon_hash = load_items_from_file("weapon_hash.pkl")
armors = load_items_from_file("armors.pkl")
armor_hash = load_items_from_file("armor_hash.pkl")
jewelrys = load_items_from_file("jewelrys.pkl")
jewelry_hash = load_items_from_file("jewelry_hash.pkl")

save_items_to_file("weapons.pkl", weapons)
save_items_to_file("weapon_hash.pkl", weapon_hash)
save_items_to_file("armors.pkl", armors)
save_items_to_file("armor_hash.pkl", armor_hash)
save_items_to_file("jewelrys.pkl", jewelrys)
save_items_to_file("jewelry_hash.pkl", jewelry_hash)
