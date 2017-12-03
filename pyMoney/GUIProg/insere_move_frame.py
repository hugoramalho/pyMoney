from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *
from .insere_refe_frame import *





#~ class insere_move_frame(c_frame_ref_compra_list):
    #~ def __init__(self, framePai):
        
        #~ c_frame_ref_compra_list.__init__(self, framePai)
        


class insere_move_frame(c_frame_insere_mov):
    
    def __init__(self, framePai):
        
        self.frameLocal1 = Frame(framePai)
        self.frameLocal1.grid(row = 0, column = 0, sticky = W)
        self.frameLocal2 = Frame(framePai)
        self.frameLocal2.grid(row = 1, column = 0)

        c_frame_insere_mov.__init__(self, self.frameLocal1)
       
        
        self.define_values_CBox1(['Compra de item/serviço', 'Pagamento de contas', 'Venda de item/serviço', 'Transferência simples'])
        self.set_CBox1_default('Escolha o tipo')
    
        self.CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.__bind_CBox1__())




    def __bind_CBox1__(self):
        #Abaixo, o tipo da movimentação é definido de acordo com a escolha na CBox1:
        tipo = self.retorna_escolha_CBox1()

        
        
        if tipo == 'Compra de item/serviço':
            #Abaixo, o frame de edição de referente é instanciado:
            self.ref_compra = insere_refeMov_frame(self.frameLocal2)
            self.ref_compra.grid_frame()
            
            

            self.entr3.config_Label(text = 'Estabelecimento/fornecedor')
            
            
            
            self.entr4.config_Label(text = 'Tipo')
            self.entr4.insert_Entry(self.CBox1.retorna_escolha_CBox())
            self.entr5.config_Label(text = 'Valor total:')
            self.entr5.insert_Entry(self.refe.m_valor())
            
            #A CBox2 recebe a lista com o nome das contas cadastradas:
            self.CBox2.set_CBox_default('Escolha a conta')
            self.CBox2.config_Label(text = 'Conta cedente')
            self.define_values_CBox2(list(self.lst_contas.m_dic_nome_id().keys()))
            

            #A CBox3 recebe a lista com o nome das contas cadastradas:
            self.CBox3.set_CBox_default('Escolha a conta')
            self.CBox3.config_Label(text = 'Conta favorecida')
            self.CBox3.define_values_CBox(list(self.lst_contas.m_dic_nome_id().keys()))
            
            print(self.refe.m_dic_cadastro())


        elif(tipo == 'Pagamento de contas'):
            pass
        elif(tipo == 'Venda de item/serviço'):
            pass
        
        elif(tipo == 'Transferência simples'):
            self.entr3.config_Label(text = 'Favorecido')
            self.entr4.config_Label(text = 'Valor da transação')
            self.entr4.config_Entry(state = 'enabled')
            self.entr5.ungrid_frame()
            


            #A CBox2 recebe a lista com o nome das contas cadastradas:
            self.CBox2.set_CBox_default('Escolha a conta')
            self.CBox2.config_Label(text = 'Conta cedente')
            self.define_values_CBox2(list(self.lst_contas.m_dic_nome_id().keys()))
            

            #A CBox3 recebe a lista com o nome das contas cadastradas:
            self.CBox3.set_CBox_default('Escolha a conta')
            self.CBox3.config_Label(text = 'Conta favorecida')
            self.CBox3.define_values_CBox(list(self.lst_contas.m_dic_nome_id().keys()))
            
            

        

    #~ def __comando_B1__(self, event = None):
        #~ pass


    #~ def __comando_B2__(self, event = None):
        #~ pass



    #~ def __comando_B3__(self, event = None):
        #~ #dic_contas_id guarda o dicionário de contas, onde a chave é o nome da conta e o valor, sua id
        #~ dic_contas_id = self.lst_contas.m_dic_nome_id()
        #~ #Abaixo, a id_cont_ced recebe a id da conta, cujo nome é foi escolhido na CBox2
        #~ id_ced = dic_contas_id[self.CBox2.retorna_escolha_CBox()]
        #~ print(id_ced)
        #~ cont_ced = self.lst_contas.m_item(id_ced)
        #~ id_fav = dic_contas_id[self.CBox3.retorna_escolha_CBox()]
        #~ cont_fav = self.lst_contas.m_item(id_fav)
        
        #~ self.refe = self.ref_compra.refe
        
        #~ if self.retorna_escolha_CBox1() ==  'Compra de item/serviço':
            #~ valor = self.refe.m_valor()
            
        #~ elif self.retorna_escolha_CBox1() == 'Transferência simples':
            #~ valor = self.entr4.retorna_entr()
        
        #~ self.mov.m_re_init(conta_fav = cont_fav, conta_ced = cont_ced, id_conta_ced = id_ced, id_conta_fav =  id_fav, valor = self.refe.m_valor())
        #~ self.mov.m_executa_move()
        #~ self.bd_prog.ins_move(insert = self.mov.m_dic_cadastro())
        #~ print(self.mov.m_dic_cadastro()) 
        
        
    #~ def __comando_B4__(self, event = None):
        #~ pass


    
    #~ def __bind_calendar__(self, event):
        #~ data = self.dat_select(tipo = 'str')
        #~ print('AQUI', data)
        #~ self.insert_entr2(data)



