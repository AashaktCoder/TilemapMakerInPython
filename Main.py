import pygame
from Button import Button

pygame.init()

def Text(win, x, y, font, color, size, msg):
    font = pygame.font.SysFont(font, size)
    txt = font.render(msg, True, color)
    win.blit(txt, (x, y))

class Grid:
    def __init__(self, win):
        self.size = 500
        self.tileSize = 50

        self.win = win

        self.gridList = [[],[],[],[],[],[],[],[],[],[]]
        for j in self.gridList:
            for i in range(10): j.append('0')

        self.BlockColor = [255, 255, 255]
        self.BlockNum = 0
        self.BlockColorList = [[self.BlockColor, f"{self.BlockNum}"]]

        self.TileButton = Button(self.win, 510, 10, 230, 50, (0, 155, 255), (0, 125, 255), lambda: Text(self.win, 515, 22, "Aerial", (255, 255, 255), 38, "Change Tile Size"), 0, 10, self.ChangeTileSize)

        self.ColorButton = Button(self.win, 510, 80, 230, 50, (0, 155, 255), (0, 125, 255), lambda: Text(self.win, 535, 92, "Aerial", (255, 255, 255), 38, "New Color"), 0, 10, self.NewColor)

        self.SelectButton = Button(self.win, 510, 150, 230, 50, (0, 155, 255), (0, 125, 255), lambda: Text(self.win, 535, 162, "Aerial", (255, 255, 255), 38, "Select Color"), 0, 10, self.SelectColor)

        self.OutputButton = Button(self.win, 510, 220, 230, 50, (0, 155, 255), (0, 125, 255), lambda: Text(self.win, 535, 232, "Aerial", (255, 255, 255), 38, "Make Grid"), 0, 10, lambda: print(self.gridList))

    def DrawGrid(self):
        for i in range(self.size//self.tileSize):
            for j in range(self.size//self.tileSize):
                pygame.draw.rect(self.win, (0, 0, 0), [i*self.tileSize, j*self.tileSize, self.tileSize, self.tileSize], 1)
        
        for Y, rows in enumerate(self.gridList):
            for X, blocks in enumerate(rows):
                x = X*self.tileSize
                y = Y*self.tileSize
                for BlockClr in self.BlockColorList:
                    if blocks == BlockClr[1]:
                        self.Block = pygame.draw.rect(self.win, BlockClr[0], [x+1, y+1, self.tileSize-2, self.tileSize-2])

        self.ColorButton.Update()
        self.TileButton.Update()
        self.SelectButton.Update()
        self.OutputButton.Update()

    def ChangeTileSize(self):
        self.tileSize = int(input("Enter new Tile Size: "))
        self.gridList = []
            
        for i in range(500//self.tileSize):
            self.gridList.append([])
        for j in self.gridList:
            for i in range(500//self.tileSize):
                j.append('')

    def PlaceBlock(self):
        mouse = pygame.mouse.get_pos()

        if 0 < mouse[0] < 500:
                self.gridList[(mouse[1]//self.tileSize)][(mouse[0]//self.tileSize)] = f'{self.BlockNum}'

    def NewColor(self):
        self.BlockColor = []
        for i in range(3):
            self.BlockColor.append(int(input("Enter new Block Color: ")))

        if not(str(self.BlockColor) in str(self.BlockColorList)):
            self.BlockNum += 1
            self.BlockColorList.append([self.BlockColor, f"{self.BlockNum}"])
        
        print(self.BlockColorList)
    
    def SelectColor(self):
        self.BlockNum = int(input("Enter Color Number: "))

        for num in self.BlockColorList:
            if num[0] == self.BlockNum:
                self.BlockColor = num[1]

    def Update(self):
        self.DrawGrid()
        if pygame.mouse.get_pressed()[0]: self.PlaceBlock()

class Window:
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height

        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

        self.run = True

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.grid = Grid(self.win)

        self.UpdateList = [self.grid]

    def Loop(self):
        while self.run:
            self.win.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

            for i in self.UpdateList: i.Update()
            pygame.display.update()
            self.clock.tick(self.FPS)

    def Update(self):
        self.Loop()

window = Window(750, 500, "Tilemap Maker")
window.Update()