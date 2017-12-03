from .GUIAbstracts.frames_prog import *

from .itens_cadastrados_frame import *
from .insere_itemServ_frame import *


class banco_itens_frame(frame_1T_3abas):
    def __init__(self, frame_master, controller):
        frame_1T_3abas.__init__(self, frame_master)

        self.config_nome_aba1("Ítens/serviços cadastrados")
        self.frame_itens_cadastrados = itens_cadastrados_frame(self.pointer_frame_aba1())
        # frame_itens_cadastrados.grid_frame()


        self.config_nome_aba2("Cadastrar ítem")
        self.frame_insere_item = insere_itemServ_frame(self.pointer_frame_aba2())

        self.config_nome_aba3("Cadastrar categoria")



class itens_cadastrados_frame(c_frame_itens_cadastrados):
    def __init__(self, framePai):
        super().__init__(self, framePai)
        self.grid_frame()

        # Instanciada a conexão com o BD:
        self.bd_prog = conexao_BD_prog()

        # ABAIXO, É INSTANCIADO O TIPO LISTA DE ELEMENTOS VINDOS DO BANCO DE DADOS(c_lst_BD)
        self.lst_bd = c_lst_BD(tipo='itens')

        # Abaixo, são configuradas as instâncias da interface:
        self.define_values_CBox1(['Itens', 'Serviços'])
        self.set_CBox1_default('Itens\Serviços')
        self.config_tit_treeView1('')
        self.config_tit_col_treeView1(0, 'Nome')
        self.config_tit_col_treeView1(1, 'Categoria')
        self.config_tit_col_treeView1(2, 'Subcategoria')
        self.config_tit_col_treeView1(3, 'Espécie')

        self.config_tit_entr1('Nome')
        self.config_tit_text1('Descrição')

        # Configurando .bind da Combobox1:
        self.pointer_CBox1().bind('<<ComboboxSelected>>', lambda event: self.__bind_CBox1__(event))

        # Configurando .bind da Treeview:
        self.pointer_treeView1().bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1(event))
        self.pointer_treeView1().bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))

        # Configurando o menu "righ-click" da treeView:
        self.menu_RC.config_nome_B1("Alterar dados")
        self.menu_RC.config_comando_B1(lambda: self.edit_itemServ())
        self.menu_RC.config_comando_B2(lambda: self.del_itemServ())
        self.menu_RC.config_nome_B2("Excluir item/Serviço")

    def __bind_CBox1__(self, event):
        tipo = self.retorna_escolha_CBox1()
        if tipo == 'Itens':
            self.clear_treeView1()
            self.config_tit_treeView1('Itens cadastrados:')
            self.lst_bd.m_carrega_lst(self.bd_prog.fetchall_itens_servs(tipo='Item'), tipo='item')
            lst_itens = self.lst_bd.m_itens()

            for elem in lst_itens:
                lst_treeView = elem.m_lst_treeView()
                self.insere_lst_elem_treeView1(lst_treeView, idd=elem.m_idd())

        if tipo == 'Serviços':
            self.clear_treeView1()
            self.config_tit_treeView1('Serviços cadastrados:')
            self.lst_bd.m_carrega_lst(self.bd_prog.fetchall_itens_servs(tipo='Serviço'), tipo='item')
            print(self.bd_prog.fetchall_itens_servs(tipo='Serviço'))
            lst_serv = self.lst_bd.m_itens()

            for elem in lst_serv:
                lst_treeView = elem.m_lst_treeView()
                self.insere_lst_elem_treeView1(lst_treeView, idd=elem.m_idd())

    def bind_event1_treeView1(self, event):
        idd_item_sel = self.idd_selection_treeView1()
        item_sel = self.lst_bd.m_item(idd_item_sel)

        # Abaixo as entradas receb os dados do fornecedor:
        self.insert_entr1(item_sel.m_nome())
        self.insert_text1(item_sel.m_descr())

    # ~ self.insert_entrN(2, )
    # ~ self.insert_entrN(3, )
    # ~ self.insert_entrN(4, )
    # ~ self.insert_entrN(5, )
    # ~ self.insert_entrN(6, )
    # ~ self.insert_entrN(7, )
    # ~ self.insert_entrN(8, )
    # ~ self.insert_entrN(9, )
    # ~ self.insert_entrN(10, )
    # ~ self.insert_entrN(11, )

    def bind_event2_treeView1(self, event):
        self.popup_menu(event)

    def edit_itemServ(self):
        idd_item_sel = self.idd_selection_treeView1()
        item_sel = self.lst_bd.m_item(idd_item_sel)
        edita_item = edita_item_frame(item_sel)

    def del_itemServ(self):
        idd_item_sel = self.idd_selection_treeView1()
        self.bd_prog.delete_itemServ(idd_item_sel)


