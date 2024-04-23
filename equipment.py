import time
import random
import hashlib
import random
import pickle
import os
import pygame
from class_define import Weapon, Armor, Jewelry

#pygame.init()

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




    
# 将数据保存到文件中
def save_items_to_file(filename, items):
    directory = 'data'
    if filename == "weapons.pkl" or filename == "armors.pkl" or filename == "jewelrys.pkl":
        for i in items:
            i.img = None
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
    items = []
    directory = 'data'
    file = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 如果文件存在则加载数据
    if os.path.exists(file):
        with open(file, 'rb') as f:
            items = pickle.load(f)
        print(f"Items loaded from {filename}.")
        return items
    # 如果文件不存在则创建一个新文件
    else:
        print(f"File {filename} does not exist. Creating a new file.")
        with open(file, 'wb') as f:
            pickle.dump(items, f)
        print(f"New file {file} created.")
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
    global weapon_hash
    for i in weapon_hash:
        print(i)
    print("\n")

#武器排序以及保存
def sort_weapon():
    global weapons
    weapons.sort(key=lambda x: x.damage, reverse=True)
    for i in weapons:
        i.img = None
    # 将 weapons 列表保存到文件中
    with open(os.path.join('data', 'weapons.pkl'), 'wb') as f:
        pickle.dump(weapons, f)
    weapons = load_items_from_file("weapons.pkl")

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
    save_items_to_file("weapon_hash.pkl",weapon_hash)
    weapon_hash = load_items_from_file("weapon_hash.pkl")
    
    

#删除武器
def delete_weapon(position_id):
    global weapons
    global weapon_hash
    id_to_remove = get_weapon_id(position_id)
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
    global armors
    armors.sort(key=lambda x: x.defense, reverse=True)
    for i in armors:
        i.img = None
    # 将 armors 列表保存到文件中
    with open(os.path.join('data', 'armors.pkl'), 'wb') as f:
        pickle.dump(armors, f)
    armors = load_items_from_file("armors.pkl")

# 打印防具列表
def generate_armor(i, luck):
    global armor_hash
    id = generate_unique_id(armor_name[i])
    for id in armor_hash:
        if id == id:
            id = generate_unique_id(armor_name[i])
    armors.append(Armor(id, armor_name[i], armor_random_rate(i, luck), armor_attribute[i]))
    sort_armor()
    armor_hash.append(id)
    save_items_to_file("armor_hash.pkl", armor_hash)
    armor_hash = load_items_from_file("armor_hash.pkl")

# 根据位置获取防具的ID
def get_armor_id(position_id):
    if len(armors) > position_id:
        return str(armors[position_id].id)
    else:
        print("Error: The position_id is out of range.")
        return None
    
# 删除防具
def delete_armor(position_id):
    global armors
    global armor_hash
    id_to_remove = get_armor_id(position_id)
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
    
# 打印防具ID列表
def print_armor_hash():
    for i in armor_hash:
        print(i)
    print("\n")

# 定义防具类

jewelry_name = ["God_ring","God_necklace","God_belt","God_cloak","God_bracelet","God_earring"]
jewelry_hp =            [10,10,10,10,10,10]
jewelry_intelligence =  [10,10,10,10,10,10]
jewelry_strength =      [10,10,10,10,10,10]
jewelry_speed =         [10,10,10,10,10,10]
jewelry_luck =          [10,10,10,10,10,10]
jewelry_defense =       [10,10,10,10,10,10]



    


# 首饰排序以及保存
def sort_jewelry():
    global jewelrys
    jewelrys.sort(key=lambda x: x.hp, reverse=True)
    # 将 jewelrys 类的图像清除后保存
    for i in jewelrys:
        i.img = None
    # 将 jewelrys 列表保存到文件中
    with open(os.path.join('data', 'jewelrys.pkl'), 'wb') as f:
        pickle.dump(jewelrys, f)
    jewelrys = load_items_from_file("jewelrys.pkl")

# 生成首饰    
def generate_jewelry(i, luck):
    global jewelry_hash
    if random.randint(0, 1000) <= luck:
        id = generate_unique_id(jewelry_name[i])
        for id in jewelry_hash:
            if id == id:
                id = generate_unique_id(jewelry_name[i])
        jewelrys.append(Jewelry(id, jewelry_name[i], jewelry_hp[i], jewelry_intelligence[i], jewelry_strength[i], jewelry_speed[i], jewelry_luck[i], jewelry_defense[i]))
        sort_jewelry()
        jewelry_hash.append(id)
        temp = jewelry_hash
        save_items_to_file("jewelry_hash.pkl", temp)

