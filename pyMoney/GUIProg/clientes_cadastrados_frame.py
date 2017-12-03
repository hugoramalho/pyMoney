from pyMoney_BD_prog import *
from classes_money import *
from .GUIAbstracts.frames_prog import c_frame_clientes_cadastrados
from insere_cliente_frame import *
from tkinter import *



class clientes_cadastrados_frame(c_frame_clientes_cadastrados):

    def __init__(self, frame_master, app_controller):
        super().__init__(self, frame_master)
        self.controller = app_controller
        self.framePai = frame_master
        self.grid_frame()

        #Abaixo é instanciada uma conexão com o banco de dados do programa:
        self.bd_prog = self.controller.load_clients()

        self.clients = c_lst_BD(self.bd_prog.fetchall_clientes(), tipo = 'cliente')



        self.insere_treeView_frame()
        #~ self.pointer_frameLocal().focus_set()
        #self.pointer_frameLocal().bind("<Button-3>", popup)
        self.pointer_treeView1().bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1(event))
        self.pointer_treeView1().bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))

        self.menu_RC.config_nome_B1("Alterar dados")
        self.menu_RC.config_comando_B1(lambda: self.edit_client())
        self.menu_RC.config_comando_B2(lambda: self.del_cliente())
        self.menu_RC.config_nome_B2("Excluir cliente")


    def insere_treeView_frame(self):
        #O PRESENTE MÉTODO PERCORRE A LISTA DE CLIENTES
        #E VAI ITERANDO, EXECUTANDO O MÉTODO m_kwargs_treeView() em cada elemento
        #E PREENCHENDO A TREEVIEW
        lst_clients = self.clients.m_itens()
        self.clear_treeView1()

        for obj in lst_clients:
            lst_treeView = obj.m_lst_treeView()
            self.treeView1.insert_kwargs_treeView(**(obj.m_kwargs_treeView()))


    def bind_event1_treeView1(self, event):
        idd_client_sel = self.idd_selection_treeView1()
        client_sel = self.clients.m_item(idd_client_sel)


        #Abaixo as entradas receb os dados do fornecedor:
        self.insert_entrN(1, client_sel.m_nome())
        self.insert_entrN(2, client_sel.m_genero())
        self.insert_entrN(3, client_sel.m_tel1())
        self.insert_entrN(4, client_sel.m_tel2())
        self.insert_entrN(5, client_sel.m_cn())
        self.insert_entrN(6, client_sel.m_email1())
        self.insert_entrN(7, client_sel.m_email2())
        self.insert_entrN(8, client_sel.m_num_resid())
        self.insert_entrN(9, client_sel.m_descr())
        #self.insert_entrN(10, client_sel.m_nascDat())
        self.insert_entrN(11, client_sel.m_uf())
        self.insert_entrN(12, client_sel.m_cidade())
        self.insert_entrN(13, client_sel.m_bairro())
        self.insert_entrN(14, client_sel.m_logradouro())
        self.insert_entrN(15, client_sel.m_tipo_resid())
        self.insert_entrN(16, client_sel.m_nome_cond())
        self.insert_entrN(17, client_sel.m_num_ape())

    def bind_event2_treeView1(self, event):
        self.popup_menu(event)

    def edit_client(self):
        idd_client_sel = self.idd_selection_treeView1()
        client_sel = self.clients.m_item(idd_client_sel)
        top = Toplevel()
        edita_cliente = edita_cliente_frame(top, client_sel)

    def del_cliente(self):
        idd_client_sel = self.idd_selection_treeView1()
        self.bd_prog.delete_cliente(idd_client_sel)



