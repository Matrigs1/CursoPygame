import pygame, sys
from pygame.locals import *
from random import randint

# Inicia o pygame.
pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('assets/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('assets/smw_coin.wav')
barulho_colisao.set_volume(0.5)

#Definindo a altura e largura da tela.
altura, largura = 720, 1290
# Achando o meio da tela ao dividir a largura por 2 e subtraindo ao tamanho do objeto / 2 (o meio do objeto).
x_cobra = (largura / 2) - 200/2
# Meio da tela em altura.
y_cobra = altura / 2

# Posições alteatórias dentro do escopo da tela para o segundo ellipse.
x_maca = randint(100, 1180)
y_maca = randint(100, 620)

# Acumulativa
pontos = 0
# Definindo fonte para ser exibida
fonte = pygame.font.SysFont('arial', 34, True, False)

# Passando largura e altura para a janela.
tela = pygame.display.set_mode((largura, altura))
# Setando o nome do jogo
pygame.display.set_caption('Jogo')
# Um clock para o framerate do jogo.
relogio = pygame.time.Clock()

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 30, 30))

lista_cobra = []

while True:
    #Colcoando o game em 60 frames.
    relogio.tick(60)
    # Enche a tela com branco a cada iteração (limpa a tela).
    tela.fill((255, 255, 255))
    # Definindo a mensagem.
    mensagem = f'Pontos: {pontos}'
    # Renderizando a mensagem passada e a sua cor.
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    # Loop que escuta por eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            if event.key == K_s:
                y += 20
        '''

    # Se a tecla estiver pressionada.
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20  
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20  
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20  

    # Desenhando um ellipse na tela, de cor vermelha e com as coordenadas x e y no meio da tela.
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 30, 30))
    # Desenhando outro ellipse na tela, mas de cor azul e com as coordenadas aleatórias.
    maca = pygame.draw.rect(tela , (255, 0, 0), (x_maca, y_maca, 30, 30))

    # Se o ellipse vermelho collidir com o azul.
    if cobra.colliderect(maca):
        x_maca = randint(30, 1250) #Muda o x do azul para uma posição aleatória dentro do intervalo.
        y_maca = randint(30, 690) #O y também.
        pontos += 1 #Aumenta um ponto.
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra) 

    # Coloca na tela o texto, com a sua devida posição.
    tela.blit(texto_formatado, (1100, 40))
    # Faz um update na tela.
    pygame.display.update()