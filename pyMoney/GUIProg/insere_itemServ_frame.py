from .GUIAbstracts.frames_prog import *

class insere_itemServ_frame(c_frame_insere_item_serv):

    def __init__(self, frame_master, app_master):
        super().__init__(self, frame_master)
        self.controller = app_master

        
        #Instanciada uma conexão com o banco de dados:
        self.bd_prog = self.controller.con_bd

        #Abaixo, a variável item recebe uma instância da classe que guardará o cadastro no banco de dados:
        item = c_item_serv()
        self.lst_itens = c_list()
        

        #Abaixo as Combo box recebem comandos via .bind:
        self.pointer_CBox1().bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())
        self.pointer_CBox2().bind('<<ComboboxSelected>>', lambda event: self.bind_CBox2())
        self.pointer_CBox3().bind('<<ComboboxSelected>>', lambda event: self.bind_CBox3())
        self.pointer_CBox4().bind('<<ComboboxSelected>>', lambda event: self.bind_CBox4())
        
        #Abaixo, o botão 1 é configurado para executar a função comando_B1:
        self.config_comando_B1(lambda: self.__comando_B1__())
        self.config_comando_B3(lambda: self.__comando_B3__())
        self.config_comando_B2(lambda: self.__comando_B2__())
        
        #~ self.__cond_B3__()


    #Abaixo, a função que recebe duas strings, e guarda nelas o nome e descrição digitados:
    def __comando_B1__(self):
        #item = c_item_serv()
        tipo = self.retorna_escolha_CBox1()
        nome = self.retorna_entr1()
        descr = self.retorna_text1()
        categ = self.retorna_escolha_CBox2()
        subCateg = self.retorna_escolha_CBox3()
        marca = self.retorna_escolha_CBox4()
        
        if nome != '':# and categ != 'Escolha a opção:' and subCateg != 'Escolha a opção:' and tipo != 'Escolha a opção:':
            #Abaixo, o item é preenchido e inserido na treeview:
            print(tipo)
            self.item = c_item_serv(tipo = tipo, nome = nome, descr = descr, categ = categ, subcateg = subCateg, marca = marca)
            #item.re_init(tipo, nome, descr, categ, subCateg, especie)
            
            self.lst_itens.m_append_item(self.item)
            lst_aux = self.lst_itens.m_itens()
            
            for elem in lst_aux:
                lst_treeview = elem.m_lst_treeView()
                self.insere_lst_elem_treeView1(lst_treeview, idd = elem.m_idd())
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
        lst_aux = self.lst_itens.m_itens()
        for elem in lst_aux:
            self.bd_prog.ins_tupl_item_serv(elem.m_tupl_cadastro())
        #DESELEGANTE! LEMBRAR DE CRIAR UMA FUNÇÃO NO BD QUE RECEBA UMA LISTA!
        #self.bd_prog.ins_lst_item_serv(lst_itens)
        self.lst_itens.m_cls_dic()
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
            


    def bind_CBox4(self): # <---- Combobox3 teria a função passiva de receber a lista de espécies
        pass
        '''
        tipo = self.retorna_escolha_CBox1()
        subCateg = self.retorna_escolha_CBox3()
        if subCateg != "Escolha a opção:" and subCateg != '':
            item_lst = self.bd_prog.fetchall_espec_str(tipo, subCateg)
            self.set_CBox4_default("Escolha a opção:")
            self.config_CBox4_state("readonly")
            self.define_values_CBox4(item_lst)
        '''
        
     

    def __cond_B3__(self):
        pass
        #~ if self.lst_itens.m_len_lst() == 0:
            #~ self.config_B3(state = 'disabled')
        #~ else:
            #~ self.config_B3(state = 'enabled')



