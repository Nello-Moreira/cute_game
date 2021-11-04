from pygame.sprite import Sprite
from random import choice


class Coracao(Sprite):

    contador_coracoes = 0

    def __init__(self, config, tela_ret):
        super().__init__()
        Coracao.contador_coracoes += 1

        # Imagem
        self.imagem = config.coracao
        self.ret = self.imagem.get_rect()

        # Posicao ao longo do jogo
        self.ret.centerx = int(tela_ret.right - self.ret.width / 2)
        self.ret.centery = int(choice(range((0 + config.coracao_altura // 2),
                                            (config.tela_altura - config.coracao_altura // 2))))

    def movimenta(self, config):
        self.ret.centerx -= config.coracao_velocidade

    def desenha(self, tela, config):
        self.movimenta(config)
        tela.blit(self.imagem, self.ret)
