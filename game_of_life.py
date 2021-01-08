import random, pygame

def main():
    width = 100
    height = 70
    cell_size = 10
    pygame.init()
    screen = pygame.display.set_mode((width*cell_size, height*cell_size))
    pygame.display.set_caption("game of life")
    done = False
    cells = [[random.randrange(2) for i in range(width)] for j in range(height)]

    def update():
        new = [[0 for i in range(width)] for j in range(height)]
        for x in range(width):
            for y in range(height):
                val = sum([cells[j%height][i%width] for i in range(x-1,x+2) for j in range(y-1,y+2) if (i,j)!=(x,y)])
                if val == 2 and cells[y][x] or val == 3:
                    new[y][x] = 1
        return new
    
    while not done:
        if any([event==pygame.QUIT for event in pygame.event.get()]):done = True
        screen.fill((0,0,0))
        for x in range(width):
            for y in range(height):
                if cells[y][x]:
                    pygame.draw.rect(screen, (255,0,0), (x*cell_size, y*cell_size, cell_size, cell_size))
        pygame.display.flip()
        cells = update()
        pygame.time.wait(10)
        
if __name__=="__main__":
    main()
    pygame.quit()
