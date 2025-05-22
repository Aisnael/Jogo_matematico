# 1- Importar as bibliotecas 
'''
Biblioteca:
pygame - usada para criar o jogo(desenhar, som, eventos).
sys - usada para encerrar o programa de forma segura.
'''
import pygame
import sys 

# 2- Inicializar o Pygame
'''
Essa lina inicializa todos os módulos do Pygame
'''
pygame.init()

# 3- Configurações da tela
screen_width = 1920
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("JOGO MATEMÁTICO - Raciocínio Lógico e Matemática Básica ")

# 4- Definir as cores - RGB (vermelho, verde e azul)
preto = (0, 0, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)

# 5- Configurações do jogador
player_size = 50
player_x = screen_width // 2 # Dividindo a largura da tela ao meio - posição inicial(horizontal)
player_y = screen_height // 2 # Dividindo a altura da tela ao meio - posição inicial(vertical)
player_speed = 1 # Velocidade de movimento

# 5.1 -Margem interna para criar o efeito no jogador
margem = 15

# 6- Loop principal do jogo
while True:
    # 6.1 - Verifica os eventos (ex: fechar a janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 6.2 - Preencher o fundo da tela
    screen.fill(preto) # cor de fundo

    # 6.3 - Desenhar o jogador(quadrado externo)
    pygame.draw.rect(screen, azul, (player_x, player_y, player_size, player_size))

    # 6.4 - Desenha o quadrado interno 
    pygame.draw.rect(screen, branco, (player_x + margem, player_y + margem, player_size - 2 * margem, player_size - 2 * margem))

    # 6.5 - Atualizar a tela
    pygame.display.flip()

    # 6.6 - Adicionando movimento
    ''' Detectar teclas pressionadas'''
    teclas = pygame.key.get_pressed() # Verifica o estado atual das teclas
    if teclas [pygame.K_LEFT]: # seta p/ esquerda
        player_x -= player_speed
    elif teclas[pygame.K_RIGHT]: # seta p/ direita
        player_x += player_speed
    elif teclas[pygame.K_UP]: # seta p/ cima
        player_y -= player_speed
    elif teclas[pygame.K_DOWN]: # seta p/ baixo
        player_y += player_speed
    
    # 7- Litador de movimento nas bordas da tela
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_size:
        player_x = screen_width - player_size
      
    if player_y < 0:
        player_y = 0
    elif player_y > screen_height - player_size:
        player_y = screen_height - player_size



