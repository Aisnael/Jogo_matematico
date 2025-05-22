# Jogo Matemático - Práticando em casa
# Jogo do Quadrado Matemático
- Um quadrado aparece na tela
- O jogador move ele com as setas
- Quando encosta em um "ponto de desafio", aparece uma conta matemática
- Se acertar, ganha ponto. Se errar, perde vida.

## Descrição 
Jogo educativo 2D feito em Python com a biblioteca Pygame, focado em desenvolver minha lógica de programação. Jogo para desenvolver raciocínio lógico e matemática básica para meus filhos haja vista que eles tem de 9 a 14 anos de idade.

## Passo a passo do desenvolvimento

### Etapa 1: Criar pasta e ambiente virtual - Comandos no Terminal

1- Criar a pasta do projeto direto no terminal:
- mkdir 02_Jogo_Matematico
- cd 02_Jogo_Matematico (entrar dentro da pasta)

2- Criar o ambiente virtual:
- python -m venv venv

3- Ativar o ambiente virtual:
- venv\Scripts\activate

### Etapa 2: Instalar o Pygame e criar o script inicial 

1- Com ambiente virtual ativado, instalar Pygame 
- pip install pygame

2- Criar aquivo de requisitos - requirements.txt
- pip freeze > requirements.txt

3- Criar a pasta src(source code) e dentro arquivo main para colocar todos códigos.py
- mkdir app
- main.py

### Etapa 3: Criar o jogador (um quadrado) e mover com as setas do teclado
--Obejtico dessa etapa:--
- Criar uma janela
- Criar um jogador (personagem)
- Mostrar um "personagem" na tela (Janela)
- Permitir movimentar ele com as setas do teclado
- Manter o jogo rodando lisinho

1- Configuração da Janela
- screen_width (largura tela)
- screen_height (altura tela)
- pygame.display.set_mode(''): cria a janela do jogo
- set_caption(''): define o título da janela

2- Configurações do Jogador
- tamanho do jogador
- posição inicial na tela
- velocidade de movimento

3- Adicionando movimento
- Com pygame.key.get_pressed() retorna uma lista com o estado de todas as teclas do teclado (se estão pressinadas ou não)
- Se a tecla seta para esquerda (K_LEFT) estiver pressionada, subtraímos (player_speed) velocidade movimento da posição
horizontal(player_x). Isso faz o jogador andar para esquerda, porque no sistema de coordenadas do Pygame, o eixo X cresce da esquerda para a direita.
- Se a tecla direita (K_RIGHT) estiver pressionada, somamos a velocidade para mover o jogador para a direita.
- Se a tecla para cima(K_UP) estiver pressionada, subtraímos o valor de (player_y), porque no Pygame o eixo Y cresce de cima para baixo — então, diminuir Y faz o jogador subir.(player_y -= player_speed)
- Se a tecla para baixo(K_DOWN) estiver pressionada, somamos o valor de (player_y), movendo o jogador pra baixo na tela.(player_y += player_speed)

