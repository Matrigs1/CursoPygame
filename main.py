import pygame, sys
from pygame.locals import *
from random import randint

# Inicia o pygame.
pygame.init()

# Dá load, ajusta o volume e toca uma música.
musica_de_fundo = pygame.mixer.music.load('assets/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1) # Vai tocar em repetição.

# Som para uma colisão. É o som que irá tocar quando um evento ocorrer.
barulho_colisao = pygame.mixer.Sound('assets/smw_coin.wav')
barulho_colisao.set_volume(0.5)

#Definindo a altura e largura da tela.
altura, largura = 720, 1280
# Achando o meio da tela ao dividir a largura por 2 e subtraindo ao tamanho do objeto / 2 (o meio do objeto).
x_cobra = (largura / 2) - 200/2
# Meio da tela em altura.
y_cobra = altura / 2

# Velocidade de movimento da cobra
velocidade = 7
# X se desloca conforme a velocidade
x_controle = velocidade
y_controle = 0

# Posições alteatórias dentro do escopo da tela para o segundo ellipse.
x_maca = randint(30, 1250)
y_maca = randint(30, 690)

# Acumulativa
pontos = 0
# Definindo fonte para ser exibida
fonte = pygame.font.SysFont('arial', 34, True, False)

# Passando largura e altura para a janela.
tela = pygame.display.set_mode((largura, altura))
# Setando o nome do jogo
pygame.display.set_caption('Snake Game')
# Um clock para o framerate do jogo.
relogio = pygame.time.Clock()

lista_cobra = []

# Definindo o comprimento inicial da cobra
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    # Para cada X e Y dentro do array da cobra
    for XeY in lista_cobra:
        # Renderizar esse retângulo
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 30, 30))

# Função que reinicia o game se a cobra colidir com ela mesma.
def reiniciar_jogo():
    # Tornando essas variáveis globais (para que seus valores sejam resetados).
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = (largura / 2) - 200/2
    y_cobra = altura / 2
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(30, 1250)
    y_maca = randint(30, 690)
    morreu = False


while True:
    #Colocando o game em 60 frames.
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

        # Se a tecla pressionada for.
        if event.type == KEYDOWN:
            if event.key == K_a:
                # Impossibilita a tecla de assumir o valor para direita. Que é sempre positivo.
                if x_controle == velocidade:
                    pass
                else:
                # Se for negativo (como deveria), assume esse valor para x e y passa a valer 0.
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    # Se a tecla estiver pressionada.
    '''
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20  
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20  
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20  
    '''

    # Posições da cobra assumem x e y controle.
    x_cobra += x_controle
    y_cobra += y_controle

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
        comprimento_inicial +=  1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    # Se a cabeça da cobra tentar assumir uma posição já existente dentro da sua lista, significa uma colisão com ela própria. É game over.
    if lista_cobra.count(lista_cabeca) > 1:
        fonte_2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente.'
        texto_formatado = fonte_2.render(mensagem, True, (0, 0, 0))
        # Joga o texto em um retângulo, para manipular o seu posicionamento.
        ret_texto = texto_formatado.get_rect()

        # Morreu passa a ser verdadeiro.
        morreu = True
        while morreu:
            # Limpa a tela novamente
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # Se o jogador pressionar R, reinicia o jogo.
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            # Centraliza o texto
            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    # Se o eixo x (horizontal) ultrapassar a largura para a direita (1280) = zera o eixo.
    if x_cobra > largura:
        x_cobra = 0
    # Se o eixo x ultrapassar a largura para a esquerda (0) = seta ele para o valor da largura (1280).
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    # Se o tamanho da cobra for maior que o comprimento inicial, deleta a primeira posição do array.
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    # E aumenta a cobra.
    aumenta_cobra(lista_cobra) 

    # Coloca na tela o texto, com a sua devida posição.
    tela.blit(texto_formatado, (1100, 40))
    # Faz um update na tela.
    pygame.display.update()