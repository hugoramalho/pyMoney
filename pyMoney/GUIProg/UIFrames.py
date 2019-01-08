from pyMoney.Models.models import *
from .widgetsProg.wd_frames import *
from .UISubframes import *
# from pyMoney.controllerProg import controller


class CarregaGerFrame(Frame):
    def __init__(self, frame_master, controller):
        super().__init__(frame_master)

        self.controller = controller
        self.lst_ger = self.controller.loadAll_model(gerencia())

        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(frame_master, text='Carregar gerência', relief=GROOVE, borderwidth=2, padx="8", pady="8")
        self.frameLocal.grid(row=0, column=0, sticky=W + E + S + N, columnspan=4)

        # Bloco do título 2:
        self.label1 = Label(self.frameLocal, text='Selecione a gerência:', font = 'VERDANA')
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.treeView1 = wd_Treeview(self.frameLocal, num_cols=2, height=4, tit='')
        self.treeView1.headingText(0, 'Nome da gerência')
        self.treeView1.headingText(1, 'Nome do gestor')
        self.treeView1.insert(self.lst_ger.to_treeView())
        self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_treeView1())
        self.treeView1.grid(row=1, column=0, sticky=N + S, padx=9)

        # Bloco button1:
        self.button1 = ttk.Button(self.frameLocal, text='Carregar', command = lambda: self.command_B1())
        self.button1.grid(row=2, column=0, pady=5, padx=5, sticky=W + E)

        # Bloco button2:
        self.button2 = ttk.Button(self.frameLocal, text='Voltar ao menu', command = lambda: self.comando_B2())
        self.button2.grid(row=3, column=0, pady=5, padx=5, sticky=W + E)

        # Bloco do Text1:
        self.blocoText = wd_Text(self.frameLocal, width=35, height=6, tit='Descrição:', state=DISABLED)
        self.blocoText.grid_frame(row=1, column=1, columnspan=2, sticky=E + N + N, padx=11, pady=12)

    def bind_treeView1(self):
        ger_sel = self.lst_ger[self.treeView1.idd_selection_treeView()]
        self.blocoText.insert_text(ger_sel.descr)

    def command_B1(self):
        idd_ger = self.treeView1.idd_selection_treeView()
        ger = self.lst_ger[idd_ger]
        self.controller.inic_session(ger)

    def comando_B2(self):
        self.controller.show_frame('MenuInic')


class StatusGeralFrame(Frame):
    def __init__(self, framePai, controller):
        mes_atual = MyDate().mes_atual

        super().__init__(framePai)
        self.controller = controller
        # Blobo (1): Configurando frame que conterá as abas, o frameAbas:
        self.frameLocal = LabelFrame(self, text='Status geral', relief=GROOVE, padx=15, pady=15)
        self.frameLocal.grid(row=0, column=0, sticky=E + W + N + S)

        # Bloco (2): O título do frame que contém abas é declarado abaixo, e recebe a variável titulo dado no __init__:
        self.label1 = Label(self.frameLocal, text='Gerência do mês de '+ mes_atual, anchor=CENTER, font='VERDANA')
        self.label1.grid(row=0, column=0, pady=10, sticky= W)

        # Bloco (3): Aqui, é instanciado o __tipo Notebook, que na verdade é um frame que conterá as abas:
        self.abasBarra = ttk.Notebook(self.frameLocal)
        self.abasBarra.grid(row=1, column=0, sticky=E + W)

        # Bloco (4): Abaixo, cada aba é instanciada, cujo frame pai é o "Abas":
        self.aba1 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba1, text='Contas')
        self.frame_resumoGer = ResumoGerFrame(self.aba1, self.controller)

        self.aba2 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba2, text='Cartões de crédito')

        #self.aba3 = ttk.Frame(self.abasBarra)
        #self.abasBarra.add(self.aba3, text='Resumo de compra de itens/serviços')

        #self.aba4 = ttk.Frame(self.abasBarra)
        #self.abasBarra.add(self.aba4, text='Status parcial')

        #self.aba5 = ttk.Frame(self.abasBarra)
        #self.abasBarra.add(self.aba5, text='Previsões')


class ResumoGerFrame(Frame):
    def __init__(self, frame_master, controller):
        super().__init__(frame_master)
        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.grid()
        self.controller = controller
        self.ger_atv = controller.ger_atv
        self.lst_contas = self.controller.loadAll_model(c_conta())

        self.frameExtrato = Frame(self)
        self.frameExtrato.grid(row=0,column=0)

        self.CBox1 = wd_CBox(self.frameExtrato, set_CBox_default='Escolha a conta', tit_CBox='Extrato mensal simples', CBox_values= self.lst_contas.to_comboBox())
        self.CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())
        self.CBox1.grid(row=0, column=0, padx = 10, pady =10)

        self.dataInic_wd = wd_DateCbox(self.frameExtrato, text = 'Data inicial')
        self.dataInic_wd.grid(row=0, column=1)

        self.dataFin_wd = wd_DateCbox(self.frameExtrato, text = 'Data final')
        self.dataFin_wd.grid(row=1, column=1)

        self.treeView1 = wd_Treeview(self.frameExtrato, num_cols=3, height=10, label='Selecione uma conta')
        self.treeView1.config_column(0, width = 120)
        self.treeView1.config_column(1, width=70)
        self.treeView1.config_column(2, width=180)
        self.treeView1.headingText(0, 'Data:')
        self.treeView1.headingText(1, 'Valor')
        self.treeView1.headingText(2, 'Tipo')

        #self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda even )
        self.treeView1.grid(row=2, column=0, columnspan = 12, sticky = 'W')


        self.contasCadastr_frame = Frame(self)
        self.contasCadastr_frame.grid(row=0, column=1)

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView2 = wd_Treeview(self.contasCadastr_frame, num_cols=3, label='Saldo das contas cadastradas', height= 6)
        self.treeView2.headingText(0, 'Nome da conta:')
        self.treeView2.headingText(1, 'Tipo:')
        self.treeView2.headingText(2, 'Saldo atual:')
        self.treeView2.insert(self.lst_contas.to_treeView())
        self.treeView2.grid(row=0, column=1, rowspan=12, sticky=N)

        #self.treeView2 = wd_Treeview(self, num_cols=3)
        #self.treeView2.grid(row=1, column=0)

        #self.treeView3 = wd_Treeview(self, num_cols=3)
        #self.treeView3.grid(row=2, column=0)


    def bind_CBox1(self):
        self.treeView1.clear_treeView()
        nome_conta = self.CBox1.get_choice()
        conta = self.lst_contas.search_name(nome_conta)

        conta = self.controller.loadExtrato(conta, self.dataInic_wd.get_date(), self.dataFin_wd.get_date())
        self.treeView1.tit_treeView.config(text = 'Extrato da conta: '+conta.nome)
        self.treeView1.insert(conta.extrato.to_treeView())


class EstoqServFrame(Frame):
    def __init__(self, frameMaster, controller):
        super().__init__(frameMaster)
        self.grid(padx="8", pady="8")
        self.controller = controller

        self.tit2 = Label(self, text='Tabela de estoque', font = 'VERDANA')
        self.tit2.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        # Frame que conterá a Combobox 1
        self.opcoes_frame = LabelFrame(self, text='Buscar:')
        self.opcoes_frame.grid(row=1, column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky = 'we')

        # Bloco wd_CBox1:
        #self.categ_CBox = wd_CBox(self.opcoes_frame, tit_CBox='', set_CBox_default="Categoria", CBox_state='disabled')
        #self.categ_CBox.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        # Bloco categ_CBox:
        #self.subCateg_CBox = wd_CBox(self.opcoes_frame, tit_CBox='', set_CBox_default="Subcategoria", CBox_state='disabled')
        #self.subCateg_CBox.grid(row=0, column=1, sticky=W, padx=10, pady=10)
        # Bloco espec_CBox:
        #self.espec_CBox = wd_CBox(self.opcoes_frame, tit_CBox='', set_CBox_default="Espécie", CBox_state='disabled')
        #self.espec_CBox.grid(row=0, column=2, sticky=W, padx=10, pady=10)

        self.buscaNome_entr = wd_Entry(self.opcoes_frame, tit_Entry='Buscar por nome:')
        self.buscaNome_entr.entry.bind('<KeyRelease>', lambda event: self.buscaNome_bind())
        self.buscaNome_entr.grid_frame(row=0, column=0, padx=10)

        self.buscaCod_entr = wd_Entry(self.opcoes_frame, tit_Entry='Buscar por código:', width= 10)
        self.buscaCod_entr.entry.bind('<KeyRelease>', lambda event: self.buscaCod_bind())
        self.buscaCod_entr.grid_frame(row=0, column=1, padx=10)

        self.perfilItemServ_button = ttk.Button(self.opcoes_frame, text='Gerenciar item', width= 15, state = 'disabled')
        self.perfilItemServ_button.grid(row=0, column=2, padx=10, sticky = 'wes')

        #self.inItemServ_button = ttk.Button(self.opcoes_frame, text='Inserir item ou serviço', width= 10, command = self.ins_itenServ)
        #self.inItemServ_button.grid(row=1, column=3, padx=10, sticky = 'we')

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1_wd = wd_Treeview(self, num_cols=3, height=16)
        self.treeView1_wd.headingText(0, 'Nome')
        self.treeView1_wd.headingText(1, 'Código')
        self.treeView1_wd.headingText(2, 'quantidade')
            # Configurando .bind da Treeview:
        #self.itens_treeView.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1(event))
        #self.itens_treeView.treeView.bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))
        self.treeView1_wd.grid(row=2, column=0, columnspan=5, padx=10, sticky = 'W')

        self.menu_RC = sub_Menu(self)

        # Configurando o menu "righ-click" da treeView:
        #self.menu_RC.config_nome_B1("Alterar dados")
        #self.menu_RC.config_comando_B1(lambda: self.edit_itemServ())
        #self.menu_RC.config_comando_B2(lambda: self.del_itemServ())
        #self.menu_RC.config_nome_B2("Excluir item/Serviço")
        self.carrega_itens()

    def buscaNome_bind(self):
        self.buscaCod_entr.limpa_entr()
        nome = self.buscaNome_entr.get_text()
        if nome != '':
            lst_item = self.controller.search_name_item(nome)
            self.treeView1_wd.clear_treeView()
            self.treeView1_wd.insert(lst_item.to_treeView())
        else:
            self.carrega_itens()

    def buscaCod_bind(self):
        self.buscaNome_entr.limpa_entr()
        code = self.buscaCod_entr.get_text()
        if code != '':
            lst_item = self.controller.search_code_item(code)
            self.treeView1_wd.clear_treeView()
            self.treeView1_wd.insert(lst_item.to_treeView())
        else:
            self.carrega_itens()

    def carrega_itens(self):
        self.treeView1_wd.clear_treeView()
        self.treeView1_wd.tit_treeView.config(text='Itens em estoque:')
        self.lst_itens = self.controller.loadAll_model(item())
        self.treeView1_wd.insert(self.lst_itens.to_treeView())


class AlteraContaFrame(Toplevel):
    def __init__(self, frameMaster, controller):
        super().__init__(frameMaster, padx=15, pady=15)
        self.update()
        self.deiconify()
        self.resizable(False, False)
        # self.grid()
        self.protocol("WM_DELETE_WINDOW", self.callback)

        self.controller = controller
        self.lst_contas = self.controller.loadAll_model(c_conta())
        self.conta_sel = c_conta()
        self.buildFrame()

    def callback(self):
        self.destroy()

    def buildFrame(self):
        self.alterConta_label = Label(self, text='Alterar dados de conta', font='VERDANA')
        self.alterConta_label.grid(row=0, column=0, sticky='W', padx=8, pady=8, columnspan=2)

        self.conta_cbox = wd_CBox(self, tit_CBox='Contas cadastradas:', set_CBox_default='Escolha uma conta', CBox_values=self.lst_contas.to_comboBox())
        self.conta_cbox.CBox.bind('<<ComboboxSelected>>', lambda event: self.conta_cbox_bind())
        self.conta_cbox.grid(row=1, column=0, sticky='W')

        self.nomeConta_entr = wd_Entry(self, label='Nome da conta:', state='readonly')
        self.nomeConta_entr.grid_frame(row=2, column=0)

        self.saldo_entr = wd_Entry(self, label='Saldo (R$):', state='readonly')
        self.saldo_entr.grid_frame(row=2, column=1)

        self.tipo_entr = wd_Entry(self, label='Tipo de conta:', state='readonly')
        self.tipo_entr.grid_frame(row=2, column=3)

        self.save_button = ttk.Button(self, text='Salvar alterações', command=lambda: self.salva_alter(), state='disabled')
        self.save_button.grid(row=3, column=0, sticky='we', padx=8, pady=8)

        self.cancel_button = ttk.Button(self, text='Cancelar', command=lambda: self.callback())
        self.cancel_button.grid(row=3, column=1, sticky='we', padx=8, pady=8)

    def conta_cbox_bind(self):
        self.conta_sel = self.lst_contas.search_name(self.conta_cbox.get_choice())
        self.save_button.config(state='enabled')
        self.nomeConta_entr.insert_text(self.conta_sel.nome)
        self.nomeConta_entr.entry.config(state='enabled')
        self.saldo_entr.insert_text(self.conta_sel.saldo)
        self.saldo_entr.entry.config(state='enabled')
        self.tipo_entr.insert_text(self.conta_sel.tipo)
        self.tipo_entr.entry.config(state='enabled')

    def salva_alter(self):
        self.conta_sel.nome = self.nomeConta_entr.get_text()
        self.conta_sel.saldo = float(self.saldo_entr.get_text())
        self.conta_sel.tipo = self.tipo_entr.get_text()
        self.controller.update_model(self.conta_sel)
        self.lst_contas = self.controller.loadAll_model(c_conta())
        self.conta_cbox.define_values_CBox(self.lst_contas.to_comboBox())
        self.conta_cbox.set_CBox_default(self.conta_sel.nome)


