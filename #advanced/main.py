import pygame
import math
import random
import os
import time
import kavdi_mapping
import threading
VERSION='1.0'
class player:
    p11_color=(200,0,0)
    p12_color=(200,0,0)
    p13_color=(200,0,0)
    p14_color=(200,0,0)
    
    p21_color=(0,200,0)
    p22_color=(0,200,0)
    p23_color=(0,200,0)
    p24_color=(0,200,0)
    
    p31_color=(0,0,200)
    p32_color=(0,0,200)
    p33_color=(0,0,200)
    p34_color=(0,0,200)
    
    p41_color=(0,200,200)
    p42_color=(0,200,200)
    p43_color=(0,200,200)
    p44_color=(0,200,200)
    
    player_name=''
    kavdi_num=0
    kavdi_selecting_val=[]
    
    kavdi_item_pos=[['p11',[]],['p22',[]],['p33',[]],['p44',[]],['p12',[]],['p13',[]],['p14',[]],['p21',[]],['p23',[]],['p24',[]],['p31',[]],['p32',[]],['p34',[]],['p41',[]],['p42',[]],['p43',[]]]
    
    kavdi_data=[[1,[],[110,80]],[2,[],[220,80]],[3,[],[330,80]],[4,[],[440,80]],[5,[],[550,80]],[6,[],[110,160]],[7,[],[220,160]],[8,[],[330,160]],[9,[],[440,160]],[10,[],[550,160]],
                [11,[],[110,240]],[12,[],[220,240]],[13,[],[330,240]],[14,[],[440,240]],[15,[],[550,240]],[16,[],[110,320]],[17,[],[220,320]],[18,[],[330,320]],[19,[],[440,320]],[20,[],[550,320]],
                [21,[],[110,400]],[22,[],[220,400]],[23,[],[330,400]],[24,[],[440,400]],[25,[],[550,400]],[26,['p11','p12','p13','p14'],[330,0]],[27,['p21','p22','p23','p24'],[0,240]],[28,['p31','p32','p33','p34'],[660,240]],[29,['p41','p42','p43','p44'],[330,480]]]
    
   
    def __init__(self):
        pass
        
    def name_read(key):
        player.player_name=player.player_name+str(key)
        
    def name_backspace():
        player.player_name=player.player_name[:-1]
    def kavdi_dice_roll(command):
        if command=='first':
            player.kavdi_num=random.randint(1,4)
        if command=='second':
            player.kavdi_num='next'
    
    def kavdi_placement(window):
        for i in player.kavdi_data:
            if i[0]==13:
                continue
            if i[1]!=[]:
                x=i[2][0]+3
                y=i[2][1]+3
                o=1
                for j in i[1]:
                    if j=='p11':
                        pygame.draw.rect(window,player.p11_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p11':
                                k[1]=[x,y]
                    elif j=='p12':
                        pygame.draw.rect(window,player.p12_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p12':
                                k[1]=[x,y]
                    elif j=='p13':
                        pygame.draw.rect(window,player.p13_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p13':
                                k[1]=[x,y]
                    elif j=='p14':
                        pygame.draw.rect(window,player.p14_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p14':
                                k[1]=[x,y]
                    elif j=='p21':
                        pygame.draw.rect(window,player.p21_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p21':
                                k[1]=[x,y]
                    elif j=='p22':
                        pygame.draw.rect(window,player.p22_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p22':
                                k[1]=[x,y]
                    elif j=='p23':
                        pygame.draw.rect(window,player.p23_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p23':
                                k[1]=[x,y]
                    elif j=='p24':
                        pygame.draw.rect(window,player.p24_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p24':
                                k[1]=[x,y]
                    elif j=='p31':
                        pygame.draw.rect(window,player.p31_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p31':
                                k[1]=[x,y]
                    elif j=='p32':
                        pygame.draw.rect(window,player.p32_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p32':
                                k[1]=[x,y]
                    elif j=='p33':
                        pygame.draw.rect(window,player.p33_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p33':
                                k[1]=[x,y]
                    elif j=='p34':
                        pygame.draw.rect(window,player.p34_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p34':
                                k[1]=[x,y]
                    elif j=='p41':
                        pygame.draw.rect(window,player.p41_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p41':
                                k[1]=[x,y]
                    elif j=='p42':
                        pygame.draw.rect(window,player.p42_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p42':
                                k[1]=[x,y]
                    elif j=='p43':
                        pygame.draw.rect(window,player.p43_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p43':
                                k[1]=[x,y]
                    elif j=='p44':
                        pygame.draw.rect(window,player.p44_color,[x,y,20,20])
                        for k in player.kavdi_item_pos:
                            if k[0]=='p44':
                                k[1]=[x,y]
                            
                    
                    
                    
                    
                    
                    x=x+23
                    o=o+1
                    if o==5:
                        o=1
                        x=i[2][0]+3
                        y=i[2][1]+26
                    
                    
    def kavdi_checking(x,y):
        flag=False
        for items in player.kavdi_item_pos:
            if items[0][0:2]=='p4':
                if x>items[1][0] and x<items[1][0]+20 and y>items[1][1] and y<items[1][1]+20:
                    player.kavdi_selecting_val=[items[0],items[1]]
                    flag=True
        if not flag:
            player.kavdi_selecting_val=[]
            
                
            
            
    def kavdi_selecting():
        if player.kavdi_selecting_val==[]:
            player.kavdi_dice_roll('second')
        else:
            player.kavdi_process(player.kavdi_selecting_val,player.kavdi_num)
            
    
    def kavdi_process(val,num):
        flag=True
        for i in player.kavdi_data:
            if val[0] in i[1] and flag:
                flag=False
                next=kavdi_mapping.kavdi_map(val[0],i[0],num)
                if i[1][0]==val[0]:
                    del i[1][0]
                elif i[1][1]==val[0]:
                    del i[1][1]
                elif i[1][2]==val[0]:
                    del i[1][2]
                elif i[1][3]==val[0]:
                    del i[1][3]        
                for k in player.kavdi_data:
                    if k[0]==next and k[1]==[]:
                        k[1].append(val[0])
                    elif k[0]==next and k[1]!=[] and val[0][0:2]=='p1':
                        if k[0]==3 or k[0]==11 or k[0]==23 or k[0]==15 or k[0]==13:
                            k[1].append(val[0])
                        else:    
                            if 'p11' in k[1] or 'p12' in k[1] or 'p13' in k[1] or 'p14' in k[1]:
                                k[1].append(val[0])
                            else:
                                m=0
                                for p in k[1]:
                                    if p[0:2]=='p1':
                                        for l in player.kavdi_data:
                                            if l[0]==26:
                                                l[1].append(p)
                                                m=m+1
                                                
                                    elif p[0:2]=='p2':
                                        for l in player.kavdi_data:
                                            if l[0]==27:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p3':
                                        for l in player.kavdi_data:
                                            if l[0]==28:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p4':
                                        for l in player.kavdi_data:
                                            if l[0]==29:
                                                l[1].append(p)
                                                
                                                m=m+1
                                for o in range(m):
                                    del k[1][0]
                                k[1].append(val[0])    
                                
                    elif k[0]==next and k[1]!=[] and val[0][0:2]=='p2':
                        if k[0]==3 or k[0]==11 or k[0]==23 or k[0]==15 or k[0]==13:
                            k[1].append(val[0])
                        else:    
                            if 'p21' in k[1] or 'p22' in k[1] or 'p23' in k[1] or 'p24' in k[1]:
                                k[1].append(val[0])
                            else:
                                m=0
                                for p in k[1]:
                                    if p[0:2]=='p1':
                                        for l in player.kavdi_data:
                                            if l[0]==26:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p2':
                                        for l in player.kavdi_data:
                                            if l[0]==27:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p3':
                                        for l in player.kavdi_data:
                                            if l[0]==28:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p4':
                                        for l in player.kavdi_data:
                                            if l[0]==29:
                                                l[1].append(p)
                                                
                                                m=m+1
                                for o in range(m):
                                    del k[1][0]        
                                k[1].append(val[0])    
                    elif k[0]==next and k[1]!=[] and val[0][0:2]=='p3':
                        if k[0]==3 or k[0]==11 or k[0]==23 or k[0]==15 or k[0]==13:
                            k[1].append(val[0])
                        else:    
                            if 'p31' in k[1] or 'p32' in k[1] or 'p33' in k[1] or 'p34' in k[1]:
                                k[1].append(val[0])
                            else:
                                m=0
                                for p in k[1]:
                                    if p[0:2]=='p1':
                                        for l in player.kavdi_data:
                                            if l[0]==26:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p2':
                                        for l in player.kavdi_data:
                                            if l[0]==27:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p3':
                                        for l in player.kavdi_data:
                                            if l[0]==28:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p4':
                                        for l in player.kavdi_data:
                                            if l[0]==29:
                                                l[1].append(p)
                                                
                                                m=m+1
                                for o in range(m):
                                    del k[1][0]        
                                k[1].append(val[0])    
                            
                    elif k[0]==next and k[1]!=[] and val[0][0:2]=='p4':
                        if k[0]==3 or k[0]==11 or k[0]==23 or k[0]==15 or k[0]==13:
                            k[1].append(val[0])
                        else:    
                            if 'p41' in k[1] or 'p42' in k[1] or 'p43' in k[1] or 'p44' in k[1]:
                                k[1].append(val[0])
                            else:
                                m=0
                                for p in k[1]:
                                    if p[0:2]=='p1':
                                        for l in player.kavdi_data:
                                            if l[0]==26:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p2':
                                        for l in player.kavdi_data:
                                            if l[0]==27:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p3':
                                        for l in player.kavdi_data:
                                            if l[0]==28:
                                                l[1].append(p)
                                                
                                                m=m+1
                                        
                                    elif p[0:2]=='p4':
                                        for l in player.kavdi_data:
                                            if l[0]==29:
                                                l[1].append(p)
                                                
                                                m=m+1
                                for o in range(m):
                                    del k[1][0]
                                k[1].append(val[0])        
                                    
        
        player.kavdi_dice_roll('second')
                                            
                                    
                                
                            
        
                        
                        
                        
                        
                        
                        
    
                    
        
            
                
            
class kavdi(player):
    white=(255,255,255)
    black=(0,0,0)
    arrow_color=(19,179,191)
    kavdi_board_color=(91,250,69)
    
    red=(240,0,0)
    green=(0,240,0)
    blue=(0,0,240)
    light_red=(100,0,0)
    light_green=(0,100,0)
    light_blue=(0,0,100)
    grey1=(100,100,100)
    grey2=(100,100,100)
    space_switch=(0,100,0)
    
    time_elapsed=0
    status='YOUR TURN'
    time_change=False
    kavdi_minutes=0
    kavdi_seconds=0
    
    
    def __init__(self):
        self.kavdi_start=False
        kavdi.font_m=pygame.font.SysFont('ariel',25)
        self.font_small=pygame.font.SysFont('ariel',20)
        self.font_medium=pygame.font.SysFont('ariel',25)
        self.font_big=pygame.font.SysFont('ariel',30)
        
    
    def kavdi_intro(self,window):
        
        kavdi_intro_page=pygame.Surface((800,600))
        
        intro_welcome=self.font_big.render('Welcome To Kavdi',True,self.light_green)
        intro_credits=self.font_small.render('Designed and Created by Aswin Mohan',True,self.light_blue)
        
        pos_welcome=intro_welcome.get_rect(center=(400,300))
        pos_credits=intro_credits.get_rect(center=(400,380))
        
        switch_intro_start=pygame.Surface((100,30))
        switch_intro_exit=pygame.Surface((100,30))
        
        switch_intro_start.fill(self.grey1)
        switch_intro_exit.fill(self.grey2)
        
        switch_start=self.font_small.render('START',True,self.green)
        switch_exit=self.font_small.render('Exit',True,self.red)
        
        pos_switch_start=switch_start.get_rect(center=(50,15))
        pos_switch_exit=switch_exit.get_rect(center=(50,15))
        
        switch_intro_start.blit(switch_start,pos_switch_start)
        switch_intro_exit.blit(switch_exit,pos_switch_exit)
        
        pos_switch1=switch_intro_start.get_rect(center=(340,420))
        pos_switch2=switch_intro_start.get_rect(center=(460,420))
        
        player_name_type=self.font_small.render('Type your name',True,self.black)
        pos_player_name_type=player_name_type.get_rect(center=(400,500))
        
        player_name_entry=self.font_small.render(player.player_name,True,self.red)
        pos_player_name_entry=player_name_entry.get_rect(center=(400,550))
        
        kavdi_intro_page.fill(self.white)
        kavdi_intro_page.blit(intro_welcome,pos_welcome)
        kavdi_intro_page.blit(intro_credits,pos_credits)
        kavdi_intro_page.blit(switch_intro_start,pos_switch1)
        kavdi_intro_page.blit(switch_intro_exit,pos_switch2)
        kavdi_intro_page.blit(player_name_type,pos_player_name_type)
        kavdi_intro_page.blit(player_name_entry,pos_player_name_entry)
        
        window.blit(kavdi_intro_page,kavdi_intro_page.get_rect(center=(500,200)))
        
        pygame.display.update()
        
    def switch_change_color(self,color,val):
        if val==1:
            self.grey1=color
        elif val==2:
            self.grey2=color
    
    def kavdi_background(self,window):
        
        kavdi_bg=pygame.Surface((800,600))
        kavdi_bg.fill(self.white)
        
        x1=110
        y1=80
        x2=660
        for i in range(6):
            pygame.draw.line(kavdi_bg,self.black,[x1,y1],[x2,y1],2)
            y1=y1+80
        x1=110
        y1=80
        y2=480
        for i in range(6):
            pygame.draw.line(kavdi_bg,self.black,[x1,y1],[x1,y2],2)
            x1=x1+110
            
        pygame.draw.line(kavdi_bg,self.black,[330,0],[440,0],2)
        pygame.draw.line(kavdi_bg,self.black,[330,80],[330,0],2)
        pygame.draw.line(kavdi_bg,self.black,[440,80],[440,0],2)
        pygame.draw.line(kavdi_bg,self.black,[0,240],[110,240],2)
        pygame.draw.line(kavdi_bg,self.black,[0,240],[0,320],2)
        pygame.draw.line(kavdi_bg,self.black,[0,320],[110,320],2)
        pygame.draw.line(kavdi_bg,self.black,[330,480],[330,560],2)
        pygame.draw.line(kavdi_bg,self.black,[330,560],[440,560],2)
        pygame.draw.line(kavdi_bg,self.black,[440,480],[440,560],2)
        pygame.draw.line(kavdi_bg,self.black,[660,240],[770,240],2)
        pygame.draw.line(kavdi_bg,self.black,[770,240],[770,320],2)
        pygame.draw.line(kavdi_bg,self.black,[660,320],[770,320],2)
        
        pygame.draw.line(kavdi_bg,self.black,[330,80],[440,160],2)
        pygame.draw.line(kavdi_bg,self.black,[330,160],[440,80],2)
        pygame.draw.line(kavdi_bg,self.black,[110,320],[220,240],2)
        pygame.draw.line(kavdi_bg,self.black,[110,240],[220,320],2)
        pygame.draw.line(kavdi_bg,self.black,[330,400],[440,480],2)
        pygame.draw.line(kavdi_bg,self.black,[330,480],[440,400],2)
        pygame.draw.line(kavdi_bg,self.black,[550,320],[660,240],2)
        pygame.draw.line(kavdi_bg,self.black,[550,240],[660,320],2)
        pygame.draw.line(kavdi_bg,self.black,[330,320],[440,240],2)
        pygame.draw.line(kavdi_bg,self.black,[330,240],[440,320],2)
        
        
        kavdi_arrow_p1=pygame.image.load(os.path.join('images','kavdi_arrow_p1.png'))
        kavdi_arrow_p2=pygame.image.load(os.path.join('images','kavdi_arrow_p2.png'))
        kavdi_arrow_p3=pygame.image.load(os.path.join('images','kavdi_arrow_p3.png'))
        kavdi_arrow_p4=pygame.image.load(os.path.join('images','kavdi_arrow_p4.png'))
        
        
        kavdi_bg.blit(pygame.transform.rotate(kavdi_arrow_p1,180),kavdi_arrow_p1.get_rect(center=[495,120]))
        kavdi_bg.blit(pygame.transform.rotate(kavdi_arrow_p2,270),kavdi_arrow_p1.get_rect(center=[165,190]))
        kavdi_bg.blit(pygame.transform.rotate(kavdi_arrow_p3,90),kavdi_arrow_p1.get_rect(center=[605,350]))
        kavdi_bg.blit(pygame.transform.rotate(kavdi_arrow_p4,0),kavdi_arrow_p1.get_rect(center=[275,440]))
        
        
        player.kavdi_placement(kavdi_bg)
        window.blit(kavdi_bg,[0,0])
        
        pygame.display.update()
            
    def kavdi_control_background(self,window):
        
        kavdi_control=pygame.Surface((200,600))
        kavdi_control.fill(self.white)
        
        player_label_name=self.font_medium.render('Player: {}'.format(player.player_name),True,self.blue)
        
        
        
        self.kavdi_seconds=int(time.time()-self.time_elapsed)
        
            
        if self.kavdi_seconds>60:
            
            self.kavdi_seconds=0
            self.time_elapsed=time.time()
            self.kavdi_minutes=kavdi.kavdi_minutes+1
            self.time_change=True
        else:
            if not self.time_change:
                self.kavdi_minutes=0
            
        kavdi_game_time_elapsed=kavdi.font_m.render('Time Elaped ={} M:{} S'.format(str(self.kavdi_minutes),str(self.kavdi_seconds)),True,(0,0,255))
            
        
        kavdi_game_status=self.font_medium.render('STATUS  ::  {}'.format(self.status),True,self.red)
        
        kavdi_dice_num=self.font_medium.render('The number = {} '.format(player.kavdi_num),True,self.black)
        
        kavdi_dice_roll_button=self.font_medium.render('PRESS SPACE',True,self.black)
        
        kavdi_dice=pygame.Surface((150,30))
        kavdi_dice.fill(self.space_switch)
        kavdi_dice.blit(kavdi_dice_roll_button,kavdi_dice_roll_button.get_rect(center=(75,15)))
        
        
        
        
        kavdi_control.blit(kavdi_dice_num,[20,400])
        kavdi_control.blit(kavdi_dice,kavdi_dice.get_rect(center=(100,500)))
        kavdi_control.blit(player_label_name,[0,5])
        kavdi_control.blit(kavdi_game_status,[0,300])
        kavdi_control.blit(kavdi_game_time_elapsed,[0,30])
        
        
        
        window.blit(kavdi_control,[800,0])
        pygame.display.update()
        
        
        
        
        
        
        
def main():
    pygame.init()
    window_width=1000
    window_height=600
    window=pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('KAVDI '+VERSION)
    pygame.display.set_icon(pygame.image.load(os.path.join('images','icon.png')))
    window.fill((255,255,255))
    
    game=kavdi()
    
    
    single_click=True
    AI=False
    game_start=False
    kavdi_roll=False
    kavdi_run=True
    in_start=False
    in_exit=False
    fps=30
    clock=pygame.time.Clock()
    current_page='intro'
    time_taking_marker=True
    while kavdi_run:
        if current_page=='intro':
            game.kavdi_intro(window)
            events=pygame.event.get()
            for event in events:
                if event.type==pygame.MOUSEMOTION:
                    pointer_pos=pygame.mouse.get_pos()
                    if pointer_pos[0]>390 and pointer_pos[0]<490 and pointer_pos[1]>303 and pointer_pos[1]<335:
                        game.switch_change_color((200,200,200),1)
                        in_start=True
                    elif pointer_pos[0]>510 and pointer_pos[0]<610 and pointer_pos[1]>303 and pointer_pos[1]<335:
                        game.switch_change_color((200,200,200),2)
                        in_exit=True
                    else:
                        game.switch_change_color((100,100,100),1)
                        game.switch_change_color((100,100,100),2)
                        in_start=False
                        in_exit=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if in_start:
                        current_page='game'
                    if in_exit:
                        return None
                if event.type==pygame.KEYDOWN and event.key!=pygame.K_BACKSPACE and event.key!=pygame.K_RETURN:
                    player.name_read(event.unicode)
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_BACKSPACE:
                    player.name_backspace()
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                    current_page='game'
                        
                    
                        
                        
                    
            
                    
        elif current_page=='game':
            if time_taking_marker:
                game.time_elapsed=time.time()
                time_taking_marker=False
            game.kavdi_background(window)
            game.kavdi_control_background(window)
            events=pygame.event.get()
            for event in events:
                if event.type==12:
                    return None
                elif event.type==pygame.MOUSEMOTION:
                    pos=pygame.mouse.get_pos()
                    if pos[0]>825 and pos[0]<975 and pos[1]>485 and pos[1]<515:
                        game.space_switch=(0,200,0)
                    else:
                        game.space_switch=(0,100,0)
                elif event.type==pygame.MOUSEBUTTONDOWN and not kavdi_roll:
                    pos=pygame.mouse.get_pos()
                    if pos[0]>825 and pos[0]<975 and pos[1]>485 and pos[1]<515:
                        game_start=True
                elif single_click and event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or game_start and single_click:
                    single_click=False
                    player.kavdi_dice_roll('first')
                    kavdi_roll=True
                    game_start=False
                elif event.type==pygame.MOUSEBUTTONDOWN and kavdi_roll or game_start:
                    kavdi_roll=False
                    game_start=False
                    single_click=True
                    pos=pygame.mouse.get_pos()
                    player.kavdi_checking(pos[0],pos[1])
                    player.kavdi_selecting()
                    AI=True
            if AI:
                game.status='AI BLUE'
                game.kavdi_background(window)
                game.kavdi_control_background(window)
                time.sleep(0.5)
                temp=[]
                for i in player.kavdi_item_pos:
                    if i[0][0:2]=='p3':
                        temp.append([i[0],i[1]])
                temp_int=random.randint(0,3)
                player.kavdi_selecting_val=temp[temp_int]
                player.kavdi_dice_roll('first')
                player.kavdi_selecting()
                
                game.status='AI RED'
                game.kavdi_background(window)
                game.kavdi_control_background(window)
                time.sleep(0.5)
                temp=[]
                for i in player.kavdi_item_pos:
                    if i[0][0:2]=='p1':
                        temp.append([i[0],i[1]])
                temp_int=random.randint(0,3)
                player.kavdi_selecting_val=temp[temp_int]
                player.kavdi_dice_roll('first')
                player.kavdi_selecting()
                
                game.status='AI GREEN'
                game.kavdi_background(window)
                game.kavdi_control_background(window)
                time.sleep(0.5)
                temp=[]
                for i in player.kavdi_item_pos:
                    if i[0][0:2]=='p2':
                        temp.append([i[0],i[1]])
                temp_int=random.randint(0,3)
                player.kavdi_selecting_val=temp[temp_int]
                player.kavdi_dice_roll('first')
                player.kavdi_selecting()
                AI=False
                game.status='YOUR TURN'
                
            for i in player.kavdi_data:
                if i[0]==13:
                    count=0
                    for j in i[1]:
                        if j[0:2]=='p1':
                            count=count+1
                    if count==4:
                        kavdi_run=False
                    count=0
                    for j in i[1]:
                        if j[0:2]=='p2':
                            count=count+1
                    if count==4:
                        kavdi_run=False
                    count=0
                    for j in i[1]:
                        if j[0:2]=='p3':
                            count=count+1
                    if count==4:
                        kavdi_run=False
                    count=0
                    for j in i[1]:
                        if j[0:2]=='p4':
                            count=count+1
                    if count==4:
                        kavdi_run=False
                
                
        
            
                    
        clock.tick(fps)
                   
main()
pygame.display.quit()
        
        
        
        
        
