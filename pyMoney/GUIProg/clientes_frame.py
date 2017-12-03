from pyMoney_BD_prog import *
from classes_money import *
from ui_frames_lib_h import *

#Abaixo são importadas as construtoras dos frames filhos
from insere_cliente_frame import *
from clientes_cadastrados_frame import *


class clientes_frame(frame_1T_3abas):
	
	def __init__(self, frame_master, app_controller):
		frame_1T_3abas.__init__(self, frame_master)

		self.controller = app_controller

		#Conteúdo da aba 1
		self.config_nome_aba1("Clientes cadastrados")
		self.frame_clientes_cadastrados = clientes_cadastrados_frame(self.pointer_frame_aba1())

		#Conteúdo da aba 2 
		self.config_nome_aba2("Cadastrar cliente")
		self.frame_insere_cliente = insere_cliente_frame(self.pointer_frame_aba2())

		#Conteúdo da aba3 
		self.config_nome_aba3("Cadastrar categoria")
		#~ self.frame_cadast_categ_client = cadast_categ_client_frame(self.pointer_frame_aba3())