class edita_cliente_frame(insere_cliente_frame):
    def __init__(self, framePai, cliente):
        super().__init__(self, framePai)
        self.config_nome_tit1("Edição de Clientes")

        self.cliente = cliente

        nome = self.cliente.m_nome()
        genero = self.cliente.m_genero()
        tel1 = self.cliente.m_tel1()
        tel2 = self.cliente.m_tel2()
        email1 = self.cliente.m_email1()
        email2 = self.cliente.m_email2()
        cn = self.cliente.m_cn()
        uf = self.cliente.m_uf()
        cidade = self.cliente.m_cidade()
        bairro = self.cliente.m_bairro()
        tipo_resid = self.cliente.m_tipo_resid()
        logradouro = self.cliente.m_logradouro()
        num_resid = self.cliente.m_num_resid()
        nome_cond = self.cliente.m_nome_cond()
        num_ape = self.cliente.m_num_ape()
        cep = self.cliente.m_cep()

        self.insert_entrN(1, nome)
        self.insert_entrN(2, tel1)
        self.insert_entrN(3, tel2)
        self.insert_entrN(4, email1)
        self.insert_entrN(5, cn)
        self.insert_entrN(6, email2)
        self.insert_entrN(7, logradouro)
        self.insert_entrN(8, num_resid)
        self.insert_entrN(9, nome_cond)
        self.insert_entrN(10, num_ape)
        self.insert_entrN(11, cep)


    def __comando_B1__(self):
        nome = self.retorna_entr1()
        genero = self.retorna_escolha_CBox1()
        tel1 = self.retorna_entr2()
        tel2 = self.retorna_entr3()
        email1 = self.retorna_entr4()
        email2 = self.retorna_entr6()
        cn = self.retorna_entr5()
        uf = self.retorna_escolha_CBox2()
        cidade = self.retorna_escolha_CBox3()
        bairro = self.retorna_escolha_CBox4()
        tipo_resid = self.retorna_escolha_CBox5()
        logradouro = self.retorna_entr7()
        num_resid = self.retorna_entr8()
        nome_cond = self.retorna_entr9()
        num_ape = self.retorna_entr10()
        cep = self.retorna_entr11()

        #Primeiro é verificado se os ítens mínimos foram preenchidos:
        if nome != '' and tel1 != '':
            #Abaixo, o cliente é redeclarado com as definições especificadas pelo usuário.
            self.cliente.m_re_init(nome = nome, cn = cn, genero = genero, tel1 = tel1, tel2 = tel2, email1 = email1, email2 = email2, uf = uf, cidade = cidade, bairro = bairro, logradouro = logradouro, num_resid = num_resid, tipo_resid = tipo_resid, num_ape = num_ape, nome_cond = nome_cond, cep = cep)

            #Abaixo, A lst_treeView recebe uma lista que será usada para preencher a treeView
            lst_treeView = self.cliente.m_lst_treeView()
            self.insere_lst_elem_treeView1(lst_treeView, idd = self.cliente.m_idd())

            #Abaixo, as entradas são limpadas e todo o frame é reiniciado
            self.limpa_todas_entr()
            self.set_CBox2_default('Escolha a opção:')


        #Caso os dados mínimos para o cadastro não sejam preenchidos:
        else:
            lst_aux = []
            if nome == '':
                lst_aux.append('Nome')
            if tel1 == '':
                lst_aux.append('Telefone principal')

            str_aux = str(lst_aux)
            str_aux = str_aux.strip(']').strip('[')
            msg = 'Você não informou os seguintes dados: ' + str_aux
            self.messagebox_info('Atenção!', msg)


    def __comando_B3__(self):
        nome = self.cliente.m_nome()
        genero = self.cliente.m_genero()
        tel1 = self.cliente.m_tel1()
        tel2 = self.cliente.m_tel2()
        email1 = self.cliente.m_email1()
        email2 = self.cliente.m_email2()
        cn = self.cliente.m_cn()
        uf = self.cliente.m_uf()
        cidade = self.cliente.m_cidade()
        bairro = self.cliente.m_bairro()
        tipo_resid = self.cliente.m_tipo_resid()
        logradouro = self.cliente.m_logradouro()
        num_resid = self.cliente.m_num_resid()
        nome_cond = self.cliente.m_nome_cond()
        num_ape = self.cliente.m_num_ape()
        cep = self.cliente.m_cep()
        id_cliente = self.cliente.m_idd()
        self.bd_prog.update_cliente(id_cliente, nome = nome, cn = cn, genero = genero, tel1 = tel1, tel2 = tel2, email1 = email1, email2 = email2, uf = uf, cidade = cidade, bairro = bairro, logradouro = logradouro, num_resid = num_resid, tipo_resid = tipo_resid, num_ape = num_ape, nome_cond = nome_cond, cep = cep)
        self.clear_treeView1()