class InsConta(Toplevel):
    def __init__(self, frameMaster, controller):
        super().__init__(padx=15, pady=15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.controller = controller
        self.tipo_sel = 'Escolha a opção'
        self.conta_in = None

        self.protocol("WM_DELETE_WINDOW", self.callback)
        self.buildFrame()

    def buildFrame(self):
        self.InsConta_label = Label(self, text='Inserir nova conta', font='VERDANA')
        self.InsConta_label.grid(row=0, column=1, sticky='W', padx=10, pady=10, columnspan=2)

        self.tipoConta_cbox = wd_CBox(self, tit_CBox='Tipo da conta:', set_CBox_default='Escolha a opção', CBox_values=['Conta corrente', 'Conta poupança'])
        self.tipoConta_cbox.CBox.bind('<<ComboboxSelected>>', lambda event: self.tipoConta_cbox_bind())
        self.tipoConta_cbox.grid(row=1, column=0, sticky='W')

        self.nomeConta_entr = wd_Entry(self, label='Nome da conta:', state='disabled')
        self.nomeConta_entr.grid_frame(row=2, column=0)

        self.saldo_entr = wd_Entry(self, label='Saldo inicial(R$):', state='disabled')
        self.saldo_entr.grid_frame(row=2, column=1)


        self.save_button = ttk.Button(self, text='Salvar conta', command=lambda: self.salva_conta(), state='disabled')
        self.save_button.grid(row=3, column=0, sticky='we', padx=8, pady=8)

        self.cancel_button = ttk.Button(self, text='Cancelar', command=lambda: self.callback())
        self.cancel_button.grid(row=3, column=1, sticky='we', padx=8, pady=8)

    def tipoConta_cbox_bind(self):
        self.tipo_sel = self.tipoConta_cbox.get_choice()
        self.nomeConta_entr.entry.config(state='enabled')
        self.saldo_entr.entry.config(state='enabled')
        self.save_button.config(state='enabled')

    def salva_conta(self):
        saldoInic = float(self.saldo_entr.get_text())
        nome_conta = self.nomeConta_entr.get_text()

        self.conta_in = c_conta()
        self.conta_in.id_ger = self.controller.ger_atv.idd
        self.conta_in.nome = nome_conta
        self.conta_in.saldo = saldoInic
        self.conta_in.tipo = self.tipo_sel

        feedback = self.controller.insert_model(self.conta_in)
        if feedback is 0:
            showinfo('Salvo!', 'Conta cadastrada com sucesso!')
            self.nomeConta_entr.limpa_entr()
            self.saldo_entr.limpa_entr()



    def callback(self):
        self.destroy()





class InsTEF(Frame):
    def __init__(self, frameMaster, controller):
        super().__init__(frameMaster)
        self.grid(padx=8,pady=8)
        self.controller = controller

        self.conta_ced = c_conta()
        self.conta_fav = c_conta()
        self.data = None

        self.lst_contas = self.controller.loadAll_model(c_conta())
        self.buildFrame()

    def buildFrame(self):

        self.tef_label = Label(self, text='Transferência de fundos', font = 'VERDANA')
        self.tef_label.grid(row=0,column=0,padx=10,pady=10, columnspan = 2, sticky = 'W')

        self.contaCed_cbox = wd_CBox(self, tit_CBox='Conta Cedente', set_CBox_default='Escolha a conta', CBox_values=self.lst_contas.to_comboBox())
        self.contaCed_cbox.grid(row=1, column=0, sticky = 'W', padx=8)

        self.contaFav_cbox = wd_CBox(self, tit_CBox='Conta Favorecida', set_CBox_default='Escolha a conta', CBox_values=self.lst_contas.to_comboBox())
        self.contaFav_cbox.grid(row=1, column=1, sticky = 'W', padx=8)

        self.valor_entr = wd_Entry(self, label='Valor (R$):')
        self.valor_entr.grid_frame(row=2,column=0, sticky = 'W')

        self.efetiva_button = ttk.Button(self, text = 'Efetivar', command = lambda: self.efetiva())
        self.efetiva_button.grid(row=3, column=0, sticky = 'W')

        self.calendar_wd = wd_calendario(self)
        self.calendar_wd.grid(row=1, column=2, rowspan = 3)

    def efetiva(self):
        if self.verfContas():
            if self.verfValor():
                conta_ced = self.lst_contas.search_name(self.contaCed_cbox.get_choice())
                conta_fav = self.lst_contas.search_name(self.contaFav_cbox.get_choice())
                valor = self.valor_entr.get_text()
                valor = float(valor)

                transac_in = transac()
                transac_in.tipo = 'TEF'
                transac_in.conta_fav = conta_fav
                transac_in.conta_ced = conta_ced
                transac_in.valor =valor
                transac_in.data = self.calendar_wd.selection()
                transac_in.efetiva()
                print(transac_in)
                print(conta_fav.saldo, conta_fav.saldo)
                self.controller.insert_model(transac_in)
        else:
            pass

    def verfValor(self):
        try:
            valor = self.valor_entr.get_text()
            valor = float(valor)
            return True
        except:
            showinfo('Atenção!', 'Valor digitado é inválido.\nDigite somente números')
            return False

    def verfContas(self):
        nome_conta_ced = self.contaCed_cbox.get_choice()
        nome_conta_fav = self.contaFav_cbox.get_choice()

        if nome_conta_ced == 'Escolha a conta':
            showinfo('Atenção!', 'Escolha uma conta cedente!')
            return False
        elif nome_conta_fav == 'Escolha a conta':
            showinfo('Atenção!', 'Escolha uma conta favorecida!')
            return False

        conta_ced = self.lst_contas.search_name(nome_conta_ced)
        conta_fav = self.lst_contas.search_name(nome_conta_fav)
        if conta_fav.idd != conta_ced.idd:
            return True
        else:
            showinfo('Atenção!', 'Conta cedente e favorecida são iguais.\nEscolha contas diferentes.')
            return False

class ItemServFrame(Frame):
    def __init__(self, frameMaster, controller):
        super().__init__(frameMaster)
        self.grid(padx="8", pady="8")
        self.controller = controller

        self.tit2 = Label(self, text='Serviços e itens cadastrados', font = 'VERDANA')
        self.tit2.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        # Frame que conterá a Combobox 1
        self.opcoes_frame = LabelFrame(self, text='Opções:')
        self.opcoes_frame.grid(row=1, column=0, padx=10, pady=5, ipadx=15, ipady=5)

        # Bloco wd_CBox1:
        self.tipo_CBox = wd_CBox(self.opcoes_frame, set_CBox_default='Itens', CBox_state='readonly',
                                 CBox_values=['Itens', 'Serviços'], tit_CBox='Filtrar por:')
        self.tipo_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_tipoCBox())

        self.tipo_CBox.grid(row=0, column=0, sticky=S, padx=10, pady=10)

        # Bloco wd_CBox1:
        self.categ_CBox = wd_CBox(self.opcoes_frame, tit_CBox='', set_CBox_default="Categoria", CBox_state='disabled')
        self.categ_CBox.grid(row=0, column=1, sticky=W, padx=10, pady=10)
        # Bloco categ_CBox:
        self.subCateg_CBox = wd_CBox(self.opcoes_frame, tit_CBox='', set_CBox_default="Subcategoria", CBox_state='disabled')
        self.subCateg_CBox.grid(row=0, column=2, sticky=W, padx=10, pady=10)
        # Bloco espec_CBox:
        self.espec_CBox = wd_CBox(self.opcoes_frame, tit_CBox='', set_CBox_default="Espécie", CBox_state='disabled')
        self.espec_CBox.grid(row=0, column=3, sticky=W, padx=10, pady=10)

        self.buscaNome_entr = wd_Entry(self.opcoes_frame, tit_Entry='Buscar por nome:')
        self.buscaNome_entr.entry.bind('<KeyRelease>', lambda event: self.buscaNome_bind())
        self.buscaNome_entr.grid_frame(row=1, column=0, padx=10)

        self.buscaCod_entr = wd_Entry(self.opcoes_frame, tit_Entry='Buscar por código:', width= 10)
        self.buscaCod_entr.entry.bind('<KeyRelease>', lambda event: self.buscaCod_bind())
        self.buscaCod_entr.grid_frame(row=1, column=1, padx=10)

        self.perfilItemServ_button = ttk.Button(self.opcoes_frame, text='Visualizar/alterar dados', width= 10)
        self.perfilItemServ_button.grid(row=1, column=2, padx=10, sticky = 'we')

        self.inItemServ_button = ttk.Button(self.opcoes_frame, text='Inserir item ou serviço', width= 10, command = self.ins_itenServ)
        self.inItemServ_button.grid(row=1, column=3, padx=10, sticky = 'we')

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.servs_treeView = wd_Treeview(self, num_cols=5, height=16)
        self.servs_treeView.headingText(0, 'Nome')
        self.servs_treeView.headingText(1, 'Código')
        self.servs_treeView.headingText(2, 'Categoria')
        self.servs_treeView.headingText(3, 'Subcategoria')
        self.servs_treeView.headingText(4, 'Espécie')
            # Configurando .bind da Treeview:
        self.servs_treeView.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1(event))
        self.servs_treeView.treeView.bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))
        #self.servs_treeView.grid(row=2, column=0, columnspan=5, padx=10, sticky = 'W')

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.itens_treeView = wd_Treeview(self, num_cols=6, height=16)
        self.itens_treeView.headingText(0, 'Nome')
        self.itens_treeView.headingText(1, 'Código')
        self.itens_treeView.headingText(2, 'quant')
        self.itens_treeView.headingText(3, 'Categoria')
        self.itens_treeView.headingText(4, 'Subcategoria')
        self.itens_treeView.headingText(5, 'Espécie')
            # Configurando .bind da Treeview:
        self.itens_treeView.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1(event))
        self.itens_treeView.treeView.bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))
        #self.itens_treeView.grid(row=2, column=0, columnspan=5, padx=10, sticky ='W')

        self.menu_RC = sub_Menu(self)

        # Configurando o menu "righ-click" da treeView:
        self.menu_RC.config_nome_B1("Alterar dados")
        self.menu_RC.config_comando_B1(lambda: self.edit_itemServ())
        self.menu_RC.config_comando_B2(lambda: self.del_itemServ())
        self.menu_RC.config_nome_B2("Excluir item/Serviço")

        self.bind_tipoCBox()

    def buscaNome_bind(self):
        self.buscaCod_entr.limpa_entr()
        nome = self.buscaNome_entr.get_text()
        if nome != '':
            tipo = self.tipo_CBox.get_choice()
            if tipo == 'Itens':
                lst_item = self.controller.search_name_item(nome)
                self.itens_treeView.clear_treeView()
                self.itens_treeView.insert(lst_item.to_treeView())
            else:
                lst_serv = self.controller.search_name_serv(nome)
                self.itens_treeView.clear_treeView()
                self.itens_treeView.insert(lst_serv.to_treeView())
        else:
            self.bind_tipoCBox()

    def buscaCod_bind(self):
        self.buscaNome_entr.limpa_entr()
        code = self.buscaCod_entr.get_text()
        if code != '':
            tipo = self.tipo_CBox.get_choice()
            if tipo == 'Itens':
                lst_item = self.controller.search_code_item(code)
                self.itens_treeView.clear_treeView()
                self.itens_treeView.insert(lst_item.to_treeView())
            else:
                lst_servs = self.controller.search_code_serv(code)
                self.itens_treeView.clear_treeView()
                self.itens_treeView.insert(lst_servs.to_treeView())

        else:
            self.bind_tipoCBox()

    def update(self):
        self.bind_tipoCBox()

    def ins_itenServ(self):
        ins_frame = InsItemServ(self, self.controller)

    def popup_menu(self, event):
        self.menu_RC.popup(event)

    def bind_tipoCBox(self):
        tipo = self.tipo_CBox.get_choice()
        if tipo == 'Itens':
            self.servs_treeView.grid_forget()
            self.itens_treeView.clear_treeView()
            self.itens_treeView.tit_treeView.config(text ='Itens cadastrados:')
            self.lst_itens = self.controller.loadAll_model(item())
            self.itens_treeView.insert(self.lst_itens.to_treeView())
            self.itens_treeView.grid(row=2, column=0, columnspan=5, padx=10, sticky='W')

        if tipo == 'Serviços':
            self.itens_treeView.grid_forget()
            self.servs_treeView.clear_treeView()
            self.servs_treeView.tit_treeView.config(text='Serviços cadastrados:')
            self.lst_servs = self.controller.loadAll_model(serv())
            self.servs_treeView.insert(self.lst_servs.to_treeView())
            self.servs_treeView.grid(row=2, column=0, columnspan=5, padx=10, sticky='W')


    def bind_event2_treeView1(self, event):
        self.popup_menu(event)

    def edit_itemServ(self):
        idd_item = self.itens_treeView.idd_selection_treeView()
        item_sel = self.lst_itens[idd_item]
        #edita_item = EditItemFrame(self, self.controller, item_sel)


class InsItemServ(Toplevel):
    def __init__(self, frameMaster, controller):
        super().__init__(padx = 15, pady = 15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.controller = controller
        self.frameMaster = frameMaster
        self.protocol("WM_DELETE_WINDOW", self.callback)

        self.__build_widgets__()

    def __build_widgets__(self):
        self.tit2 = Label(self, text='Cadastrar item ou serviço', font='VERDANA')
        self.tit2.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        # Frame que conterá a Combobox 1
        self.opcoes_frame = LabelFrame(self, text='LabelFrame', relief=FLAT)
        self.opcoes_frame.grid(row=1, column=0, padx=10, pady=5, ipadx=15, ipady=5)

        # Bloco wd_CBox1:
        self.tipo_CBox = wd_CBox(self.opcoes_frame, set_CBox_default='Escolha a opção', CBox_state='readonly',
                                 CBox_values=['Item', 'Serviço',], tit_CBox='Tipo:')
        self.tipo_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_tipo_CBox())
        self.tipo_CBox.grid(row=0, column=0, sticky=S, padx=10, pady=10)

        # Bloco wd_CBox1:
        self.categ_CBox = wd_CBox(self.opcoes_frame, tit_CBox='Categoria', set_CBox_default='Escolha a opção',
                                  CBox_state='disabled')
        self.categ_CBox.grid(row=0, column=1, sticky=W, padx=10, pady=10)
        # Bloco categ_CBox:
        self.subCateg_CBox = wd_CBox(self.opcoes_frame, tit_CBox='Subcategoria', set_CBox_default='Escolha a opção',
                                     CBox_state='disabled')
        self.subCateg_CBox.grid(row=0, column=2, sticky=W, padx=10, pady=10)
        # Bloco espec_CBox:
        #self.espec_CBox = wd_CBox(self.opcoes_frame, tit_CBox='Espécie', set_CBox_default="Escolha a opção", CBox_state='readonly')
        #self.espec_CBox.grid(row=0, column=3, sticky=W, padx=10, pady=10)

        self.nome_entr = wd_Entry(self.opcoes_frame, tit_Entry='Nome:', state='disabled')
        self.nome_entr.grid_frame(row=1, column=0, padx=10)

        self.cod_entr = wd_Entry(self.opcoes_frame, tit_Entry='Defina um código:', width= 10, state = 'disabled')
        self.cod_entr.grid_frame(row=1, column=1, padx=10)

        self.cancel_button = ttk.Button(self.opcoes_frame, text='Cancelar', width= 10, command = self.cancel)
        self.cancel_button.grid(row=1, column=2, padx=10, sticky = 'we')

        self.save_button = ttk.Button(self.opcoes_frame, text='Salvar', width= 10, command = self.save)
        self.save_button.grid(row=1, column=3, padx=10, sticky = 'we')

        self.descr_bloco = wd_Text(self.opcoes_frame, label='Descrição', width= 45, state=DISABLED)
        self.descr_bloco.grid_frame(row=2, column=0, columnspan = 6)

    def bind_tipo_CBox(self):
        tipo = self.tipo_CBox.get_choice()
        if tipo != 'Escolha a opção':
            self.nome_entr.entry.config(state ='enabled')
            self.cod_entr.entry.config(state='enabled')
            self.descr_bloco.text.config(state=NORMAL)

    def save(self):
        tipo = self.tipo_CBox.get_choice()
        if tipo == 'Item':
            item_ins = item()
            item_ins.nome = self.nome_entr.get_text()
            item_ins.codigo = self.cod_entr.get_text()
            item_ins.descr = self.descr_bloco.get_text()
            self.controller.insert_model(item_ins)

        if tipo == 'Serviço':
            serv_ins = serv()
            serv_ins.nome = self.nome_entr.get_text()
            serv_ins.codigo = self.cod_entr.get_text()
            serv_ins.descr = self.descr_bloco.get_text()
            self.controller.insert_model(serv_ins)

    def cancel(self):
        self.callback()

    def callback(self):
        self.frameMaster.update()
        self.destroy()


class MenuInic(Frame):
    def __init__(self, framePai, controller, **kwargs):
        super().__init__(framePai, **kwargs)
        self.controller = controller
        # Bloco (2.1): Abaixo, é declarado o frame que conterá o menu. O frame está contido no frame-pai:
        self.frameLocal = Frame(self)
        self.frameLocal.grid(row=0, column=0, sticky=N + S, pady=2, padx=2)
        self.grid()

        # Subtítulos do programa:
        # O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.label1 = Label(self.frameLocal, anchor=CENTER, width=18, text="Bem Vindo ao pyMoney!")
        self.label1.grid(row=0, column=0, sticky=E + W)  # Subtitulo fixado na origem do "frameLocal"(row=0, column=0)

        self.separator = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        self.separator.grid(row=1, column=0, sticky='we', pady=2, padx=2)

        # O subtitulo3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.label2 = Label(self.frameLocal, padx=5, text="Inicie ou carregue uma gerência para começar...")
        self.label2.grid(row=2, column=0, sticky=E + W)

        # O button1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.button1 = ttk.Button(self.frameLocal, text="Nova gerência", command=lambda: self.comando_B1())
        self.button1.grid(row=3, column=0, sticky=W + E, padx=2)

        # O  button2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.button2 = ttk.Button(self.frameLocal, text="Carregar gerência", command=lambda: self.comando_B2())
        self.button2.grid(row=4, column=0, sticky=W + E, padx=2)

        # O  button2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.button3 = ttk.Button(self.frameLocal, text="Ajuda", command=lambda: self.comando_B3())
        self.button3.grid(row=5, column=0, sticky=W + E, padx=2)

    def comando_B1(self):
        self.controller.show_frame('NovaGerFrame')

    def comando_B2(self):
        self.controller.show_frame('frame_carrega_ger')

    def comando_B3(self):
        pass


class NovaGerFrame(Frame):
    def __init__(self, frame_master, controller, **kwargs):
        super().__init__(frame_master, **kwargs)
        self.controller = controller
        self.lst_contas = MyCollection()
        self.id_ger = None

        self.__build_widgets__()

    def __build_widgets__(self):

        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(self, text='Incluir nova gerência', relief=GROOVE, borderwidth=2, padx="8",
                                     pady="8")
        self.frameLocal.grid(row=0, column=0, sticky=W + E + S + N)

        # Bloco entr1:
        self.entr1 = wd_Entry(self.frameLocal, label='Nome da gerência:')
        self.entr1.grid_frame(row=0, column=0, padx=5)

        # Bloco entr2:
        self.entr2 = wd_Entry(self.frameLocal, label='Nome do gestor:')
        self.entr2.grid_frame(row=1, column=0, padx=5)

        # Separador 1:
        self.separador1 = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        self.separador1.grid(row=2, column=0, pady=6, columnspan=3, sticky='we')

        # Bloco do título ?:
        self.tit2 = Label(self.frameLocal, text='Incluir contas:')
        self.tit2.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        # Bloco wd_CBox1:
        self.CBox1 = wd_CBox(self.frameLocal, set_CBox_default='Tipo de conta:')
        self.CBox1.define_values_CBox(['Conta corrente', 'Conta poupança', 'Cartão de crédito', 'Carteira', 'Caixa'])
        self.CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.__bind_CBox1__())
        self.CBox1.grid_frame(row=4, column=0, padx=5, pady=5)

        # Bloco entr3:
        self.entr3 = wd_Entry(self.frameLocal, label='Nome da conta:')
        self.entr3.grid_frame(row=4, column=1, padx=5, pady=5)

        # Bloco entr4:
        self.entr4 = wd_Entry(self.frameLocal, label='Saldo inicial:')
        self.entr4.grid_frame(row=4, column=2, padx=5, pady=5)

        # Bloco button1:
        self.botao1 = ttk.Button(self.frameLocal, text='Enviar conta', command=lambda: self.__comando_B1__())
        self.botao1.grid(row=5, column=0, pady=5, padx=5, sticky=W + E)

        # Separador 2:
        self.separador2 = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        self.separador2.grid(row=6, column=0, pady=6, columnspan=3, sticky='we')

        # Bloco button2:
        self.botao2 = ttk.Button(self.frameLocal, text='Voltar ao menu', command=lambda: self.__comando_B2__())
        self.botao2.grid(row=7, column=0, pady=5, padx=5, sticky=W + E)

        # Bloco button3:
        self.botao3 = ttk.Button(self.frameLocal, text='Salvar gerência', command=lambda: self.__comando_B3__())
        self.botao3.grid(row=7, column=1, columnspan=2, pady=5, padx=5, sticky=W + E)

        # Bloco do Text1:
        self.blocoText = wd_Text(self.frameLocal, width=35, height=4, label='Descrição da gerência')
        self.blocoText.grid_frame(row=0, column=1, rowspan=2, columnspan=2, sticky=E + N + N, padx=11, pady=12)

        self.treeView1 = wd_Treeview(self.frameLocal, num_cols=3, height=11, rowspan=13)
        self.treeView1.headingText(0, 'Nome da conta:')
        self.treeView1.headingText('1', 'Tipo:')
        self.treeView1.headingText('2', 'Saldo inicial: (R$)')
        self.treeView1.grid(row=0, column=3, rowspan=8, sticky=N + S, columnspan=2, padx=9)


    def __comando_B1__(self):
        # Abaixo são capturados os dados inseridos:
        tipo = self.CBox1.get_choice()
        nome_conta = self.entr3.get_text()
        saldo_inic = self.entr4.get_text()

        # Abaixo, a conta é instanciada:
        conta = c_conta(tipo=tipo, nome=nome_conta, saldo=saldo_inic)
        self.lst_contas.append(conta)

        print(self.lst_contas)
        # Abaixo, a conta é inserida na treeView:
        self.treeView1.insert(conta.to_treeView())
        # Abaixo os elementos da interface são reiniciados/limpados:
        self.entr3.limpa_entr()
        self.entr4.limpa_entr()
        self.CBox1.set_CBox_default('Escolha a opção:')

    def __comando_B3__(self):
        nome_ger = self.entr1.get_text()
        nome_gest = self.entr2.get_text()
        descr = self.blocoText.get_text()
        self.treeView1.clear_treeView()

        ger = gerencia(nome_ger=nome_ger, nome_gest=nome_gest, descr=descr, lst_contas=self.lst_contas)
        # ABAIXO A GERENCIA É ENVIADA AO CONTROLLER PARA SER SALVA NO BANCO DE DADOS:
        self.controller.insert_model(ger)

    def __bind_CBox1__(self):
        tipo = self.CBox1.get_choice()
        if tipo == 'Cartão de crédito':
            self.entr4.config_Entry_state('disabled')
        else:
            self.entr4.config_Entry_state('enabled')

    def __comando_B2__(self):
        self.controller.show_frame('MenuInic')


