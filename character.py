import random
from jewelry import jewelry
from Weapon import *




class character:
    def __init__(self, Lv, Exp, HP, Intelligence, Strength, Defense, Speed, Luck, x, y, Jewelry=None, Weapon=None, Armor=None):
        self.lv = Lv
        self.exp = Exp
        self.exp_needed = 10 * 1.1 ** self.lv
        self.hp = HP
        self.intelligence = Intelligence
        self.strength = Strength
        self.defense = Defense
        self.speed = Speed
        self.luck = Luck
        self.critical_damage_percentage = 1.2
        self.x = x
        self.y = y
        self.jewelry = None
        
        self.weapon_critical_damage_percentage = 0
        

        #武器属性
        if Weapon != None:
            self.weapon = Weapon
            self.weapon_damage = self.weapon.damage
            self.weapon_attribute = self.weapon.attribute
            self.weapon_type = self.weapon.type
            self.weapon_critical_damage_percentage = self.weapon.critical_damage_percentage
        else:
            self.weapon_damage = 0
            self.weapon_attribute = None
            self.weapon_type = None
            self.weapon_critical_damage_percentage = 1.2

        #防具属性
        if Armor != None:
            self.armor_defense = Armor.defense
            self.armor_attribute = Armor.attribute
        else:
            self.armor_defense = 0
            self.armor_attribute = None

        #珠宝属性
        if Jewelry != None:
            self.jewelry_hp = Jewelry.hp
            self.jewelry_intelligence = Jewelry.intelligence
            self.jewelry_strength = Jewelry.strength
            self.jewelry_defense = Jewelry.defense
            self.jewelry_speed = Jewelry.speed
            self.jewelry_luck = Jewelry.luck
        else:
            self.jewelry_hp = 0
            self.jewelry_intelligence = 0
            self.jewelry_strength = 0
            self.jewelry_defense = 0
            self.jewelry_speed = 0
            self.jewelry_luck = 0

        #战斗属性
        self.temp_hp = self.hp + self.jewelry_hp
        self.temp_strength = self.strength + self.jewelry_strength
        self.temp_intelligence = self.intelligence + self.jewelry_intelligence
        self.temp_defense = self.defense + self.armor_defense + self.jewelry_defense
        self.temp_speed = self.speed + self.jewelry_speed
        self.temp_luck = self.luck + self.jewelry_luck

        self.damage_type = self.damage_type_func()
        self.base_damage = self.base_damage_func()
        
        

    # 战斗属性更新
    def temp_refresh(self):
        self.temp_hp = self.hp + self.jewelry_hp
        self.temp_strength = self.strength + self.jewelry_strength
        self.temp_intelligence = self.intelligence + self.jewelry_intelligence
        self.temp_defense = self.defense + self.armor_defense + self.jewelry_defense
        self.temp_speed = self.speed + self.jewelry_speed
        self.temp_luck = self.luck + self.jewelry_luck


    # 养成类
    # 血量增加
    def hp_add(self):
        self.hp += 10
        self.temp_refresh()

    # 力量增加
    def strength_add(self):
        self.strength += 1
        self.temp_refresh()

    # 智力增加
    def intelligence_add(self):
        self.intelligence += 1
        self.temp_refresh()

    # 防御增加
    def defense_add(self):
        self.defense += 1
        self.temp_refresh()

    # 速度增加
    def speed_add(self):
        self.speed += 1
        self.temp_refresh()

    # 升级奖励函数
    def lv_up_reward(self):
        self.hp_add()
        self.intelligence_add()
        self.strength_add()
        self.defense_add()
        self.speed_add()
        self.luck += 1
        self.temp_refresh()
        
    # 升级函数
    def level_update(self):
        if self.exp >= self.exp_needed:
            self.lv += 1
            self.exp -= self.exp_needed
            self.exp_needed = 10 ^ self.lv
            # 升级加点
            self.lv_up_reward()
        else:
            pass

    # 经验条增加
    def exp_add(self, exp):
        self.exp += exp
        self.level_update()


    # 战斗类
    # 伤害类型判断
    def damage_type_func(self):
        if self.weapon_type == "melee":
            return "physical"
        elif self.weapon_type == "ranged":
            return "physical"
        elif self.weapon_type == "magic":
            return "magical"
        else:
            return "physical"

    # 基础伤害值
    def base_damage_func(self):
        
        if self.damage_type == "magical":
            return self.temp_intelligence + self.weapon_damage
        else:
            return self.temp_strength + self.weapon_damage

    # 暴击伤害判断
    def critical_damage(self):
        if random.randint(1, 100) <= self.temp_luck:  
            # 发生暴击，返回暴击伤害
            if self.weapon_critical_damage_percentage == 0:
                return self.base_damage * self.critical_damage_percentage
            else:
                return self.base_damage * self.weapon_critical_damage_percentage
        else:
            # 未发生暴击，返回基础伤害
            return self.base_damage
        
    #伤害输出
    def damage(self):
        return self.critical_damage()

    # 死亡判断
    def die_detect(self):
        if self.temp_hp <= 0:
            return True
            # 死亡动画并结束战斗
        else:
            return False
            # 受伤动画

    #闪避判断
    def miss_hit(self):
        if random.randint(1, 100) <= self.temp_speed:
            # 闪避成功
            return False
        else:
            # 闪避失败
            return True
        
    #魔法伤害倍率计算
    def magical_damage(self, attribute):
        # 光属性伤害
        if attribute == "light":
            # 相同属性
            if self.armor_attribute == "light":
                return 0.8
            # 相克属性
            elif self.armor_attribute == "dark":
                return  1.5
            # 无属性
            else:
                return 1
        # 暗属性伤害
        else:
            # 相同属性
            if self.armor_attribute == "dark":
                return 0.8
            # 相克属性
            elif self.armor_attribute == "light":
                return  1.5
            # 无属性
            else:
                return 1

    #受伤函数
    def get_hurt(self, enemy_damage, damage_type, attribute=None):
        # 闪避失败
        if self.miss_hit() == True:
            # 魔法伤害计算
            if damage_type == "magical":
                self.temp_hp -= (enemy_damage * self.magical_damage(attribute) - self.temp_intelligence)
            # 物理伤害计算
            else:
                self.temp_hp -= (enemy_damage - self.temp_defense)
            self.die_detect()
        else:
            print("Miss Hit!")

    # 武器类
    def weapon_on(self, Weapon):
        self.weapon = Weapon
        self.weapon_damage = self.weapon.damage
        self.weapon_attribute = self.weapon.attribute
        self.weapon_type = self.weapon.type
        self.critical_damage_percentage = self.weapon.critical_damage_percentage
        self.base_damage = self.base_damage_func()

    def weapon_off(self):
        self.weapon_damage = 0
        self.weapon_attribute = None
        self.weapon_type = None
        self.critical_damage_percentage = 1.2
        self.base_damage = self.base_damage_func()


    # 防具类
    def armor_on(self, armor):
        self.armor_defense = armor.defense
        self.armor_attribute = armor.attribute
        self.base_damage = self.base_damage_func()
        self.temp_refresh()

    def armor_off(self):
        self.armor_defense = 0
        self.armor_attribute = None
        self.base_damage = self.base_damage_func()
        self.temp_refresh()

    # 珠宝类
    def jewelry_on(self, jewelry):
        self.jewelry_hp = jewelry.hp
        self.jewelry_intelligence = jewelry.intelligence
        self.jewelry_strength = jewelry.strength
        self.jewelry_defense = jewelry.defense
        self.jewelry_speed = jewelry.speed
        self.jewelry_luck = jewelry.luck
        self.temp_refresh()

    def jewelry_off(self):
        self.jewelry_hp = 0
        self.jewelry_intelligence = 0
        self.jewelry_strength = 0
        self.jewelry_defense = 0
        self.jewelry_speed = 0
        self.jewelry_luck = 0
        self.temp_refresh()

    # 状态类
    # 状态刷新
    def refresh(self):
        self.damage_type = self.damage_type_func()
        self.base_damage = self.base_damage_func()

    # 状态显示
    def show(self):
        print("Lv:", self.lv)
        print("Exp:", self.exp)
        print("HP:", self.hp)
        print("Intelligence:", self.intelligence)
        print("Strength:", self.strength)
        print("Defense:", self.defense + self.armor_defense)
        print("Speed:", self.speed)
        print("Luck:", self.luck)
        print("Weapon_attribute:", self.weapon_attribute)
        print("Weapon_type:", self.weapon_type)
        print("Armor_defense:", self.armor_defense)
        print("Armor_attribute:", self.armor_attribute)
        print("Base_damage:", self.base_damage)
        print("Critical_damage_percentage:", self.critical_damage_percentage)
        print("Jewelry:", self.jewelry)
        print("\n")

    def show_luck(self):
        return self.luck
    

