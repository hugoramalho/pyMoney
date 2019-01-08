from .widgetsProg.wd_frames import *
from pyMoney.modelsProg.models import enderecoIdent, Estab, CategEstab


class EnderFrame(Frame):
    def __init__(self, frameMaster, controller, ender: enderecoIdent = None):
        super().__init__(frameMaster)
        self.controller = controller
        if ender is None:
            self.__ender = enderecoIdent()
            self.build_frame()
        else:
            self.__ender = ender
            self.build_frame()
            self.set_ender(self.__ender)

    def build_frame(self):
        self.frame_ender = LabelFrame(self, text='Endereço')  # , relief = FLAT)
        self.frame_ender.grid(row=2, column=0, sticky=W, ipadx=10, ipady=10, padx=10, pady=10)

        self.lst_estados = self.controller.load_UF()
        self.estado_CBox = wd_CBox(self.frame_ender, tit_CBox='Estado', set_CBox_default='Estado',
                                   CBox_values=self.lst_estados, width=21, CBox_state='readonly')
        self.estado_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_estado_CBox())
        self.estado_CBox.grid(row=0, column=0, padx=5, sticky=W + E, columnspan=2)

        self.cidade_CBox = wd_CBox(self.frame_ender, tit_CBox='Cidade:', set_CBox_default='Cidade',
                                   CBox_state='disabled', width=21)
        self.cidade_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_cidade_CBox())
        self.cidade_CBox.grid(row=0, column=2, padx=5, sticky=W + E)

        self.bairro_CBox = wd_CBox(self.frame_ender, tit_CBox='Bairro:', set_CBox_default='Bairro', width=21,
                                   CBox_state='disabled')
        self.bairro_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_bairro_CBox())
        self.bairro_CBox.grid(row=0, column=3, padx=5, sticky=W, columnspan=3)

        self.cep_entr = wd_Entry(self.frame_ender, width=10, label='CEP:')
        self.cep_entr.grid_frame(row=1, column=0, padx=5, sticky=W + E)

        self.buscaCep_button = ttk.Button(self.frame_ender, text='Buscar CEP', command=self.buscaCep)
        self.buscaCep_button.grid(row=1, column=1, padx=5, sticky=W + E + S)

        self.lograd_entr = wd_Entry(self.frame_ender, width=24, label='Logradouro:')
        self.lograd_entr.grid_frame(row=1, column=2, padx=5, sticky=W, columnspan=2)

        self.numero_entr = wd_Entry(self.frame_ender, width=7, label='Número:')
        self.numero_entr.grid_frame(row=1, column=3, padx=5, sticky=W + E)

        self.numApart_entr = wd_Entry(self.frame_ender, width=7, label='Nº apart/sala/loja:', state_Entry='disabled')
        self.numApart_entr.grid_frame(row=1, column=4, padx=5)

        self.bloco_entr = wd_Entry(self.frame_ender, width=7, label='Bloco (Se houver):', state_Entry='disabled')
        self.bloco_entr.grid_frame(row=1, column=5, padx=5)

        self.tipoRes_CBox = wd_CBox(self.frame_ender, tit_CBox='Tipo:', set_CBox_default='Casa',
                                    CBox_values=["Casa", "Apartamento", "Estabelecimento", "Sala", 'Loja'], width=21, CBox_state='readonly')
        self.tipoRes_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_tipoRes_CBox())
        self.tipoRes_CBox.grid(row=2, column=0, padx=5, sticky=W + E, columnspan=2)

        self.nomeCond_entr = wd_Entry(self.frame_ender, width=24, label='Nome do edifício/condomínio:',
                                      state_Entry='disabled')
        self.nomeCond_entr.grid_frame(row=2, column=2, padx=5)

        self.refe_entr = wd_Entry(self.frame_ender, width=24, label='Complemento/Referência:')
        self.refe_entr.grid_frame(row=2, column=3, padx=5, columnspan=2)

        self.bind_tipoRes_CBox()

    def wd_state(self, state):
        self.estado_CBox.CBox.config(state = state, values = self.lst_estados)
        self.estado_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_estado_CBox())

        self.cidade_CBox.CBox.config(state=state)
        self.cidade_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_cidade_CBox())

        self.bairro_CBox.CBox.config(state=state)
        self.bairro_CBox.CBox.bind('<<ComboboxSelected>>', lambda event: self.bind_bairro_CBox())

        self.cep_entr.entry.config(state=state)

        self.buscaCep_button.config(state=state)

        self.lograd_entr.entry.config(state=state)

        self.numero_entr.entry.config(state=state)

        self.numApart_entr.entry.config(state=state)

        self.bloco_entr.entry.config(state=state)

        self.tipoRes_CBox.CBox.config( state=state, values=["Casa", "Apartamento", "Sala"])

        self.nomeCond_entr.entry.config(state=state)

        self.refe_entr.entry.config(state=state)
        self.bind_tipoRes_CBox()

    def __fill_ender__(self):
        self.__ender.cep = self.cep_entr.get_text()
        self.__ender.estado = self.estado_CBox.get_choice()
        self.__ender.cidade = self.cidade_CBox.get_choice()
        self.__ender.bairro = self.bairro_CBox.get_choice()
        self.__ender.logradouro = self.lograd_entr.get_text()
        self.__ender.numero = self.numero_entr.get_text()
        self.__ender.num_apart = self.numApart_entr.get_text()
        self.__ender.bloco = self.bloco_entr.get_text()
        self.__ender.tipo_resid = self.tipoRes_CBox.get_choice()
        self.__ender.edificio = self.nomeCond_entr.get_text()
        self.__ender.referencia = self.refe_entr.get_text()

    def __fill_frame__(self):
        self.cep_entr.insert_text(self.__ender.cep)
        self.estado_CBox.set_CBox_default(self.__ender.estado)
        self.cidade_CBox.set_CBox_default(self.__ender.cidade)
        self.bairro_CBox.set_CBox_default(self.__ender.bairro)
        self.lograd_entr.insert_text(self.__ender.logradouro)
        self.numero_entr.insert_text(self.__ender.numero)
        self.numApart_entr.insert_text(self.__ender.num_apart)
        self.bloco_entr.insert_text(self.__ender.bloco)
        self.tipoRes_CBox.set_CBox_default(self.__ender.tipo_resid)
        self.nomeCond_entr.insert_text(self.__ender.edificio)
        self.refe_entr.insert_text(self.__ender.referencia)

    def wd_config(self, **kwargs):
        state = kwargs.get('state', 'enabled')
        state_cbox = state
        if state != 'enabled':
            state_cbox = 'disabled'

        self.cep_entr.entry.config(state=state)
        self.estado_CBox.CBox.config(state=state_cbox)
        self.cidade_CBox.CBox.config(state=state_cbox)
        self.bairro_CBox.CBox.config(state=state_cbox)
        self.lograd_entr.entry.config(state=state)
        self.numero_entr.entry.config(state=state)
        self.numApart_entr.entry.config(state=state)
        self.bloco_entr.entry.config(state=state)
        self.tipoRes_CBox.CBox.config(state=state_cbox)
        self.nomeCond_entr.entry.config(state=state)
        self.refe_entr.entry.config(state=state)

    def get_ender(self):
        self.__fill_ender__()
        return self.__ender


    def set_ender(self, ender:enderecoIdent):
        if isinstance(ender, enderecoIdent) is False:
            raise Exception('Precisa ser um __tipo enderecoIdent')
        else:
            self.__ender = ender
            self.__fill_frame__()

    @property
    def cep(self):
        return self.cep_entr.get_text()

    @cep.setter
    def cep(self, cep):
        self.cep_entr.insert_text(cep)

    @property
    def numApart(self):
        return self.cep_entr.get_text()

    @numApart.setter
    def numApart(self, numApart):
        self.numApart_entr.insert_text(numApart)

    def buscaCep(self):
        cep = self.cep_entr.get_text()
        cep = cep.replace('-', '')
        cep = cep.replace(' ', '')
        cep = cep.replace(';', '')
        cep = cep.replace(',', '')
        cep = cep.replace('.', '')
        self.cep_entr.insert_text(cep)
        ender = self.controller.search_CEP(cep)
        if ender is not None:
            self.lograd_entr.insert_text(ender.tipo_logra + ' ' + ender.logradouro)
            self.bairro_CBox.set_CBox_default(ender.bairro)
            self.bairro_CBox.CBox.config(values=[], state='readonly')
            self.estado_CBox.set_CBox_default(ender.estado)
            self.cidade_CBox.set_CBox_default(ender.cidade)
            self.cidade_CBox.CBox.config(values=[], state='readonly')
        else:
            self.cep_entr.limpa_entr()
            self.lograd_entr.insert_text('CEP não encontrado!')

    def bind_tipoRes_CBox(self):
        tipo_res = self.tipoRes_CBox.get_choice()
        if tipo_res == 'Sala' or tipo_res == 'Apartamento' or tipo_res == 'Loja':
            self.nomeCond_entr.entry.config(state='enabled')
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
        # self.ender_estab.bairro = self.bairro_CBox.get_choice()
        pass

    def bind_cidade_CBox(self):
        # self.ender_estab.cidade = self.cidade_CBox.get_choice()
        lst_bairros = self.controller.load_BAIRROS(self.cidade_CBox.get_choice())
        self.bairro_CBox.config_CBox_state('readonly')
        self.bairro_CBox.define_values_CBox(lst_bairros)

    def bind_estado_CBox(self):
        # self.ender_estab.estado = self.estado_CBox.get_choice()
        lst_cidades = self.controller.load_CIDADES(self.estado_CBox.get_choice())
        self.cidade_CBox.config_CBox_state('readonly')
        self.cidade_CBox.define_values_CBox(lst_cidades)


