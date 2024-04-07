import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
position = [width // 2, height // 2]
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # 使用WASD和箭头键控制移动
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        position[0] -= 5
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        position[0] += 5
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        position[1] -= 5
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        position[1] += 5

    # 限制移动范围，确保对象不会离开屏幕
    position[0] = max(0, min(position[0], width))
    position[1] = max(0, min(position[1], height))

    screen.fill((0, 0, 0))  # 填充屏幕背景为黑色
    pygame.draw.circle(screen, (0, 255, 0), position, 10)  # 绘制绿色的圆形
    pygame.display.flip()  # 更新显示

    clock.tick(60)  # 设置帧率为60fps

pygame.quit()

#lack：
#1.这只是一部分代码，行走区域没有被严格限制，与地图的交互键也没有被设置
#2.这是个基本样本，后续还得导入图片的移动函数。