player = character(1, 0, 100, 10, 10, 10, 10, 10, 0, 0)
generate_weapon(1, player.show_luck())
player.show()
show_weapon()
player.weapon_on(weapons[0])
player.show()













# 怪物各项属性
enemy_name = ["Goblin",  "Skeleton", "Boar", "Light_Fairy", "Dark_Fairy"]
enemy_hp_base =                     [15, 10, 20, 10, 10]
enemy_hp_rate =                     [5, 3, 8, 4, 4]
enemy_intelligence_base =           [2, 3, 2, 10, 10]
enemy_intelligence_rate =           [1, 2, 1, 3, 3]
enemy_strength_base =               [3, 5, 2, 3, 3]
enemy_strength_rate =               [2, 4, 1, 3, 3]
enemy_defense_base =                [3, 2, 4, 1, 1]
enemy_defense_rate =                [2, 1, 3, 1, 1]
enemy_speed_base =                  [3, 1, 3, 5, 5]
enemy_speed_rate =                  [1, 1, 1, 2, 2]
enemy_critical_damage_percentage =  [1.2, 1.4, 1.0, 1.6, 1.6]
enemy_attribute =                   [None, None, None, "light", "dark"]
enemy_damage_type =                 ["physical", "physical", "physical", "magical", "magical"]