class AlteraGerFrame(Toplevel):
    def __init__(self, frame_master, controller):
        super().__init__()
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.controller = controller
        self.ger_atv = self.controller.ger_atv
        #self.lst_contas = MyCollection()
        #self.id_ger = None

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):

        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(self, text='Alterar gerência', relief=FLAT, borderwidth=2, padx="15",
                                     pady="15", font = 'VERDANA')
        self.frameLocal.grid(row=0, column=0, sticky=W + E + S + N)

        # Bloco entr1:
        self.entr1 = wd_Entry(self.frameLocal, label='Nome da gerência:', set_Entry_default=self.ger_atv.nome_ger)
        self.entr1.grid_frame(row=0, column=0, padx=5)

        # Bloco entr2:
        self.entr2 = wd_Entry(self.frameLocal, label='Nome do gestor:', set_Entry_default=self.ger_atv.nome_gest)
        self.entr2.grid_frame(row=1, column=0, padx=5)

        # Separador 1:
        self.separador1 = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        self.separador1.grid(row=2, column=0, pady=6, columnspan=3, sticky='we')

        # Bloco do título ?:
        #self.tit2 = entry_Label(self.frameLocal, text='Incluir contas:')
        #self.tit2.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        # Bloco wd_CBox1:
        #self.tipo_CBox = wd_CBox(self.frameLocal, set_CBox_default='Tipo de conta:')
        #self.tipo_CBox.define_values_CBox(['Conta corrente', 'Conta poupança', 'Cartão de crédito', 'Carteira', 'Caixa'])
        #self.tipo_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_tipoCBox())
        #self.tipo_CBox.grid(row=4, column=0, padx=5, pady=5)

        # Bloco entr3:
        #self.entr3 = wd_Entry(self.frameLocal, entry_Label='Nome da conta:')
        #self.entr3.grid(row=4, column=1, padx=5, pady=5)

        # Bloco entr4:
        #self.entr4 = wd_Entry(self.frameLocal, entry_Label='Saldo inicial:')
        #self.entr4.grid(row=4, column=2, padx=5, pady=5)

        # Bloco button1:
        #self.botao1 = ttk.Button(self.frameLocal, text='Enviar conta', command=lambda: self.__comando_B1__())
        #self.botao1.grid(row=5, column=0, pady=5, padx=5, sticky=W + E)

        # Separador 2:
        #self.separador2 = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        #self.separador2.grid(row=6, column=0, pady=6, columnspan=3, sticky='we')

        # Bloco button2:
        self.botao2 = ttk.Button(self.frameLocal, text='Cancelar', command=lambda: self.__comando_B2__())
        self.botao2.grid(row=7, column=0, pady=5, padx=5, sticky=W + E)

        # Bloco button3:
        self.botao3 = ttk.Button(self.frameLocal, text='Salvar alterações', command=lambda: self.__comando_B3__())
        self.botao3.grid(row=7, column=1, columnspan=2, pady=5, padx=5, sticky=W + E)

        # Bloco do Text1:
        self.blocoText = wd_Text(self.frameLocal, width=35, height=4, label='Descrição da gerência')
        self.blocoText.insert_text(self.ger_atv.descr)
        self.blocoText.grid_frame(row=0, column=1, rowspan=2, columnspan=2, sticky=E + N + N, padx=11, pady=12)

        #self.treeView1 = wd_Treeview(self.frameLocal, num_cols=3, height=11, rowspan=13)
        #self.treeView1.headingText(0, 'Nome da conta:')
        #self.treeView1.headingText('1', 'Tipo:')
        #self.treeView1.headingText('2', 'Saldo inicial: (R$)')
        #self.treeView1.grid(row=0, column=3, rowspan=8, sticky=N + S, columnspan=2, padx=9)


    def __comando_B1__(self):
        # Abaixo são capturados os dados inseridos:
        #__tipo = self.tipo_CBox.get_choice()
        #nome_conta = self.entr3.get_text()
        #saldo_inic = self.entr4.get_text()

        # Abaixo, a conta é instanciada:
        #conta = c_conta(__tipo=__tipo, nome=nome_conta, saldo=saldo_inic)
        #self.lst_contas.append(conta)

        #print(self.lst_contas)
        # Abaixo, a conta é inserida na treeView:
        #self.treeView1.insert(conta.to_treeView())
        # Abaixo os elementos da interface são reiniciados/limpados:
        #self.entr3.limpa_entr()
        #self.entr4.limpa_entr()
        #self.tipo_CBox.set_CBox_default('Escolha a opção:')
        pass

    def __comando_B3__(self):
        #nome_ger = self.entr1.get_text()
        #nome_gest = self.entr2.get_text()
        #descr = self.text.get_text()
        #self.treeView1.clear_treeView()

        #ger = gerencia(nome_ger=nome_ger, nome_gest=nome_gest, descr=descr, lst_contas=self.lst_contas)
        # ABAIXO A GERENCIA É ENVIADA AO CONTROLLER PARA SER SALVA NO BANCO DE DADOS:
        self.ger_atv.nome_ger = self.entr1.get_text()
        self.ger_atv.nome_gest = self.entr2.get_text()
        self.ger_atv.descr = self.blocoText.get_text()

        self.controller.update_model(self.ger_atv)

    def __bind_CBox1__(self):
        #__tipo = self.tipo_CBox.get_choice()
        #if __tipo == 'Cartão de crédito':
            #self.entr4.config_Entry_state('disabled')
        #else:
            #self.entr4.config_Entry_state('enabled')
        pass

    def __comando_B2__(self):
        #self.controller.show_frame('MenuInic')
        self.callback()

    def callback(self):
        self.destroy()


class ClientesFrame(LabelFrame):
    def __init__(self, framePai, controller):
        super().__init__(framePai, text = 'Clientes')
        self.grid()

        self.controller = controller
        self.ger_atv = controller.ger_atv
        self.lst_clientes = self.controller.loadAll_model(cliente())

        self.__build_widgets__()

    def update_frame(self):
        self.lst_clientes = self.controller.loadAll_model(cliente())
        self.__build_widgets__()

    def __build_widgets__(self):
        self.frameLocal = LabelFrame(self, relief=FLAT, text='', padx="8", pady="8")
        self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)

        self.altera_button = ttk.Button(self.frameLocal, text = 'Visualizar/Alterar perfil', command = self.perfilCliente)
        self.altera_button.grid(row = 0, column = 0, sticky = 'we', padx = 5)

        #self.separatorV = ttk.Separator(self.frameLocal, orient = VERTICAL)
        #self.separatorV.grid(row = 0, column = 1, sticky = 'nsw')

        self.insCliente_button = ttk.Button(self.frameLocal, text = 'Inserir cliente', command = lambda: self.insCliente())
        self.insCliente_button.grid(row=0, column=2, sticky = 'we', padx = 5)

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = wd_Treeview(self.frameLocal, num_cols=5, height=16, tit= 'Clientes cadastrados:')
        self.treeView1.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
        self.treeView1.headingText(0, 'Nome')
        self.treeView1.headingText(1, 'Celular')
        self.treeView1.headingText(2, 'Telefone')
        self.treeView1.headingText(3, 'E-mail')
        self.treeView1.headingText(4, 'Cidade')
        self.treeView1.config_column(3, width=160)


        self.treeView1.insert(self.lst_clientes.to_treeView())


        #self.pointer_frameLocal().focus_set()
        #self.pointer_frameLocal().bind("<Button-3>", popup)

        self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda event: self.verf_treeView())
        self.treeView1.treeView.bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))

        self.verf_treeView()


    def verf_treeView(self):
        if self.treeView1.idd_selection_treeView() is None:
            self.altera_button.config(state='disabled')
        else:
            self.altera_button.config(state='enabled')

    def perfilCliente(self):
        cliente_escolhido = self.lst_clientes[self.treeView1.idd_selection_treeView()]
        perfil = PerfilClienteFrame(self, self.controller, cliente_escolhido)


    def insCliente(self):
        frameIns = InsClienteFrame(self, self.controller)



    def bind_event2_treeView1(self, event):
        #self.menu_RC(event)
        pass

    def del_cliente(self):
        idd_client_sel = self.treeView1.idd_selection_treeView()
        cliente = self.lst_clientes[idd_client_sel]
        cliente.delete()


class InsClienteFrame(Toplevel):
    def __init__(self, frame_master, controller):
        super().__init__(padx = 15, pady = 15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frame_master = frame_master
        self.controller = controller
        self.ger_atv = controller.ger_atv

        self.ender_cliente = enderecoIdent()
        self.contat_cliente = contato()
        self.cliente_ins = cliente()

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        #self.wd_CBox1 = wd_CBox(self, tit_CBox='Tipo:', set_CBox_default='Escolha a opção', width=21, CBox_values=["Pessoa Física", "Pessoa Jurídica"], CBox_state='readonly')
        #self.wd_CBox1.grid(row=0, column=0, padx=5)
        #self.wd_CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())

        self.label = ttk.Label(self, text = 'Inserir cliente', font = 'VERDANA')
        self.label.grid(row = 0, column = 0, sticky = 'WN', pady = 7)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=3, column=0, sticky='we')

        self.cancel_button = ttk.Button(self.frame_buttons, text='Fechar', command=lambda: self.callback())
        self.cancel_button.grid(row=0, column=0, sticky='we', padx = 10)
        self.save_button = ttk.Button(self.frame_buttons, text = 'Salvar cadastro', command=lambda: self.salva_cliente())
        self.save_button.grid(row = 0, column = 1, sticky = 'we', padx = 10)

        self.__build_ins_PF__()
        self.__build_ins_ender__()

    def __build_ins_PF__(self):
        self.frame_PF = LabelFrame(self, text = 'Dados gerais')#, relief = FLAT)
        self.frame_PF.grid(row = 1, column = 0, sticky = W, ipadx = 10, ipady = 10, padx = 10)

        self.nome_entr = wd_Entry(self.frame_PF, width=47, tit_Entry='Nome completo:')
        self.nome_entr.grid_frame(row=0, column=0, padx=5, columnspan=3)#, sticky=W+E)

        self.cpf_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='CPF:')
        self.cpf_entr.grid_frame(row=0, column=2, padx=5)#, sticky=W+E)

        self.tel1_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='Telefone Fixo:')
        self.tel1_entr.grid_frame(row=1, column=0, padx=5, sticky=W + E)

        self.cel1_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='Telefone Celular:')
        self.cel1_entr.grid_frame(row=1, column=1, padx=5, sticky=W + E)

        self.email1_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='E-mail:')
        self.email1_entr.grid_frame(row=1, column=2, padx=5, sticky=W + E)

        self.gen_CBox = wd_CBox(self.frame_PF, tit_CBox='Gênero:', set_CBox_default='Não declarado', width=21, CBox_values=["Feminino", "Masculino", "Não declarado"], CBox_state='readonly')
        self.gen_CBox.grid(row=2, column=0, padx=5)

        self.nasc_dat_wd = wd_DateCbox(self.frame_PF, text ='Data de nascimento')
        self.nasc_dat_wd.grid(row=2, column=1, columnspan=3, sticky=W+E)

        self.__build_ins_ender__()

    def __build_ins_ender__(self):
        self.frame_ender = EnderFrame(self, self.controller)
        self.frame_ender.grid(row=2, column=0, sticky = W)

    def salva_cliente(self):
        self.cliente_ins.ender = self.frame_ender.get_ender()

        self.contat_cliente.tel1 = self.tel1_entr.get_text()
        self.contat_cliente.cel1 = self.cel1_entr.get_text()
        self.contat_cliente.email1 = self.email1_entr.get_text()
        self.cliente_ins.contato = self.contat_cliente

        self.cliente_ins.dataNasc = self.nasc_dat_wd.get_date()
        self.cliente_ins.nome = self.nome_entr.get_text()
        self.cliente_ins.cpf = self.cpf_entr.get_text()
        self.cliente_ins.genero = self.gen_CBox.get_choice()
        self.cliente_ins.id_ger = self.ger_atv.idd

        self.controller.insert_model(self.cliente_ins)

    def callback(self):
        self.frame_master.update_frame()
        self.destroy()


class InsFornecFrame(Toplevel):
    def __init__(self, frame_master, app_controller):
        super().__init__(padx=15, pady=15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frame_master = frame_master
        self.controller = app_controller
        self.ger_atv = self.controller.ger_atv

        self.ender_fornec = enderecoIdent()
        self.contat_fornec = contato()
        self.fornec_ins = fornec()

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        # self.wd_CBox1 = wd_CBox(self, tit_CBox='Tipo:', set_CBox_default='Escolha a opção', width=21, CBox_values=["Pessoa Física", "Pessoa Jurídica"], CBox_state='readonly')
        # self.wd_CBox1.grid(row=0, column=0, padx=5)
        # self.wd_CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())

        self.label = ttk.Label(self, text='Inserir Fornecedor', font='VERDANA')
        self.label.grid(row=0, column=0, sticky='WN', pady=7)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=3, column=0, sticky='we')

        self.cancel_button = ttk.Button(self.frame_buttons, text='Fechar', command=lambda: self.callback())
        self.cancel_button.grid(row=0, column=0, sticky='we', padx=10)
        self.save_button = ttk.Button(self.frame_buttons, text='Salvar cadastro', command=lambda: self.salva_fornec())
        self.save_button.grid(row=0, column=1, sticky='we', padx=10)

        self.__build_ins_PJ__()
        self.__build_ins_ender__()

    def __build_ins_PJ__(self):
        self.frame_PJ = LabelFrame(self, text='Dados gerais')  # , relief = FLAT)
        self.frame_PJ.grid(row=1, column=0, sticky=W, ipadx=10, ipady=10, padx=10)

        self.nome_entr = wd_Entry(self.frame_PJ, width=47, tit_Entry='Nome Fantasia:')
        self.nome_entr.grid_frame(row=0, column=0, padx=5, columnspan=3)  # , sticky=W+E)

        self.cnpj_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='CNPJ:')
        self.cnpj_entr.grid_frame(row=0, column=2, padx=5)  # , sticky=W+E)

        self.ramo_CBox = wd_CBox(self.frame_PJ, tit_CBox='Ramo:', set_CBox_default='Não especificado', width=21,
                                 CBox_values=["Alimentício", "Cosmético", "Outros"], CBox_state='readonly')
        self.ramo_CBox.grid(row=1, column=0, padx=5)

        self.razSoc_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='Razão Social:')
        self.razSoc_entr.grid_frame(row=1, column=1, padx=5, sticky=W + E)

        self.tel1_entr = wd_Entry(self.frame_PJ, width=24, label='Telefone Fixo:')
        self.tel1_entr.grid_frame(row=2, column=0, padx=5, sticky=W + E)

        self.cel1_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='Telefone Celular:')
        self.cel1_entr.grid_frame(row=2, column=1, padx=5, sticky=W + E)

        self.email1_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='E-mail:')
        self.email1_entr.grid_frame(row=2, column=2, padx=5, sticky=W + E)

    def __build_ins_ender__(self):
        self.ender_frame = EnderFrame(self, self.controller)
        self.ender_frame.grid(row=2, column=0, sticky=W)

    def salva_fornec(self):
        self.contat_fornec.tel1 = self.tel1_entr.get_text()
        self.contat_fornec.cel1 = self.cel1_entr.get_text()
        self.contat_fornec.email1 = self.email1_entr.get_text()


        self.fornec_ins.contato = self.contat_fornec
        self.fornec_ins.ender = self.ender_frame.get_ender()
        self.fornec_ins.nome = self.nome_entr.get_text()
        self.fornec_ins.cnpj = self.cnpj_entr.get_text()
        self.fornec_ins.ramo = self.ramo_CBox.get_choice()
        self.fornec_ins.raz_soc = self.razSoc_entr.get_text()
        self.fornec_ins.id_ger = self.ger_atv.idd

        self.controller.insert_model(self.fornec_ins)

    def callback(self):
        self.frame_master.update_frame()
        self.destroy()


class InsEstabFrame(Toplevel):
    def __init__(self, frame_master, app_controller):
        super().__init__(padx=15, pady=15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frame_master = frame_master
        self.controller = app_controller
        self.ger_atv = self.controller.ger_atv
        self.lst_categs = self.controller.loadAll_model(CategEstab())

        self.ender_estab = enderecoIdent()
        self.contat_estab = contato()
        self.estab_ins = Estab()


        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        # self.wd_CBox1 = wd_CBox(self, tit_CBox='Tipo:', set_CBox_default='Escolha a opção', width=21, CBox_values=["Pessoa Física", "Pessoa Jurídica"], CBox_state='readonly')
        # self.wd_CBox1.grid(row=0, column=0, padx=5)
        # self.wd_CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())

        self.label = ttk.Label(self, text='Inserir Estabelecimento/Identificações', font='VERDANA')
        self.label.grid(row=0, column=0, sticky='WN', pady=7)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=3, column=0, sticky='we')

        self.cancel_button = ttk.Button(self.frame_buttons, text='Fechar', command=lambda: self.callback())
        self.cancel_button.grid(row=0, column=0, sticky='we', padx=10)
        self.save_button = ttk.Button(self.frame_buttons, text='Salvar cadastro', command=lambda: self.salva_estab())
        self.save_button.grid(row=0, column=1, sticky='we', padx=10)

        self.__build_ins_Estab__()
        self.__build_ins_ender__()

    def __build_ins_Estab__(self):
        self.frame_dadosEstab = LabelFrame(self, text='Dados gerais')  # , relief = FLAT)
        self.frame_dadosEstab.grid(row=1, column=0, sticky=W, ipadx=10, ipady=10, padx=10)

        self.nome_entr = wd_Entry(self.frame_dadosEstab, width=47, label='Nome:')
        self.nome_entr.grid_frame(row=0, column=0, padx=5, columnspan=3)  # , sticky=W+E)

        self.ramo_CBox = wd_CBox(self.frame_dadosEstab, tit_CBox='Ramo:', set_CBox_default='Não especificado', width=21,
                                 CBox_values=self.lst_categs.to_comboBox(), CBox_state='readonly')
        self.ramo_CBox.grid(row=0, column=2, padx=5)


        self.tel1_entr = wd_Entry(self.frame_dadosEstab, width=24, label='Telefone Fixo:')
        self.tel1_entr.grid_frame(row=1, column=0, padx=5, sticky=W + E)

        self.cel1_entr = wd_Entry(self.frame_dadosEstab, width=24, label='Telefone Celular:')
        self.cel1_entr.grid_frame(row=1, column=1, padx=5, sticky=W + E)

        self.email1_entr = wd_Entry(self.frame_dadosEstab, width=24, label='E-mail:')
        self.email1_entr.grid_frame(row=1, column=2, padx=5, sticky=W + E)

        self.descr_text = wd_Text(self.frame_dadosEstab, label='Descrição')
        self.descr_text.grid_frame(row = 2, column = 0, columnspan = 6)

    def __build_ins_ender__(self):
        self.ender_frame = EnderFrame(self, self.controller)
        self.ender_frame.grid(row=2, column=0, sticky=W)

    def salva_estab(self):
        self.contat_estab.tel1 = self.tel1_entr.get_text()
        self.contat_estab.cel1 = self.cel1_entr.get_text()
        self.contat_estab.email1 = self.email1_entr.get_text()

        self.estab_ins.contato = self.contat_estab
        # Endereço é obtido pelo enderFrame:
        self.estab_ins.ender = self.ender_frame.get_ender()
        self.estab_ins.nome = self.nome_entr.get_text()
        self.estab_ins.descr = self.descr_text.get_text()
        self.estab_ins.categ = self.lst_categs.search_name(self.ramo_CBox.get_choice())
        print(self.lst_categs.search_name(self.ramo_CBox.get_choice()))
        self.estab_ins.id_ger = self.ger_atv.idd
        # Controller insere o modelo:
        self.controller.insert_model(self.estab_ins)

    def callback(self):
        self.frame_master.update_frame()
        self.destroy()


