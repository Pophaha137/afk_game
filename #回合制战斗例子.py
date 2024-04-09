#回合制战斗例子

import threading
import time
import random

# 战斗者类
class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.turn_event = threading.Event()

    def attack(self, opponent):
        # 模拟攻击花费时间
        time.sleep(random.uniform(0.5, 1.5))
        # 计算伤害值
        damage = random.randint(1, self.attack_power)
        # 应用伤害
        opponent.health -= damage
        print(f"{self.name} attacks! {opponent.name} takes {damage} damage. (Health: {opponent.health})")

    # 回合开始
    def start_turn(self):
        # 等待回合事件被设置
        self.turn_event.wait()
        self.turn_event.clear()

    # 结束回合
    def end_turn(self):
        # 通知该回合结束
        self.turn_event.set()

# 战斗逻辑
def turn_based_fight(fighter1, fighter2):
    current_fighter = fighter1
    other_fighter = fighter2
    while fighter1.health > 0 and fighter2.health > 0:
        # 当前战斗者开始回合
        current_fighter.start_turn()
        # 进行攻击
        current_fighter.attack(other_fighter)
        # 回合结束
        current_fighter.end_turn()
        # 交换战斗者
        current_fighter, other_fighter = other_fighter, current_fighter
    # 宣布胜利者
    winner = fighter1 if fighter1.health > 0 else fighter2
    print(f"{winner.name} wins the fight!")

# 创建两个战斗者
fighter1 = Fighter("Warrior")
fighter2 = Fighter("Mage")

# 启动两个线程进行战斗
fight_thread = threading.Thread(target=turn_based_fight, args=(fighter1, fighter2))
fight_thread.start()

# 设置初始战斗者的回合
fighter1.turn_event.set()

# 等待战斗结束
fight_thread.join()