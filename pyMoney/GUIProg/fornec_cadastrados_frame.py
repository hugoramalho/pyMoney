from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *
from .InsFornecFrame import *


class fornec_cadastrados_frame(c_frame_fornec_cadastrados):
    
    def __init__(self, frame_master, app_controller):
        super().__init__(self, frame_master)
        self.controller = app_controller
        self.grid_frame()
        
        #Abaixo é instanciada uma conexão com o banco de dados do programa:
        self.bd_prog = conexao_BD_prog()
        
        #Abaixo, são configuradas as instâncias da interface:


        self.fornecs = c_lst_BD(self.bd_prog.fetchall_fornec(), tipo = 'fornec')


        ##
        self.insere_treeView_frame()
        self.pointer_treeView1().bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1())
        self.pointer_treeView1().bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))

        self.menu_RC.config_nome_B1("Alterar dados")
        self.menu_RC.config_comando_B1(lambda: self.edit_fornec())
        self.menu_RC.config_comando_B2(lambda: self.del_fornec())
        self.menu_RC.config_nome_B2("Excluir cliente")
        

    def insere_treeView_frame(self):
        lst_fornecs = self.fornecs.m_itens()
        self.clear_treeView1()
        #print(self.lst_fornecs)
        try:
            for obj in lst_fornecs:
                self.insere_elem_treeView1(obj.m_nome(), obj.m_categ(), obj.m_tel1(), obj.m_email(), idd = obj.m_idd())
        except Exception as Expt:
            print(str(Expt))
            pass
    

    def bind_event1_treeView1(self):
        idd_fornec_sel = self.idd_selection_treeView1()

        fornec_sel = self.fornecs.m_item(idd_fornec_sel)
        #Abaixo as entradas receb os dados do fornecedor:
        self.insert_entr1(fornec_sel.m_nome())
        self.insert_entr2(fornec_sel.m_categ())
        self.insert_entr3(fornec_sel.m_tel1())
        self.insert_entr4(fornec_sel.m_tel2())
        self.insert_entr5(fornec_sel.m_email())
        self.insert_entr6(fornec_sel.m_cn())
        self.insert_entr7(fornec_sel.m_local())
        self.insert_text1(fornec_sel.m_descr())


    def bind_event2_treeView1(self, event):
        self.popup_menu(event)

    def edit_fornec(self):
        idd_fornec_sel = self.idd_selection_treeView1()
        fornec_sel = self.fornecs.m_item(idd_fornec_sel)
        top = Toplevel()
        edita_fornec = edita_fornec_frame(top, fornec_sel)

    def del_fornec(self):
        idd_fornec_sel = self.idd_selection_treeView1()
        self.bd_prog.delete_fornec(idd_fornec_sel)



class edita_fornec_frame(InsFornecFrame):
    def __init__(self, framePai, fornec, app_controller):
        InsFornecFrame.__init__(self, framePai)
        self.controller = app_controller
        
        self.config_nome_tit1("Edição de Fornecedor")
        
        self.fornec = fornec
        
        nome = self.fornec.m_nome()
        tel1 = self.fornec.m_tel1()
        tel2 = self.fornec.m_tel2()
        email = self.fornec.m_email()
        cn = self.fornec.m_cn()
        uf = self.fornec.m_uf()
        cidade = self.fornec.m_cidade()


        self.insert_entrN(1, nome)
        self.insert_entrN(2, tel1)
        self.insert_entrN(3, tel2)
        self.insert_entrN(4, email)
        self.insert_entrN(5, cn)
        self.insert_entrN(6, uf)
        self.insert_entrN(7, cidade)
        #~ self.insert_entrN(8, nome_cond)


    def __comando_B1__(self):
        categ = self.retorna_escolha_CBox1()
        subCateg = self.retorna_escolha_CBox2()
        nome = self.retorna_entr1()
        descr = self.retorna_text1()
        tel1 = self.retorna_entr2()
        tel2 = self.retorna_entr3()
        email = self.retorna_entr4()
        CN = self.retorna_entr5()
        UF = self.retorna_entr6()
        Cit = self.retorna_entr7()
        
        #Primeiro é verificado se os ítens mínimos foram preenchidos:
        if nome != '' and tel1 != '' and categ != 'Escolha a opção:' and subCateg != 'Escolha a opção:':
            #Abaixo, o fornecedor é preenchido e inserido na treeview:
            self.fornec.m_re_init(nome = nome, descr = descr, categoria = categ, subcategoria = subCateg, tel1 = tel1, tel2 = tel2, email = email, uf = UF, cidade = Cit, cn = CN)

            #~ self.__cond_B3__()
            #self.insere_elem_treeView1(nome, categ, subCateg, tel1, Cit)
            self.treeView1.insert_kwargs_treeView(**(self.fornec.m_kwargs_treeView()))
            self.limpa_CaixaTexto()
            self.limpa_entr1()
            self.set_CBox2_default('Escolha a opção:')
        
        else:
        
            lst_aux = []
            if nome == '':
                lst_aux.append('Nome')
            if tel1 == '':
                lst_aux.append('Telefone principal')
            if categ == 'Escolha a opção:':
                lst_aux.append('Categoria')
            if subCateg == 'Escolha a opção:':
                lst_aux.append('Subcategoria')
            str_aux = str(lst_aux)
            str_aux = str_aux.strip(']').strip('[')
            msg = 'Você não informou os seguintes dados: ' + str_aux
            self.messagebox_info('Atenção!', msg)


    def __comando_B3__(self):
        descr = self.fornec.m_descr()
        nome = self.fornec.m_nome()
        tel1 = self.fornec.m_tel1()
        tel2 = self.fornec.m_tel2()
        email = self.fornec.m_email()
        cn = self.fornec.m_cn()
        uf = self.fornec.m_uf()
        cidade = self.fornec.m_cidade()
        categ = self.fornec.m_categ()
        subCateg = self.fornec.m_subcateg()
        
        id_fornec = str(self.fornec.m_idd())
        self.bd_prog.update_fornec(id_fornec, nome = nome, descr = descr, categoria = categ, subcategoria = subCateg, tel1 = tel1, tel2 = tel2, email = email, uf = uf, cidade = cidade, cn = cn)
        #DESELEGANTE! LEMBRAR DE CRIAR UMA FUNÇÃO NO BD QUE RECEBA UMA LISTA!
        #bd_prog.ins_lst_item_serv(lst_itens)
        self.clear_treeView1()



    def __cond_B3__(self):
        pass
        #~ """
        #~ O PRESENTE MÉTODO VERIFICA SE HÁ ELEMENTOS NA LISTA DE CADASTRO,
        #~ CASO HAJA, O BOTÃO 3 É DESCONGELADO, TAL BOTÃO É RESPONSÁVEL 
        #~ POR ENVIAR OS FORNECEDORES EM EDIÇÃO PARA O BANCO DE DADOS
        #~ """		
        #~ if self.lst_fornecs.m_len_lst() == 0:
            #~ #CASO O TAMANHO DA LISTA DE FORNECEDORES SENDO EDITADOS SEJA IGUAL A ZERO...
            #~ self.config_B3(state = 'disabled')
        #~ else:
            #~ self.config_B3(state = 'enabled')

