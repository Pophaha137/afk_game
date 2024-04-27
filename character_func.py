import os
import pygame
import pickle
from character import *
from lib import *
# 怪物各项属性

#测试部分
# 保存player数据


def load_player():
    with open('data/player.pkl', 'rb') as input:
        player = pickle.load(input)
        return player

def check_player():
    # 确保data文件夹存在，否则创建
    if not os.path.exists('data'):
        os.makedirs('data')
    # 确保player.pkl存在，否则创建
    if not os.path.exists('data/player.pkl'):
        with open('data/player.pkl', 'wb') as output:
            player = character(1, 0, 100, 10, 10, 10, 10, 10, 0, 0)
            pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)
    else:
        player = load_player()

def save_player():
    with open('data/player.pkl', 'wb') as output:
        pickle.dump(player, output, pickle.HIGHEST_PROTOCOL)


check_player()
player = load_player()

"""
#武器测试
generate_weapon(0, player.show_luck())
print_weapons()
print_weapon_hash()
player.weapon_on(weapons[0])
player.show()
#player.weapon_off()
#player.show()

#防具测试
generate_armor(0,player.show_luck())
print_armors()
print_armor_hash()
player.armor_on(armors[0])
player.show()
#player.armor_off()
#player.show()

#珠宝测试
generate_jewelry(0,player.show_luck())
print_jewelrys()
print_jewelry_hash()
if len(jewelrys) != 0:
    player.jewelry_on(jewelrys[0])
player.show()
#player.jewelry_off()
#player.show()

player.show()
"""


"""
#删除测试
delete_weapon(0)
delete_armor(0)
delete_jewelry(0)
print("After delete:\n")
print("Weapons:\n")
print_weapons()
print("Weapons Hash:\n")
print_weapon_hash()
print("Armors:")
print_armors()
print("Armors Hash:\n")
print_armor_hash()
print("Jewelrys:\n")
print_jewelrys()
print("Jewelrys Hash:\n")
print_jewelry_hash()
"""

#plyaer.show()


generate_enemy(0, 1)
generate_enemy(1, 2)
generate_enemy(2, 3)
generate_enemy(3, 3)
generate_enemy(4, 3)


fight(player, enemy[0])
fight(player, enemy[0])
fight(player, enemy[0])
fight(player, enemy[0])
fight(player, enemy[0])

player.show_all()
save_player()