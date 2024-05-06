import pygame
from Textbutton import TButton
from function import *
from equipment import *
from character_func import *


def print_img(surface, print_page, page=0):
    items_per_page = 30  # 每页的物品数量
    items_per_row = 6  # 每行的物品数量
    start_index = items_per_page * page  # 开始的索引
    end_index = start_index + items_per_page  # 结束的索引

    if print_page == 0:
        weapons = load_items_from_file("weapons.pkl")
        img_list = weapons[start_index:end_index]  # 获取当前页的物品
    elif print_page == 1:
        armors = load_items_from_file("armors.pkl")
        img_list = armors[start_index:end_index]
    elif print_page == 2:
        jewelrys = load_items_from_file("jewelrys.pkl")
        img_list = jewelrys[start_index:end_index]
    else:
        print_page = 0

    x = 368  # 初始x坐标
    y = 42  # 初始y坐标
    count = 0  # 当前行的物品数量
    for item in img_list:
        img = item.get_img()  # 获取物品图片
        surface.blit(img, (x, y))  # 将图片绘制到surface上
        x += img.get_width() + 9  # 更新x坐标以便下一个图片不会覆盖当前图片
        count += 1  # 更新当前行的物品数量
        if count == items_per_row:  # 如果当前行的物品数量达到了6，就换行
            x = 368  # 重置x坐标
            y += img.get_height() + 16  # 更新y坐标以便下一个图片在新的一行
            count = 0  # 重置当前行的物品数量


def position_id(mx, my):
    x = 368
    y = 42
    count = 0
    for i in range(30):
        if x < mx < x + 89 and y < my < y + 91:
            # print (i)
            return i
        x += 89 + 9
        count += 1
        if count == 6:
            x = 368
            y += 91 + 16
            count = 0
    # print(-1)
    return -1


def print_text(surface, text, x, y, font_size, color):
    font = pygame.font.Font('VonwaonBitmap-12px.ttf', font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)  # 设置文本矩形的左上角坐标
    surface.blit(text_surface, text_rect)


def print_title(surface, print_page):
    x = 45
    y = 100
    size = 40
    if print_page == 0:
        print_text(surface, "Weapon", x, y, size, (0, 0, 0))
    elif print_page == 1:
        print_text(surface, "Armor", x, y, size, (0, 0, 0))
    elif print_page == 2:
        print_text(surface, "Jewelry", x, y, size, (0, 0, 0))


def print_info(surface, print_page, page, position_id, selected_id):
    size = 14
    x = 45
    y = 150
    if selected_id != -1:
        if print_page == 0:
            weapons = load_items_from_file("weapons.pkl")
            if selected_id < len(weapons):
                item = weapons[selected_id]
                text_dict = item.to_dict()

                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20
        elif print_page == 1:
            armors = load_items_from_file("armors.pkl")
            if selected_id < len(armors):
                item = armors[selected_id]
                text_dict = item.to_dict()

                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20
        elif print_page == 2:
            jewelrys = load_items_from_file("jewelrys.pkl")
            if selected_id < len(jewelrys):
                item = jewelrys[selected_id]
                text_dict = item.to_dict()

                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20

    elif position_id != -1 and selected_id == -1:
        i = position_id + page * 30
        if print_page == 0:
            weapons = load_items_from_file("weapons.pkl")
            if i < len(weapons):
                item = weapons[i]
                text_dict = item.to_dict()

                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20  # 更新y坐标以便下一个文本在新的一行
        elif print_page == 1:
            armors = load_items_from_file("armors.pkl")
            if i < len(armors):
                item = armors[i]
                text_dict = item.to_dict()

                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20  # 更新y坐标以便下一个文本在新的一行
        elif print_page == 2:
            jewelrys = load_items_from_file("jewelrys.pkl")
            if i < len(jewelrys):
                item = jewelrys[i]
                text_dict = item.to_dict()

                for key, value in text_dict.items():
                    text = f"{key}: {value}"
                    print_text(surface, text, x, y, size, (0, 0, 0))
                    y += 20  # 更新y坐标以便下一个文本在新的一行


def get_selected_id(mx, my, selected_id):
    global current_page, print_page
    x = 368
    y = 42
    count = 0
    if print_page == 0:
        weapons = load_items_from_file("weapons.pkl")
        for i in range(30):
            if x < mx < x + 89 and y < my < y + 91:
                if i + current_page * 30 == selected_id or i + current_page * 30 >= len(weapons):
                    return -1
                return i + current_page * 30
            x += 89 + 9
            count += 1
            if count == 6:
                x = 368
                y += 91 + 16
                count = 0
        return selected_id
    elif print_page == 1:
        armors = load_items_from_file("armors.pkl")
        for i in range(30):
            if x < mx < x + 89 and y < my < y + 91:
                if i + current_page * 30 == selected_id or i + current_page * 30 >= len(armors):
                    return -1
                return i + current_page * 30
            x += 89 + 9
            count += 1
            if count == 6:
                x = 368
                y += 91 + 16
                count = 0
        return selected_id
    elif print_page == 2:
        jewelrys = load_items_from_file("jewelrys.pkl")
        for i in range(30):
            if x < mx < x + 89 and y < my < y + 91:
                if i + current_page * 30 == selected_id or i + current_page * 30 >= len(jewelrys):
                    return -1
                return i + current_page * 30
            x += 89 + 9
            count += 1
            if count == 6:
                x = 368
                y += 91 + 16
                count = 0
        return selected_id