class PerfilFornecFrame(Toplevel):
    def __init__(self, frame_master, controller, fornec_perfil:fornec):
        super().__init__(padx = 15, pady = 15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frame_master = frame_master
        self.controller = controller
        self.ger_atv = controller.ger_atv

        self.ender_fornec = fornec_perfil.ender
        self.contat_fornec = fornec_perfil.contato
        self.fornec_perfil = fornec_perfil

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        self.label = ttk.Label(self, text = 'Perfil do Cliente', font = 'VERDANA')
        self.label.grid(row = 0, column = 0, sticky = 'WN', pady = 7)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=0, column=1, sticky='we')

        self.cancel_button = ttk.Button(self.frame_buttons, text='Fechar', command=lambda: self.callback())
        self.cancel_button.grid(row=0, column=0, sticky='we', padx = 10)
        self.alter_button = ttk.Button(self.frame_buttons, text ='Alterar Cadastro', command=lambda: self.altera_fornec())
        self.alter_button.grid(row = 0, column = 1, sticky ='we', padx = 10)
        self.save_button = ttk.Button(self.frame_buttons, text ='Salvar alterações', command=lambda: self.update_fornec())
        #self.save_button.grid(row=0, column=2, sticky='we', padx=10)

        self.__build_perfil_PJ__()
        self.__build_perfil_ender__()

    def __build_perfil_PJ__(self):
        self.frame_PJ = LabelFrame(self, text ='Dados gerais')#, relief = FLAT)
        self.frame_PJ.grid(row = 1, column = 0, sticky = W, ipadx = 10, ipady = 10, padx = 10, columnspan = 4)

        self.nome_entr = wd_Entry(self.frame_PJ, width=47, tit_Entry='Nome completo:', set_Entry_default=self.fornec_perfil.nome, state_Entry='readonly')
        self.nome_entr.grid_frame(row=0, column=0, padx=5, columnspan=3)#, sticky=W+E)

        self.cnpj_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='CNPJ:', set_Entry_default=self.fornec_perfil.cnpj, state_Entry='readonly')
        self.cnpj_entr.grid_frame(row=0, column=2, padx=5)#, sticky=W+E)

        self.ramo_CBox = wd_CBox(self.frame_PJ, tit_CBox='Ramo:', values = ['Alimentício', 'Cosmético', 'Outros'], set_CBox_default=self.fornec_perfil.ramo, width=21, CBox_state='disabled')
        self.ramo_CBox.grid(row=1, column=0, padx=5)

        self.razSoc_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='Razão Social:', set_Entry_default=self.fornec_perfil.raz_soc, state_Entry='readonly')
        self.razSoc_entr.grid_frame(row=1, column=1, padx=5, sticky=W + E)

        self.tel1_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='Telefone Fixo:', set_Entry_default=self.fornec_perfil.tel1, state_Entry='readonly')
        self.tel1_entr.grid_frame(row=2, column=0, padx=5, sticky=W + E)

        self.cel1_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='Telefone Celular:', set_Entry_default=self.fornec_perfil.cel1, state_Entry='readonly')
        self.cel1_entr.grid_frame(row=2, column=1, padx=5, sticky=W + E)

        self.email1_entr = wd_Entry(self.frame_PJ, width=24, tit_Entry='E-mail:', set_Entry_default=self.fornec_perfil.email1, state_Entry='readonly')
        self.email1_entr.grid_frame(row=2, column=2, padx=5, sticky=W + E)

    def __build_perfil_ender__(self):
        self.frame_ender = LabelFrame(self, text = 'Endereço')#, relief = FLAT)
        self.frame_ender.grid(row=2, column=0, sticky = W, ipadx = 10, ipady = 10, padx = 10, pady = 10, columnspan = 4)

        #lst_estados = self.controller.load_UF()
        self.estado_CBox = wd_CBox(self.frame_ender, tit_CBox='Estado', width=21, set_CBox_default= self.fornec_perfil.estado, CBox_state='disabled')
        #self.estado_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_estado_CBox())
        self.estado_CBox.grid(row=0, column=0, padx=5, sticky=W+E, columnspan=2)

        self.cidade_CBox = wd_CBox(self.frame_ender, tit_CBox='Cidade:', set_CBox_default=self.fornec_perfil.cidade, CBox_state='disabled', width=21)
        #self.cidade_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_cidade_CBox())
        self.cidade_CBox.grid(row=0, column=2, padx=5, sticky=W+E)

        self.bairro_CBox = wd_CBox(self.frame_ender, tit_CBox='Bairro:', set_CBox_default=self.fornec_perfil.bairro, width=21, CBox_state='disabled')
        #self.bairro_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_bairro_CBox())
        self.bairro_CBox.grid(row=0, column=3, padx=5, sticky=W, columnspan=2)

        self.cep_entr = wd_Entry(self.frame_ender, width=10, tit_Entry='CEP:', set_Entry_default= self.fornec_perfil.cep, state_Entry='readonly')
        self.cep_entr.grid_frame(row=1, column=0, padx=5, sticky=W+E)

        self.buscaCep_button = ttk.Button(self.frame_ender, text = 'Buscar CEP', command = self.buscaCep, state = 'disabled')
        self.buscaCep_button.grid(row=1, column=1, padx=5, sticky=W+E+S)

        self.lograd_entr = wd_Entry(self.frame_ender, width=24, tit_Entry='Logradouro:', set_Entry_default= self.fornec_perfil.logradouro, state_Entry='readonly')
        self.lograd_entr.grid_frame(row=1, column=2, padx=5, sticky=W, columnspan=2)

        self.numero_entr = wd_Entry(self.frame_ender, width=7, tit_Entry='Número:', set_Entry_default= self.fornec_perfil.numero, state_Entry='readonly')
        self.numero_entr.grid_frame(row=1, column=3, padx=5, sticky=W+E)

        self.numApart_entr = wd_Entry(self.frame_ender, width=7, tit_Entry='Nº apart/sala:', set_Entry_default= self.fornec_perfil.num_apart, state_Entry='readonly')
        self.numApart_entr.grid_frame(row=1, column=4, padx=5)

        self.bloco_entr = wd_Entry(self.frame_ender, width=7, tit_Entry='Bloco (Se houver):', set_Entry_default= self.fornec_perfil.bloco, state_Entry='readonly')
        self.bloco_entr.grid_frame(row=1, column=5, padx=5)

        self.tipoRes_CBox = wd_CBox(self.frame_ender, tit_CBox='Tipo:', set_CBox_default=self.fornec_perfil.tipo_resid, width=21, CBox_state='disabled')
        self.tipoRes_CBox.grid(row=2, column=0, padx=5, sticky=W+E, columnspan=2)
        self.tipoRes_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_tipoRes_CBox())

        self.nomeCond_entr = wd_Entry(self.frame_ender, width=24, tit_Entry='Nome do edifício/condomínio:', set_Entry_default= self.fornec_perfil.edificio, state_Entry='readonly')
        self.nomeCond_entr.grid_frame(row=2, column=2, padx=5)

        self.refe_entr = wd_Entry(self.frame_ender, width=24, tit_Entry='Complemento/Referência:', set_Entry_default= self.fornec_perfil.referencia, state_Entry='readonly')
        self.refe_entr.grid_frame(row=2, column=3, padx=5, columnspan= 2)

    def __build_alter_dados__(self):
        self.razSoc_entr.entry.config(state ='enabled')

        self.nome_entr.entry.config(state='enabled')

        self.cnpj_entr.entry.config(state='enabled')

        self.tel1_entr.entry.config(state ='enabled')

        self.cel1_entr.entry.config(state ='enabled')

        self.email1_entr.entry.config(state ='enabled')

        self.ramo_CBox.CBox.config(state ='readonly', values = ['Alimentício', 'Cosmético', 'Outros'])

    def __build_alter_ender__(self):
        lst_estados = self.controller.load_UF()
        self.estado_CBox.CBox.config(state = 'enabled', values = lst_estados)
        self.estado_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_estado_CBox())

        self.cidade_CBox.CBox.config(state='enabled')
        self.cidade_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_cidade_CBox())

        self.bairro_CBox.CBox.config(state='enabled')
        self.bairro_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_bairro_CBox())

        self.cep_entr.entry.config(state ='enabled')

        self.buscaCep_button.config(state = 'enabled')

        self.lograd_entr.entry.config(state ='enabled')

        self.numero_entr.entry.config(state ='enabled')

        self.numApart_entr.entry.config(state ='enabled')

        self.bloco_entr.entry.config(state ='enabled')

        self.tipoRes_CBox.CBox.config(values = ["Casa", "Apartamento", "Sala"], state = 'readonly')

        self.nomeCond_entr.entry.config(state ='enabled')

        self.refe_entr.entry.config(state ='enabled')
        self.bind_tipoRes_CBox()

    def altera_fornec(self):
        self.__build_alter_dados__()
        self.__build_alter_ender__()
        self.save_button.grid(row=0, column=2, sticky='we', padx=10)
        self.cancel_button.config(text = 'Cancelar')

    def update_fornec(self):
        self.contat_fornec.tel1 = self.tel1_entr.get_text()
        self.contat_fornec.cel1 = self.cel1_entr.get_text()
        self.contat_fornec.email1 = self.email1_entr.get_text()

        self.ender_fornec.cep = self.cep_entr.get_text()
        self.ender_fornec.estado = self.estado_CBox.get_choice()
        self.ender_fornec.cidade = self.cidade_CBox.get_choice()
        self.ender_fornec.bairro = self.bairro_CBox.get_choice()
        self.ender_fornec.logradouro = self.lograd_entr.get_text()
        self.ender_fornec.numero = self.numero_entr.get_text()
        self.ender_fornec.num_apart = self.numApart_entr.get_text()
        self.ender_fornec.bloco = self.bloco_entr.get_text()
        self.ender_fornec.tipo_resid = self.tipoRes_CBox.get_choice()
        self.ender_fornec.edificio = self.nomeCond_entr.get_text()
        self.ender_fornec.referencia = self.refe_entr.get_text()

        self.fornec_perfil.contato = self.contat_fornec
        self.fornec_perfil.ender = self.ender_fornec

        self.fornec_perfil.raz_soc = self.razSoc_entr.get_text()
        self.fornec_perfil.nome = self.nome_entr.get_text()
        self.fornec_perfil.cpf = self.cnpj_entr.get_text()
        self.fornec_perfil.ramo = self.ramo_CBox.get_choice()

        self.controller.update_model(self.fornec_perfil)

    def buscaCep(self):
        cep = self.cep_entr.get_text()
        ender = self.controller.search_CEP(cep)
        if ender is not None:
            self.lograd_entr.insert_text(ender.tipo_logra + ' ' + ender.logradouro)
            self.bairro_CBox.set_CBox_default(ender.bairro)
            self.bairro_CBox.CBox.config(values=[], state = 'readonly')
            self.estado_CBox.set_CBox_default(ender.estado)
            self.cidade_CBox.set_CBox_default(ender.cidade)
            self.cidade_CBox.CBox.config(values=[], state='readonly')
        else:
            self.cep_entr.insert_text('CEP não encontrado')

    def bind_tipoRes_CBox(self):
        tipo_res = self.tipoRes_CBox.get_choice()
        if tipo_res == 'Sala' or tipo_res == 'Apartamento':
            self.nomeCond_entr.entry.config(state ='enabled')
            self.bloco_entr.entry.config(state='enabled')
            self.numApart_entr.entry.config(state='enabled')
        else:
            self.nomeCond_entr.limpa_entr()
            self.nomeCond_entr.entry.config(state='disabled')
            self.bloco_entr.limpa_entr()
            self.bloco_entr.entry.config(state='disabled')
            self.numApart_entr.limpa_entr()
            self.numApart_entr.entry.config(state='disabled')

    def bind_bairro_CBox(self):
        self.ender_fornec.bairro = self.bairro_CBox.get_choice()

    def bind_cidade_CBox(self):
        self.ender_fornec.cidade = self.cidade_CBox.get_choice()
        lst_bairros = self.controller.load_BAIRROS(self.cidade_CBox.get_choice())
        self.bairro_CBox.config_CBox_state('readonly')
        self.bairro_CBox.define_values_CBox(lst_bairros)

    def bind_estado_CBox(self):
        self.ender_fornec.estado = self.estado_CBox.get_choice()
        lst_cidades = self.controller.load_CIDADES(self.estado_CBox.get_choice())
        self.cidade_CBox.config_CBox_state('readonly')
        self.cidade_CBox.define_values_CBox(lst_cidades)

    def callback(self):
        self.frame_master.update_frame()
        self.destroy()


class PerfilEstabFrame(Toplevel):
    def __init__(self, frame_master, controller, estab_perfil:Estab):
        super().__init__(padx = 15, pady = 15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frame_master = frame_master
        self.controller = controller
        self.ger_atv = controller.ger_atv

        self.lst_categs = self.controller.loadAll_model(CategEstab())

        self.ender_estab = estab_perfil.ender
        self.contat_estab = estab_perfil.contato
        self.estab_perfil = estab_perfil

        self.build_Frame()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def build_Frame(self):
        self.label = ttk.Label(self, text = 'Perfil do Cliente', font = 'VERDANA')
        self.label.grid(row = 0, column = 0, sticky = 'WN', pady = 7)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=0, column=0, sticky='we')

        self.cancel_button = ttk.Button(self.frame_buttons, text='Fechar', command=lambda: self.callback())
        self.cancel_button.grid(row=0, column=0, sticky='we', padx = 10)
        self.alter_button = ttk.Button(self.frame_buttons, text ='Alterar Cadastro', command=lambda: self.altera_fornec())
        self.alter_button.grid(row = 0, column = 1, sticky ='we', padx = 10)
        self.save_button = ttk.Button(self.frame_buttons, text ='Salvar alterações', command=lambda: self.update_fornec())
        #self.save_button.grid(row=0, column=2, sticky='we', padx=10)

        self.build_frameDados()
        self.build_frameEnder()

    def build_frameDados(self):
        self.frame_dadosEstab = LabelFrame(self, text='Dados gerais')  # , relief = FLAT)
        self.frame_dadosEstab.grid(row=1, column=0, sticky=W, ipadx=10, ipady=10, padx=10)

        self.nome_entr = wd_Entry(self.frame_dadosEstab, width=47, label='Nome:', state='readonly')
        self.nome_entr.insert_text(self.estab_perfil.nome)
        self.nome_entr.grid_frame(row=0, column=0, padx=5, columnspan=3)  # , sticky=W+E)

        self.ramo_CBox = wd_CBox(self.frame_dadosEstab, tit_CBox='Ramo\Categoria:', set_CBox_default=self.estab_perfil.categ.nome, width=21,
                                 CBox_values=self.lst_categs.to_comboBox(), CBox_state='disabled')
        self.ramo_CBox.grid(row=0, column=2, padx=5)

        self.tel1_entr = wd_Entry(self.frame_dadosEstab, width=24, label='Telefone Fixo:', state='readonly')
        self.tel1_entr.insert_text(self.estab_perfil.tel1)
        self.tel1_entr.grid_frame(row=1, column=0, padx=5, sticky=W + E)

        self.cel1_entr = wd_Entry(self.frame_dadosEstab, width=24, label='Telefone Celular:', state='readonly')
        self.cel1_entr.insert_text(self.estab_perfil.cel1)
        self.cel1_entr.grid_frame(row=1, column=1, padx=5, sticky=W + E)

        self.email1_entr = wd_Entry(self.frame_dadosEstab, width=24, label='E-mail:', state='readonly')
        self.email1_entr.insert_text(self.estab_perfil.email1)
        self.email1_entr.grid_frame(row=1, column=2, padx=5, sticky=W + E)

        self.descr_text = wd_Text(self.frame_dadosEstab, label='Descrição', state=DISABLED)
        self.descr_text.insert_text(self.estab_perfil.descr)
        self.descr_text.grid_frame(row = 2, column = 0, columnspan = 6)

    def build_frameEnder(self):
        self.ender_frame = EnderFrame(self, self.controller, self.estab_perfil.ender)
        self.ender_frame.wd_config(state='readonly')
        self.ender_frame.grid(row=2, column=0, sticky=W, ipadx=10, padx=10)

    def build_alterDados(self):
        self.nome_entr.entry.config(state='enabled')

        self.tel1_entr.entry.config(state ='enabled')

        self.cel1_entr.entry.config(state ='enabled')

        self.email1_entr.entry.config(state ='enabled')

        self.ramo_CBox.CBox.config(state ='readonly', values = self.lst_categs.to_comboBox())

        self.descr_text.text.config(state=NORMAL)

    def build_alterEnder(self):
        self.ender_frame.wd_config(state='enabled')


    def altera_fornec(self):
        self.build_alterDados()
        self.build_alterEnder()
        self.save_button.grid(row=0, column=2, sticky='we', padx=10)
        self.cancel_button.config(text = 'Cancelar')
        self.alter_button.grid_forget()

    def update_fornec(self):
        self.estab_perfil.ender = self.ender_frame.get_ender()

        self.contat_estab.tel1 = self.tel1_entr.get_text()
        self.contat_estab.cel1 = self.cel1_entr.get_text()
        self.contat_estab.email1 = self.email1_entr.get_text()
        self.estab_perfil.contato = self.contat_estab


        self.estab_perfil.nome = self.nome_entr.get_text()
        self.estab_perfil.categ = self.lst_categs.search_name(self.ramo_CBox.get_choice())
        self.estab_perfil.descr = self.descr_text.get_text()

        self.controller.update_model(self.estab_perfil)
        self.build_Frame()




    def callback(self):
        self.frame_master.update_frame()
        self.destroy()


