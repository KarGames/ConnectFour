import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 700, 600
ROWS, COLS = 7, 6
FPS = 60
BACKGROUND_COLOR = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

board = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""]
]

dropCol = None
player = "red"
coinDropped = False
running = True
win = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def drawBoardLines():
    for row in range(ROWS):
        pygame.draw.line(screen, (255, 255, 255), (row*100, 0), (row*100, screen.get_height()), 1)
    for col in range(COLS):
        pygame.draw.line(screen, (255, 255, 255), (0, col*100), (screen.get_width(), col*100), 1)
    
#check where player wants to drop piece and puts correct player value in that location
def handleDrop():
        if dropCol != None and coinDropped:
            row = 5
            try:
                while board[row][dropCol-1] != "": 
                    row-=1
                board[row][dropCol-1] = player
            except IndexError:
                pass
        
def drawPieces():
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == "red":
                pygame.draw.rect(screen, RED, pygame.Rect(x * 100, y * 100, 100, 100))
                
            elif col == "yellow":
                pygame.draw.rect(screen, YELLOW, pygame.Rect(x * 100, y * 100, 100, 100))

def checkWin():
    playerVal = ""
    if player == "red":
        playerVal = "yellow"
    elif player == "yellow":
        playerVal = "red"
    
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            try:
                #check horizontal win
                if x <= 3 and col == row[x+1] == row[x+2] == row[x+3] == playerVal:
                    print(f"{playerVal} Wins!")
                    return True
                #check vertical win
                elif y <= 3 and col == board[y+1][x] == board[y+2][x] == board[y+3][x] == playerVal:
                    print(f"{playerVal} Wins!")
                    return True
                    
                #check negative slope diagonal win
                elif board[y][x] == board[y+1][x+1] == board[y+2][x+2] == board[y+3][x+3] == playerVal:
                    print(f"{playerVal} Wins!")
                    return True
                
                #check positive slope diagonal win
                elif board[y][x] == board[y+1][x-1] == board[y+2][x-2] == board[y+3][x-3] == playerVal:
                    print(f"{playerVal} Wins!")
                    return True
                
            except IndexError:
                pass
                

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check where player chooses to place piece
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                dropCol = 1
                coinDropped = True
            if event.key == pygame.K_2:
                dropCol = 2
                coinDropped = True
            if event.key == pygame.K_3:
                dropCol = 3
                coinDropped = True
            if event.key == pygame.K_4:
                dropCol = 4
                coinDropped = True
            if event.key == pygame.K_5:
                dropCol = 5
                coinDropped = True
            if event.key == pygame.K_6:
                dropCol = 6
                coinDropped = True
            if event.key == pygame.K_7:
                dropCol = 7
                coinDropped = True
        
    screen.fill(BACKGROUND_COLOR)
    
    handleDrop()
    drawPieces()
    drawBoardLines()
    if checkWin():
        running = False
    
    #switch player turn
    if coinDropped:
        if player == "red":
            player = "yellow"
        elif player == "yellow":
            player = "red"
        coinDropped = False
        
    pygame.display.flip()
        
pygame.quit()