from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *
from .insere_refe_frame import *


class nova_gerencia_frame(c_frame_nova_gerencia):

    def __init__(self, frame_master, app_controller):
        #INSTANCIADO A INTERFACE REFERENTE A ESSE FRAME:
        super().__init__(frame_master)
        self.controller = app_controller


        self.lst_contas = []
        self.id_ger = None
        self.pointer_CBox1().bind('<<ComboboxSelected>>', lambda event: bind_CBox1())
        self.config_comando_B1(lambda: self.__comando_B1__())
        self.config_comando_B2(lambda: self.__comando_B2__())
        self.config_comando_B3(lambda: self.__comando_B3__())

    #Abaixo, a função que recebe duas strings, e guarda nelas o nome e descrição digitados:
    def __comando_B1__(self):
        tipo = self.retorna_escolha_CBox1()
        nome_conta = self.retorna_entr3()
        saldo_inic =  self.retorna_entr4()

        #Abaixo, o item é preenchido e inserido na treeview:
        conta = c_conta(tipo = tipo, nome = nome_conta, saldo = saldo_inic)
        self.lst_contas.append(conta)
        print(lst_contas)

        self.insere_elem_treeView1(nome_conta, tipo, saldo_inic)
        self.limpa_entr3()
        self.limpa_entr4()
        self.set_CBox1_default('Escolha a opção:')

    def __comando_B3__(self):
        n = 0
        nome_ger = self.retorna_entr1()
        nome_gest = self.retorna_entr2()
        descr = self.return_text1()

        tupl_cadastro = (nome_ger, nome_gest, descr)
        print(tupl_cadastro)
        bd_prog.ins_tupl_ger(tupl_cadastro)
        self.id_ger = bd_prog.fetch_id_ger(nome_ger)

        while n < len(lst_contas):
            self.lst_contas[n].m_re_init(id_ger = id_ger)
            bd_prog.ins_tupl_conta(lst_contas[n].tupl_cadastro())
            n = n + 1
        self.clear_treeView1()

    def __bind_CBox1__(self):
        tipo = frame_nova_gerencia.retorna_escolha_CBox1()
        if tipo == 'Cartão de crédito':
            self.config_entr4_state('disabled')
        else:
            self.config_entr4_state('enabled')

    def __comando_B2__(self):
        self.controller.show_frame('menu_inic')






def frame_nova_gerencia_constr(janelaPai, frame_menu_inic):
    #Instanciada uma conexão com o banco de dados do programa:
    bd_prog = conexao_BD_prog()
    #LEMBRAR DE FINALIZAR CONEXÃO:
    #bd_prog.finaliza_conexao()

    frame_nova_gerencia = c_frame_nova_gerencia(janelaPai)
    frame_nova_gerencia.config_nome_tit1('Incluir nova gerência')
    frame_nova_gerencia.config_tit_entr1('Nome da gerência:')
    frame_nova_gerencia.config_tit_entr2('Nome do gestor:')
    frame_nova_gerencia.config_tit_text1('Descrição da gerência')

    frame_nova_gerencia.config_nome_tit2('Incluir contas:')
    frame_nova_gerencia.config_tit_CBox1('Tipo de conta:')
    frame_nova_gerencia.set_CBox1_default('Escolha a opção:')
    frame_nova_gerencia.define_values_CBox1(['Conta corrente', 'Conta poupança', 'Cartão de crédito', 'Carteira', 'Caixa'])
    frame_nova_gerencia.config_tit_entr3('Nome da conta:')
    frame_nova_gerencia.config_tit_entr4('Saldo inicial: ')

    frame_nova_gerencia.config_tit_col_treeView1(0, 'Nome da conta:')
    frame_nova_gerencia.config_tit_col_treeView1('1', 'Tipo:')
    frame_nova_gerencia.config_tit_col_treeView1('2', 'Saldo inicial: (R$)')

    frame_nova_gerencia.config_text_B1('Enviar conta')
    frame_nova_gerencia.config_text_B2('Voltar ao menu')
    frame_nova_gerencia.config_text_B3('Salvar gerência')


    lst_contas = []
    id_ger = None


    #Abaixo, a função que recebe duas strings, e guarda nelas o nome e descrição digitados:
    def comando_B1():
        tipo = frame_nova_gerencia.retorna_escolha_CBox1()
        nome_conta = frame_nova_gerencia.retorna_entr3()
        saldo_inic =  frame_nova_gerencia.retorna_entr4()

        #Abaixo, o item é preenchido e inserido na treeview:
        conta = c_conta(tipo = tipo, nome = nome_conta, saldo = saldo_inic)
        lst_contas.append(conta)
        print(lst_contas)

        frame_nova_gerencia.insere_elem_treeView1(nome_conta, tipo, saldo_inic)
        frame_nova_gerencia.limpa_entr3()
        frame_nova_gerencia.limpa_entr4()
        frame_nova_gerencia.set_CBox1_default('Escolha a opção:')


    def comando_B3():
        nome_ger = frame_nova_gerencia.retorna_entr1()
        nome_gest = frame_nova_gerencia.retorna_entr2()
        descr = frame_nova_gerencia.return_text1()

        tupl_cadastro = (nome_ger, nome_gest, descr)
        print(tupl_cadastro)
        bd_prog.ins_tupl_ger(tupl_cadastro)
        id_ger = bd_prog.fetch_id_ger(nome_ger)

        for elem in lst_contas:
            elem.m_re_init(id_ger = id_ger)
            bd_prog.ins_tupl_conta(elem.m_tupl_cadastro())


        frame_nova_gerencia.clear_treeView1()


    def bind_CBox1():
        tipo = frame_nova_gerencia.retorna_escolha_CBox1()
        if tipo == 'Cartão de crédito':
            frame_nova_gerencia.config_entr4_state('disabled')
        else:
            frame_nova_gerencia.config_entr4_state('enabled')

    def comando_B2():
        frame_menu_inic.grid_frame()
        frame_nova_gerencia.finaliza()



    #Abaixo as Combo box recebem comandos via .bind:
    frame_nova_gerencia.pointer_CBox1().bind('<<ComboboxSelected>>', lambda event: bind_CBox1())
    frame_nova_gerencia.config_comando_B1(lambda: comando_B1())
    frame_nova_gerencia.config_comando_B2(lambda: comando_B2())
    frame_nova_gerencia.config_comando_B3(lambda: comando_B3())


    return(frame_nova_gerencia)
