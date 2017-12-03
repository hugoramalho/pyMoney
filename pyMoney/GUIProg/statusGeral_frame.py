from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *
from .resumuGer_frame import *


class statusGeral_frame(frame_1T_5abas):
	def __init__(self, framePai):
		frame_1T_5abas.__init__(self, framePai)

		self.config_tit1("Status geral")
		
		self.config_tit2("Gerência do mês ***")


		self.config_nome_aba2("Movimentações do mês atual")
		self.config_nome_aba3("Resumo de compra de itens/serviços")
		self.config_nome_aba4("Status parcial")
		self.config_nome_aba5("Previsões")

		#ABA 1:
		self.config_nome_aba1("Resumo gerencial")
			#CONSTRUTOR DO FRAME CONTIDO NA ABA 1:
		self.frame_resumoGer = resumuGer_frame(self.pointer_frame_aba1())
		self.frame_resumoGer.grid_frame()


'''
AS FUNÇÕES CONSTRUTORAS ABAIXO DEVERÃO SER DESLOCADAS PARA UM SCRIPT PRÓPRIO:


def menu_centr_1_aba2_constr(menu_centr_1_abas):
	#-> PRECISARÁ SER IMPLEMENTADO EM OUTRA CAMADA DE CONSTRUÇÃO!
	frame_tabela_mov = frame_2T_2Tview(menu_centr_1_abas.pointer_frame_aba2())
	frame_tabela_mov.grid_frame()
	return(frame_tabela_mov)


def menu_centr_1_aba3_constr(menu_centr_1_abas):
	#-> PRECISARÁ SER IMPLEMENTADO EM OUTRA CAMADA DE CONSTRUÇÃO!
	frame_tabela_compra_items = frame_2T_2Tview(menu_centr_1_abas.pointer_frame_aba3())
	frame_tabela_compra_items.grid_frame()
	return(frame_tabela_compra_items)
'''

