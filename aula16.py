import pygame

pygame.init()

tamanho = 500,500
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('jogo ping pong')

BEJE = (245,222,179)
PRETA = (0,0,0)

raquete1_x,raquete1_y = 50,225
raquete2_x,raquete2_y = 450,250

ball_x, ball_y = 250,250

velocidade_bola_x = 0.3
velocidade_raquete = 0.3
velocidade_bola_y = 0.3

raquete_altura, largura_raquete = 20,150
bola_largura, bola_altura = 20,20

placar1 = 0
placar2 = 0

font = pygame.font.SysFont(None,55)


def desenhar():
    tela.fill(BEJE)

    pygame.draw.rect(tela, PRETA,(raquete1_x,raquete1_y, raquete_altura, largura_raquete ))
    pygame.draw.rect(tela, PRETA,(raquete2_x,raquete2_y, raquete_altura, largura_raquete ))
    pygame.draw.ellipse(tela, PRETA,(ball_x, ball_y, bola_largura, bola_altura))

    placar_texto = font.render(f' {placar1}   |   {placar2} ', True, BEJE)

    tela.blit(placar_texto,(200,20) )


LOOP = True
while LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LOOP == False
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500:
        raquete1_y += velocidade_raquete

    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500:
        raquete2_y += velocidade_raquete  

    ball_x += velocidade_bola_x
    ball_y += velocidade_bola_y

    if ball_y <= 2 or ball_y >= 496:
        velocidade_bola_y = -velocidade_bola_y
    
    if (raquete1_x < ball_x < raquete1_x + largura_raquete) and (raquete1_y < ball_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if (raquete2_x < ball_x < raquete2_x + largura_raquete) and (raquete2_y < ball_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x


    if ball_x > 500:
       placar1 =+ 1
    #   ball_x, ball_y = 250,250
    

    if ball_x > 500:
       placar2 =+ 1
    #   ball_x, ball_y = 250,250

    desenhar()

    pygame.display.update()


pygame.quit()





