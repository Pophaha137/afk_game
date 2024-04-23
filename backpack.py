import pygame
from Textbutton import TButton
from function import *
from equipment import *


def print_img(surface, print_page,page = 0):
    items_per_page = 24  # 每页的物品数量
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

def position_id(mx,my):
    x = 100
    y = 100
    count = 0
    for i in range(24):
        if x < mx < x + 50 and y < my < y + 50:
            #print (i)
            return i
        x += 50 + 10
        count += 1
        if count == 6:
            x = 100
            y += 50 + 10
            count = 0
    #print(-1)
    return -1


def backpack(surface):
    page = 0
    from Ffloor import FirstFloor
    #时钟
    clock = pygame.time.Clock()
    font = pygame.font.Font("./VonwaonBitmap-12px.ttf", 80)
    #image import
    crossN = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossN.png"),(50,50))
    crossD = pygame.transform.scale(pygame.image.load("./resource/background/Error/crossD.png"),(50,50))
    pakage = pygame.transform.scale(pygame.image.load("./resource/character/inventory.png"),(1080,600))
    
    #背包物品展示
    select_position_id = -1  # 选中的物品的索引
    print_page = 0  # 当前选择页数

    

    #button
    esc = TButton(1230,0, " ", crossN, crossN,crossD,FirstFloor, font,(0,0,0))
    running = True
    
    while running:
        for event in pygame.event.get():
            mx,my = pygame.mouse.get_pos()
            position_id(mx,my)
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                esc.getFocus(mx,my)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    esc.mouseDown(mx,my)
                    if 600 < mx < 700 and 600 < my < 700:
                        if page >= 1:
                            page -= 1
                        
                    elif 750 < mx < 850 and 600 < my < 700:
                        if page <= 18:
                            page += 1
                    elif 900 < mx < 1000 and 600 < my < 700:
                        print_page += 1
                        if print_page == 3:
                            print_page = 0
                    elif 1000 < mx < 1100 and 600 < my < 700:
                        if print_page != 0:
                            print_page -= 1

                    else:
                        generate_weapon(0,10)
            elif event.type == pygame.MOUSEBUTTONUP:
                esc.mouseUp(mx,my)
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(600, 600, 100, 100), 2)
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(750, 600, 100, 100), 2)
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(900, 600, 100, 100), 2)
        pygame.draw.rect(screen, (255,0,255), pygame.Rect(1000, 600, 100, 100), 2)

        surface.blit(pakage,(0,0))
        esc.draw(screen)
        print_img(screen, print_page , page)
        print(page)
        pygame.display.flip()
        clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((1280, 800))



if __name__ == '__main__':
    backpack(screen)