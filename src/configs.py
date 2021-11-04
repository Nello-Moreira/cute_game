import pygame


class Configuracoes():
    def __init__(self):
        # Tela
        self.tela_largura = 1300
        self.tela_altura = 600
        self.tela_cor = [255, 255, 255]
        self.tela_titulo = 'Jogo fofo'
        self.tela_icone = './assets/coracao.png'
        self.tela_texto_cor = [0, 0, 0]
        self.tela_texto_fonte = 'Times New Roman'
        self.tela_texto_tamanho = 25

        # Jogo
        self.fps = 60
        self.relogio = pygame.time.Clock()

        # Dificuldade
        self.coracao_velocidade = 5
        self.coracao_velocidade_aumento = 1
        self.coracao_aumento_velocidade = 3  # A cada "x" coracoes, a velocidade do coracao vai aumentar
        self.coracao_aumento_disparo = 7  # A cada "x" coracoes, a velocidade do disparo de coracao vai aumentar
        self.loops = 100   # A cada "x" loops atira um coracao
        self.loops_aumento = -5   # Cada vez que aumentar a taxa de disparo, é aumentada em "x" loops

        # Coracao
        self.coracao_imagem = pygame.image.load('./assets/coracao.png')
        self.coracao_escala = 0.2
        self.coracao_largura = int(self.coracao_imagem.get_width() * self.coracao_escala)
        self.coracao_altura = int(self.coracao_imagem.get_height() * self.coracao_escala)
        self.coracao = pygame.transform.scale(self.coracao_imagem, (self.coracao_largura, self.coracao_altura))

        # Jogador
        self.jogador_imagem = pygame.image.load('./assets/lavi.jpg')
        self.jogador_escala = 0.075
        self.jogador_largura = int(self.jogador_imagem.get_width() * self.jogador_escala)
        self.jogador_altura = int(self.jogador_imagem.get_height() * self.jogador_escala)
        self.jogador = pygame.transform.scale(self.jogador_imagem, (self.jogador_largura, self.jogador_altura))
        self.jogador_velocidade = 10

        # Gabriel
        self.gabriel_imagem = pygame.image.load('./assets/manda_beijo.jpg')
        self.gabriel_escala = 0.047
        self.gabriel_largura = int(self.gabriel_imagem.get_width() * self.gabriel_escala)
        self.gabriel_altura = int(self.gabriel_imagem.get_height() * self.gabriel_escala)
        self.gabriel = pygame.transform.scale(self.gabriel_imagem, (self.gabriel_largura, self.gabriel_altura))

        # Perdeu
        self.perdeu_imagem = pygame.image.load('./assets/perdeu_jogo.jpg')
        self.perdeu_escala = 0.15
        self.perdeu_largura = int(self.perdeu_imagem.get_width() * self.perdeu_escala)
        self.perdeu_altura = int(self.perdeu_imagem.get_height() * self.perdeu_escala)
        self.perdeu = pygame.transform.scale(self.perdeu_imagem, (self.perdeu_largura, self.perdeu_altura))
