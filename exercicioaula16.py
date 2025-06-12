# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




# são 2 variáveis  de altura e largura
largura, altura = 400, 400

# 1  variavel atribuido a ela uma função, criando a tela 
tela = pygame.display.set_mode((largura, altura))


# titulo da tela 
# módulo > submodulo > função 
pygame.display.set_caption("Labirinto")

# Tupla 
preto = (0, 0, 0)
# Tupla 
branco = (255, 255, 255)

# Tupla
vermelho = (255, 0, 0)

# variável
tamanho_celula = 40

# é lista / matriz
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# variável x 
x, y = 1 * tamanho_celula, 1 * tamanho_celula
# variavel 
velocidade = 40



# função
def desenhar_labirinto():
    # loop aninhado 
    # ninho loops
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            # variável que atribuida a uma lista 
            cor = preto if labirinto[linha][coluna] == 1 else branco
            # desenhando um retangulo na tela
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# loop 
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Script que mostra a utilização do teclado do computador
    teclas = pygame.key.get_pressed()

    # condicional 
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        # condicional  
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    # fjnção para preencher a tela
    tela.fill(branco)

    # chamando a função labirinto para desenhar o labiririnto
    desenhar_labirinto()
    # desenhando um retangulo
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    #  atualização da tela 
    pygame.display.flip()

    # contagem de quadros
    pygame.time.Clock().tick(10)

# função de saída 
pygame.quit()
