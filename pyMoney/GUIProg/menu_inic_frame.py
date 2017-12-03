from .GUIAbstracts.frames_prog import *

class coll_menu_frame(coll_menu):

    def __init__(self, app_controller, frame_master):
        super().__init__(frame_master)
        self.controller = app_controller
        self.desativa_todos_Rb()

        self.config_comando_Rb1(self.abre_frame_statusGeral)

        #self.config_comando_Rb2()

        #self.config_comando_Rb3()

        self.config_comando_Rb4(self.abre_frame_insere_refe)

        self.config_comando_Rb5(self.abre_frame_insere_move)

        #self.config_comando_Rb6()

        self.config_comando_Rb7(self.abre_frame_banco_itens)

        self.config_comando_Rb8(self.abre_frame_fornec)

        self.config_comando_Rb9(self.abre_frame_clientes)

    def abre_frame_statusGeral(self):
        self.controller.show_frame('statusGeral_frame')

    def abre_frame_banco_itens(self):
        self.controller.show_frame('banco_itens_frame')

    def abre_frame_insere_move(self):
        self.controller.show_frame('insere_move_frame')

    def abre_frame_banco_refs(self):
        self.controller.show_frame('frame_banco_refs_constr')

    def abre_frame_fornec(self):
        self.controller.show_frame('fornec_frame')

    def abre_frame_insere_refe(self):
        self.controller.show_frame('insere_refe_frame')

    def abre_frame_clientes(self):
        self.controller.show_frame('clientes_frame')