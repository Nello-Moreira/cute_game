import pygame
from sys import exit
from .heart import Coracao


def verifica_eventos(objeto):
    for event in pygame.event.get():
        # Fechar o jogo
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            botao_pressionado(event, objeto)

        elif event.type == pygame.KEYUP:
            botao_levantado(event, objeto)


def botao_pressionado(event, objeto):
    if event.key == pygame.K_UP:
        objeto.movimento_cima = True

    elif event.key == pygame.K_DOWN:
        objeto.movimento_baixo = True

    elif event.key == pygame.K_LEFT:
        objeto.movimento_esquerda = True

    elif event.key == pygame.K_RIGHT:
        objeto.movimento_direita = True


def botao_levantado(event, objeto):
    if event.key == pygame.K_UP:
        objeto.movimento_cima = False
    elif event.key == pygame.K_DOWN:
        objeto.movimento_baixo = False
    elif event.key == pygame.K_LEFT:
        objeto.movimento_esquerda = False
    elif event.key == pygame.K_RIGHT:
        objeto.movimento_direita = False


def atira_coracao(config, coracoes, tela_ret, loops, lavinia):
    if loops % config.loops == 0:
        coracao = Coracao(config, tela_ret)
        coracoes.add(coracao)

        # Aumenta a dificuldade
        if Coracao.contador_coracoes > 0 and Coracao.contador_coracoes % config.coracao_aumento_velocidade == 0:
            config.coracao_velocidade += config.coracao_velocidade_aumento
            lavinia.velocidade_x += config.coracao_velocidade_aumento
            config.jogador_velocidade += config.coracao_velocidade_aumento

        if Coracao.contador_coracoes > 0 and Coracao.contador_coracoes % config.coracao_aumento_disparo == 0:
            if config.loops + config.loops_aumento > 0:
                config.loops += config.loops_aumento


def apaga_coracao(coracoes, lavinia):
    for coracao in coracoes.sprites():
        if coracao.ret.colliderect(lavinia.ret):
            coracoes.remove(coracao)
            lavinia.pontuacao += 1


def verifica_perdeu(coracoes):
    for coracao in coracoes.sprites():
        if coracao.ret.left <= 0:
            return True
        else:
            return False


def atualiza_tela(tela, lavinia, coracoes, config):
    # Apaga a tela
    tela.fill(config.tela_cor)

    # Verifica se o jogador perdeu
    if not verifica_perdeu(coracoes):
        # Desenha lavinia
        lavinia.desenha(tela, config)

        # Desenha os coracoes
        for coracao in coracoes.sprites():
            coracao.desenha(tela, config)

        # Desenha o Gabriel mandando o coracao
        if len(coracoes.sprites()) > 0:
            tela.blit(config.gabriel, [(config.tela_largura - config.gabriel_largura), (coracoes.sprites()[-1].ret.top)])


        # Desenha a pontuacao
        tela.blit(pygame.font.SysFont(config.tela_texto_fonte,
                                      config.tela_texto_tamanho).render(f'Pontuação: {lavinia.pontuacao}',
                                                                        True, config.tela_texto_cor), [0, 0])
    else:
        # Desenha a mensagem de fim
        texto = pygame.font.SysFont(config.tela_texto_fonte,
                                      config.tela_texto_tamanho).render(f'Você não me amou o suficiente! Sua pontuação foi: {lavinia.pontuacao}',
                                                                        True, config.tela_texto_cor)
        texto_largura = texto.get_width()
        texto_altura = texto.get_height()
        tela.blit(config.perdeu, [(config.tela_largura - config.perdeu_largura) // 2, (config.tela_altura // 2) - config.perdeu_altura + 70])
        tela.blit(texto, [(config.tela_largura - texto_largura) // 2, config.tela_altura // 2 + 70])

    # Atualiza
    pygame.display.update()
