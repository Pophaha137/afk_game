import pygame
from Textbutton import TButton
from function import *
from forge import *
from equipment import *
from character_func import *

page = 0
selected_id = -1

def get_position_id(mx, my):
    x = 807
    y = 16
    count = 0
    for i in range(24):
        if x < mx < x + 60 and y < my < y + 60:
            #print (i)
            return i
        x += 100
        count += 1
        if count == 4:
            x = 807
            y += 100
            count = 0
    #print(-1)
    return -1

def print_text(surface, text, x, y, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def color_of_text(item_id):
    item_list = load_items_from_file("item_list.pkl")
    if item_list[item_id].number < 3:
        return (255, 0, 0)
    else:
        return (255,255,255)

def print_metarial(page = 0):
    global selected_id
    item_list = load_items_from_file("item_list.pkl")
    if selected_id != None:
        selected_id += page * 24
        xy1 = (50,520)
        xy2 = (260,520)
        xy3 = (500,520)
        x4 = 60
        y4 = 600
        x5 = 270
        y5 = 600
        font_size = 20
        if 0 <= selected_id < 4 :
            screen.blit(item_img[0],xy1)
            screen.blit(item_img[3],xy2)
            screen.blit(forge_img[selected_id],xy3)
            print_text(screen, str(item_list[0].number) + "/3", x4, y4, font_size, color_of_text(0))
            print_text(screen, str(item_list[3].number) + "/3", x5, y5, font_size, color_of_text(3))
        elif 4 <= selected_id < 8:
            screen.blit(item_img[1],xy1)
            screen.blit(item_img[4],xy2)
            screen.blit(forge_img[selected_id],xy3)
            print_text(screen, str(item_list[1].number) + "/3", x4, y4, font_size, color_of_text(1))
            print_text(screen, str(item_list[4].number) + "/3", x5, y5, font_size, color_of_text(4))
        elif 8 <= selected_id < 10:
            screen.blit(item_img[2],xy1)
            screen.blit(item_img[5],xy2)
            screen.blit(forge_img[selected_id],xy3)
            print_text(screen, str(item_list[2].number) + "/3", x4, y4, font_size, color_of_text(2))
            print_text(screen, str(item_list[5].number) + "/3", x5, y5, font_size, color_of_text(5))
        elif 10 <= selected_id < 14 :
            screen.blit(item_img[0],xy1)
            screen.blit(item_img[3],xy2)
            screen.blit(forge_img[selected_id],xy3)
            print_text(screen, str(item_list[0].number) + "/3", x4, y4, font_size, color_of_text(0))
            print_text(screen, str(item_list[3].number) + "/3", x5, y5, font_size, color_of_text(3))
        elif 14 <= selected_id < 18:
            screen.blit(item_img[1],xy1)
            screen.blit(item_img[4],xy2)
            screen.blit(forge_img[selected_id],xy3)
            print_text(screen, str(item_list[1].number) + "/3", x4, y4, font_size, color_of_text(1))
            print_text(screen, str(item_list[4].number) + "/3", x5, y5, font_size, color_of_text(4))
        elif 18 <= selected_id < 20:
            screen.blit(item_img[2],xy1)
            screen.blit(item_img[5],xy2)
            screen.blit(forge_img[selected_id],xy3)
            print_text(screen, str(item_list[2].number) + "/3", x4, y4, font_size, color_of_text(2))
            print_text(screen, str(item_list[5].number) + "/3", x5, y5, font_size, color_of_text(5))


def generate_item(luck, page = 0 ):
    global selected_id
    item_list = load_items_from_file("item_list.pkl")
    if selected_id == None or selected_id == -1:
        return
    sid = selected_id + page * 24
    if sid < 0 or sid >= len(forge_img):
        return
    weapon_len = len(sword_name)
    armor_len = len(armor_name)
    if 0 <= sid < weapon_len:
        if sid < 4:
            if item_list[0].number >= 3 and item_list[3].number >= 3:
                item_list[0].number -= 3
                item_list[3].number -= 3
                weapons = load_items_from_file("weapons.pkl")
                generate_weapon(sid, luck)
                save_items_to_file("item_list.pkl", item_list)
                item_list = load_items_from_file("item_list.pkl")
        elif 4<= sid < 8:
            if item_list[1].number >= 3 and item_list[4].number >= 3:
                item_list[1].number -= 3
                item_list[4].number -= 3
                weapons = load_items_from_file("weapons.pkl")
                generate_weapon(sid, luck)
                save_items_to_file("item_list.pkl", item_list)
                item_list = load_items_from_file("item_list.pkl")
        elif 8 <= sid < 10:
            if item_list[2].number >= 3 and item_list[5].number >= 3:
                item_list[2].number -= 3
                item_list[5].number -= 3
                weapons = load_items_from_file("weapons.pkl")
                generate_weapon(sid, luck)
                save_items_to_file("item_list.pkl", item_list)
                item_list = load_items_from_file("item_list.pkl")
    elif weapon_len <= sid < weapon_len + armor_len:
        if 10 <= sid < 14:
            if item_list[0].number >= 3 and item_list[3].number >= 3:
                item_list[0].number -= 3
                item_list[3].number -= 3
                armors = load_items_from_file("armors.pkl")
                generate_armor(sid - weapon_len, luck)
                save_items_to_file("item_list.pkl", item_list)
                item_list = load_items_from_file("item_list.pkl")
        elif 14 <= sid < 18:
            if item_list[1].number >= 3 and item_list[4].number >= 3:
                item_list[1].number -= 3
                item_list[4].number -= 3
                armors = load_items_from_file("armors.pkl")
                generate_armor(sid - weapon_len, luck)
                save_items_to_file("item_list.pkl", item_list)
                item_list = load_items_from_file("item_list.pkl")
        elif 18 <= sid < 20:
            if item_list[2].number >= 3 and item_list[5].number >= 3:
                item_list[2].number -= 3
                item_list[5].number -= 3
                armors = load_items_from_file("armors.pkl")
                generate_armor(sid - weapon_len, luck)
                save_items_to_file("item_list.pkl", item_list)
                item_list = load_items_from_file("item_list.pkl")
        
def get_real_position(position_id, page=0):
    position_id += page * 24
    weapon_len = len(sword_name)
    armor_len = len (armor_name)
    

    if  0 <= position_id < weapon_len:
        print_text(screen, "Sword Name:  " + str(sword_name[position_id]), 650, 615, 20, (0, 0, 0))
        print_text(screen, "Base Damage: " + str(sword_base_damage[position_id]), 650, 635, 20, (0, 0, 0))
        print_text(screen, "Attribute:   " + str(sword_attribute[position_id]), 650, 655, 20, (0, 0, 0))
        print_text(screen, "Pecentage:   " + str(sword_critical_damage_percentage[position_id]), 650, 675, 20, (0, 0, 0))
        


    elif weapon_len <=  position_id < weapon_len + armor_len:
        print_text(screen, "Armor Name:   " + str(armor_name[position_id - weapon_len]), 650, 615, 20, (0, 0, 0))
        print_text(screen, "Base Defense: " + str(armor_base_defense[position_id - weapon_len]), 650, 635, 20, (0, 0, 0))
        print_text(screen, "Attribute:    " + str(armor_attribute[position_id - weapon_len]), 650, 655, 20, (0, 0, 0))
        

def get_selected_id(mx, my, page=0):
    global selected_id
    x = 807
    y = 16
    count = 0
    for i in range(24):
        if x < mx < x + 60 and y < my < y + 60:
            #print (i)
            if i + page * 24 == selected_id:
                selected_id = -1
            else:
                selected_id = i + page * 24
        x += 100
        count += 1
        if count == 4:
            x = 807
            y += 100
            count = 0


def print_img(surface, page=0):
    items_per_page = 24  # 每页的物品数量
    items_per_row = 4  # 每行的物品数量
    start_index = items_per_page * page  # 开始的索引
    end_index = start_index + items_per_page  # 结束的索引
    x = 807  # 初始x坐标
    y = 16  # 初始y坐标
    count = 0  # 当前行的物品数量
    for img in forge_img:
        surface.blit(img, (x, y))  # 将图片绘制到surface上
        x += 100  # 更新x坐标以便下一个图片不会覆盖当前图片
        count += 1  # 更新当前行的物品数量
        if count == items_per_row:  # 如果当前行的物品数量达到了6，就换行
            x = 807  # 重置x坐标
            y += 100  # 更新y坐标以便下一个图片在新的一行
            count = 0  # 重置当前行的物品数量

def generate_equipment(self):
    generate_item(player.show_luck(), page)

def smithy(surface):

    from Ffloor import FirstFloor
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    small_font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 24)
    #image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"),(50,50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"),(50,50))
    generateN = pygame.transform.scale(pygame.image.load("./resource/background/button/deleteN.png"), (200, 50))
    generateD = pygame.transform.scale(pygame.image.load("./resource/background/button/deleteD.png"), (200, 50))
    smithy = pygame.transform.scale(pygame.image.load("./resource/background/equip_background.png"),(1500,1000))
    equip_background = pygame.transform.scale(pygame.image.load("./resource/background/equip_background.png"),(1000,1400))
    reforging_background = pygame.transform.scale(pygame.image.load("./resource/background/button/block.png"),(600,600))
    forge = pygame.transform.scale(pygame.image.load("./resource/character/forge.png"), (300, 300))
    first_item_display = pygame.transform.scale(pygame.image.load("./resource/background/button/item_display.png"),(90,90))
    second_item_display = pygame.transform.scale(pygame.image.load("./resource/background/button/item_display.png"),(90,90))
    result_display = pygame.transform.scale(pygame.image.load("./resource/background/button/item_display.png"),(90,90))
    add_button = pygame.transform.scale(pygame.image.load("./resource/background/button/add.png"),(60,60))
    equal_button = pygame.transform.scale(pygame.image.load("./resource/background/button/equal.png"), (60,60))
    item_slot = pygame.transform.scale(pygame.image.load("./resource/background/button/item_slot.png"),(60,60))

    rows, columns = 6, 4
    slot_width, slot_height = 90, 90
    slot_margin = 10  # Margin between slots
    start_x, start_y = 800, 10  # Starting position of the grid

    #button
    esc = TButton(1230,0, " ", crossN, crossN,crossD,FirstFloor, font,(0,0,0))
    generate = TButton(180,650, "Generate", generateN, generateN, generateD, generate_equipment, small_font, (0,0,0))
    running = True
    while running:
        for event in pygame.event.get():
            mx,my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx,my)
                generate.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    esc.mouseDown(mx,my)
                    generate.mouseDown(mx,my)
                    get_selected_id(mx, my)
            elif event.type == pygame.MOUSEBUTTONUP:
                esc.mouseUp(mx,my)
                generate.mouseUp(mx,my)
            surface.blit(smithy,(-400,-200))
            surface.blit(equip_background,(600,-200))
            surface.blit(reforging_background,(0,400))
            surface.blit(first_item_display,(30,500))
            surface.blit(second_item_display, (240, 500))
            surface.blit(result_display,(480,500))
            surface.blit(add_button,(150,515))
            surface.blit(equal_button,(380,515))
            surface.blit(forge, (150, 100))
            
            for row in range(rows):
                for column in range(columns):
                    slot_x = start_x + column * (slot_width + slot_margin)
                    slot_y = start_y + row * (slot_height + slot_margin)
                    surface.blit(item_slot, (slot_x, slot_y))
            #可打造装备图
            print_img(surface, page)
            #展示数据
            potision_id = get_position_id(mx, my)
            get_real_position(potision_id, page)
            print_metarial(page)
            generate.draw(screen)
            esc.draw(screen)
            pygame.draw.rect(surface, (170,121,89), pygame.Rect(600, 585, 680,20))
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1280, 800))
if __name__ == '__main__':
    smithy(screen)