class EscolhaEstabFrame(Frame):
    def __init__(self, frameMaster, controller):
        super().__init__(frameMaster)
        self.grid()
        self.controller = controller
        self.lst_estab = self.controller.loadAll_model(Estab())
        self.lst_tipoEstab = self.controller.loadAll_model(CategEstab())
        self.estab_sel = Estab()

        self.nomeEstab_cbox = wd_CBox(self, tit_CBox='Selecione o estabelecimento/identificação:', set_CBox_default='Escolha a opção', CBox_values = self.lst_estab.to_comboBox(), width= 40)
        self.nomeEstab_cbox.CBox.bind('<<ComboboxSelected>>', lambda event: self.__setEstab__())
        self.nomeEstab_cbox.CBox.bind('<KeyRelease>', lambda event: self.__buscaEstab__())
        self.nomeEstab_cbox.grid(row=0, column=0, sticky='W')

        self.tipoEstab_Cbox = wd_CBox(self, CBox_values=self.lst_tipoEstab, CBox_state='disabled', tit_CBox= 'Filtrar por categoria')
        self.tipoEstab_Cbox.CBox.bind('<<ComboboxSelected>>', lambda event: self.__filtraEstab__())
        self.tipoEstab_Cbox.grid(row=0, column=1, sticky='w', padx=5)

    def __filtraEstab__(self):
        tipo = self.tipoEstab_Cbox.get_choice()
        self.lst_estab = self.controller.search_tipo_estab(tipo)
        self.nomeEstab_cbox.define_values_CBox(self.lst_estab)

    def __setEstab__(self):
        pass

    def __buscaEstab__(self):
        pass

    def get_estab(self):
        nome_estab = self.nomeEstab_cbox.get_choice()
        estab_sel = self.lst_estab.search_name(nome_estab)
        return estab_sel