# 怪物队列
enemy = []

#生成敌人
def generate_enemy(i, lv):
    enemy.append(Enemy(i, lv))

#删除敌人
def delete_enemy(i):
    enemy.pop(i)


class Enemy:
    def __init__(self, i, lv):
        self.name = enemy_name[i]
        self.level = lv
        self.damage_type = enemy_damage_type[i]
        self.hp =           self.calculate_attribute(enemy_hp_base[i], enemy_hp_rate[i])
        self.temp_hp =      self.hp
        self.intelligence = self.calculate_attribute(enemy_intelligence_base[i], enemy_intelligence_rate[i])
        self.strength =     self.calculate_attribute(enemy_strength_base[i], enemy_strength_rate[i])
        self.luck =         self.lucky()
        self.speed =        self.calculate_attribute(enemy_speed_base[i], enemy_speed_rate[i])
        self.defense =      self.calculate_attribute(enemy_defense_base[i], enemy_defense_rate[i])
        self.exp =          self.exp_cal()
        self.critical_damage_percentage = enemy_critical_damage_percentage[i]
        self.attribute =    enemy_attribute[i]

    
    def __str__(self) -> str:
        pass

    def calculate_attribute(self, base, rate):
        """
        Randomly generates an attribute based on the enemy's level.
        """
        return base + rate * self.level * (random.randint(80,120)/100)
    
    # 幸运值计算
    def lucky(self):
        lv = self.level
        if lv >= 20:
            return 20
        return lv
    
    # 经验值计算
    def exp_cal(self):
        return int (5 * ((random.randint(100,120)/100) ** self.level))


    def base_damage(self):
        """
        Calculates base damage depending on damage type.
        """
        if self.damage_type == "magical":
            return self.intelligence
        else:
            return self.strength

    def critical_damage(self):
        """
        Determines if a critical hit occurs and calculates damage accordingly.
        """
        if random.randint(1, 100) <= self.luck:  # Assuming higher luck means higher chance of crit
            return float(self.base_damage() * self.critical_damage_percentage)
        return float(self.base_damage())

    def damage_cal(self):
        """
        Returns damage and attribute (if any) related to the attack.
        """
        return self.critical_damage()
    
    # 死亡判断
    def die_detect(self):
        if self.temp_hp <= 0:
            delete_enemy(0)
            return True
            # 死亡动画
        else:
            return False
            # 受伤动画

    #闪避判断
    def miss_hit(self):
        if random.randint(1, 100) <= self.speed:
            # 闪避成功
            return False
        else:
            # 闪避失败
            return True
        
    #魔法伤害倍率计算
    def magical_damage(self, attribute):
        # 光属性伤害
        if attribute == "light":
            # 相同属性
            if self.attribute == "light":
                return 0.8
            # 相克属性
            elif self.attribute == "dark":
                return  1.5
            # 无属性
            else:
                return 1
        # 暗属性伤害
        else:
            # 相同属性
            if self.attribute == "dark":
                return 0.8
            # 相克属性
            elif self.attribute == "light":
                return  1.5
            # 无属性
            else:
                return 1
            
    #受伤函数
    def get_hurt(self, damage, damage_type, attribute=None): 
        # 闪避失败
        if self.miss_hit() == True:
            if damage_type == "magical":
                self.temp_hp -= (self.magical_damage(attribute) * damage - self.intelligence)
            else:
                self.temp_hp -= (damage - self.defense)
            self.die_detect()
        else:
            print("Miss Hit!")

    def show(self):
        print("Name:", self.name)
        print("Level:", self.level)
        print("HP:", self.hp)
        print("Intelligence:", self.intelligence)
        print("Strength:", self.strength)
        print("Defense:", self.defense)
        print("Speed:", self.speed)
        print("Luck:", self.luck)
        print("Critical_damage_percentage:", self.critical_damage_percentage)
        print("Attribute:", self.attribute)
        print("\n")

