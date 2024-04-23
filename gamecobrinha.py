import pygame
import random

# Iniciando o pygame
pygame.init()

# Definindo cores (RGB)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
laranja = (255, 165, 0)
verde = (0, 255, 0)

# Definindo tamanho da tela do jogo (em pixels)
largura, altura = 600, 400
tela_jogo = pygame.display.set_mode((largura, altura))

# Definindo nome do jogo
pygame.display.set_caption('Jogo da Cobra')

# Definindo um relógio que mantém o tempo, o tamanho da cobra e a velocidade (em pixels)
relogio = pygame.time.Clock()
tamanho_cobra = 10
velocidade_cobra = 15

# Definindo a fonte ('nome da fonte', tamanho): escolha uma fonte de sua preferência
fonte_mensagem = pygame.font.SysFont('roboto', 30)
fonte_pontuacao = pygame.font.SysFont('roboto', 25)


# Função para atualizar a pontuação
def mostra_pontuacao(pontuacao):
    texto = fonte_pontuacao.render('Pontuação: ' + str(pontuacao), True, verde)
    tela_jogo.blit(texto, [0, 0])


# Função para desenhar a cobra (tamanho, movimento)
def desenha_cobra(tamanho_cobra, pixels_cobra):
    for pixel in pixels_cobra:
        pygame.draw.rect(tela_jogo, branco, [pixel[0], pixel[1], tamanho_cobra, tamanho_cobra])


# Função do funcionamento do jogo
def executar_jogo():
    jogo_acabou = False
    jogo_pausado = False

    # Posição inicial
    x = largura / 2
    y = altura / 2

    # Velocidade inicial
    velocidade_x = 0
    velocidade_y = 0

    # Tamanho da cobra. A lista vazia serve para definir o crescimento da cobra ao longo do jogo
    pixels_cobra = []
    comprimento_cobra = 1

    # Definindo a posição da comida
    comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10
    comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10

    # Loop do jogo
    while not jogo_acabou:

        while jogo_pausado:
            tela_jogo.fill(preto)
            mensagem_jogo_acabou = fonte_mensagem.render('Fim de Jogo!', True, vermelho)
            mensagem_sair = fonte_mensagem.render('Pressione Q para sair', True, vermelho)
            mensagem_reiniciar = fonte_mensagem.render('Pressione R para reiniciar', True, vermelho)
            tela_jogo.blit(mensagem_jogo_acabou, [largura / 3, altura / 3])
            tela_jogo.blit(mensagem_sair, [largura / 3, (altura / 3) + 30])
            tela_jogo.blit(mensagem_reiniciar, [largura / 3, (altura / 3) + 60])
            mostra_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        jogo_acabou = True
                        jogo_pausado = False
                    if event.key == pygame.K_r:
                        executar_jogo()
                if event.type == pygame.QUIT:
                    jogo_acabou = True
                    jogo_pausado = False

        # Estabelece as setas do teclado para movimentar a cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo_acabou = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -tamanho_cobra
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT:
                    velocidade_x = tamanho_cobra
                    velocidade_y = 0
                if event.key == pygame.K_UP:
                    velocidade_x = 0
                    velocidade_y = -tamanho_cobra
                if event.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = tamanho_cobra

        # Condição para fim de jogo caso a cobra bata na parede
        if x >= largura or x < 0 or y >= altura or y < 0:
            jogo_pausado = True

        # Faz a cobra se movimentar baseado na velocidade
        x += velocidade_x
        y += velocidade_y

        # Colocando a cor de fundo e posicionando os elementos na tela
        tela_jogo.fill(preto)
        pygame.draw.rect(tela_jogo, laranja, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])

        pixels_cobra.append([x, y])

        if len(pixels_cobra) > comprimento_cobra:
            del pixels_cobra[0]

        for pixel in pixels_cobra[:-1]:
            if pixel == [x, y]:
                jogo_pausado = True

        desenha_cobra(tamanho_cobra, pixels_cobra)
        mostra_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_cobra) / 10.0) * 10
            comida_y = round(random.randrange(0, altura - tamanho_cobra) / 10.0) * 10
            comprimento_cobra += 1

        relogio.tick(velocidade_cobra)

    pygame.quit()
    quit()


executar_jogo()
