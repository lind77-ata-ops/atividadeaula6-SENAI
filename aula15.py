import pygame
pygame.init()
tela  = pygame.display.set_mode((300,300))



         
run = True         
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
            pygame.quit()
    tela.fill('green') 
    pygame.draw.rect(tela,('red'),(150,150,70,70))
    pygame.display.flip()      
                   