generate_enemy(0, 1)
enemy[0].show()
generate_enemy(3, 1)
enemy[1].show()






def player_attack(player, opponent):
    player_damage = player.damage()
    opponent.get_hurt(player_damage, player.damage_type, player.weapon_attribute)
    print(f"Player attacks {opponent.name} for {player_damage} damage. Remaining HP of {opponent.name}: {opponent.hp}")


def opponent_attack(player, opponent):
    enemy_damage = opponent.damage_cal()
    player.get_hurt(enemy_damage, opponent.damage_type, opponent.attribute)
    print(f"{opponent.name} attacks Player for {enemy_damage} damage. Remaining HP of Player: {player.hp}")

def fight(player, opponent):
    turn = 0
    while player.temp_hp > 0 and opponent.temp_hp > 0:
        if player.speed >= opponent.speed:
            turn += 1
            print(f"--- Turn {turn} ---")
            player_attack(player, opponent)
            if opponent.temp_hp <= 0:
                print(f"{opponent.name} defeated!")
                player.exp_add(opponent.exp)
                print(f"Player gained {opponent.exp} experience.")
                player.level_update()
                break
            opponent_attack(player, opponent)
            if player.temp_hp <= 0:
                print("Player defeated! Game Over.")
        else:
            turn += 1
            print(f"--- Turn {turn} ---")
            opponent_attack(player, opponent)
            if player.temp_hp <= 0:
                print("Player defeated! Game Over.")
                break
            player_attack(player, opponent)
            if opponent.temp_hp <= 0:
                print(f"{opponent.name} defeated!")
                player.exp_add(opponent.exp)
                print(f"Player gained {opponent.exp} experience.")
                player.level_update()
                break
            

"""


def battle_interaction(player, opponent):
    turn = 0
    while player.temp_hp > 0 and opponent.temp_hp > 0:
        turn += 1
        print(f"--- Turn {turn} ---")

        # Player's turn to attack
        player_damage = player.critical_damage()
        opponent.hp -= player_damage
        print(f"Player attacks {opponent.name} for {player_damage} damage. Remaining HP of {opponent.name}: {opponent.hp}")

        if opponent.hp <= 0:
            print(f"{opponent.name} defeated!")
            player.exp_add(opponent.exp)  # Grant exp to player
            print(f"Player gained {opponent.exp} experience.")
            player.level_update()  # Check and process level up
            break

        # Enemy's turn to attack
        enemy_damage, _ = opponent.damage()
        player.get_hurt(enemy_damage, opponent.damage_type)
        print(f"{opponent.name} attacks Player for {enemy_damage} damage. Remaining HP of Player: {player.hp}")

        if player.hp <= 0:
            print("Player defeated! Game Over.")

"""
fight(player, enemy[0])
fight(player, enemy[0])