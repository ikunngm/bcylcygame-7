import random,time,sys,os
from 变量 import*
while True: 	
    for user_input in pygame.event.get():	
        mouse = pygame.mouse.get_pos()
        key = pygame.key.get_pressed()
        #退出
        if user_input.type == pygame.QUIT:	
            pygame.quit()
            sys.exit()  
        if game_over == False and set_enter == False:
            #检测"a"是否被持续按下
            if key[pygame.K_a]:
                background_move_right = True
            else:
                background_move_right = False   
            #检测"d"是否被持续按下
            if key[pygame.K_d]:
                background_move_left = True
            else:
                background_move_left = False  
            #检测"空格"是否被按下
            if key[pygame.K_SPACE] and on_ground == True:
                background_move_down = True
            #检测"s"是否被按下
            if key[pygame.K_s]:
                #魔王在勇者左边(左边攻击范围300px)
                if enemy_x <= 475 and enemy_x >= 175:
                    enemy_hp -= 1
                    enemy_move_x -= 1
                #魔王在勇者右边(右边攻击范围300px)
                if enemy_x >= 475 and enemy_x <= 775:
                    enemy_hp -= 1
                    enemy_move_x += 1
        #点击判定
        if user_input.type == pygame.MOUSEBUTTONDOWN:
            #设置
            if 900 <= mouse[0] <= 1000 and 450 <= mouse[1] <= 500:                  
                if set_enter == False: 
                    pygame.draw.rect(screen,(255,255,255),(900,450,100,50),1)#绘制白色按钮特效矩形                  
                    pygame.display.update()#更新屏幕                 
                    time.sleep(0.1)#特效延迟                  
                    pygame.draw.rect(screen,(0,0,0),(900,450,100,50),1)#绘制黑色按钮特效矩形                  
                    pygame.display.update()#更新屏幕                  
                    time.sleep(0.1)#特效延迟                   
                    set_enter = True#设置已打开
            #返回				
            if 0 <= mouse[0] <= 100 and 0 <= mouse[1] <= 50:
                if set_enter == True:                  
                    pygame.draw.rect(screen,(255,255,255),(0,0,100,50),1)#绘制白色按钮特效矩形                  
                    pygame.display.update()#更新屏幕                   
                    time.sleep(0.1)#特效延迟                   
                    pygame.draw.rect(screen,(0,0,0),(0,0,100,50),1)#绘制黑色按钮特效矩形                  
                    pygame.display.update()#更新屏幕                 
                    time.sleep(0.1)#特效延迟                 
                    set_enter = False#设置已关闭
            #剧情
            if 0 <= mouse[0] <= 100 and 50 <= mouse[1] <= 100:
                if set_enter == True:							
                    pygame.draw.rect(screen,(255,255,255),(0,50,100,50),1)#绘制白色按钮特效矩形						
                    pygame.display.update()#更新屏幕							
                    time.sleep(0.1)#特效延迟						
                    pygame.draw.rect(screen,(0,0,0),(0,50,100,50),1)#绘制黑色按钮特效矩形							
                    pygame.display.update()#更新屏幕
                    os.system(r"notepad 剧情.txt")#打开"剧情.txt"
    if set_enter == True:
        #设置打开时的特效
        if move_set_x != -1000:
            move_set_x -= 2
            move_set_y -= 1 
    if set_enter == False:    
        #设置关闭时的特效
        if move_set_x != 0:
            move_set_x += 2
            move_set_y += 1
        if game_over == False:
            #魔王位置
            enemy_x = background_x + enemy_move_x + 2500
            enemy_y = background_y - 55
            #勇者与魔王接触时受伤
            if enemy_x >= 475 and enemy_x <= 525 and enemy_y >= 145 and enemy_y <= 245:
                soldier_hp -= 1
            #游戏整体速度
            stop = random.randint(1, int(1/0.5))    
            if stop == 1:
                time.sleep(0.001)
            #背景向左方移动+空气墙
            if background_move_left == True and background_x + 2741 != 525:
                background_x -= 1
            #背景向右方移动+空气墙
            if background_move_right == True and background_x - 1608 != 475:
                background_x += 1
            #勇者是否在地面上
            if background_y != 200:
                on_ground = False
            else:
                on_ground = True
            #勇者上升
            if background_move_down == True and background_y < 400:
                background_y +=1
            #勇者上升到极限
            if background_y == 400:   
                background_move_down = False
            #勇者落地
            if background_move_down == False and background_y > 200:
                background_y -= 1
            #魔王移动速度
            enemy_move = random.randint(1, int(1/0.2))
            if enemy_move == 1:    
                if enemy_x <= 475:
                    enemy_move_x += 1
                else:
                    enemy_move_x -= 1
            #结束判定
            if enemy_hp <= 0 or soldier_hp <= 0:
                game_over = True#游戏结束                    
        screen.fill((50,150,255))#蓝色天空
        screen.blit(background,(background_x,background_y))#地图(中间)
        #地图(左边)
        screen.blit(background,(background_x - 1133,background_y))
        screen.blit(background,(background_x - 2266,background_y))
        #地图(右边)
        screen.blit(background,(background_x + 1133,background_y))
        screen.blit(background,(background_x + 2266,background_y))       
        screen.blit(stone_left,(background_x - 2083,background_y - 500))#石头(左边)       
        screen.blit(stone_right,(background_x + 2741,background_y - 500))#石头(右边)              
        pygame.draw.rect(screen,(0,0,0),(475,145,50,100),0)#勇者    
        pygame.draw.rect(screen,(255,0,0),(enemy_x,enemy_y,50,100),0)#魔王
        #设置     
        pygame.draw.rect(screen,(0,0,0),(900,450,100,50),1)#绘制黑色按钮特效矩形     
        pygame.draw.rect(screen,(255,127,38),(901,451,98,48),0)#绘制设置矩形     
        screen.blit(text_set,(920,457))#打印设置字体
        #当前魔王血量
        text_enemy_hp = font_30_size.render(("魔王的血量还有" + str(enemy_hp)),True,(0,0,0))
        screen.blit(text_enemy_hp,(0,5))
        #当前勇者血量
        text_soldier_hp = font_30_size.render(("你的血量还有" + str(soldier_hp)),True,(0,0,0))
        screen.blit(text_soldier_hp,(0,45))        
        photo_background_x = 1000 + move_set_x#背景X轴位置      
        photo_background_y = 500 + move_set_y#背景y轴位置        
        pygame.draw.rect(screen,(50,150,255),(photo_background_x,photo_background_y,1000,500),0)#绘制背景
    photo_background_x = 1000 + move_set_x#背景X轴位置
    photo_background_y = 500 + move_set_y#背景y轴位置  
    pygame.draw.rect(screen,(50,150,255),(photo_background_x,photo_background_y,1000,500),0)#绘制背景
    #返回   
    pygame.draw.rect(screen,(0,0,0),(1000 + move_set_x,500 + move_set_y,100,50),1)#绘制黑色按钮特效矩形      
    pygame.draw.rect(screen,(185,122,87),(1001 + move_set_x,501 + move_set_y,98,48),0)#绘制返回矩形       
    screen.blit(text_back,(1020 + move_set_x,507 + move_set_y))#打印返回字体
    #剧情		
    pygame.draw.rect(screen,(0,0,0),(1000 + move_set_x,550 + move_set_y,100,50),1)#绘制黑色按钮特效矩形			
    pygame.draw.rect(screen,(106,59,187),(1001 + move_set_x,551 + move_set_y,98,48),0)#绘制帮助矩形		
    screen.blit(text_story,(1020 + move_set_x,557 + move_set_y))#打印剧情字体
    if game_over == True and set_enter == False:
        #结局
        if enemy_hp <= 0 and soldier_hp <= 0:           
            screen.blit(text_none_winner,(0,85))#同归于尽
        else:    
            if enemy_hp <= 0:
                screen.blit(text_win,(0,85))#胜利 
            if soldier_hp <= 0:
                screen.blit(text_die,(0,85))#失败   
    pygame.display.update()#更新屏幕