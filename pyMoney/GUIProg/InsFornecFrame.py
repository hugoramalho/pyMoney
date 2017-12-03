from BDProg.pyMoney_BD_prog import *
from .GUIAbstracts.frames_prog import *
from classes_money import *



class InsFornecFrame(c_frame_insere_fornec):

    def __init__(self, frame_master, app_controller):
        super().__init__(self, frame_master)
        self.controller = app_controller
        self.grid_frame()
        #Abaixo é instanciada uma conexão com o BD:
        self.bd_prog = conexao_BD_prog()

        self.fornec = None
        self.lst_fornecs = c_list()
        
        
        self.config_comando_B1(lambda: self.__comando_B1__())
        self.config_comando_B3(lambda: self.__comando_B3__())
        self.config_comando_B2(lambda: self.__comando_B2__())
        self.__cond_B3__()

    #Abaixo, a função que recebe duas strings, e guarda nelas o nome e descrição digitados:
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
            self.fornec = c_fornec(nome = nome, descr = descr, categoria = categ, subcategoria = subCateg, tel1 = tel1, tel2 = tel2, email = email, uf = UF, cidade = Cit, cn = CN)
            self.lst_fornecs.m_append_item(self.fornec)
            
            self.__cond_B3__()
            self.treeView1.insert_kwargs_treeView(**(self.fornec.m_kwargs_treeView()))
            #self.insere_elem_treeView1(nome, categ, subCateg, tel1, Cit)
            self.limpa_CaixaTexto()
            self.limpa_entr1()
            self.set_CBox2_default('Escolha a opção:')
            self.__cond_B3__()
        
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
        
        
    def __comando_B2__(self):
        pass
        
        
    def __comando_B3__(self):
        if self.fornec != None:
            lst_cadast = self.lst_fornecs.m_itens()
            self.lst_fornecs.m_cls_dic()
            print('\nA lista de fornecedores a serem cadastrados:', lst_cadast)
            #O LOOP ABAIXO PERCORRE A LISTA(lst_aux) E VAI CADASTRANDO ITEM POR ITEM NO BANCO DE DADOS
            for elem in lst_cadast:
                self.bd_prog.ins_tupl_fornecs(elem.m_tupl_cadastro())
            #DESELEGANTE! LEMBRAR DE CRIAR UMA FUNÇÃO NO BD QUE RECEBA UMA LISTA!
            #bd_prog.ins_lst_item_serv(lst_itens)
            self.lst_fornecs.m_cls_dic()
            self.clear_treeView1()
            self.__cond_B3__()

    def __cond_B3__(self):
        """
        O PRESENTE MÉTODO VERIFICA SE HÁ ELEMENTOS NA LISTA DE CADASTRO,
        CASO HAJA, O BOTÃO 3 É DESCONGELADO, TAL BOTÃO É RESPONSÁVEL 
        POR ENVIAR OS FORNECEDORES EM EDIÇÃO PARA O BANCO DE DADOS
        """		
        if self.lst_fornecs.m_len_lst() == 0:
            #CASO O TAMANHO DA LISTA DE FORNECEDORES SENDO EDITADOS SEJA IGUAL A ZERO...
            self.config_B3(state = 'disabled')
        else:
            self.config_B3(state = 'enabled')

