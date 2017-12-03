from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *

# Abaixo são importadas as construtoras dos frames filhos
from .InsFornecFrame import *
from .fornec_cadastrados_frame import *


class fornec_frame(frame_1T_3abas):
    def __init__(self, framePai, app_controller):
        frame_1T_3abas.__init__(self, framePai)
        self.controller = app_controller
        # Conteúdo da aba1
        self.config_nome_aba1("Estabelecimentos/Identificações cadastrados")
        # O frame instaciado abaixo estará na aba1:
        frame_fornec_cadastrados = fornec_cadastrados_frame(self.pointer_frame_aba1())

        # Conteúdo da aba2
        self.config_nome_aba2("Cadastrar estabelecimento/identificação")
        # O frame instaciado abaixo estará na aba2, NECESSIDA SER IMPLEMENTADO EM OUTRA CAMADA!
        frame_insere_fornec = InsFornecFrame(self.pointer_frame_aba2())

        # Conteúdo da aba3 -> PRECISARÁ SER IMPLEMENTADO EM OUTRA CAMADA DE CONSTRUÇÃO!
        self.config_nome_aba3("Cadastrar categoria")