class PerfilClienteFrame(Toplevel):
    def __init__(self, frame_master, controller, cliente_perfil:cliente):
        super().__init__(padx = 15, pady = 15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frame_master = frame_master
        self.controller = controller
        self.ger_atv = controller.ger_atv

        self.ender_cliente = cliente_perfil.ender
        self.contat_cliente = cliente_perfil.contato
        self.cliente_perfil = cliente_perfil

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        self.label = ttk.Label(self, text = 'Perfil do Cliente', font = 'VERDANA')
        self.label.grid(row = 0, column = 0, sticky = 'WN', pady = 7)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=0, column=1, sticky='we')

        self.cancel_button = ttk.Button(self.frame_buttons, text='Fechar', command=lambda: self.callback())
        self.cancel_button.grid(row=0, column=0, sticky='we', padx = 10)
        self.alter_button = ttk.Button(self.frame_buttons, text ='Alterar Cadastro', command=lambda: self.altera_cliente())
        self.alter_button.grid(row = 0, column = 1, sticky ='we', padx = 10)
        self.save_button = ttk.Button(self.frame_buttons, text ='Salvar alterações', command=lambda: self.update_cliente())
        #self.save_button.grid(row=0, column=2, sticky='we', padx=10)

        self.__build_perfil_PF__()
        self.__build_perfil_ender__()

    def __build_perfil_PF__(self):
        self.frame_PF = LabelFrame(self, text ='Dados gerais')#, relief = FLAT)
        self.frame_PF.grid(row = 1, column = 0, sticky = W, ipadx = 10, ipady = 10, padx = 10, columnspan = 4)

        self.nome_entr = wd_Entry(self.frame_PF, width=47, tit_Entry='Nome completo:', set_Entry_default=self.cliente_perfil.nome, state_Entry='readonly')
        self.nome_entr.grid_frame(row=0, column=0, padx=5, columnspan=3)#, sticky=W+E)

        self.cpf_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='CPF:', set_Entry_default=self.cliente_perfil.cpf, state_Entry='readonly')
        self.cpf_entr.grid_frame(row=0, column=2, padx=5)#, sticky=W+E)

        self.gen_CBox = wd_CBox(self.frame_PF, tit_CBox='Gênero:', set_CBox_default=self.cliente_perfil.genero, width=21, CBox_values=["Feminino", "Masculino", "Não declarado"], CBox_state='disabled')
        self.gen_CBox.grid(row=2, column=0, padx=5)


        self.tel1_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='Telefone Fixo:', set_Entry_default=self.cliente_perfil.tel1, state_Entry='readonly')
        self.tel1_entr.grid_frame(row=1, column=0, padx=5, sticky=W+E)

        self.cel1_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='Telefone Celular:', set_Entry_default=self.cliente_perfil.cel1, state_Entry='readonly')
        self.cel1_entr.grid_frame(row=1, column=1, padx=5, sticky=W + E)

        self.email1_entr = wd_Entry(self.frame_PF, width=24, tit_Entry='E-mail:', set_Entry_default=self.cliente_perfil.email1, state_Entry='readonly')
        self.email1_entr.grid_frame(row=1, column=2, padx=5, sticky=W+E)

        self.nasc_dat_wd = wd_DateCbox(self.frame_PF, text ='Data de nascimento', choice=False, date=self.cliente_perfil.dataNasc)
        self.nasc_dat_wd.grid(row=2, column=1, columnspan=3, sticky=W+E)

    def __build_perfil_ender__(self):
        self.frame_ender = LabelFrame(self, text = 'Endereço')#, relief = FLAT)
        self.frame_ender.grid(row=2, column=0, sticky = W, ipadx = 10, ipady = 10, padx = 10, pady = 10, columnspan = 4)

        #lst_estados = self.controller.load_UF()
        self.estado_CBox = wd_CBox(self.frame_ender, tit_CBox='Estado', width=21, set_CBox_default= self.cliente_perfil.estado, CBox_state='disabled')
        #self.estado_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_estado_CBox())
        self.estado_CBox.grid(row=0, column=0, padx=5, sticky=W+E, columnspan=2)

        self.cidade_CBox = wd_CBox(self.frame_ender, tit_CBox='Cidade:', set_CBox_default=self.cliente_perfil.cidade, CBox_state='disabled', width=21)
        #self.cidade_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_cidade_CBox())
        self.cidade_CBox.grid(row=0, column=2, padx=5, sticky=W+E)

        self.bairro_CBox = wd_CBox(self.frame_ender, tit_CBox='Bairro:', set_CBox_default=self.cliente_perfil.bairro, width=21, CBox_state='disabled')
        #self.bairro_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_bairro_CBox())
        self.bairro_CBox.grid(row=0, column=3, padx=5, sticky=W, columnspan=2)

        self.cep_entr = wd_Entry(self.frame_ender, width=10, tit_Entry='CEP:', set_Entry_default= self.cliente_perfil.cep, state_Entry='readonly')
        self.cep_entr.grid_frame(row=1, column=0, padx=5, sticky=W+E)

        self.buscaCep_button = ttk.Button(self.frame_ender, text = 'Buscar CEP', command = self.buscaCep, state = 'disabled')
        self.buscaCep_button.grid(row=1, column=1, padx=5, sticky=W+E+S)

        self.lograd_entr = wd_Entry(self.frame_ender, width=24, tit_Entry='Logradouro:', set_Entry_default= self.cliente_perfil.logradouro, state_Entry='readonly')
        self.lograd_entr.grid_frame(row=1, column=2, padx=5, sticky=W, columnspan=2)

        self.numero_entr = wd_Entry(self.frame_ender, width=7, tit_Entry='Número:', set_Entry_default= self.cliente_perfil.numero, state_Entry='readonly')
        self.numero_entr.grid_frame(row=1, column=3, padx=5, sticky=W+E)

        self.numApart_entr = wd_Entry(self.frame_ender, width=7, tit_Entry='Nº apart/sala:', set_Entry_default= self.cliente_perfil.num_apart, state_Entry='readonly')
        self.numApart_entr.grid_frame(row=1, column=4, padx=5)

        self.bloco_entr = wd_Entry(self.frame_ender, width=7, tit_Entry='Bloco (Se houver):', set_Entry_default= self.cliente_perfil.bloco, state_Entry='readonly')
        self.bloco_entr.grid_frame(row=1, column=5, padx=5)

        self.tipoRes_CBox = wd_CBox(self.frame_ender, tit_CBox='Tipo:', set_CBox_default=self.cliente_perfil.tipo_resid, width=21, CBox_state='disabled')
        self.tipoRes_CBox.grid(row=2, column=0, padx=5, sticky=W+E, columnspan=2)
        self.tipoRes_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_tipoRes_CBox())

        self.nomeCond_entr = wd_Entry(self.frame_ender, width=24, tit_Entry='Nome do edifício/condomínio:', set_Entry_default= self.cliente_perfil.edificio, state_Entry='readonly')
        self.nomeCond_entr.grid_frame(row=2, column=2, padx=5)

        self.refe_entr = wd_Entry(self.frame_ender, width=24, tit_Entry='Complemento/Referência:', set_Entry_default= self.cliente_perfil.referencia, state_Entry='readonly')
        self.refe_entr.grid_frame(row=2, column=3, padx=5, columnspan= 2)

    def altera_cliente(self):
        self.__build_alter_dados__()
        self.__build_alter_ender__()
        self.save_button.grid(row=0, column=2, sticky='we', padx=10)

    def update_cliente(self):
        self.contat_cliente.tel1 = self.tel1_entr.get_text()
        self.contat_cliente.cel1 = self.cel1_entr.get_text()
        self.contat_cliente.email1 = self.email1_entr.get_text()

        self.ender_cliente.cep = self.cep_entr.get_text()
        self.ender_cliente.estado = self.estado_CBox.get_choice()
        self.ender_cliente.cidade = self.cidade_CBox.get_choice()
        self.ender_cliente.bairro = self.bairro_CBox.get_choice()
        self.ender_cliente.logradouro = self.lograd_entr.get_text()
        self.ender_cliente.numero = self.numero_entr.get_text()
        self.ender_cliente.num_apart = self.numApart_entr.get_text()
        self.ender_cliente.bloco = self.bloco_entr.get_text()
        self.ender_cliente.tipo_resid = self.tipoRes_CBox.get_choice()
        self.ender_cliente.edificio = self.nomeCond_entr.get_text()
        self.ender_cliente.referencia = self.refe_entr.get_text()

        self.cliente_perfil.dataNasc = self.nasc_dat_wd.get_date()
        self.cliente_perfil.contato = self.contat_cliente
        self.cliente_perfil.ender = self.ender_cliente
        self.cliente_perfil.nome = self.nome_entr.get_text()
        self.cliente_perfil.cpf = self.cpf_entr.get_text()
        self.cliente_perfil.genero = self.gen_CBox.get_choice()

        self.controller.update_model(self.cliente_perfil)

    def buscaCep(self):
        cep = self.cep_entr.get_text()
        ender = self.controller.search_CEP(cep)
        if ender is not None:
            self.lograd_entr.insert_text(ender.tipo_logra + ' ' + ender.logradouro)
            self.bairro_CBox.set_CBox_default(ender.bairro)
            self.bairro_CBox.CBox.config(values=[], state = 'readonly')
            self.estado_CBox.set_CBox_default(ender.estado)
            self.cidade_CBox.set_CBox_default(ender.cidade)
            self.cidade_CBox.CBox.config(values=[], state='readonly')
        else:
            self.cep_entr.insert_text('CEP não encontrado')

    def __build_alter_dados__(self):

        self.nome_entr.entry.config(state='enabled')

        self.cpf_entr.entry.config(state='enabled')

        self.tel1_entr.entry.config(state ='enabled')

        self.cel1_entr.entry.config(state ='enabled')

        self.email1_entr.entry.config(state ='enabled')

        self.gen_CBox.CBox.config(state = 'readonly', values = ['Masculino', 'Feminino', 'Não especificado'])

        self.nasc_dat_wd.config_wd(choice=True)

    def __build_alter_ender__(self):

        lst_estados = self.controller.load_UF()
        self.estado_CBox.CBox.config(state = 'enabled', values = lst_estados)
        self.estado_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_estado_CBox())


        self.cidade_CBox.CBox.config(state='enabled')
        self.cidade_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_cidade_CBox())

        self.bairro_CBox.CBox.config(state='enabled')
        self.bairro_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_bairro_CBox())


        self.cep_entr.entry.config(state ='enabled')

        self.buscaCep_button.config(state = 'enabled')

        self.lograd_entr.entry.config(state ='enabled')

        self.numero_entr.entry.config(state ='enabled')

        self.numApart_entr.entry.config(state ='enabled')

        self.bloco_entr.entry.config(state ='enabled')

        self.tipoRes_CBox.CBox.config(values = ["Casa", "Apartamento", "Sala"], state = 'readonly')

        self.nomeCond_entr.entry.config(state ='enabled')

        self.refe_entr.entry.config(state ='enabled')
        self.bind_tipoRes_CBox()

    def bind_tipoRes_CBox(self):
        tipo_res = self.tipoRes_CBox.get_choice()
        if tipo_res == 'Sala' or tipo_res == 'Apartamento':
            self.nomeCond_entr.entry.config(state ='enabled')
            self.bloco_entr.entry.config(state='enabled')
            self.numApart_entr.entry.config(state='enabled')
        else:
            self.nomeCond_entr.limpa_entr()
            self.nomeCond_entr.entry.config(state='disabled')
            self.bloco_entr.limpa_entr()
            self.bloco_entr.entry.config(state='disabled')
            self.numApart_entr.limpa_entr()
            self.numApart_entr.entry.config(state='disabled')

    def bind_bairro_CBox(self):
        self.ender_cliente.bairro = self.bairro_CBox.get_choice()

    def bind_cidade_CBox(self):
        self.ender_cliente.cidade = self.cidade_CBox.get_choice()
        lst_bairros = self.controller.load_BAIRROS(self.cidade_CBox.get_choice())
        self.bairro_CBox.config_CBox_state('readonly')
        self.bairro_CBox.define_values_CBox(lst_bairros)

    def bind_estado_CBox(self):
        self.ender_cliente.estado = self.estado_CBox.get_choice()
        lst_cidades = self.controller.load_CIDADES(self.estado_CBox.get_choice())
        self.cidade_CBox.config_CBox_state('readonly')
        self.cidade_CBox.define_values_CBox(lst_cidades)

    def callback(self):
        self.frame_master.update_frame()
        self.destroy()


class FornecFrame(LabelFrame):
    def __init__(self, frame_master, controller):
        super().__init__(frame_master, text='Fornecedores', padx=15, pady=15)
        self.grid()
        self.controller = controller
        self.lst_fornec = self.controller.loadAll_model(fornec())
        self.__build_widgets__()

    def __build_widgets__(self):
        self.alterarFornec_button = ttk.Button(self, text='Visualizar/Alterar perfil',
                                               command=lambda: self.perfilFornec())
        self.alterarFornec_button.grid(row=0, column=0, sticky='WE', padx=5)

        # self.separatorV = ttk.Separator(self, orient=VERTICAL)
        # self.separatorV.grid(row=0, column=1, sticky='WE', padx=4)

        self.insFornec_button = ttk.Button(self, text='Inserir fornecedor', command=lambda: self.ins_fornec())
        self.insFornec_button.grid(row=0, column=2, sticky='WE', padx=5)

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = wd_Treeview(self, num_cols=5, height=16)
        self.treeView1.headingText(0, "Nome:")
        self.treeView1.headingText(1, "Ramo:")
        self.treeView1.headingText(2, "Telefone:")
        self.treeView1.headingText(3, "Email:")
        self.treeView1.headingText(4, "Cidade:")
        self.treeView1.config_column(3, width=160)
        self.treeView1.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda event: self.verf_treeView())
        self.treeView1.insert(self.lst_fornec.to_treeView())

        self.menu_RC = sub_Menu(self)
        self.verf_treeView()

    def verf_treeView(self):
        if self.treeView1.idd_selection_treeView() is None:
            self.alterarFornec_button.config(state='disabled')
        else:
            self.alterarFornec_button.config(state='enabled')

    def update_frame(self):
        self.lst_fornec = self.controller.loadAll_model(fornec())
        self.__build_widgets__()

    def popup_menu(self, event):
        self.menu_RC.popup(event)

    def perfilFornec(self):
        fornec_escolhido = self.lst_fornec[self.treeView1.idd_selection_treeView()]
        perfil = PerfilFornecFrame(self, self.controller, fornec_escolhido)

    def ins_fornec(self):
        ins_fornecedor = InsFornecFrame(self, self.controller)


class EstabFrame(LabelFrame):
    def __init__(self, frame_master, controller):
        super().__init__(frame_master, text='Estabelecimentos/Identificações', padx=15, pady=15)
        self.grid()
        self.controller = controller
        self.lst_estabs = self.controller.loadAll_model(Estab())
        self.__build_widgets__()

    def __build_widgets__(self):
        self.alterarFornec_button = ttk.Button(self, text='Visualizar/Alterar estabelecimento',
                                               command=lambda: self.perfilEstab())
        self.alterarFornec_button.grid(row=0, column=0, sticky='WE', padx=5)

        # self.separatorV = ttk.Separator(self, orient=VERTICAL)
        # self.separatorV.grid(row=0, column=1, sticky='WE', padx=4)

        self.insFornec_button = ttk.Button(self, text='Inserir estabelecimento/Identificação', command=lambda: self.ins_estab())
        self.insFornec_button.grid(row=0, column=2, sticky='WE', padx=5)

        self.editaCateg_button = ttk.Button(self, text='Inserir/editar categorias', command=lambda: self.edita_Categ())
        self.editaCateg_button.grid(row=0, column=3, sticky='WE', padx=5)

        # Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = wd_Treeview(self, num_cols=5, height=16)
        self.treeView1.headingText(0, "Nome:")
        self.treeView1.headingText(1, "Ramo:")
        self.treeView1.config_column(1, width = 150)
        self.treeView1.headingText(2, "Cidade:")
        self.treeView1.headingText(3, "Bairro:")
        self.treeView1.headingText(4, "Telefone:")
        self.treeView1.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda event: self.verf_treeView())
        self.treeView1.insert(self.lst_estabs.to_treeView())

        self.menu_RC = sub_Menu(self)
        self.verf_treeView()

    def verf_treeView(self):
        if self.treeView1.idd_selection_treeView() is None:
            self.alterarFornec_button.config(state='disabled')
        else:
            self.alterarFornec_button.config(state='enabled')

    def update_frame(self):
        self.lst_estabs = self.controller.loadAll_model(Estab())
        self.__build_widgets__()

    def popup_menu(self, event):
        self.menu_RC.popup(event)

    def perfilEstab(self):
        estab_sel = self.lst_estabs[self.treeView1.idd_selection_treeView()]
        perfil = PerfilEstabFrame(self, self.controller, estab_sel)

    def edita_Categ(self):
        edita_categ = CategEstabFrame(self, self.controller)

    def ins_estab(self):
        ins_estab = InsEstabFrame(self, self.controller)


class CategEstabFrame(Toplevel):
    def __init__(self, frameMaster, controller):
        super().__init__(padx=15, pady=15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.controller = controller
        self.lst_categs = self.controller.loadAll_model(CategEstab())
        self.categ_sel = CategEstab()

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        self.editaLabel = ttk.Label(self, text = 'Categorias de estabelecimento', font = 'VERDANA')
        self.editaLabel.grid(row=0, column=0, columnspan=3, sticky='w', padx = 10, pady=10)

        self.frame_buttons = Frame(self)
        self.frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky = N)

        self.editaCateg_button = ttk.Button(self.frame_buttons, text = 'Editar categoria', command = self.alteraCateg, state='disabled')
        self.editaCateg_button.grid(row = 0, column = 0, sticky = 'we', padx = 10, pady=5)

        self.addCateg_button = ttk.Button(self.frame_buttons, text='Adicionar categoria', command=self.insCateg)
        self.addCateg_button.grid(row=0, column=1, sticky='we', padx = 10, pady=5)

        self.categs_treeView = wd_Treeview(self, num_cols=1, label='Categorias', height=10)
        self.categs_treeView.headingText(0, 'Nome')
        self.categs_treeView.insert(self.lst_categs.to_treeView())
        self.categs_treeView.treeView.bind('<<TreeviewSelect>>', lambda event: self.treeView_bind())
        self.categs_treeView.grid(row = 1, column=1, padx=10, pady=10, rowspan=3)

        self.editaCateg_frame = LabelFrame(self, text = 'Categoria')
        self.editaCateg_frame.grid(row=2, column=0, ipadx=15, ipady=15, sticky=W+E, padx=10)
        self.nomeCateg_entry = wd_Entry(self.editaCateg_frame, label='Nome', state_Entry='readonly')
        self.nomeCateg_entry.grid_frame(row=0, column=0, padx=10)
        self.salvaCateg_button = ttk.Button(self.editaCateg_frame, text = 'Salvar alteração', command=self.salva_categ)


    def update_frame(self):
        self.lst_categs = self.controller.loadAll_model(CategEstab())
        self.__build_widgets__()

    def salva_categ(self):
        self.editaCateg_frame.config(text='Categoria')
        nome = self.nomeCateg_entry.get_text()
        self.categ_sel.nome = nome
        self.controller.update_model(self.categ_sel)
        self.lst_categs = self.controller.loadAll_model(CategEstab())
        self.categs_treeView.clear_treeView()
        self.categs_treeView.insert(self.lst_categs.to_treeView())
        self.nomeCateg_entry.entry.config(state='readonly')
        self.editaCateg_button.config(state='disabled')
        self.salvaCateg_button.grid_forget()

    def alteraCateg(self):
        self.nomeCateg_entry.entry.config(state='enabled')
        self.editaCateg_frame.config(text='Editar categoria')
        self.salvaCateg_button.grid(row=1, column=0, padx=10, pady=5, sticky='we')

    def treeView_bind(self):
        self.editaCateg_button.config(state='enabled')
        self.categ_sel = self.lst_categs[self.categs_treeView.idd_selection_treeView()]
        self.nomeCateg_entry.insert_text(self.categ_sel.nome)

    def insCateg(self):
        inscategFrame = InsCategEstab(self, self.controller)

    def callback(self):
        self.destroy()


class InsCategEstab(Toplevel):
    def __init__(self, frameMaster, controller):
        super().__init__(padx=15, pady=15)
        self.update()
        self.deiconify()
        self.resizable(False, False)

        self.frameMaster = frameMaster
        self.controller = controller

        self.__build_widgets__()
        self.protocol("WM_DELETE_WINDOW", self.callback)

    def __build_widgets__(self):
        self.insCategEstab_label = ttk.Label(self, text = 'Inserir categoria de Estabelecimento', font = 'VERNADA')
        self.insCategEstab_label.grid(row=0, column=0, sticky='w')

        atenc = 'Atenção!\nAo criar uma categoria, defina um nome que caracterize um __tipo de estabelecimento,\ntal qual os já cadastrados, (ex: Supermercado, Papelaria, Farmárcia, etc).' \
                '\nÉ de grande importância a precisão da categoria para a geração de relatórios.'
        self.insCategAviso_label = ttk.Label(self, text=atenc)
        self.insCategAviso_label.grid(row=1, column=0, sticky='we', columnspan=3)


        self.insCateg_container = Frame(self)
        self.insCateg_container.grid(row=2, column=0, ipadx=15, ipady=15, sticky=W+E, padx=10)

        self.nomeCateg_entry = wd_Entry(self.insCateg_container , label='Nome da categoria:')
        self.nomeCateg_entry.entry.bind('<KeyRelease>', lambda event: self.nomeEntry_bind())
        self.nomeCateg_entry.grid_frame(row=0, column=0, sticky=W+E)

        self.insCateg_button = ttk.Button(self.insCateg_container, text = 'Salvar categoria', command = self.salvaCateg, state='disabled')
        self.insCateg_button.grid(row=1, column=0, sticky='we')

        self.cancel_button = ttk.Button(self.insCateg_container, text='Cancelar', command = self.callback)
        self.cancel_button.grid(row=2, column=0, sticky='we')

    def nomeEntry_bind(self):
        if len(self.nomeCateg_entry.get_text()) != 0:
            self.insCateg_button.config(state='enabled')

    def salvaCateg(self):
        categ = CategEstab()
        categ.nome = self.nomeCateg_entry.get_text()
        self.controller.insert_model(categ)
        self.nomeCateg_entry.limpa_entr()
        self.insCateg_button.config(state='disabled')



    def callback(self):
        self.frameMaster.update_frame()
        self.destroy()