def highlight_selected_item(surface, mx, my, selected_id, current_page):
    x = 368
    y = 42
    if selected_id == -1:
        return
    s_id = selected_id % 30
    c_page = selected_id // 30
    row = s_id // 6
    col = s_id % 6
    x += col * 98
    y += row * 107
    if c_page != current_page:
        return
    else:
        pygame.draw.rect(surface, (255, 255, 255), (x, y, 89, 91), 2)


def page_change_click(self):
    global current_page
    if current_page >= 1:
        current_page = current_page - 1


def page_change_plus(self):
    global current_page
    if current_page <= 18:
        current_page = current_page + 1


def page_change_box(self):
    global print_page
    if print_page != 0:
        pass


def rotate_to_right(self):
    global print_page, current_page, selected_id
    print_page += 1
    current_page = 0
    selected_id = -1
    if print_page == 3:
        print_page = 0


def rotate_to_left(self):
    global print_page, current_page, selected_id
    print_page -= 1
    current_page = 0
    selected_id = -1
    if print_page == -1:
        print_page = 2


def delete_equipment(mx, my, selected_id):
    global print_page
    global current_page

    if selected_id == -1:
        return
    if print_page == 0:
        weapons = load_items_from_file("weapons.pkl")
        if len(weapons) > 0:
            if player.weapon_id != weapons[selected_id].id:
                delete_weapon(get_selected_id(mx, my, selected_id))
                print("weapon deleted")
    elif print_page == 1:
        armors = load_items_from_file("armors.pkl")
        if len(armors) > 0:
            delete_armor(get_selected_id(mx, my, selected_id))
    elif print_page == 2:
        jewelrys = load_items_from_file("jewelrys.pkl")
        if len(jewelrys) > 0:
            delete_jewelry(get_selected_id(mx, my, selected_id))


def delete_func(self):
    global mx, my, selected_id
    delete_equipment(mx, my, selected_id)
    selected_id = -1


current_page = 0
print_page = 0
mx, my = 0, 0
selected_id = -1

def print_equipfunc():
    global print_page, selected_id
    font_size = 25
    if selected_id == -1:
        print_text(screen, "Equip", 140, 360, font_size, (0, 0, 0))
    else:
        if print_page == 0:
            weapons = load_items_from_file("weapons.pkl")
            if len(weapons) > selected_id:
                if player.weapon_id != weapons[selected_id].id:
                    print_text(screen, "Equip", 140, 360, font_size, (0, 0, 0))
                elif player.weapon_id == weapons[selected_id].id:
                    print_text(screen, "Unequip", 120, 360, font_size, (0, 0, 0))
        elif print_page == 1:
            armors = load_items_from_file("armors.pkl")
            if len(armors) > selected_id:
                if player.armor_id != armors[selected_id].id:
                    print_text(screen, "Equip", 140, 360, font_size, (0, 0, 0))
                elif player.armor_id == armors[selected_id].id:
                    print_text(screen, "Unequip", 120, 360, font_size, (0, 0, 0))
        elif print_page == 2:
            jewelrys = load_items_from_file("jewelrys.pkl")
            if len(jewelrys) > selected_id:
                if player.jewelry_id != jewelrys[selected_id].id:
                    print_text(screen, "Equip", 140, 360, font_size, (0, 0, 0))
                elif player.jewelry_id == jewelrys[selected_id].id:
                    print_text(screen, "Unequip", 120, 360, font_size, (0, 0, 0))
    


def equip_func(self):
    global print_page, selected_id, player
    if selected_id == -1:
        return
    if print_page == 0:
        weapons = load_items_from_file("weapons.pkl")
        if len(weapons) > selected_id:
            if player.weapon_id != weapons[selected_id].id:
                player.weapon_on(weapons[selected_id])
            elif player.weapon_id == weapons[selected_id].id:
                player.weapon_off()
    elif print_page == 1:
        armors = load_items_from_file("armors.pkl")
        if len(armors) > selected_id:
            if player.armor_id != armors[selected_id].id:
                player.armor_on(armors[selected_id])
            elif player.armor_id == armors[selected_id].id:
                player.armor_off()
    elif print_page == 2:
        jewelrys = load_items_from_file("jewelrys.pkl")
        if len(jewelrys) > selected_id:
            if player.jewelry_id != jewelrys[selected_id].id:
                player.jewelry_on(jewelrys[selected_id])
            elif player.jewelry_id == jewelrys[selected_id].id:
                player.jewelry_off()
    player.show()
    save_player()
    


