class Player:

    pontuacao = 0

    def __init__(self, config, tela_ret):
        # Imagem
        self.imagem = config.jogador
        self.ret = self.imagem.get_rect()

        # Movimentos
        self.velocidade_x = config.jogador_velocidade
        self.movimento_cima = False
        self.movimento_baixo = False
        self.movimento_esquerda = False
        self.movimento_direita = False

        # Posicao ao longo do jogo
        self.ret.centerx = int(tela_ret.left + self.ret.width / 2)
        self.ret.centery = int(tela_ret.centery)

    def movimenta(self, config):
        if self.movimento_cima and self.ret.top >= config.jogador_velocidade:
            self.ret.centery -= config.jogador_velocidade

        elif self.movimento_baixo and self.ret.bottom <= config.tela_altura - config.jogador_velocidade:
            self.ret.centery += config.jogador_velocidade

        elif self.movimento_esquerda and self.ret.left >= self.velocidade_x:
            self.ret.centerx -= self.velocidade_x

        elif self.movimento_direita and self.ret.right <= config.tela_largura - self.velocidade_x:
            self.ret.centerx += self.velocidade_x

    def desenha(self, tela, config):
        self.movimenta(config)
        tela.blit(self.imagem, self.ret)