class ins_itemServ_frame(Frame):
    def __init__(self, frame_master, controller, **kwargs):
        super().__init__(frame_master, **kwargs)
        self.grid()
        self.controller = controller
        #self.lstItemServ = self.controller.loadAll_model(c_item())


        self.__build_widgets__()

    def __build_widgets__(self):
        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(self, text='Cadastro de itens/serviços', relief=FLAT, borderwidth=2, padx="10",
                                     pady="10")
        self.frameLocal.grid(row=0, column=0, sticky=W + E + S + N)

        # Bloco (2): Configurando o título d, que receberá variável "label2":
        self.tit2 = Label(self.frameLocal, text='Especifique os dados:', pady=5)
        self.tit2.grid(row=0, column=0, columnspan=3, sticky=W + N)

        self.CBox1 = wd_CBox(self.frameLocal, set_CBox_default='Escolha a opção:', tit_CBox='Tipo:')
        self.CBox1.define_values_CBox(["Item", "Serviço"])
        self.CBox1.grid_frame(row=1, column=0, padx=5)

        self.CBox2 = wd_CBox(self.frameLocal, set_CBox_default='', tit_CBox='Categoria:')
        self.CBox2.config_CBox_state('disabled')
        self.CBox2.grid_frame(row=1, column=1, padx=5)

        self.CBox3 = wd_CBox(self.frameLocal, set_CBox_default='', tit_CBox='Subcategoria:')
        self.CBox3.config_CBox_state('disabled')
        self.CBox3.grid_frame(row=1, column=2, padx=5)

        self.separador1 = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        self.separador1.grid(row=3, column=0, columnspan=5, sticky="we", pady=10)

        self.caixa_entr1 = wd_Entry(self.frameLocal, width=51, tit_Entry='Nome:')
        self.caixa_entr1.grid_frame(column=0, row=4, padx=5, columnspan=3, sticky=W + E)

        self.CBox4 = wd_CBox(self.frameLocal, set_CBox_default='', tit_CBox='Espécie:')
        self.CBox4.config_CBox_state('disabled')
        self.CBox4.grid_frame(row=4, column=2, padx=5)

        # Bloco button1:
        self.botao1 = ttk.Button(self.frameLocal, text='Enviar para a lista:', command=lambda: self.__comando_B1__(),
                                 padding="30 5 30 5")
        self.botao1.grid(row=5, column=2, columnspan=2)

        self.blocoText = wd_Text(self.frameLocal, height=4, state=NORMAL, width=50)
        self.blocoText.grid_frame(row=1, column=0)

        self.separador2 = ttk.Separator(self.frameLocal, orient=HORIZONTAL)
        self.separador2.grid(row=6, column=0, columnspan=5, sticky="we")

        # Bloco do frame da Treeview:
        self.treeView1 = wd_Treeview(self.frameLocal, num_cols=5, height=5, label="Itens a cadastrar:")
        self.treeView1.headingText(0, "Nome:")
        self.treeView1.headingText(1, "Tipo:")
        self.treeView1.headingText(2, "Categoria:")
        self.treeView1.headingText(3, "Subcategoria:")
        self.treeView1.headingText(4, "Marca")
        self.treeView1.grid(row=7, column=0, columnspan=8)

        # Bloco do botão2:
        self.botao2 = ttk.Button(self.frameLocal, text='Cancelar cadastro', command=lambda: self.__comando_B2__())
        self.botao2.grid(row=8, column=0, padx=8, pady=6, sticky=W + E)

        # BLoco do botão3:
        self.botao3 = ttk.Button(self, text='Salvar cadastro', command=lambda: self.__comando_B3__())
        self.botao3.grid(row=8, column=1, padx=8, pady=6, sticky=W + E)

    def __comando_B1__(self):
        '''
        # item = c_item_serv()
        __tipo = self.retorna_escolha_CBox1()
        nome = self.retorna_entr1()
        descr = self.retorna_text1()
        categ = self.retorna_escolha_CBox2()
        subCateg = self.retorna_escolha_CBox3()
        marca = self.retorna_escolha_CBox4()

        if nome != '':  # and categ != 'Escolha a opção:' and subCateg != 'Escolha a opção:' and __tipo != 'Escolha a opção:':
            # Abaixo, o item é preenchido e inserido na treeview:
            print(__tipo)
            self.item = c_item_serv(__tipo=__tipo, nome=nome, descr=descr, categ=categ, subcateg=subCateg, marca=marca)
            # item.re_init(__tipo, nome, descr, categ, subCateg, especie)

            self.lst_itens.m_append_item(self.item)
            lst_aux = self.lst_itens.m_itens()

            for elem in lst_aux:
                lst_treeview = elem.to_treeView()
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
            if __tipo == 'Escolha a opção:':
                lst_aux.append('__tipo')
            if categ == 'Escolha a opção:':
                lst_aux.append('Categoria')
            if subCateg == 'Escolha a opção:':
                lst_aux.append('Subcategoria')

            str_aux = str(lst_aux)
            str_aux = str_aux.strip(']').strip('[')
            msg = 'Você não informou os seguintes dados: ' + str_aux
            # messagebox.showinfo('Atenção!', msg)
            self.__cond_B3__()'''
        pass

    def __comando_B3__(self):
        lst_aux = self.lst_itens.m_itens()
        for elem in lst_aux:
            self.bd_prog.ins_tupl_item_serv(elem.m_tupl_cadastro())
        # DESELEGANTE! LEMBRAR DE CRIAR UMA FUNÇÃO NO BD QUE RECEBA UMA LISTA!
        # self.bd_prog.ins_lst_item_serv(lst_itens)
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

    def bind_CBox4(self):  # <---- Combobox3 teria a função passiva de receber a lista de espécies
        pass
        '''
        __tipo = self.retorna_escolha_CBox1()
        subCateg = self.retorna_escolha_CBox3()
        if subCateg != "Escolha a opção:" and subCateg != '':
            item_lst = self.bd_prog.fetchall_espec_str(__tipo, subCateg)
            self.set_CBox4_default("Escolha a opção:")
            self.config_CBox4_state("readonly")
            self.define_values_CBox4(item_lst)
        '''

    def __cond_B3__(self):
        pass
        # ~ if self.lst_itens.m_len_lst() == 0:
        # ~ self.config_B3(state = 'disabled')
        # ~ else:
        # ~ self.config_B3(state = 'enabled')


class ins_move_frame(Frame):
    def __init__(self, frame_master, controller, **kwargs):
        super().__init__(frame_master, **kwargs)
        self.grid(row=0, column=0, sticky = N)
        self.controller = controller
        self.ger_atv = controller.ger_atv

        # Bloco: Configurando frameLocal e seu título (LabelFrame):
        self.subFrame1 = ttk.Frame(self)
        self.subFrame1.grid(row=0, column=0, sticky='w', padx="8", pady="8")

        # Bloco: Configurando o título d, que receberá variável "label2":
        self.label1 = Label(self.subFrame1, text='Selecione o __tipo de movimentação', pady=5, font = 'VERNADA')
        self.label1.grid(row=0, column=0, columnspan=5, sticky=W)

        # Bloco button1:
        self.button1 = ttk.Button(self.subFrame1, text='Transferência entre contas', command=lambda: self.tef_frame())
        self.button1.grid(row=1, column=1, padx = 5, pady=3, sticky = 'we')

        # Bloco button1:
        self.button2 = ttk.Button(self.subFrame1, text='Compra de itens/serviços', command=lambda: self.comprasFrame())
        self.button2.grid(row=1, column=2, padx = 5, pady=3, sticky = 'we')

        # Bloco button1:
        self.button3 = ttk.Button(self.subFrame1, text='Pagamento de contas')#, command=lambda: self.comprasFrame())
        self.button3.grid(row=2, column=1, padx = 5, pady=3, sticky = 'we')

        # Bloco: Configurando frameLocal e seu título (LabelFrame):
        self.frame_vendas = Frame(self, padx="8", pady="8")
        #self.frame_local.grid(row=2, column=0, sticky=W+E+S+N)

        self.buscaNome_entr = wd_Entry(self.frame_vendas, label='Buscar por nome:')
        self.buscaNome_entr.entry.bind('<KeyRelease>', lambda event: self.buscaNome_bind())
        self.buscaNome_entr.grid_frame(row=0, column=0, padx=10)

        self.buscaCod_entr = wd_Entry(self.frame_vendas, label='Buscar por código:', width= 10)
        self.buscaCod_entr.entry.bind('<KeyRelease>', lambda event: self.buscaCod_bind())
        self.buscaCod_entr.grid_frame(row=0, column=1, padx=10)

        self.quant_entr = wd_Entry(self.frame_vendas, label='Quantidade comprada:', width= 10)
        #self.quant_entr.entry.bind('<KeyRelease>', lambda event: self.buscaCod_bind())
        self.quant_entr.grid_frame(row=1, column=1, padx=10)

        self.enviaItem_button = ttk.Button(self.frame_vendas, text='Enviar para a lista', command = lambda: self.envia_lst())
        self.enviaItem_button.grid(row=1, column=0, pady=3, sticky = 'wes', padx=10)

        self.treeView1_wd = wd_Treeview(self.frame_vendas, num_cols=3, height=16)
        self.treeView1_wd.headingText(0, 'Nome')
        self.treeView1_wd.headingText(1, 'Código')
        self.treeView1_wd.headingText(2, 'quantidade')
        self.treeView1_wd.config_column(0, width=150)
        self.treeView1_wd.config_column(1, width=50)
        self.treeView1_wd.config_column(2, width=50)
        # Configurando .bind da Treeview:
        #self.itens_treeView.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_event1_treeView1(event))
        #self.itens_treeView.treeView.bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))
        self.treeView1_wd.grid(row=2, column=0, columnspan=3, padx=10, sticky = 'W')

        self.lstVenda_treeView = wd_Treeview(self.frame_vendas, label='Lista de itens comprados:', num_cols=3, height=16)
        self.lstVenda_treeView.headingText(0, 'Nome')
        self.lstVenda_treeView.headingText(1, 'Código')
        self.lstVenda_treeView.headingText(2, 'quantidade')
        self.lstVenda_treeView.config_column(0, width=150)
        self.lstVenda_treeView.config_column(1, width = 50)
        self.lstVenda_treeView.config_column(2, width=50)
        self.lstVenda_treeView.grid(row=2, column=3, columnspan=5, padx=10, sticky='W')

        self.valorTotal_entr = wd_Entry(self.frame_vendas, label = 'Valor a ser pago:', state='readonly')
        self.valorTotal_entr.grid_frame(row = 1, column=3, sticky='W', padx=10)

        self.confirmaVenda_button = ttk.Button(self.frame_vendas, text = 'Confirmar venda')
        self.confirmaVenda_button.grid(row = 1, column=4, sticky='WES', padx=10)

        self.carrega_itens()

    def envia_lst(self):
        item_escolha = self.lst_itens[self.treeView1_wd.idd_selection_treeView()]
        quant = int(self.quant_entr.get_text())
        item_estoque = itemVenda(item=item_escolha)
        if item_estoque.itemVenda(quant) is False:
            showinfo('Estoque', 'Quantidade não dispnível em estoque!')
        else:
            item_estoque.quant = quant
            self.vendas_lst.append(item_estoque)
            self.lstVenda_treeView.insert(self.vendas_lst.to_treeView())

    def tef_frame(self):
        tef = InsTEF(self, self.controller)
        tef.grid(row=2, column=0, sticky=W+E+S+N)

    def comprasFrame(self):
        vends = InsComprasFrame(self, self.controller)
        vends.grid(row=2, column=0)

    def buscaNome_bind(self):
        self.buscaCod_entr.limpa_entr()
        nome = self.buscaNome_entr.get_text()
        if nome != '':
            lst_item = self.controller.search_name_item(nome)
            self.treeView1_wd.clear_treeView()
            self.treeView1_wd.insert(lst_item.to_treeView())
        else:
            self.carrega_itens()

    def buscaCod_bind(self):
        self.buscaNome_entr.limpa_entr()
        code = self.buscaCod_entr.get_text()
        if code != '':
            lst_item = self.controller.search_code_item(code)
            self.treeView1_wd.clear_treeView()
            self.treeView1_wd.insert(lst_item.to_treeView())
        else:
            self.carrega_itens()

    def carrega_itens(self):
        self.treeView1_wd.clear_treeView()
        self.treeView1_wd.tit_treeView.config(text='Itens em estoque:')
        self.lst_itens = self.controller.loadAll_model(item())
        self.treeView1_wd.insert(self.lst_itens.to_treeView())


class InsComprasFrame(Frame):
    def __init__(self, frame_master, controller, **kwargs):
        super().__init__(frame_master, **kwargs)
        self.grid(row=0, column=0, sticky = N)
        self.controller = controller
        self.ger_atv = controller.ger_atv

        self.lst_compras = MyCollection()
        self.lst_contas = self.controller.loadAll_model(c_conta())
        self.contaCed = c_conta()
        self.compra = CompraItemServ()
        self.valorTotal = 0
        self.build_frame()

    def build_frame(self):
        self.contaCed_cbox = wd_CBox(self, tit_CBox='Conta cedente:', set_CBox_default='Escolha a conta', CBox_values=self.lst_contas.to_comboBox())
        self.contaCed_cbox.CBox.bind('<<ComboboxSelected>>', lambda event: self.contaCed_bind())
        self.contaCed_cbox.grid(row=0, column = 0, sticky=W)

        self.calendario = wd_calendario(self)
        self.calendario.grid(row=0, column=1, sticky=W, rowspan=2)

        self.frame_estab = EscolhaEstabFrame(self, self.controller)
        self.frame_estab.grid(row=1, column=0, sticky = W, padx=10)
        self.frame_local = Frame(self, padx="8", pady="8")
        self.frame_local.grid(row=2, column=0, sticky=W+E+S+N, columnspan = 2)


        self.buscaNome_entr = wd_Entry(self.frame_local, label='Buscar por nome:')
        self.buscaNome_entr.entry.bind('<KeyRelease>', lambda event: self.buscaNome_bind())
        self.buscaNome_entr.grid_frame(row=0, column=0, padx=10)

        self.buscaCod_entr = wd_Entry(self.frame_local, label='Buscar por código:', width= 10)
        self.buscaCod_entr.entry.bind('<KeyRelease>', lambda event: self.buscaCod_bind())
        self.buscaCod_entr.grid_frame(row=0, column=1, padx=10)

        self.quant_entr = wd_Entry(self.frame_local, label='Quantidade comprada:', width= 10, state_Entry='disabled')
        #self.quant_entr.entry.bind('<KeyRelease>', lambda event: self.buscaCod_bind())
        self.quant_entr.grid_frame(row=1, column=1, padx=10)

        self.valorUnit_entr = wd_Entry(self.frame_local, label='Valor unitário (R$):', width= 10, state_Entry='disabled')
        #self.valorUnit_entr.entry.bind('<KeyRelease>', lambda event: self.())
        self.valorUnit_entr.grid_frame(row=1, column=2, padx=10)

        self.valorTotal_entr = wd_Entry(self.frame_local, label='Valor Total (R$):', width= 10)
        #self.valorUnit_entr.entry.bind('<KeyRelease>', lambda event: self.())
        self.valorTotal_entr.grid_frame(row=1, column=3, padx=10)

        self.enviaItem_button = ttk.Button(self.frame_local, text='Enviar para a lista', state = 'disabled', command = lambda: self.envia_lst())
        self.enviaItem_button.grid(row=1, column=0, pady=3, sticky = 'wes', padx=10)

        self.treeView1_wd = wd_Treeview(self.frame_local, num_cols=5, height=16, label='Lista de itens: ')
        self.treeView1_wd.headingText(0, 'Nome')
        self.treeView1_wd.headingText(1, 'Código')
        self.treeView1_wd.headingText(2, 'Categoria')
        self.treeView1_wd.headingText(3, 'Subcategoria')
        self.treeView1_wd.headingText(4, 'Espécie')
        self.treeView1_wd.config_column(0, width=150)
        self.treeView1_wd.config_column(1, width=50)
        self.treeView1_wd.config_column(2, width=50)
        self.treeView1_wd.config_column(3, width=50)
        self.treeView1_wd.config_column(4, width=50)
        self.treeView1_wd.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_treeview1())
        #self.itens_treeView.treeView.bind('<Button-3>', lambda event: self.bind_event2_treeView1(event))
        self.treeView1_wd.grid(row=2, column=0, columnspan=3, padx=10, sticky = 'W')

        self.lstCompras_treeView = wd_Treeview(self.frame_local, label='Lista de itens comprados:', num_cols=4, height=16)
        self.lstCompras_treeView.headingText(0, 'Nome')
        self.lstCompras_treeView.headingText(1, 'quant')
        self.lstCompras_treeView.headingText(2, 'Valor unit')
        self.lstCompras_treeView.headingText(3, 'Valor total')
        self.lstCompras_treeView.config_column(0, width=150)
        self.lstCompras_treeView.config_column(1, width=50)
        self.lstCompras_treeView.config_column(2, width=60)
        self.lstCompras_treeView.config_column(3, width=65)
        self.lstCompras_treeView.grid(row=2, column=3, columnspan=5, padx=10, sticky='W')

        self.valorTotal_entr = wd_Entry(self.frame_local, label ='Valor a ser pago:', state='readonly')
        self.valorTotal_entr.grid_frame(row = 1, column=3, sticky='W', padx=10)

        self.confirmaVenda_button = ttk.Button(self.frame_local, text ='Confirmar compra', command = self.confirmaTransac)
        self.confirmaVenda_button.grid(row = 1, column=4, sticky='WES', padx=10)
        self.carrega_itens()

    def confirmaTransac(self):
        self.compra.data = self.calendario.selection()
        self.compra.valor = float(self.valorTotal)
        self.compra.estab = self.frame_estab.get_estab()
        self.compra.conta_ced = self.contaCed
        self.compra.compras_list = self.lst_compras
        self.compra.efetiva()

        # ABAIXO O CONTROLLER EFETIVA A TRANSAÇÃO:
        feedback = self.controller.efetivaCompra(self.compra)
        if feedback == 0:
            showinfo('Compra', 'Compra adiciona com sucesso no banco de dados!')
            self.build_frame()
            print('Compra: ', self.compra)
            print('Conta cedente: ', self.contaCed)

    def bind_treeview1(self):
        self.enviaItem_button.config(state = 'enabled')
        self.valorUnit_entr.entry.config(state = 'enabled')
        self.quant_entr.entry.config(state = 'enabled')

    def contaCed_bind(self):
        nomeConta = self.contaCed_cbox.get_choice()
        self.contaCed = self.lst_contas.search_name(nomeConta)
        print('Conta ced escolhida: ', self.contaCed)

    def envia_lst(self):
        self.verf_dados()
        item_escolha = self.lst_itens[self.treeView1_wd.idd_selection_treeView()]
        quant = float(self.quant_entr.get_text())
        valor_unit = float(self.valorUnit_entr.get_text())
        self.valorTotal = self.valorTotal + quant*valor_unit
        self.valorTotal_entr.insert_text(str(self.valorTotal))

        itemServ_aux = ItemServCompra()
        itemServ_aux.itemServ = item_escolha
        itemServ_aux.quant = quant
        itemServ_aux.valor_unit = valor_unit
        # itemServ_aux.__tipo = self.tipo_Cbox.retorna_escolha_Cbox()
        itemServ_aux.tipo = 'Item'

        self.lst_compras.append(itemServ_aux)
        self.lstCompras_treeView.clear_treeView()
        self.lstCompras_treeView.insert(self.lst_compras.to_treeView())

    def verf_dados(self):
        pass


    def vendasFrame(self):
        self.vendas_lst = vendasLst()
        self.frame_local.grid(row=2, column=0, sticky=W + E + S + N)

    def buscaNome_bind(self):
        self.buscaCod_entr.limpa_entr()
        nome = self.buscaNome_entr.get_text()
        if nome != '':
            lst_item = self.controller.search_name_item(nome)
            self.treeView1_wd.clear_treeView()
            self.treeView1_wd.insert(lst_item.to_treeView())
        else:
            self.carrega_itens()

    def buscaCod_bind(self):
        self.buscaNome_entr.limpa_entr()
        code = self.buscaCod_entr.get_text()
        if code != '':
            lst_item = self.controller.search_code_item(code)
            self.treeView1_wd.clear_treeView()
            self.treeView1_wd.insert(lst_item.to_treeView())
        else:
            self.carrega_itens()

    def carrega_itens(self):
        self.treeView1_wd.clear_treeView()
        self.treeView1_wd.tit_treeView.config(text='Itens cadastrados:')
        self.lst_itens = self.controller.loadAll_model(item())
        self.treeView1_wd.insert(self.lst_itens.to_treeView())