class edita_item_frame(insere_itemServ_frame):
    def __init__(self, frame_master, itemServ, controller):
        super().__init__(self, frame_master)
        self.item = itemServ

    # Abaixo, a função que recebe duas strings, e guarda nelas o nome e descrição digitados:
    def __comando_B1__(self):
        # item = c_item_serv()
        tipo = self.retorna_escolha_CBox1()
        nome = self.retorna_entr1()
        descr = self.retorna_text1()
        categ = self.retorna_escolha_CBox2()
        subCateg = self.retorna_escolha_CBox3()
        marca = self.retorna_escolha_CBox4()

        if nome != '':  # and categ != 'Escolha a opção:' and subCateg != 'Escolha a opção:' and tipo != 'Escolha a opção:':
            # Abaixo, o item é preenchido e inserido na treeview:

            self.item.m_re_init(tipo=tipo, nome=nome, descr=descr, categ=categ, subcateg=subCateg, marca=marca)

            self.lst_itens.m_append_item(self.item)
            lst_aux = self.lst_itens.m_itens()

            for elem in lst_aux:
                lst_treeview = elem.m_lst_treeView()
                self.insere_lst_elem_treeView1(lst_treeview, idd=elem.m_idd())
                self.limpa_CaixaTexto()
                self.limpa_entr1()
                self.set_CBox2_default('Escolha a opção:')
                self.config_CBox2_state('disabled')
                self.set_CBox3_default('Escolha a opção:')
                self.config_CBox3_state('disabled')
                self.set_CBox4_default('Escolha a opção:')
                self.config_CBox4_state('disabled')

        else:
            lst_aux = []
            if nome == '':
                lst_aux.append('Nome')
            if tipo == 'Escolha a opção:':
                lst_aux.append('tipo')
            if categ == 'Escolha a opção:':
                lst_aux.append('Categoria')
            if subCateg == 'Escolha a opção:':
                lst_aux.append('Subcategoria')

            str_aux = str(lst_aux)
            str_aux = str_aux.strip(']').strip('[')
            msg = 'Você não informou os seguintes dados: ' + str_aux
            messagebox.showinfo('Atenção!', msg)
            self.__cond_B3__()

    def __comando_B3__(self):

        id_itemServ = self.item.m_idd()
        tipo = self.item.m_tipo()
        nome = self.item.m_nome()
        descr = self.item.m_descr()
        categ = self.item.m_categ()
        subCateg = self.item.m_subcateg()
        marca = self.item.m_marca()
        self.bd_prog.update_itemServ(id_itemServ, tipo=tipo, nome=nome, descr=descr, categ=categ, subcateg=subCateg,
                                     marca=marca)
        self.clear_treeView1()
        self.__cond_B3__()

    def __comando_B2__(self):
        pass

    def bind_CBox1(self):
        tipo = self.retorna_escolha_CBox1()
        if tipo != "Escolha a opção:":
            self.config_CBox2_state("readonly")
            self.set_CBox2_default("Escolha a opção:")
            categ_lst = self.bd_prog.fetchall_categ_str(tipo)
            self.define_values_CBox2(categ_lst)

    def bind_CBox2(self):
        tipo = self.retorna_escolha_CBox1()
        categ = self.retorna_escolha_CBox2()
        if categ != "Escolha a opção:":
            subCateg_lst = self.bd_prog.fetchall_subcateg_str(tipo, categ)
            self.set_CBox3_default("Escolha a opção:")
            self.config_CBox3_state("readonly")
            self.define_values_CBox3(subCateg_lst)

    def bind_CBox3(self):
        tipo = self.retorna_escolha_CBox1()
        subCateg = self.retorna_escolha_CBox3()
        if subCateg != "Escolha a opção:" and subCateg != '':
            item_lst = self.bd_prog.fetchall_espec_str(tipo, subCateg)
            self.set_CBox4_default("Escolha a opção:")
            self.config_CBox4_state("readonly")
            self.define_values_CBox4(item_lst)

    def bind_CBox4(self):  # <---- Combobox3 teria a função passiva de receber a lista de espécies
        pass

    def __cond_B3__(self):
        pass

    # ~ if self.lst_itens.m_len_lst() == 0:
    # ~ self.config_B3(state = 'disabled')
    # ~ else:
    # ~ self.config_B3(state = 'enabled')