def backpack(surface):
    global current_page
    global print_page
    global mx, my
    global selected_id
    # page = 0
    from Ffloor import FirstFloor
    # 时钟
    clock = pygame.time.Clock()
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    page_font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 24)
    # image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"), (50, 50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"), (50, 50))
    pakage = pygame.transform.scale(pygame.image.load("./resource/character/inventory.png"), (1080, 600))
    left_page = pygame.transform.scale(pygame.image.load("./resource/background/button/left.png"), (100, 100))
    right_page = pygame.transform.scale(pygame.image.load("./resource/background/button/right.png"), (100, 100))
    leftD_page = pygame.transform.scale(pygame.image.load("./resource/background/button/leftD.png"), (100, 100))
    rightD_page = pygame.transform.scale(pygame.image.load("./resource/background/button/rightD.png"), (100, 100))
    deleteN = pygame.transform.scale(pygame.image.load("./resource/background/button/deleteN.png"), (200, 50))
    deleteD = pygame.transform.scale(pygame.image.load("./resource/background/button/deleteD.png"), (200, 50))
    equipN = pygame.transform.scale(pygame.image.load("./resource/background/button/deleteN.png"), (200, 50))
    equipD = pygame.transform.scale(pygame.image.load("./resource/background/button/deleteD.png"), (200, 50))
    rotate_rightN = pygame.transform.scale(pygame.image.load("./resource/background/button/rotate_rightN.png"),
                                           (100, 100))
    rotate_rightD = pygame.transform.scale(pygame.image.load("./resource/background/button/rotata_rightD.png"),
                                           (100, 100))
    rotate_leftN = pygame.transform.scale(pygame.image.load("./resource/background/button/rotate_leftN.png"),
                                          (100, 100))
    rotate_leftD = pygame.transform.scale(pygame.image.load("./resource/background/button/rotata_leftD.png"),
                                          (100, 100))
    # 背包物品展示
    print_page = 0  # 前选择页数当

    # button
    esc = TButton(1230, 0, " ", crossN, crossN, crossD, FirstFloor, font, (0, 0, 0))
    left = TButton(970, 70, " ", left_page, left_page, leftD_page, page_change_click, font, (0, 0, 0))
    right = TButton(970, 210, " ", right_page, right_page, rightD_page, page_change_plus, font, (0, 0, 0))
    delete = TButton(80, 450, "Delete", deleteN, deleteN, deleteD, delete_func, page_font, (0, 0, 0))
    equip = TButton(80, 350, "", equipN, equipN, equipD, equip_func, page_font, (0, 0, 0))
    rotate_right = TButton(970, 335, " ", rotate_rightN, rotate_rightN, rotate_rightD, rotate_to_right, font, (0, 0, 0))
    rotate_left = TButton(970, 465, " ", rotate_leftN, rotate_leftN, rotate_leftD, rotate_to_left, font, (0, 0, 0))
    running = True

    # event
    EVENT1 = pygame.USEREVENT
    pygame.time.set_timer(EVENT1, 1000)
    while running:
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            position_id(mx, my)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx, my)
                left.getFocus(mx, my)
                right.getFocus(mx, my)
                delete.getFocus(mx, my)
                equip.getFocus(mx, my)
                rotate_right.getFocus(mx, my)
                rotate_left.getFocus(mx, my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    esc.mouseDown(mx, my)
                    left.mouseDown(mx, my)
                    right.mouseDown(mx, my)
                    delete.mouseDown(mx, my)
                    equip.mouseDown(mx, my)
                    rotate_right.mouseDown(mx, my)
                    rotate_left.mouseDown(mx, my)
                    selected_id = get_selected_id(mx, my, selected_id)

            elif event.type == pygame.MOUSEBUTTONUP:
                esc.mouseUp(mx, my)
                left.mouseUp(mx, my)
                right.mouseUp(mx, my)
                delete.mouseUp(mx, my)
                equip.mouseUp(mx, my)
                rotate_right.mouseUp(mx, my)
                rotate_left.mouseUp(mx, my)

            elif event.type == EVENT1:
                pygame.display.update()

        surface.blit(pakage, (0, 0))

        rect_x, rect_y, rect_width, rect_height = 350, 600, 100, 50
        pygame.draw.rect(surface, (196, 164, 132), [rect_x, rect_y, rect_width, rect_height])
        page_num_text = page_font.render(f'Page {current_page}', True, (255, 255, 255))
        text_rect = page_num_text.get_rect(center=(rect_x + rect_width / 2, rect_y + rect_height / 2))
        surface.blit(page_num_text, text_rect)
        load_player()
        esc.draw(screen)
        left.draw(screen)
        right.draw(screen)
        delete.draw(screen)
        equip.draw(screen)
        rotate_right.draw(screen)
        rotate_left.draw(screen)
        print_img(screen, print_page, current_page)
        print_title(screen, print_page)
        print_info(screen, print_page, current_page, position_id(mx, my), selected_id)
        highlight_selected_item(screen, mx, my, selected_id, current_page)
        print_equipfunc()
        pygame.display.flip()
        clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((1280, 800))

if __name__ == '__main__':
    backpack(screen)
