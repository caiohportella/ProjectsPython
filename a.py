import pygame as pg
from random import randint, choice


class player(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = int((x - width) / 2)
        self.y = int(y*0.75)
        self.walk = 9
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = [pg.image.load('sprites/R1.png'), pg.image.load('sprites/R2.png'), pg.image.load('sprites/R3.png'), 
                    pg.image.load('sprites/R4.png'), pg.image.load('sprites/R5.png'), pg.image.load('sprites/R6.png'), 
                    pg.image.load('sprites/R7.png'), pg.image.load('sprites/R8.png'), pg.image.load('sprites/R9.png')]
        self.walkLeft = [pg.image.load('sprites/L1.png'), pg.image.load('sprites/L2.png'), pg.image.load('sprites/L3.png'), 
                    pg.image.load('sprites/L4.png'), pg.image.load('sprites/L5.png'), pg.image.load('sprites/L6.png'), 
                    pg.image.load('sprites/L7.png'), pg.image.load('sprites/L8.png'), pg.image.load('sprites/L9.png')]
        self.char_img = pg.image.load('sprites/R1.png')
        self.char_img = pg.transform.scale(self.char_img, [self.width, self.height])
        for i in range(len(self.walkRight)):
            self.walkRight[i] = pg.transform.scale(self.walkRight[i], [self.width, self.height])
            self.walkLeft[i] = pg.transform.scale(self.walkLeft[i], [self.width, self.height])

        
    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            screen.blit(self.char_img, (self.x,self.y))


class connector(object):
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y        
        self.vel = 6

    def create_draw(self, screen, item):
        screen.blit(item, (int(self.x),int(self.y)))



def life():
    pass

def mission():
    pass        

# def define_item(fase):
#     if fase in [1,2]:
#         itens = {"*":pg.image.load('sprites/and.png'), "+":pg.image.load('sprites/or.png'), "!":pg.image.load('sprites/not.png'), 
#                 "A":pg.image.load('sprites/A.png'), "B":pg.image.load('sprites/B.png')}
#         itens["B"] = pg.transform.scale(itens["B"], [60,60])
#     else:
#         itens = {"*":pg.image.load('sprites/and.png'), "+":pg.image.load('sprites/or.png'), "!":pg.image.load('sprites/not.png'), 
#                 "A":pg.image.load('sprites/A.png'), "B":pg.image.load('sprites/B.png'), "C":pg.image.load('sprites/C.png')}
#         itens["B"] = pg.transform.scale(itens["B"], [60,60])
#         itens["C"] = pg.transform.scale(itens["C"], [60,60])    
#     return itens

# def fases(fase):
#     respostas = []
#     itens = []
#     if fase == 1:
#         respostas = [["+"], ["*"], ["!"], ["A"], ["B"]]
#         itens = define_item(fase)
#     elif fase == 2:
#         respostas = [["A", "+", "B"],
#                      ["A", "*", "B"],
#                      ["A", "+", "!", "B"],
#                      ["A", "*", "!", "B"],
#                      ["!", "A", "*" , "!", "B"]]
#         itens = define_item(fase)
#     elif fase == 3:
#         respostas = [["A", "*", "B" ,"+" ,"C"],
#                      ["!","A", "+", "C", "*", "!","A" ,"+" ,"B"],
#                      ["A", "*", "C", "+", "B", "*", "!", "C"],
#                      ["!", "C", "*", "A", "+", "B"],
#                      ["B", "+", "!", "A", "*", "!", "C"]]
#         itens = define_item(fase)
#     elif fase == 4:
#         respostas = [["A","*","B", "+", "!","A","*","!","B","*","C"],
#                      ["A","*","!","B","*","!","C"],
#                      ["B","!","A","+","A", "+", "A","!","C"],
#                      ["A","*","!","B", "+", "!","A","*","B", "+", "C"],
#                      ["!","A","+","B", "*" ,"B","*","!","C"]]
#         itens = define_item(fase)
        
#     elif fase == 5:
#         respostas = [["E", "+", "!", "A", "*", "B", "*", "!","C"],
#                      ["!", "A", "!", "B", "+", "A", "*", "B" + "!", "C"],
#                      ["!", "A", "*", "!","C", "+", "!","B","*","C"],
#                      ["!", "A", "+", "!", "B", "*", "C", "*","!", "B"],
#                      ["A","*","B", "+" ,"A","*","B","*","C", "+", "!","A","*","!","B","*","C"]]
#         itens = define_item(fase)
#     return respostas, itens
        
def redraw(char, screen, conns, tipos, itens):
    screen.fill((0,0,0))
    char.draw(screen)
    for i in range(len(conns)):
        conns[i].create_draw(screen, itens[tipos[i]])
    pg.display.update() 
    
def create_conn(start_x, start_y, screen_width, conns, dimension):
    conn_x = randint(start_x,screen_width-start_x)
    for j in conns:
        while conn_x <= j.x + 60 and conn_x >= j.x - 60:
            lugar = randint(start_x,screen_width-start_x)
    return connector(conn_x, start_y, dimension,dimension)
        
def jogar():
    screen_height = 800
    screen_width = 600
    start_y = -60
    start_x = 30
    conn_d = 60
    delay = 30
    itens = {"*":pg.image.load('sprites/and.png'), "+":pg.image.load('sprites/or.png'), "!":pg.image.load('sprites/not.png'), 
             "A":pg.image.load('sprites/A.png'), "B":pg.image.load('sprites/B.png'), "C":pg.image.load('sprites/C.png')}
    itens["B"] = pg.transform.scale(itens["B"], [conn_d,conn_d])
    itens["C"] = pg.transform.scale(itens["C"], [conn_d,conn_d])
    conns = []
    conn_type = []
    conn = connector(randint(start_x,screen_width-start_x), start_y, conn_d,conn_d)
    char = player(screen_width, screen_height, 80, 100)
    pg.init()
    screen = pg.display.set_mode((screen_width,screen_height))
    pg.display.set_caption("Space Bools")
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(27)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False       
        for i in conns:
            if i.y <= char.y + char.height - start_y:
                i.y += i.vel
            if (char.y <= i.y + (conn_d/2) and i.y <= char.y + char.height and char.x <= i.x + (conn_d/2) and i.x <= char.x + char.width) or (i.y >= char.y + char.height):
                conn_type.pop(conns.index(i))
                conns.pop(conns.index(i))
                conns.append(create_conn(start_x, start_y, screen_width, conns, create_conn))
                conn_type.append(choice(list(itens.keys())))
                 
        if len(conns) < len(itens) + 1 and delay == 30:
            delay = 0
            conns.append(create_conn(start_x, start_y, screen_width, conns, create_conn))
            conn_type.append(choice(list(itens.keys())))
        delay +=1 
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and char.x > 5: 
            char.x -= char.walk
            char.right = False
            char.left = True
        elif keys[pg.K_RIGHT] and char.x < screen_width - char.width - 5:  
            char.x += char.walk
            char.right = True 
            char.left = False
        else: 
            char.right = False
            char.left = False
            char.walkCount = 0
            
        redraw(char, screen, conns, conn_type, itens)
        conn.y += conn.vel   
jogar()