class InsAgendFrame(LabelFrame):
    def __init__(self, frame_master, controller, **kwargs):
        super().__init__(frame_master, **kwargs)
        self.grid(row=0, column=0)
        self.controller = controller
        self.ger_atv = controller.ger_atv

        self.canv = Canvas(self, width=600, height=400,
                              scrollregion=(0, 0, 1200, 800))
        self.canv.grid(row=0, column=0)
        self.scrollY = Scrollbar(self, orient=VERTICAL,
                                    command=self.canv.yview)
        self.scrollY.grid(row=0, column=1, sticky=N + S)
        self.scrollX = Scrollbar(self, orient=HORIZONTAL,
                                    command=self.canv.xview)
        self.scrollX.grid(row=1, column=0, sticky=E + W)
        self.canv['xscrollcommand'] = self.scrollX.set
        self.canv['yscrollcommand'] = self.scrollY.set


        # TODO IMPLEMENTAR O METODO ABAIXO
        self.lst_contas = self.ger_atv.lst_contas

        # Bloco: Configurando frameLocal e seu título (LabelFrame):
        self.subFrame1 = Frame(self.canv, padx="8", pady="8")
        self.subFrame1.grid(row=0, column=0, sticky=W + E + S + N)

        # Bloco: Configurando o título d, que receberá variável "label2":
        self.label1 = Label(self.subFrame1, text='Transferência entre contas', pady=5)
        self.label1.grid(row=0, column=0, columnspan=5, sticky=W + N)

        self.label2 = Label(self.subFrame1, text='Selecione a data', pady=5)
        self.label2.grid(row=1, column=0, columnspan=5, sticky=N + W)

        # Bloco entr1:
        self.entr1 = wd_Entry(self.subFrame1, tit_Entry='Nome da movimentação', width=55)
        self.entr1.grid_frame(row=1, column=1, sticky=W + E, padx=10, columnspan=2)

        # Bloco entr2:
        self.entr2 = wd_Entry(self.subFrame1, tit_Entry='Data da movimentação:', state_Entry='readonly', width=26)
        self.entr2.grid_frame(row=5, column=0, sticky=W + N, padx=10)

        # Bloco entr3:
        self.entr3 = wd_Entry(self.subFrame1, tit_Entry='Valor')
        self.entr3.grid_frame(row=5, column=1, sticky=W + E, padx=10, columnspan=2)

        # Bloco wd_CBox1:
        self.CBox1 = wd_CBox(self.subFrame1, CBox_values=self.lst_contas.to_comboBox(), tit_Cbox='wd_CBox1',
                             set_CBox_default='Selecionar conta', tit_CBox='Conta cedente', width=23)
        self.CBox1.grid_frame(row=4, column=1, sticky=W + N, padx=10)

        # Bloco categ_CBox:
        self.CBox2 = wd_CBox(self.subFrame1, CBox_values=self.lst_contas.to_comboBox(), tit_Cbox='categ_CBox',
                             set_CBox_default='Selecionar conta', tit_CBox='Conta favorecida', width=23)
        self.CBox2.grid_frame(row=4, column=2, sticky=W + N, padx=10)

        # Bloco button1:
        self.button1 = ttk.Button(self.subFrame1, text='Efetivar', command=lambda: self.efetivar())
        self.button1.grid(row=5, column=2, pady=3, rowspan=2)

        # Instanciando o bloco Text:
        self.blocoText = wd_Text(self.subFrame1, width=35, height=3, bd=3, tit="Descrição:")
        self.blocoText.grid_frame(row=2, column=1, rowspan=2, columnspan=2, sticky=W, padx=11, pady=12)

        # Bloco 4: instanciando o frame que conterá o calendário:
        self.calendario = wd_calendario(self.subFrame1)
        self.calendario.grid_frame(row=2, column=0, rowspan=3, padx=10)

    def confirma_move(self, move):
        confirm = confirm_move_frame(move)
        return confirm

    def verf_value(self):
        # VERIFRICAR SE OS DADOS DA TRANSAÇÃO ESTÃO OK
        return True

    def efetivar(self):
        if (self.verf_value()):
            dic_move = {}
            dic_move['conta_ced'] = self.lst_contas.search_name(self.CBox1.get_choice())
            dic_move['conta_fav'] = self.lst_contas.search_name(self.CBox2.get_choice())
            dic_move['valor'] = self.entr3.get_text()
            dic_move['descr'] = self.blocoText.get_text()
            dic_move['data'] = self.calendario.selection_date()
            dic_move['__tipo'] = 'TEF'
            print('AQUI PORRA', dic_move)
            move = c_move(**dic_move)
            move.efetiva()
            # confirm = self.confirma_move(move)
            # if confirm == True:
            # LIMPAR O FRAME
            # pass
            # else:
            # MANTER O FRAME
            #  pass


class ins_venda_frame(Frame):
    def __init__(self, framePai, controller, **kwargs):
        super().__init__(framePai, **kwargs)
        self.grid()
        self.controller = controller
        self.ger_atv = controller.ger_atv
        self.lst_clients = self.ger_atv.load_clientes()
        self.lst_itens = self.ger_atv.load_itens()


        self.lst_compras = MyCollection()
        self.ref_compras = CompraItemServ()
        self.itemServ_sel = None

        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(self, text='Lista de compras', borderwidth=2, padx="10", pady="10")
        self.frameLocal.grid(row=1, column=0)

        ########## BLOCO DO SUBFRAME1: ###########
        self.subFrame1 = Frame(self.frameLocal, padx=5, pady=5)
        self.subFrame1.grid(row=0, column=0, sticky=W + E + S + N)

        # Bloco (2): Configurando o label2:
        self.label1 = Label(self.subFrame1, text='Estabelecimento', pady=5)
        self.label1.grid(row=0, column=0, columnspan=2, sticky=W + N)

        # Bloco entr1 (3):
        self.entry1 = wd_Entry(self.subFrame1, width=45, tit_Entry="Buscar estabelecimento",
                               set_Entry_default='Digite o nome do estabelecimento')
        self.entry1.grid_frame(row=1, column=0, columnspan=2, sticky=W, padx=5)

        # Bloco button1:
        self.button1 = ttk.Button(self.subFrame1, text="Enviar", command=self.command_button1)
        self.button1.grid(row=1, column=2, sticky=S)

        # Bloco do frame da Treeview1:
        self.treeView1 = wd_Treeview(self.subFrame1, num_cols=2, height=3, tit='Estabelecimentos')
        self.treeView1.headingText(0, 'Nome:')
        self.treeView1.headingText('1', 'Cidade:')
        self.treeView1.insert(self.lst_clients.to_treeView())
        self.treeView1.grid(row=5, column=0, sticky=W, columnspan=4, pady=5, padx=5)

        # Bloco do separator1:
        self.separator1 = ttk.Separator(self.subFrame1, orient=HORIZONTAL)
        self.separator1.grid(row=6, column=0, columnspan=5, pady=10, padx=10, sticky="we")

        ############## BLOCO DO SUBFRAME2: ############
        self.subFrame3 = Frame(self.frameLocal, padx=5, pady=5)
        self.subFrame3.grid(row=1, column=0, sticky=W + E + S + N)

        # Bloco (2): Configurando o label2:
        self.label2 = Label(self.subFrame3, text='Listar Itens/Serviços', pady=5)
        self.label2.grid(row=7, column=0, columnspan=2, sticky=W + N)

        # Bloco entr2:
        self.entry2 = wd_Entry(self.subFrame3, width=45, tit_Entry="Buscar Itens/Serviços",
                               set_Entry_default='Digite o nome', state_Entry='disabled')
        self.entry2.grid_frame(row=8, column=0, columnspan=3, sticky=W + E, padx=5)

        # Bloco wd_CBox1:
        self.CBox1 = wd_CBox(self.subFrame3, tit_CBox='Tipo', width=15, CBox_values=['Item', 'Serviço'],
                             set_CBox_default='Escolha a opção')
        self.CBox1.grid_frame(row=8, column=2, padx=10)

        # Bloco entr3:
        self.entry3 = wd_Entry(self.subFrame3, tit_Entry='Quantidade', width=15, set_Entry_default='kg/litros/unit..',
                               state_Entry='disabled')
        self.entry3.grid_frame(row=9, column=0, sticky=W, padx=5)

        # Bloco entr4:
        self.entry4 = wd_Entry(self.subFrame3, tit_Entry="Preço quantidade", width=15, set_Entry_default='R$',
                               state_Entry='disabled')
        self.entry4.grid_frame(row=9, column=1, sticky=W, padx=5)

        # Bloco entr5:
        self.entry5 = wd_Entry(self.subFrame3, tit_Entry="Preço total", width=15, state_Entry='disabled')
        self.entry5.grid_frame(row=9, column=2, sticky=W, padx=5)

        # Bloco button2:
        self.botao2 = ttk.Button(self.subFrame3, text="Enviar", command=self.command_button2)
        self.botao2.grid(row=9, column=2, sticky=E + S)

        # Bloco do frame da Treeview2:
        self.treeView2 = wd_Treeview(self.subFrame3, num_cols=4)
        self.treeView2.headingText(0, 'Nome:')
        self.treeView2.headingText('1', 'Tipo:')
        self.treeView2.headingText('2', 'Categoria')
        self.treeView2.headingText('3', 'Subcategoria')
        self.treeView2.grid(row=14, column=0, sticky=W, padx=5, pady=5, columnspan=4)

        # ~ #Bloco do separador2:
        # ~ self.separador2 = ttk.Separator(self.subFrame3, orient = HORIZONTAL)
        # ~ self.separador2.grid(row = 15, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "we")

        ########### BLOCO DO SUBFRAME3: ##########
        self.subFrame4 = Frame(self.frameLocal, padx=5, pady=5)
        self.subFrame4.grid(row=0, column=1, rowspan=2, sticky=W + E + S + N)

        self.separador3 = ttk.Separator(self.subFrame4, orient=VERTICAL)
        self.separador3.grid(row=0, column=0, rowspan=40, pady=10, padx=10, sticky="sn")

        self.entry6 = wd_Entry(self.subFrame4, width=51, tit_Entry='Estabelecimento', state_Entry='disabled')
        self.entry6.grid_frame(row=0, column=1, sticky=W, padx=5)

        self.treeView3 = wd_Treeview(self.subFrame4, num_cols=4, height=17, tit='Lista de itens/serviços')
        self.treeView3.headingText(0, 'Nome:')
        self.treeView3.headingText('1', 'quantidade:')
        self.treeView3.headingText('2', 'preço unit.')
        self.treeView3.headingText('3', 'preço total')
        self.treeView3.grid(row=1, column=1, sticky=W, padx=5, pady=5, rowspan=18, columnspan=4, num_cols=4)

        self.button3 = ttk.Button(self.subFrame4, text="Enviar", command=self.command_button3())
        self.button3.grid(row=20, column=1, sticky=W, pady=10)

        self.label4 = ttk.Label(self.subFrame4, text='Valor total:')
        self.label4.grid(row=20, column=2, sticky=E)

        # ABAIXO, SETANDO OS .bind():
        # .bind da Combobox:
        self.CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())

        # .bind da treeView2:
        self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_treeView1())

        # .bind da treeView2:
        self.treeView2.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_treeView2())

        # .bind DA ENTRY3:
        self.entry3.entry.bind('<FocusIn>', lambda event: self.bind1_entry3())
        self.entry3.entry.bind('<KeyRelease>', lambda event: self.bind2_entry3())

        # .bind DA ENTRY4:
        self.entry4.entry.bind('<FocusIn>', lambda event: self.bind1_entry4())
        self.entry4.entry.bind('<KeyRelease>', lambda event: self.bind2_entry4())

        # .bind DA ENTRY1:
        self.entry1.entry.bind('<FocusIn>', lambda event: self.bind1_entry1())
        self.entry1.entry.bind('<KeyRelease>', lambda event: self.bind2_entry1())
        # .bind DA ENTRY2:
        self.entry2.entry.bind('<FocusIn>', lambda event: self.bind1_entry2())
        self.entry2.entry.bind('<KeyRelease>', lambda event: self.bind2_entry2())


    def bind_CBox1(self):
        tipo = self.CBox1.get_choice()
        self.entry2.config_Entry(state='enabled')
        self.entry3.config_Entry(state='enabled')
        self.entry4.config_Entry(state='enabled')
        if tipo == 'Item':
            self.treeView2.clear_treeView()
            self.treeView2.insert(self.lst_itens.to_treeView())
        else:
            self.treeView2.clear_treeView()
            self.treeView2.insert(self.lst_servs.to_treeView())

    def command_button1(self):
        self.entry6.insert_text(self.ref_compras.estab.nome)

    def command_button2(self):
        quant = self.entry3.get_text()
        preco_unit = self.entry4.get_text()
        preco_total = self.entry5.get_text()

        itemServ = c_itemServ_ref(itemServ=self.itemServ_sel, quant=quant, preco_unit=preco_unit,
                                  preco_total=preco_total)
        self.lst_compras.append(itemServ)
        self.treeView3.clear_treeView()
        self.treeView3.insert(self.lst_compras.to_treeView())

    def command_button3(self):
        pass

    def bind_treeView1(self):
        estab_id = self.treeView1.idd_selection_treeView()
        estab = self.lst_clients[estab_id]
        self.ref_compras.estab = estab
        self.entry1.insert_text(estab.nome)
        # self.entry1.insert_text(estab.nome())

    def bind_treeView2(self):
        tipo = self.CBox1.get_choice()
        if tipo == 'Item':
            item_id = self.treeView2.idd_selection_treeView()
            self.itemServ_sel = self.lst_itens[item_id]
            self.entry2.insert_text(self.itemServ_sel.nome)
        else:
            serv_id = self.treeView2.idd_selection_treeView()
            self.itemServ_sel = self.lst_servs[serv_id]
            self.entry2.insert_text(self.itemServ_sel.nome)

    def bind1_entry1(self):
        self.entry1.limpa_entr()

    def bind2_entry1(self):
        # METODO DE BUSCA
        pass

    def bind1_entry2(self):
        self.entry2.limpa_entr()
        pass

    def bind2_entry2(self):
        # METODO DE BUSCA
        pass

    def bind1_entry3(self):
        self.entry3.limpa_entr()

    def bind1_entry4(self):
        self.entry4.limpa_entr()

    def bind2_entry3(self):
        quant = self.entry3.get_text()
        valor_unit = self.entry4.get_text()

        if quant is not '' and valor_unit is not '':
            try:
                quant = float(quant)
                valor_unit = float(valor_unit)
                valor_total = quant * valor_unit
                self.entry5.insert_text(str(valor_total))
            except:
                pass

    def bind2_entry4(self):
        quant = self.entry3.get_text()
        valor_unit = self.entry4.get_text()

        if quant is not '' and valor_unit is not '':
            try:
                quant = float(quant)
                valor_unit = float(valor_unit)
                valor_total = quant * valor_unit
                self.entry5.insert_text(str(valor_total))
            except:
                pass


class ins_compras_list_frame(Frame):
    def __init__(self, framePai, controller, **kwargs):
        super().__init__(framePai, **kwargs)
        self.grid()
        self.controller = controller
        self.ger_atv = controller.ger_atv
        self.lst_estabs = self.ger_atv.load_estabs()
        self.lst_itens = self.ger_atv.load_itens()
        self.lst_servs = self.ger_atv.load_servs()

        self.lst_compras = MyCollection()
        self.ref_compras = CompraItemServ()
        self.itemServ_sel = None

        # Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(self, text='Lista de compras', borderwidth=2, padx="10", pady="10")
        self.frameLocal.grid(row=1, column=0)

        ########## BLOCO DO SUBFRAME1: ###########
        self.subFrame1 = Frame(self.frameLocal, padx=5, pady=5)
        self.subFrame1.grid(row=0, column=0, sticky=W + E + S + N)

        # Bloco (2): Configurando o label2:
        self.label1 = Label(self.subFrame1, text='Estabelecimento', pady=5)
        self.label1.grid(row=0, column=0, columnspan=2, sticky=W + N)

        # Bloco entr1 (3):
        self.entry1 = wd_Entry(self.subFrame1, width=45, tit_Entry="Buscar estabelecimento",
                               set_Entry_default='Digite o nome do estabelecimento')
        self.entry1.grid_frame(row=1, column=0, columnspan=2, sticky=W, padx=5)

        # Bloco button1:
        self.button1 = ttk.Button(self.subFrame1, text="Enviar", command=self.command_button1)
        self.button1.grid(row=1, column=2, sticky=S)

        # Bloco do frame da Treeview1:
        self.treeView1 = wd_Treeview(self.subFrame1, num_cols=2, height=3, tit='Estabelecimentos')
        self.treeView1.headingText(0, 'Nome:')
        self.treeView1.headingText('1', 'Cidade:')
        self.treeView1.insert(self.lst_estabs.to_treeView())
        self.treeView1.grid(row=5, column=0, sticky=W, columnspan=4, pady=5, padx=5)

        # Bloco do separator1:
        self.separator1 = ttk.Separator(self.subFrame1, orient=HORIZONTAL)
        self.separator1.grid(row=6, column=0, columnspan=5, pady=10, padx=10, sticky="we")

        ############## BLOCO DO SUBFRAME2: ############
        self.subFrame3 = Frame(self.frameLocal, padx=5, pady=5)
        self.subFrame3.grid(row=1, column=0, sticky=W + E + S + N)

        # Bloco (2): Configurando o label2:
        self.label2 = Label(self.subFrame3, text='Listar Itens/Serviços', pady=5)
        self.label2.grid(row=7, column=0, columnspan=2, sticky=W + N)

        # Bloco entr2:
        self.entry2 = wd_Entry(self.subFrame3, width=45, tit_Entry="Buscar Itens/Serviços",
                               set_Entry_default='Digite o nome', state_Entry='disabled')
        self.entry2.grid_frame(row=8, column=0, columnspan=3, sticky=W + E, padx=5)

        # Bloco wd_CBox1:
        self.CBox1 = wd_CBox(self.subFrame3, tit_CBox='Tipo', width=15, CBox_values=['Item', 'Serviço'],
                             set_CBox_default='Escolha a opção')
        self.CBox1.grid_frame(row=8, column=2, padx=10)

        # Bloco entr3:
        self.entry3 = wd_Entry(self.subFrame3, tit_Entry='Quantidade', width=15, set_Entry_default='kg/litros/unit..',
                               state_Entry='disabled')
        self.entry3.grid_frame(row=9, column=0, sticky=W, padx=5)

        # Bloco entr4:
        self.entry4 = wd_Entry(self.subFrame3, tit_Entry="Preço quantidade", width=15, set_Entry_default='R$',
                               state_Entry='disabled')
        self.entry4.grid_frame(row=9, column=1, sticky=W, padx=5)

        # Bloco entr5:
        self.entry5 = wd_Entry(self.subFrame3, tit_Entry="Preço total", width=15, state_Entry='disabled')
        self.entry5.grid_frame(row=9, column=2, sticky=W, padx=5)

        # Bloco button2:
        self.botao2 = ttk.Button(self.subFrame3, text="Enviar", command=self.command_button2)
        self.botao2.grid(row=9, column=2, sticky=E + S)

        # Bloco do frame da Treeview2:
        self.treeView2 = wd_Treeview(self.subFrame3, num_cols=4)
        self.treeView2.headingText(0, 'Nome:')
        self.treeView2.headingText('1', 'Tipo:')
        self.treeView2.headingText('2', 'Categoria')
        self.treeView2.headingText('3', 'Subcategoria')
        self.treeView2.grid(row=14, column=0, sticky=W, padx=5, pady=5, columnspan=4)

        # ~ #Bloco do separador2:
        # ~ self.separador2 = ttk.Separator(self.subFrame3, orient = HORIZONTAL)
        # ~ self.separador2.grid(row = 15, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "we")

        ########### BLOCO DO SUBFRAME3: ##########
        self.subFrame4 = Frame(self.frameLocal, padx=5, pady=5)
        self.subFrame4.grid(row=0, column=1, rowspan=2, sticky=W + E + S + N)

        self.separador3 = ttk.Separator(self.subFrame4, orient=VERTICAL)
        self.separador3.grid(row=0, column=0, rowspan=40, pady=10, padx=10, sticky="sn")

        self.entry6 = wd_Entry(self.subFrame4, width=51, tit_Entry='Estabelecimento', state_Entry='disabled')
        self.entry6.grid_frame(row=0, column=1, sticky=W, padx=5)

        self.treeView3 = wd_Treeview(self.subFrame4, num_cols=4, height=17, tit='Lista de itens/serviços')
        self.treeView3.headingText(0, 'Nome:')
        self.treeView3.headingText('1', 'quantidade:')
        self.treeView3.headingText('2', 'preço unit.')
        self.treeView3.headingText('3', 'preço total')
        self.treeView3.grid(row=1, column=1, sticky=W, padx=5, pady=5, rowspan=18, columnspan=4, num_cols=4)

        self.button3 = ttk.Button(self.subFrame4, text="Enviar", command=self.command_button3())
        self.button3.grid(row=20, column=1, sticky=W, pady=10)

        self.label4 = ttk.Label(self.subFrame4, text='Valor total:')
        self.label4.grid(row=20, column=2, sticky=E)

        # ABAIXO, SETANDO OS .bind():
        # .bind da Combobox:
        self.CBox1.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_CBox1())

        # .bind da treeView2:
        self.treeView1.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_treeView1())

        # .bind da treeView2:
        self.treeView2.treeView.bind('<<TreeviewSelect>>', lambda event: self.bind_treeView2())

        # .bind DA ENTRY3:
        self.entry3.entry.bind('<FocusIn>', lambda event: self.bind1_entry3())
        self.entry3.entry.bind('<KeyRelease>', lambda event: self.bind2_entry3())

        # .bind DA ENTRY4:
        self.entry4.entry.bind('<FocusIn>', lambda event: self.bind1_entry4())
        self.entry4.entry.bind('<KeyRelease>', lambda event: self.bind2_entry4())

        # .bind DA ENTRY1:
        self.entry1.entry.bind('<FocusIn>', lambda event: self.bind1_entry1())
        self.entry1.entry.bind('<KeyRelease>', lambda event: self.bind2_entry1())
        # .bind DA ENTRY2:
        self.entry2.entry.bind('<FocusIn>', lambda event: self.bind1_entry2())
        self.entry2.entry.bind('<KeyRelease>', lambda event: self.bind2_entry2())


    def bind_CBox1(self):
        tipo = self.CBox1.get_choice()
        self.entry2.config_Entry(state='enabled')
        self.entry3.config_Entry(state='enabled')
        self.entry4.config_Entry(state='enabled')
        if tipo == 'Item':
            self.treeView2.clear_treeView()
            self.treeView2.insert(self.lst_itens.to_treeView())
        else:
            self.treeView2.clear_treeView()
            self.treeView2.insert(self.lst_servs.to_treeView())

    def command_button1(self):
        self.entry6.insert_text(self.ref_compras.estab.nome)

    def command_button2(self):
        quant = self.entry3.get_text()
        preco_unit = self.entry4.get_text()
        preco_total = self.entry5.get_text()

        itemServ = c_itemServ_ref(itemServ=self.itemServ_sel, quant=quant, preco_unit=preco_unit,
                                  preco_total=preco_total)
        self.lst_compras.append(itemServ)
        self.treeView3.clear_treeView()
        self.treeView3.insert(self.lst_compras.to_treeView())

    def command_button3(self):
        pass

    def bind_treeView1(self):
        estab_id = self.treeView1.idd_selection_treeView()
        estab = self.lst_estabs[estab_id]
        self.ref_compras.estab = estab
        self.entry1.insert_text(estab.nome)
        # self.entry1.insert_text(estab.nome())

    def bind_treeView2(self):
        tipo = self.CBox1.get_choice()
        if tipo == 'Item':
            item_id = self.treeView2.idd_selection_treeView()
            self.itemServ_sel = self.lst_itens[item_id]
            self.entry2.insert_text(self.itemServ_sel.nome)
        else:
            serv_id = self.treeView2.idd_selection_treeView()
            self.itemServ_sel = self.lst_servs[serv_id]
            self.entry2.insert_text(self.itemServ_sel.nome)

    def bind1_entry1(self):
        self.entry1.limpa_entr()

    def bind2_entry1(self):
        # METODO DE BUSCA
        pass

    def bind1_entry2(self):
        self.entry2.limpa_entr()
        pass

    def bind2_entry2(self):
        # METODO DE BUSCA
        pass

    def bind1_entry3(self):
        self.entry3.limpa_entr()

    def bind1_entry4(self):
        self.entry4.limpa_entr()

    def bind2_entry3(self):
        quant = self.entry3.get_text()
        valor_unit = self.entry4.get_text()

        if quant is not '' and valor_unit is not '':
            try:
                quant = float(quant)
                valor_unit = float(valor_unit)
                valor_total = quant * valor_unit
                self.entry5.insert_text(str(valor_total))
            except:
                pass

    def bind2_entry4(self):
        quant = self.entry3.get_text()
        valor_unit = self.entry4.get_text()

        if quant is not '' and valor_unit is not '':
            try:
                quant = float(quant)
                valor_unit = float(valor_unit)
                valor_total = quant * valor_unit
                self.entry5.insert_text(str(valor_total))
            except:
                pass


