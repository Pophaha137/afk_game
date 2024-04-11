import random
from jewelry import jewelry


class character:
    def __init__(self, Lv, Exp, HP, Intelligence, Strength, Defense, Speed, Luck, x, y, Jewelry=None, Weapon=None,
                 Armor=None):
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
        self.jewelry = Jewelry
        self.damage_type = None
        self.base_damage = None
        self.weapon_critical_damage_percentage = 0

        if Weapon != None:
            self.weapon_damage = Weapon.damage
            self.weapon_attribute = Weapon.attribute
            self.weapon_type = Weapon.type
            self.weapon_critical_damage_percentage = Weapon.critical_damage_percentage
        else:
            self.weapon_damage = 0
            self.weapon_attribute = None
            self.weapon_type = None
            self.weapon_critical_damage_percentage = 1.2

        if Armor != None:
            self.armor_defense = Armor.defense
            self.armor_attribute = Armor.attribute

    # 养成类
    # 经验条增加
    def exp_add(self, exp):
        self.exp += exp

    # 升级函数
    def level_update(self):
        if self.exp >= self.exp_needed:
            self.lv += 1
            self.exp -= self.exp_needed
            # 升级加点
            self.lv_up_reward()
        else:
            pass

    # 升级奖励函数
    def lv_up_reward(self):
        self.hp += 10
        self.intelligence += 1
        self.strength += 1
        self.defense += 1
        self.speed += 1
        self.luck += 1
        self.exp_needed = 10 ^ self.lv

    # 血量增加
    def hp_add(self):
        self.hp += 10

    # 力量增加
    def strength_add(self):
        self.strength += 1

    # 智力增加
    def intelligence_add(self):
        self.intelligence += 1

    # 防御增加
    def defense_add(self):
        self.defense += 1

    # 速度增加
    def speed_add(self):
        self.speed += 1

    # 珠宝增益???感觉不对
    def jewelry(self, jewelry):
        self.hp += jewelry.hp_rate
        self.intelligence += jewelry.intelligence_rate
        self.strength += jewelry.strength_rate
        self.defense += jewelry.defense_rate
        self.speed += jewelry.speed_rate
        self.luck += jewelry.luck_rate

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
    @property
    def base_damage_func(self):
        if self.damage_type == "magical":
            return self.intelligence + self.weapon_damage
        else:
            return self.strength + self.weapon_damage

    # 暴击伤害判断
    def critical_damage(self):
        if random.randint(1, 100) >= self.luck:
            if self.weapon_critical_damage_percentage == 0:
                return self.base_damage * self.critical_damage_percentage
            else:
                return self.base_damage * self.weapon_critical_damage_percentage
        else:
            # 未发生暴击，返回基础伤害
            return self.base_damage

    # 死亡判断
    def die_detect(self):
        if self.hp <= 0:
            return True
            # 死亡动画并结束战斗
        else:
            return False
            # 受伤动画

    # 受伤函数
    def get_hurt(self, damage, damage_type):
        if damage_type == "magical":
            if self.armor_attribute == None:
                self.hp -= (damage - self.defense)
            elif self.armor_attribute == "dark":
                if damage_type == "light":
                    self.hp -= (damage - self.defense) * 1.5
                else:
                    self.hp -= (damage - self.defense) * 0.8
            elif self.armor_attribute == "light":
                if damage_type == "dark":
                    self.hp -= (damage - self.defense) * 1.5
                else:
                    self.hp -= (damage - self.defense) * 0.8
        else:
            self.hp -= (damage - self.defense)
        self.die_detect()

    # 武器类
    def weapon_on(self, weapon):
        self.weapon_damage = weapon.damage
        self.weapon_attribute = weapon.attribute
        self.weapon_type = weapon.type
        self.critical_damage_percentage = weapon.critical_damage_percentage
        self.base_damage = self.base_damage_func()

    def weapon_off(self):
        self.weapon_damage = 0
        self.weapon_attribute = None
        self.weapon_type = None
        self.critical_damage_percentage = 1.2
        self.base_damage = self.base_damage_func()

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


class Enemy:
    def __init__(self, name, level, damage_type):
        self.name = name
        self.level = level
        self.damage_type = damage_type
        self.hp = self.calculate_attribute(20, 5)
        self.intelligence = self.calculate_attribute(10, 2)
        self.strength = self.calculate_attribute(10, 2)
        self.luck = self.calculate_attribute(10, 2)
        self.speed = self.calculate_attribute(10, 2)
        self.defense = self.calculate_attribute(10, 2)
        self.exp = self.calculate_attribute(10, 3)  # Experience points given upon defeat
        self.critical_damage_percentage = 1.2
        self.attribute = None  # Can be set or determined later, if needed

    def calculate_attribute(self, base, growth):
        """
        Randomly generates an attribute based on the enemy's level.
        """
        return base + growth * self.level + random.randint(-growth, growth)

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
            return self.base_damage * self.critical_damage_percentage
        return self.base_damage

    def damage(self):
        """
        Returns damage and attribute (if any) related to the attack.
        """
        return [self.critical_damage(), self.attribute]

    def show(self):
        print(self.name)
        print("lv:", self.level)
        print("HP:", self.hp)
        print("Intelligence:", self.intelligence)
        print("Strength:", self.strength)
        print("Defense:", self.defense)
        print("Speed:", self.speed)
        print("Luck:", self.luck)
        print("\n")


def battle_interaction(player, opponent):
    turn = 0
    while player.hp > 0 and opponent.hp > 0:
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


enemy = Enemy("Goblin", 1, "magical")
print(enemy.show())