class insere_refeMov_frame(c_frame_ref_compra_list):
    
    def __init__(self, framePai):
        c_frame_ref_compra_list.__init__(self, framePai) 
        
        
        #Instanciada uma conexão com o banco de dados do programa:
        self.bd_prog = conexao_BD_prog()
        
        self.fornec_sel = None
        self.itemServ_sel = None
        self.refe = c_refe(tipo = 'compras_list')
        self.itemServ = c_item_serv()
        self.itemServ_ref = c_itemServ_ref()
        self.valor_ref = 0
        
        self.cont = 0
        
        self.lst_itens = c_lst_BD(self.bd_prog.fetchall_itens_servs(tipo = 'Item'), tipo = 'item')
        self.lst_fornec = c_lst_BD(self.bd_prog.fetchall_fornec(), tipo = 'fornec')
        

        self.config_nome_tit1("Compra de supermercado")
        self.config_nome_tit2("Buscar estabelecimento/fornecedor")
        self.config_tit_entr1("Estabelecimento/fornecedor:")
        #~ self.config_tit_entr2("Buscar:")
        #self.config_tit_treeView1('')
        
        
        self.config_tit_CBox1('Tipo:')
        self.set_CBox1_default('Item/Serviço')
        self.config_nome_tit3("Buscar ítens")
        self.config_tit_entr2("Ítem:")
        self.config_tit_entr3("Quantidade:")
        self.config_tit_entr4("Preço unitário ou preço/quant:")
        self.config_tit_entr5("Preço total:")
        #~ self.config_tit_entr7("Buscar:")
        self.config_tit_treeView2('')
        
        self.config_tit_entr6('Estabelecimento/fornecedor')
        
        
        self.config_B3(text = 'Salvar Referente')
        #~ self.config_tit_treeView3('Lista de ítens:')
        #~ self.config_tit_col0_treeView3('Ítem:')
        #~ self.config_tit_col1_treeView3('Quantidade:')
        #~ self.config_tit_col2_treeView3('Valor unitário:')
        #~ self.config_tit_col3_treeView3('Valor total:')
        
        self.label4.config(text = 'Valor total')


   
        self.insert_lst_treeView1(self.lst_fornec.m_lst_treeView())
        self.insert_lst_treeView2(self.lst_itens.m_lst_treeView())


        self.config_B3(command = lambda: self.__comando_B3__())
            
            
        self.config_B1(command = lambda: self.__comando_B1__())
        self.config_B2(command = lambda: self.__comando_B2__())

        
        self.pointer_treeView1().bind('<<TreeviewSelect>>', lambda event: self.__bind_1_treeView1__())
        self.pointer_treeView2().bind('<<TreeviewSelect>>', lambda event: self.__bind_1_treeView2__())
        
        self.pointer_entr1().bind('<KeyRelease>', lambda event: self.__bind_entr1__())
        self.pointer_entr3().bind('<KeyRelease>', lambda event: self.__bind_entr3_4__())
        self.pointer_entr4().bind('<KeyRelease>', lambda event: self.__bind_entr3_4__())
        
        self.config_entr5_state('disabled')
        self.config_entr6_state('disabled')





    def __bind_entr1__(self, event = None):
        nome_estab = self.retorna_entr1()
        self.lst_fornec.m_carrega_lst(self.bd_prog.fetchall_fornec(like = nome_estab), tipo = 'fornec')
        self.clear_treeView1()
        self.insert_lst_treeView1(self.lst_fornec.m_lst_treeView())



    def __bind_entr3_4__(self, event = None):
        #Função de multiplicar a quantidade e preço unitário
        #Obtendo o preço total pago pelo produto
        #E inseri-lo na entr5
        quant = self.retorna_entr3()
        preco_unit = self.retorna_entr4()
        
        if quant != '' and preco_unit != '' and quant != None and preco_unit != None:
            try:
                quant = float(quant)
                preco_unit = float(preco_unit)
                self.insert_entr5(quant*preco_unit)
            except(ValueError):
                pass
        else:
            pass

    def __comando_B1__(self):
        #~ print('comando_B1__', self.fornec_sel)
        if self.fornec_sel != None:
            self.insert_entr6(self.fornec_sel.m_nome())
            self.refe.m_re_init(id_fornec = self.fornec_sel.m_idd())
            #~ print(self.fornec_sel.m_idd())
    


    def __comando_B2__(self):
        quant = float(self.retorna_entr3())
        preco_unit = float(self.retorna_entr4())
        preco_tot = float(self.retorna_entr5())
        self.valor_ref = self.valor_ref + preco_tot
        
        self.itemServ_ref = c_itemServ_ref(nome = self.itemServ_sel.m_nome(), preco_unit = preco_unit, quant = quant, preco_total = preco_tot)
        
        self.refe.m_append_item(self.itemServ_ref)
        #~ print(quant, preco_unit, preco_tot)
        self.clear_treeView3()
        self.insert_lst_treeView3(self.refe.m_lst_treeView())
        self.label4.config(text = 'Valor total:  R$ ' + str(self.valor_ref))
        




    def __comando_B3__(self):
        self.set_refe()


    def set_refe(self):
        if self.fornec_sel != None:
            self.refe.m_re_init(valor = self.valor_ref, nome_fornec = self.fornec_sel.m_nome(), cn_fornec = self.fornec_sel.m_cn())
            print(self.refe.m_dic_cadastro(), '\n\n')
            return(self.refe)
        else:
            return(None)
            print('Selecione o estabelecimento/fornecedor')


    def save_refe(self, ref):
        self.bd_prog.ins_refe(insert = ref.m_dic_cadastro())


    def __bind_1_treeView1__(self):
        id_fornec = self.idd_selection_treeView1()
        self.fornec_sel = self.lst_fornec.m_item(id_fornec)
        self.insert_entr1(self.fornec_sel.m_nome())
        
    def __bind_1_treeView2__(self):
        id_item = self.idd_selection_treeView2()
        self.itemServ_sel = self.lst_itens.m_item(id_item)
        self.insert_entr2(self.itemServ_sel.m_nome())



class transf:
    def __init__(self):
        pass
        



