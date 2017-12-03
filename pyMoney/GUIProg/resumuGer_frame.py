from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *




class resumuGer_frame(c_frame_resumoGer):
    def __init__(self, frame_master, app_controller):
        super().__init__(self, frame_master)
        self.controller = app_controller


        self.bd_prog = conexao_BD_prog()
        self.lst_contas = self.bd_prog.select_conta_ger()
        print(self.bd_prog.fetchall_transac())
        


        self.insere_lst_treeView(self.treeView1, self.lst_contas)


    def insere_lst_treeView(self, treeView, lst_elem):
        for elem in lst_elem:
            treeView.insere_lst_elem_treeView(elem)
