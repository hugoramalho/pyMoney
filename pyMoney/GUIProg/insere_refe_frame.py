from ..BDProg.pyMoney_BD_prog import *
from ..classesProg.classes_money import *
from .GUIAbstracts.frames_prog import *
from .insere_refe_frame import *





##########################################
#########################################
##########  LEMBRAR DE SEPARAR AS CLASSES




class insere_refe_frame(c_frame_ref):

#~ class refe_frame(c_frame_ref):
    
    
    def __init__(self, framePai):
        c_frame_ref.__init__(self, framePai)
        
        self.config_nome_aba1('Referentes cadastrados')
        self.refe_cadastrados = refe_cadastrados_frame(self.pointer_frame_aba1())
        
        self.config_nome_aba2('Cadastrar referente')
        self.insere_refe = insere_refe_frame_troll(self.pointer_frame_aba2())
        

        
        

class refe_cadastrados_frame(c_frame_ref_cadastrados):
    def __init__(self, framePai):
        c_frame_ref_cadastrados.__init__(self, framePai)
        
        self.bd_prog = conexao_BD_prog()
        
        self.lst_refs = c_lst_BD(self.bd_prog.fetchall_ref(tipo = 'dict', cond = 'status_move = True'), tipo = 'ref')
    
        
        self.treeView1.config_heading('#0', text = 'Estabelecimento/fornecedor')
        self.treeView1.config_column('#0', width = 400)
        self.treeView1.config_heading('1', text = 'Tipo de referente')
        self.treeView1.config_heading('2', text = 'Valor total')
        self.treeView1.pointer_treeView().bind('<<TreeviewSelect>>', lambda event: self.__bind1_treeView1__())        
        self.insert_lst_treeView1(self.lst_refs.m_lst_treeView(tipo = 'referente'))
        
        
        self.treeView2.config_heading('#0', text = 'Item/Serviço')
        self.treeView2.config_heading('1', text = 'Quantidade')
        self.treeView2.config_heading('2', text = 'Valor unitário (R$)')
        self.treeView2.config_heading('3', text = 'Valor total (R$)')
        
        self.entr1.config_Label(text = 'Estabelecimento/Fornecedor')
        self.entr1.config_Entry(state = 'disabled')
        
        
        
    def __bind1_treeView1__(self, event = None):
        self.clear_treeView2()
        ref_select = self.lst_refs.m_item(self.idd_selection_treeView1())
        self.insert_lst_treeView2(ref_select.m_lst_treeView())
        self.entr1.insert_Entry(ref_select.m_nome_fornec())
    

    

class insere_refe_frame_troll(c_frame_ref_compra_list):
    
    def __init__(self, framePai, **kwargs):
        c_frame_ref_compra_list.__init__(self, framePai) 
        
        modo = kwargs.get('modo', 'insere_refe')
        
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

        if modo == 'insere_refe':
            self.config_B3(command = lambda: self.__comando1_B3__())
            
        if modo == 'insere_mov':
            self.config_B3(command = lambda: self.__comando2_B3__())
            
            
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
        


    def __comando1_B3__(self):
        ref = self.set_refe()
        if ref != None:
            self.save_refe(ref)
    

    def __comando2_B3__(self):
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



