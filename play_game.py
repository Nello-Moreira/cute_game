import pygame
from pygame.sprite import Group
from src.configs import Configuracoes
from src.player import Player
# import jogo_coracao.coracao as coracao
import src.game_functions as game_func


def play_game():
    # Iniciando o pygame
    pygame.init()

    # Instanciando as configuracoes que serao usadas
    cfg = Configuracoes()

    # Criando a tela
    tela = pygame.display.set_mode([cfg.tela_largura, cfg.tela_altura])
    tela_ret = tela.get_rect()
    pygame.display.set_caption(cfg.tela_titulo)
    pygame.display.set_icon(pygame.image.load(cfg.tela_icone))

    # Instanciando o player
    lavi = Player(cfg, tela_ret)

    # Cria um container de coracao
    coracoes = Group()

    # Cria um contador de loops para atirar o coracao
    loops = 0

    while True:
        # Frames
        cfg.relogio.tick(cfg.fps)

        # Checa eventos
        game_func.verifica_eventos(lavi)

        # Atira um coracao
        game_func.atira_coracao(cfg, coracoes, tela_ret, loops, lavi)

        # Atualiza as posicoes e tela
        game_func.atualiza_tela(tela, lavi, coracoes, cfg)

        # Apaga os coracoes que entraram em contato com a lavinia
        game_func.apaga_coracao(coracoes, lavi)

        loops += 1


play_game()
