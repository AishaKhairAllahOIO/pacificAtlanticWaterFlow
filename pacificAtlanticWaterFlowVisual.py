import pygame

CELL_SIZE=100
BORDER_SIZE=80
FONT_SIZE=30
PACIFIC_COLOR=(0,0,254)
ATLANTIC_COLOR=(102,178,254)
BOTH_COLOR=(255,242,207)
NEITHER_COLOR=(255,255,255)
GRID_COLOR=(0,0,0) 
TEXT_COLOR=(0,0,0)

def visualSolution(island,pacific,atlantic):
    
    pygame.init()

    rows,cols=len(island),len(island[0])
    width=cols*CELL_SIZE+2*BORDER_SIZE
    height=rows*CELL_SIZE+2*BORDER_SIZE

    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Pacific Atlantic Visualization")
    font=pygame.font.SysFont('Arial',FONT_SIZE)
    label_font=pygame.font.SysFont('Arial',35,bold=False)

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen,PACIFIC_COLOR,(0,0,width-BORDER_SIZE,BORDER_SIZE)) 
    pygame.draw.rect(screen,PACIFIC_COLOR,(0,0,BORDER_SIZE,height-BORDER_SIZE))
    pacific_label=label_font.render("PACIFIC OCEAN",True,(0,0,0))
    screen.blit(pacific_label,(20,30))

    pygame.draw.rect(screen,ATLANTIC_COLOR,(width-BORDER_SIZE,0,BORDER_SIZE,height))
    pygame.draw.rect(screen,ATLANTIC_COLOR,(0,height-BORDER_SIZE,width,BORDER_SIZE))  
    atlantic_label=label_font.render("ATLANTIC OCEAN",True,(0,0,0))
    screen.blit(atlantic_label,(width-BORDER_SIZE-180,height-BORDER_SIZE+30))

    for r in range(rows):
        for c in range(cols):
            x=c*CELL_SIZE+BORDER_SIZE
            y=r*CELL_SIZE+BORDER_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if (r, c) in pacific and (r, c) in atlantic:
                color=BOTH_COLOR
            else:
                color=NEITHER_COLOR

            pygame.draw.rect(screen,color,rect)
            pygame.draw.rect(screen,GRID_COLOR,rect,1)
            text=font.render(str(island[r][c]),True,TEXT_COLOR)
            text_rect=text.get_rect(center=(x+CELL_SIZE/2,y+CELL_SIZE/2))
            screen.blit(text,text_rect)

    pygame.display.flip()

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

    pygame.quit()