from .GUIAbstracts.frames_prog import *



class carrega_ger_frame(c_frame_carrega_ger):

    def __init__(self, frame_master, app_controller):
        super().__init__(frame_master)
        self.controller = app_controller
        # Abaixo é instanciada uma conexão com o banco de dados do programa:
        bd_prog = self.controller.


        #Abaixo, são configuradas as instâncias da interface:


        self.config_nome_tit1("Carregar gerência")
        self.config_nome_tit2("Selecione a gerência:")

        self.config_tit_col_treeView1(0, 'Nome da gerência')
        self.config_tit_col_treeView1(1, 'Nome do gestor')

        self.config_text_B1('Carregar')
        self.config_text_B2('Voltar ao menu')

        lst_ger = []
        lst_ger = bd_prog.fetchall_ger()
        for elem in lst_ger:
            self.insere_lst_elem_treeView1(elem)


        def comando_B1():
            lst_ger = self.selection_treeView1()
            dict_ger = self.item_treeView1(lst_ger[0])
            nome_ger = dict_ger['text']
            #~ print('NOME GER', nome_ger)
            id_ger = bd_prog.fetch_id_ger(nome_ger)
            #~ print('\nA ID DA GERENCIA ESCOLHIDA:', id_ger)
            #~ print(type(id_ger))
            bd_prog.drop_gerencia_carregada()
            bd_prog.ins_gerencia_carregada(id_ger)
            #~ print(id_ger, bd_prog.fetch_ger_carregada())

            self.controller.inic_session(**dic_ger)



        def comando_B2():
            frame_menu_inic.grid_frame()
            self.finaliza()
            bd_prog.finaliza_conexao()

        self.config_comando_B1(lambda: comando_B1())
        self.config_comando_B2(lambda: comando_B2())



