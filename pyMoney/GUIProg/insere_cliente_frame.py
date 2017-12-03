from pyMoney_BD_prog import *
from .GUIAbstracts.frames_prog import *
from classes_money import c_cliente, c_list


class insere_cliente_frame(c_frame_insere_cliente):

    def __init__(self, framePai, app_controller):
        c_frame_insere_cliente.__init__(self, framePai)
        self.controller = app_controller
        self.grid_frame()
        #Abaixo é instanciada uma conexão com o banco de dados do programa:
        self.bd_prog = conexao_BD_prog()

        self.lst_clientes = c_list()
        self.cliente = c_cliente()



        #Abaixo, o botão 1 é configurado para executar a função comando_B1:
        self.config_comando_B1(lambda: self.__comando_B1__())
        self.config_comando_B2(lambda: self.__comando_B2__())
        self.config_comando_B3(lambda: self.__comando_B3__())
        self.config_comando_B4(lambda: self.__comando_B4__())
        self.__cond_B3__()

    #Abaixo, a função que recebe duas strings, e guarda nelas o nome e descrição digitados:
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
            #Em seguida adicionado à lista de clientes a cadastrar
            self.cliente = c_cliente(nome = nome, cn = cn, genero = genero, tel1 = tel1, tel2 = tel2, email1 = email1, email2 = email2, uf = uf, cidade = cidade, bairro = bairro, logradouro = logradouro, num_resid = num_resid, tipo_resid = tipo_resid, num_ape = num_ape, nome_cond = nome_cond, cep = cep)
            self.lst_clientes.m_append_item(self.cliente)
            
            #Abaixo, A lst_treeView recebe uma lista que será usada para preencher a treeView
            lst_treeView = self.cliente.m_lst_treeView()
            self.insere_lst_elem_treeView1(lst_treeView, idd = self.cliente.m_idd())
            
            self.pointer_treeView1().bind('<<TreeviewSelect>>', lambda event: self.__bind_treeView1__())
            
            

            
            #Abaixo, as entradas são limpadas e todo o frame é reiniciado
            self.limpa_todas_entr()
            self.set_CBox2_default('Escolha a opção:')
        
            self.__cond_B3__()
        
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


    def __bind_treeView1__(self):
        print(self.pointer_treeView1().selection())
        print(self.pointer_treeView1().selection()[0])

    def __comando_B2__(self):
        pass

    def __comando_B3__(self):

        lst_cadast = self.lst_clientes.m_itens()
        
        print('\nA lista de clientes a serem cadastrados:', lst_cadast)
        #O LOOP ABAIXO PERCORRE A LISTA(lst_aux) E VAI CADASTRANDO ITEM POR ITEM NO BANCO DE DADOS
        for elem in lst_cadast:
            self.bd_prog.ins_tupl_cliente(elem.m_tupl_cadastro())
        #DESELEGANTE! LEMBRAR DE CRIAR UMA FUNÇÃO NO BD QUE RECEBA UMA LISTA!
        #self.bd_prog.ins_lst_item_serv(lst_itens)

        self.lst_clientes.m_cls_dic()
        self.clear_treeView1()
        self.__cond_B3__()

    def __comando_B4__(self):
        cep = self.retorna_entr11()
        bd_ender = conexao_BD_ender()
        dic_ender = bd_ender.fetch_ender_cep(cep)
        
        if dic_ender != None:
            self.limpa_entr7()
            self.insert_entrN(7, dic_ender['tipo'] + ' ' + dic_ender['rua'])
            self.set_CBox3_default(dic_ender['cidade'])
            self.set_CBox2_default(dic_ender['estado'])
            self.set_CBox4_default(dic_ender['bairro'])
        else:
            self.limpa_entr7()
            self.limpa_entr11()
            self.insert_entrN(11, 'CEP não encontrado')
            
        
        

    def __cond_B3__(self):
        pass
        #~ """
        #~ O PRESENTE MÉTODO VERIFICA SE HÁ ELEMENTOS NA LISTA DE CADASTRO,
        #~ CASO HAJA, O BOTÃO 3 É DESCONGELADO, TAL BOTÃO É RESPONSÁVEL 
        #~ POR ENVIAR OS FORNECEDORES EM EDIÇÃO PARA O BANCO DE DADOS
        #~ """
        #~ if self.lst_clientes.m_len_lst() == 0:
            #~ self.config_B3(state = 'disabled')
        #~ else:
            #~ self.config_B3(state = 'enabled')