# 根据位置获取首饰的ID
def get_jewelry_id(position_id):
    if len(jewelrys) > position_id:
        return str(jewelrys[position_id].id)
    else:
        print("Error: The position_id is out of range.")
        return None
    
# 删除首饰
def delete_jewelry(position_id):
    global jewelrys
    global jewelry_hash
    id_to_remove = get_jewelry_id(position_id)
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

# 打印首饰ID列表
def print_jewelry_hash():
    for i in jewelry_hash:
        print(i)
    print("\n")

def w_id_to_position_id(id):
    if id == None:
        return None
    for i in range(len(weapons)):
        if weapons[i].id == id:
            return i
    return None

def a_id_to_position_id(id):
    if id == None:
        return None
    for i in range(len(armors)):
        if armors[i].id == id:
            return i
    return None

def j_id_to_position_id(id):
    if id == None:
        return None
    for i in range(len(jewelrys)):
        if jewelrys[i].id == id:
            return i
    return None


"""
#武器测试

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

"""
# 从文件中加载数据
def load_items_from_file(filename):
    items = []
    directory = 'data'
    file = os.path.join(directory, filename)
    # 如果文件夹不存在则创建文件夹
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 如果文件存在则加载数据
    if os.path.exists(file):
        with open(file, 'rb') as f:
            items = pickle.load(f)
        print(f"Items loaded from {filename}.")
        return items
    # 如果文件不存在则创建一个新文件
    else:
        print(f"File {filename} does not exist. Creating a new file.")
        with open(filename, 'wb') as f:
            pickle.dump(items, f)
        print(f"New file {filename} created.")
        return items
"""

weapons =       load_items_from_file("weapons.pkl")
weapon_hash =   load_items_from_file("weapon_hash.pkl")
armors =        load_items_from_file("armors.pkl")
armor_hash =    load_items_from_file("armor_hash.pkl")
jewelrys =      load_items_from_file("jewelrys.pkl")
jewelry_hash =  load_items_from_file("jewelry_hash.pkl")

"""
generate_weapon(0, 10)
generate_weapon(0, 10)
generate_weapon(0, 10)
generate_weapon(0, 10)


print("weapons:\n")
print_weapons()
print("weapons Hash:\n")
print_weapon_hash()
"""


"""
print("Armors:")
print_armors()
print("Armors Hash:\n")
print_armor_hash()
print("Jewelrys:\n")
print_jewelrys()
print("Jewelrys Hash:\n")
print_jewelry_hash()
"""

"""
#显示函数测试

screen = pygame.display.set_mode((1280, 800))
def print_img(surface, print_page):
    page = 0
    items_per_page = 24  # 每页的物品数量
    items_per_row = 6  # 每行的物品数量
    start_index = items_per_page * page  # 开始的索引
    end_index = start_index + items_per_page  # 结束的索引

    if print_page == 0:
        img_list = weapons[start_index:end_index]  # 获取当前页的物品
    elif print_page == 1:
        img_list = armors[start_index:end_index]
    elif print_page == 2:
        img_list = jewelrys[start_index:end_index]
    else:
        print_page = 0
        

    x = 100  # 初始x坐标
    y = 100  # 初始y坐标
    count = 0  # 当前行的物品数量
    for item in img_list:
        img = item.get_img()  # 获取物品图片
        surface.blit(img, (x, y))  # 将图片绘制到surface上
        x += img.get_width() + 10  # 更新x坐标以便下一个图片不会覆盖当前图片
        count += 1  # 更新当前行的物品数量
        if count == items_per_row:  # 如果当前行的物品数量达到了6，就换行
            x = 100  # 重置x坐标
            y += img.get_height() + 10  # 更新y坐标以便下一个图片在新的一行
            count = 0  # 重置当前行的物品数量

running = True
while running:
    for event in pygame.event.get():
        mx,my = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        screen.fill((255, 255, 255))
        print_img(screen, 0)
        pygame.display.flip()


"""



save_items_to_file("weapons.pkl", weapons)
save_items_to_file("weapon_hash.pkl", weapon_hash)
save_items_to_file("armors.pkl", armors)
save_items_to_file("armor_hash.pkl", armor_hash)
save_items_to_file("jewelrys.pkl", jewelrys)
save_items_to_file("jewelry_hash.pkl", jewelry_hash)