class MenuColl(Frame):
    def __init__(self, frame_master, controller):
        # Bloco (2.1): Abaixo, é declarado o frame que conterá o menu. O frame está contido no frame-pai:
        super().__init__(frame_master)
        self.frameLocal = Frame(self, padx=2, pady=4)
        self.frameLocal.grid(row=0, column=0, sticky=N + S)
        self.controller = controller

        # Subtítulos do programa:
        # O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.tit1 = Label(self.frameLocal, text='pyMoney v0.01', font='Verdana', anchor=CENTER, relief=GROOVE, padx=3,
                          pady=3)
        self.tit1.grid(row=0, column=0, sticky=E + W, padx=3,
                       pady=3)  # , sticky = E+W)#Subtitulo fixado na origem do "frameLocal"(row=0, column=0)

        self.separadorV1 = ttk.Separator(self.frameLocal, orient=VERTICAL, style="TSeparator")
        self.separadorV1.grid(row=0, column=1, rowspan=13, sticky="ns", padx=2, pady=3)

        # O subtitulo3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.tit2 = Label(self.frameLocal, text="Carregue uma conta", font='Verdana', anchor=CENTER, relief=GROOVE,
                          padx=3, pady=3)
        self.tit2.grid(row=1, column=0, sticky=E + W, padx=3, pady=3)

        # O subtitulo4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.tit3 = Label(self.frameLocal, text="Menu", relief=FLAT, font='Verdana', anchor=CENTER)
        self.tit3.grid(row=2, column=0, sticky=E + W)

        # ttk.Style().configure("Toolbutton", relief = "ridge")
        # ttk.Style().configure('Toolbutton.label', 'sticky' = 'we')
        # ~ print(ttk.Style().layout('Toolbutton'))

        # O button1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        # A variável varRb guardará o valor dos Radiobuttons

        self.varRb = IntVar()
        self.Rb1 = ttk.Radiobutton(self.frameLocal, text="Status geral - Mês atual", value=1, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb1.grid(row=3, column=0, sticky=E + W, padx=3, pady=1)
        self.config_comando_Rb1(lambda: self.controller.show_frame('StatusGeralFrame'))

        # O  button2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb2 = ttk.Radiobutton(self.frameLocal, text="Status geral - Meses anteriores", value=2,
                                   variable=self.varRb, style='Toolbutton')
        self.Rb2.grid(row=4, column=0, sticky=E + W, padx=3, pady=1)
        # self.config_comando_Rb2(lambda: )

        # O  button3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb3 = ttk.Radiobutton(self.frameLocal, text="Análises/relatórios", value=3, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb3.grid(row=5, column=0, sticky=E + W, padx=3, pady=1)
        # self.config_comando_Rb3(lambda: )

        # O  button1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb4 = ttk.Radiobutton(self.frameLocal, text="Editar/inserir referente", value=4, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb4.grid(row=6, column=0, sticky=E + W, padx=3, pady=1)
        self.config_comando_Rb4(lambda: self.controller.show_frame('insere_refe_frame'))

        # O  botao5 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb5 = ttk.Radiobutton(self.frameLocal, text="Inserir movimentação", value=5, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb5.grid(row=7, column=0, sticky=E + W, padx=3, pady=1)
        self.config_comando_Rb5(lambda: self.controller.show_frame('ins_move_frame'))

        # O  botao6 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb6 = ttk.Radiobutton(self.frameLocal, text="Estoque de Itens", value=6, variable=self.varRb,
                                   style='Toolbutton', command = lambda: self.controller.show_frame('EstoqServFrame'))
        self.Rb6.grid(row=8, column=0, sticky=E + W, padx=3, pady=1)
        # self.config_comando_Rb6(lambda: )

        self.separadorH2 = ttk.Separator(self.frameLocal, orient=HORIZONTAL, style="TSeparator")
        self.separadorH2.grid(row=9, column=0, sticky="we", padx=4, pady=3)

        # O  botao7 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb7 = ttk.Radiobutton(self.frameLocal, text="Banco de itens/Serviços", value=7, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb7.grid(row=10, column=0, sticky=E + W, padx=3, pady=1)
        self.config_comando_Rb7(lambda: self.controller.show_frame('banco_itens_frame'))

        # O  botao8 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb8 = ttk.Radiobutton(self.frameLocal, text="Banco de fornecedores", value=8, variable=self.varRb,
                                   style='Toolbutton')
        self.Rb8.grid(row=11, column=0, sticky=E + W, padx=3, pady=1)
        self.config_comando_Rb8(lambda: self.controller.show_frame('FornecFrame'))

        # O  botao9 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb9 = ttk.Radiobutton(self.frameLocal, text="Banco de clientes", value=9, variable=self.varRb,
                                   style='Toolbutton', command = lambda: self.controller.show_frame('ClientesFrame'))
        self.Rb9.grid(row=12, column=0, sticky=E + W, padx=3, pady=1)

        # O  botao9 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb10 = ttk.Radiobutton(self.frameLocal, text="Banco de Estabelecimentos", value=10, variable=self.varRb,
                                   style='Toolbutton', command = lambda: self.controller.show_frame('EstabFrame'))
        self.Rb10.grid(row=13, column=0, sticky=E+W, padx=3, pady=1)

        # Abaixo, os botoões são desativados por padrão:
        self.desativa_todos_Rb()

    def desativa_todos_Rb(self):
        self.Rb1.config(state="disabled")
        self.Rb2.config(state="disabled")
        self.Rb3.config(state="disabled")
        self.Rb4.config(state="disabled")
        self.Rb5.config(state="disabled")
        self.Rb6.config(state="disabled")
        self.Rb7.config(state="disabled")
        self.Rb8.config(state="disabled")
        self.Rb9.config(state="disabled")
        self.Rb10.config(state="disabled")

    def ativa_todos_Rbs(self):
        self.Rb1.config(state="eneable")
        self.Rb2.config(state="eneable")
        self.Rb3.config(state="eneable")
        self.Rb4.config(state="eneable")
        self.Rb5.config(state="eneable")
        self.Rb6.config(state="eneable")
        self.Rb7.config(state="eneable")
        self.Rb8.config(state="eneable")
        self.Rb9.config(state="eneable")
        self.Rb10.config(state="eneable")


    def config_nome_tit1(self, titulo):
        self.tit1.config(text=titulo)

    def config_nome_tit2(self, titulo):
        self.tit2.config(text=titulo)

    def config_nome_tit3(self, titulo):
        self.tit3.config(text=titulo)

    def config_nome_Rb1(self, titulo):
        self.Rb1.config(text=titulo)

    def config_nome_Rb2(self, titulo):
        self.Rb2.config(text=titulo)

    def config_nome_Rb3(self, titulo):
        self.Rb3.config(text=titulo)

    def config_nome_Rb4(self, titulo):
        self.Rb4.config(text=titulo)

    def config_nome_Rb5(self, titulo):
        self.Rb5.config(text=titulo)

    def config_nome_Rb6(self, titulo):
        self.Rb6.config(text=titulo)

    def config_nome_Rb7(self, titulo):
        self.Rb7.config(text=titulo)

    def config_nome_Rb8(self, titulo):
        self.Rb8.config(text=titulo)

    def config_nome_Rb9(self, titulo):
        self.Rb9.config(text=titulo)

    def config_comando_Rb1(self, comando):
        self.Rb1.config(command=comando)

    def config_comando_Rb2(self, comando):
        self.Rb2.config(command=comando)

    def config_comando_Rb3(self, comando):
        self.Rb3.config(command=comando)

    def config_comando_Rb4(self, comando):
        self.Rb4.config(command=comando)

    def config_comando_Rb5(self, comando):
        self.Rb5.config(command=comando)

    def config_comando_Rb6(self, comando):
        self.Rb6.config(command=comando)

    def config_comando_Rb7(self, comando):
        self.Rb7.config(command=comando)

    def config_comando_Rb8(self, comando):
        self.Rb8.config(command=comando)

    def config_comando_Rb9(self, comando):
        self.Rb9.config(command=comando)

    def pointer_frameLocal(self):
        return (self.frameLocal)

    def grid_frame(self):
        self.frameLocal.grid(row=0, column=0, sticky=N + S + W + E)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def escolha_Rb(self):
        escolha = self.varRb.get()
        return (escolha)

    def finaliza(self):
        self.frameLocal.destroy()


class MainWindow(Frame):
    def __init__(self, master, controller):
        # Bloco (1) Configurando frame principal(janela-pai):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.master.configure(background="#b2b2b2")
        # Comando abaixo configura a resoluação padrão da janela como sendo a resolução do PC em questão:
        # self.master.geometry("{}x{}".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # self.master.geometry("900x400")
        # Comando abaixo configura a janela para iniciar como "maximizada":
        self.master.state('zoomed')
        # Comando abaixo configura o título da janela:
        self.master.title('pyMoney')
        # Comando abaixo printa no terminal a resolução configurada para a máquina em questão:
        # ~ print(self.master.winfo_screenwidth(), self.master.winfo_screenheight())

        # Abaixo é declarada a janela-pai
        # self.scroll_win = ScrolledWindow(self.master)#, relief = GROOVE, padx = 10, pady = 4)

        # self.framePai = self.scroll_win.scrollwindow
        self.framePai = self
        self.framePai.grid()
        # self.framePai = master
        #
        # Fim do Bloco (1)
        # ------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        # ------------------------------------------------------------------------------------------------------------------#

        # Bloco (2) Declaração do menu superior da janela-pai:
        self.menuSuperior = Menu(self.master)
        self.master.config(menu=self.menuSuperior)

        # Abaixo a declaração e as Sub-opções dentro da opção "Arquivo":
        self.menuArquivo = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuArquivo, label='Arquivo')
        # Sub-opções dentro da opção "Arquivo":
        self.menuArquivo.add_command(label="Trocar gerência", command=self.troca_ger)
        # Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuArquivo.add_separator()  # Esse comando adciona um layout de separação entre as opções do menu

        # Abaixo a declaração e as Sub-opções dentro da opção "Configurações":
        self.menuConfiguracoes = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuConfiguracoes, label='Ferramentas')
        # Sub-opções dentro da opção "Configurações":,
        self.menuConfiguracoes.add_command(label="Configurações")
        self.menuConfiguracoes.add_command(label="Configurar gerência atual", command=self.config_ger)
        self.menuConfiguracoes.add_command(label="Configurar contas cadastradas", command=self.config_conta)
        self.menuConfiguracoes.add_command(label="Cadastrar nova conta", command=self.ins_conta)
        # Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuConfiguracoes.add_separator()

        # Abaixo a declaração e as Sub-opções dentro da opção "Ajuda":
        self.menuAjuda = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuAjuda, label='Ajuda')
        # Sub-opções dentro da opção "Ajuda":
        self.menuAjuda.add_command(label="Tutorial")
        self.menuAjuda.add_command(label="Sobre")
        # Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuAjuda.add_separator()

        # Comando que exibe o menu:
        # master.config(menu=self.menuSuperior)

        # Fim do bloco (2)
        # ------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        # ------------------------------------------------------------------------------------------------------------------#

        # Bloco (3) Declarando sub-frames da janela-pai:
        '''A janela-pai está dividida em três sub-frames, lateral esquerdo, central, lateral direito, e um sub-frame de rodapé.
                Na presente classe, cada um dos três sub-frames não admite sub-divisões, sendo containeres.
                Sendo assim, adimitindo o maior grau de divisão de frames na classe, a janela-pai terá a seguinte divisão:

                ______________________________janela-pai______________________________
                |(subFrameLateralEsquerdo)|(subFrameCentral)|(subFrameLateralDireito)|
                |							subFrameInferior-rodapé						 |

        '''

        # Bloco (3.1): Abaixo, é declarado o frame lateral esquerdo. O frame está contido no frame-pai:
        self.frame_esquerdo = Frame(self.framePai, padx="4", pady="4")
        self.frame_esquerdo.grid(row=0, column=0, sticky=N + S)
        self.sideMenu = MenuColl(self.frame_esquerdo, self.controller)
        self.sideMenu.grid()

        # Bloco (3.3): Abaixo, é declarado o frame central. O frame está contido no frame-pai:
        self.main_frame = Frame(self.framePai)  # , padx ="4", pady = "4")
        self.main_frame.grid(row=0, column=1)  # , sticky = N+S+W+E)

        # Bloco (3.4): Abaixo, é declarado o frame lateral direito. O frame está contido no frame-pai:
        # self.frame_direito = Frame(self.framePai, padx ="4", pady = "4")
        # self.frame_direito.grid(row = 0, column = 2, sticky = N+S)

        # Bloco (3.5): Abaixo, é declarado o frame inferior no rodapé da do frame-pai(note o columnspan = 3):
        # self.frame_infe = Frame(self.framePai, padx ="4")
        # self.frame_infe.grid(row = 1, column = 0, columnspan = 3, sticky = W+E)

    def pointer_frame_esq(self):
        return (self.frame_esquerdo)

    def pointer_frame_cent(self):
        return (self.main_frame)

    def pointer_frame_master(self):
        return (self.master)

    def load_file_txt(self):
        # A rotina abaixo abre o .txt, retornando um string, tratando eventuais erros com o encode:
        def tryOpen(filename):
            try:
                arq = open(filename, 'r', encoding='utf-8')
            except (UnicodeDecodeError, UnicodeEncodeError):  # Aqui a função trata erros de enconding
                try:
                    print('\n*** Observação: UnicodeDecodeError, tentando encoding = charmap ***')
                    arq = open(filename, 'r', encoding='charmap')
                except (UnicodeDecodeError, UnicodeEncodeError):
                    try:
                        print('\n*** Observação: UnicodeDecodeError, tentando encoding = CP-1252 ***')
                        arq = open(filename, 'r', encoding='cp1252')
                    except (UnicodeDecodeError, UnicodeEncodeError):
                        print('\n*** Atenção, não foi possível carregar o texto:', arqtxt, 'por erros no encoding ***')
                        arq.close()
            string = arq.read()
            arq.close()
            return (string)

        filename = filedialog.askopenfilename()
        print("\n" + filename)
        string = tryOpen(filename)

        # Abaixo, vamos extrair o nome do texto carregador:
        listaux = filename.split('/')
        nomeTxt = listaux[len(listaux) - 1]

        return (string, nomeTxt)

    def troca_ger(self):
        escolha = askyesno('Trocar gerência', 'Deseja trocar a gerência atual?')
        if escolha is True:
            self.controller.show_frame('MenuInic')

    def config_ger(self):
        self.controller.show_frame('AlteraGerFrame')

    def config_conta(self):
        self.controller.show_frame('AlteraContaFrame')

    def ins_conta(self):
        self.controller.show_frame('InsConta')

    def destroi_framesFilhos(self, frame):
        if frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].destroy()
                cont = cont + 1
        else:
            return None

    def ungrid_framesFilhos(self, frame):
        if frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].grid_forget()
                cont = cont + 1
        else:
            return None

    def ungrid_framesFilhos_cent(self):
        self.ungrid_framesFilhos(self.main_frame)

    def destroi_framesFilhos_cent(self):
        self.destroi_framesFilhos(self.main_frame)

    def ungrid_framesFilhos_esqr(self):
        self.ungrid_framesFilhos(self.frame_esquerdo)

    def lst_framesFilhos_cent(self):
        return (self.main_frame.winfo_children())