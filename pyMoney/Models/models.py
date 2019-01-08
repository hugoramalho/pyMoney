from datetime import *


class Categ:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')

    def update(self, **kwargs):
        self.nome = kwargs.get('nome', self.nome)

    def __str__(self):
        return str(self.__dict__)

    def to_comboBox(self):
        return self.nome

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = []
        return dic_treeView


class CategEstab(Categ):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SubCateg:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')
        self.categ = kwargs.get('categ', Categ())


    def update(self, **kwargs):
        self.nome = kwargs.get('nome', self.nome)
        self.categ = kwargs.get('categ', self.categ)

    def __str__(self):
        return str(self.__dict__)


class Especie:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')
        self.subCateg = kwargs.get('subCateg', SubCateg())


    def update(self, **kwargs):
        self.subCateg = kwargs.get('Subcateg', self.subCateg)
        self.nome = kwargs.get('nome', self.nome)

    @property
    def categ(self):
        return self.subCateg.categ

    @property
    def subCateg(self):
        return self.subCateg

    @property
    def categ(self):
        return self.subCateg.categ


    @subCateg.setter
    def subCateg(self, sub_categ):
        if isinstance(sub_categ, SubCateg):
            self.subCateg = sub_categ
        else:
            raise Exception('Bad interface! Class: ', self.__class__.__name__)

    def __str__(self):
        return str(self.__dict__)


class itemServ:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')
        self.codigo = kwargs.get('codigo', None)

        self.especie = kwargs.get('especie', None)

        self.descr = kwargs.get('descr', '')
        self.tipo = kwargs.get('__tipo', '')

    def __str__(self):
        return str(self.__dict__)

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.codigo]  # , self.categ, self.subCateg, self.especie]
        return dic_treeView


class item(itemServ):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = 'Item'
        self.quant = kwargs.get('quant', 0)

    def to_treeView(self):
        dic_treeView = super().to_treeView()
        dic_treeView['values'] = [self.codigo, self.quant]  # , self.categ, self.subCateg, self.especie]
        return dic_treeView


class serv(itemServ):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = 'Serviço'


class itemVenda:
    def __init__(self, **kwargs):
        self.item = kwargs.get('item', itemEstoque())
        self.idd = self.item.idd
        self.quant = kwargs.get('quant')
        self.valor_unit = kwargs.get('valor_unit')
        #self.valor_total = self.valor_unit*self.quant
        self.__verf_quant__()

    def verf_quant(self, quant_in):
        return self.item.verf_quant(self.quant)

    def __verf_quant__(self):
        if self.item.verf_quant(self.quant) is False:
            raise Exception('Produto indisponível em estoque!')

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.item.idd
        dic_treeView['text'] = self.item.nome
        dic_treeView['values'] = [self.quant]
        return dic_treeView

    def __str__(self):
        return str(self.__dict__)


class ItemServCompra:
    #idd_aux = 1
    def __init__(self, **kwargs):

        self.itemServ = kwargs.get('item', itemServ())
        self.tipo = self.itemServ.tipo

        self.idd = self.__setIdd__(kwargs.get('idd', None))

        #if self.idd is None:
        #self.idd = self.__class__.idd_aux
            #self.__class__.increment_idd()


        self._quant = kwargs.get('quant', 0)
        self.__valor_unit = kwargs.get('valor_unit', 0)

        self.__valor_total = self._quant * self.__valor_unit

    def __setIdd__(self, idd):
        if idd is None:
            self.idd = self.itemServ.idd

    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, quant_in):
        try:
            quant_in = float(quant_in)
            self._quant = quant_in
            self.__valor_total = self._quant*self.__valor_unit
        except Exception as Expt:
            print(Expt)

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def valor_unit(self):
        return self.__valor_unit

    @valor_unit.setter
    def valor_unit(self, valor):
        try:
            valor = float(valor)
            self.__valor_unit = valor
            self.__valor_total = self._quant*self.__valor_unit
        except Exception as Expt:
            print(Expt)

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.itemServ.idd
        dic_treeView['text'] = self.itemServ.nome
        dic_treeView['values'] = [self._quant, self.__valor_unit, self.__valor_total]
        return dic_treeView

    @classmethod
    def increment_idd(cls):
        cls.idd_aux = cls.idd_aux+1

    def __str__(self):
        return str(self.__dict__)


class venda:
    def __init__(self, **kwargs):
        self.lst_itens = kwargs.get('lst_itens', MyCollection())
        self.valor_total = kwargs.get('valor_total')
        self.cliente = kwargs.get('cliente', cliente())


    def __str__(self):
        return str(self.__dict__)


class endereco:
    def __init__(self, **kwargs):
        self.cep = kwargs.get('cep', 'Não Informado')
        self.logradouro = kwargs.get('logradouro', 'Não Informado')
        self.tipo_logra = kwargs.get('__tipo', 'Não Informado')

        self.bairro = kwargs.get('bairro', 'Não Informado')
        self.id_bairro = kwargs.get('id_bairro', None)

        self.cidade = kwargs.get('cidade', 'Não Informado')
        self.id_cidade = kwargs.get('id_cidade', None)

        self.estado = kwargs.get('estado', 'Não Informado')
        self.uf = kwargs.get('uf', 'Não Informado')
        self.id_estado = kwargs.get('id_estado', None)
        self.pais = kwargs.get('pais', 'Não Informado')

    def update(self, **kwargs):
        self.cep = kwargs.get('cep', self.cep)
        self.logradouro = kwargs.get('logradouro', self.logradouro)
        self.tipo_logra = kwargs.get('__tipo', self.tipo_logra)

        self.bairro = kwargs.get('bairro', self.bairro)
        self.id_bairro = kwargs.get('id_bairro', self.id_bairro)

        self.cidade = kwargs.get('cidade', self.cidade)
        self.id_cidade = kwargs.get('id_cidade', self.id_cidade)

        self.estado = kwargs.get('estado', self.estado)
        self.uf = kwargs.get('uf', self.uf)
        self.id_estado = kwargs.get('id_estado', self.id_estado)
        self.pais = kwargs.get('pais', self.pais)

    def to_db(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)


class enderecoIdent(endereco):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.idd = kwargs.get('idd')
        self.numero = kwargs.get('numero', '')
        self.tipo_resid = kwargs.get('tipo_resid', '')
        self.num_apart = kwargs.get('num_apart', '')
        self.bloco = kwargs.get('bloco', '')
        self.referencia = kwargs.get('referencia', '')
        self.edificio = kwargs.get('edificio', '')
        self.num_sala = kwargs.get('num_sala', '')

    def update(self, **kwargs):
        super().update(**kwargs)
        self.numero = kwargs.get('numero', self.numero)
        self.tipo_resid = kwargs.get('tipo_resid', self.tipo_resid)
        self.num_apart = kwargs.get('num_apart', self.num_apart)
        self.bloco = kwargs.get('bloco', self.bloco)
        self.referencia = kwargs.get('referencia', self.referencia)
        self.edificio = kwargs.get('edificio', self.edificio)
        self.num_sala = kwargs.get('num_sala', self.num_sala)


class conta_credito:
    def __init__(self):
        self.nome_gest = ''
        self.anuidade = 0
        self.saldo = 0
        self.bandeira = ''
        self.lst_transac = lst_transac()


class CartaoCredito:
    def __init__(self):
        self.idd = None
        self.id_ger = None
        self.nome = ''
        self.anuidade = 0
        self.data_fechamento = None
        self.limite = 0
        self.bandeira = ''
        self.fatura_atual = None
        self.prox_fatura = None
        self.fatura_anterior = None
        self.saldoCredito = 0
        self.saldo = 0

    def efetuaPagamento(self, valor_pago):
        valor_restante = self.fatura_atual.efetuaPagamento()
        self.saldo = self.saldo + valor_restante


class FaturaCredito:
    def __init__(self):
        self.idd = None
        self.status = ''
        self.dataInic = None
        self.dataFin = None
        self.rangeDate = (self.dataInic, self.dataFin)
        self.valor_total = 0
        self.valor_pago = 0
        self.lst_compras = None


class transac_extrato:
    def __init__(self):
        self.idd = None
        self.data = None
        self.conta_fav = c_conta()
        self.conta_ced = c_conta()
        self.tipo = 'Transação sem __tipo'
        self.valor = 0

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = str(self.data)
        dic_treeView['values'] = [self.valor, self.tipo]
        return dic_treeView

    def __str__(self):
        return str(self.__dict__)


class transac:
    def __init__(self):
        self.idd = None
        self._data = None
        self.conta_fav = c_conta()
        self.conta_ced = c_conta()
        self.valor = 0
        self.tipo = 'Transação sem __tipo'

        self.__ultimo_valor__ = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: date):
        self._data = MyDate()
        self._data.data = data

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = str(self._data)
        dic_treeView['values'] = [self.valor, self.tipo]
        return dic_treeView

    def efetiva(self):
        self.__ultimo_valor__ = self.valor
        valor_out = -1*self.valor
        self.conta_ced.move(valor_out)
        self.conta_fav.move(self.valor)

    def desEfetivar(self):
        valor_out = -1*self.__ultimo_valor__
        self.conta_fav.move(valor_out)
        self.conta_ced.move(self.__ultimo_valor__)

    def __eq__(self, obj):
        return (self._data == obj.data)

    def __ne__(self, obj):
        return (self._data != obj.data)

    def __lt__(self, obj):
        return (self._data < obj.data)

    def __le__(self, obj):
        return (self._data <= obj.data)

    def __gt__(self, obj):
        return (self._data > obj.data)

    def __ge__(self, obj):
        return (self._data >= obj.data)

    def __str__(self):
        return str(self.__dict__)


class contato:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd')
        self.tel1 = kwargs.get('tel1', 'Não informado')
        self.tel2 = kwargs.get('tel2', 'Não informado')

        self.cel1 = kwargs.get('cel1', 'Não informado')
        self.cel2 = kwargs.get('cel2', 'Não informado')

        self.email1 = kwargs.get('email1', 'Não informado')
        self.email2 = kwargs.get('email2', 'Não informado')

    def __str__(self):
        return str(self.__dict__)

    def to_db(self):
        return self.__dict__


class ident:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd')
        self.id_ger = kwargs.get('id_ger', '')
        self.lst_contas = kwargs.get('lst_contas')
        self.nome = kwargs.get('nome', '')
        self.tipo_pessoa = kwargs.get('tipo_pessoa', '')
        self.ender = kwargs.get('ender', enderecoIdent())
        self.contato = kwargs.get('contato', contato())
        self.descr = kwargs.get('descr', '')

    def update(self, **kwargs):
        self.lst_contas = kwargs.get('lst_contas', self.lst_contas)
        self.nome = kwargs.get('nome', self.nome)
        self.tipo_pessoa = kwargs.get('tipo_pessoa', self.tipo_pessoa)
        self.contato = kwargs.get('contato', self.contato)
        self.descr = kwargs.get('descr', self.descr)
        self.ender = kwargs.get('ender', self.ender)

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = []
        return dic_treeView

    @property
    def cel1(self):
        return self.contato.cel1

    @property
    def cel2(self):
        return self.contato.cel2

    @property
    def tel1(self):
        return self.contato.tel1

    @property
    def tel2(self):
        return self.contato.tel2

    @property
    def email1(self):
        return self.contato.email1

    @property
    def email2(self):
        return self.contato.email2

    @property
    def cidade(self):
        return self.ender.cidade

    @property
    def estado(self):
        return self.ender.estado

    @property
    def uf(self):
        return self.ender.uf

    @property
    def cep(self):
        return self.ender.cep

    @property
    def numero(self):
        return self.ender.numero

    @property
    def tipo_resid(self):
        return self.ender.tipo_resid

    @property
    def num_apart(self):
        return self.ender.num_apart

    @property
    def bloco(self):
        return self.ender.bloco

    @property
    def referencia(self):
        return self.ender.referencia

    @property
    def edificio(self):
        return self.ender.edificio

    @property
    def num_sala(self):
        return self.ender.num_sala

    @property
    def logradouro(self):
        return self.ender.logradouro

    @property
    def tipo_logra(self):
        return self.ender.tipo_logra

    @property
    def bairro(self):
        return self.ender.bairro

    @property
    def referencia(self):
        return self.ender.referencia

    def to_db(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)


class fornec(ident):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cnpj = kwargs.get('cnpj', '')
        # Razão social:
        self.raz_soc = kwargs.get('raz_soc', '')
        self.ramo = kwargs.get('ramo', '')

    def update(self, **kwargs):
        super().update(**kwargs)
        self.cnpj = kwargs.get('cnpj', self.cnpj)
        self.raz_soc = kwargs.get('raz_soc', self.raz_soc)

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.ramo, self.tel1, self.email1, self.cidade]
        return dic_treeView


class Estab(ident):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.categ = kwargs.get('categ', CategEstab())
        self.ramo = self.categ
        #self.conta_generica = kwargs.get('conta', c_conta(nome = 'Conta genérica do estabelecimento '+self.nome))
        self.conta_generica = c_conta(nome='Conta abstrata')

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.categ.nome, self.cidade, self.bairro, self.tel1]
        return dic_treeView

    def to_comboBox(self):
        return self.nome


class cliente(ident):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cpf = kwargs.get('cpf')
        self.rg = kwargs.get('rg')
        self.genero = kwargs.get('genero')

        try:
            print(kwargs.get('dataNasc'))
            self.dataNasc = datetime.strptime(kwargs.get('dataNasc'), '%Y-%m-%d')
            # print('a data de nascimento:', self.dataNasc)
        except Exception as Expt:
            print('Caiu aqui')
            print(Expt)
            self.dataNasc = datetime.strptime('0001-01-01', '%Y-%m-%d')

    def update(self, **kwargs):
        super().update(**kwargs)
        self.cpf = kwargs.get('cpf', self.cpf)
        self.rg = kwargs.get('rg', self.rg)
        self.ender = kwargs.get('ender', self.ender)
        self.genero = kwargs.get('genero', self.genero)
        self.dataNasc = kwargs.get('dataNasc', self.dataNasc)

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.cel1, self.tel1, self.email1, self.cidade]
        return dic_treeView


class gerencia:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.tipo = kwargs.get('__tipo', None)
        self.nome_ger = kwargs.get('nome_ger', '')
        self.nome_gest = kwargs.get('nome_gest', '')
        self.lst_contas = kwargs.get('lst_contas', None)
        self.descr = kwargs.get('descr', '')

    def update(self, **kwargs):
        self.tipo = kwargs.get('__tipo', self.tipo)
        self.nome_ger = kwargs.get('nome_ger', '')
        self.nome_gest = kwargs.get('nome_gest', '')
        self.descr = kwargs.get('descr', '')
        self.lst_contas = kwargs.get('lst_contas', None)

    def __str__(self):
        return str(self.__dict__)

    def to_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome_ger
        dic_treeView['values'] = [self.nome_gest]
        return dic_treeView

    def to_db(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'gerencia'
        dic_cadastro['nome_ger'] = self.nome_ger
        dic_cadastro['nome_gest'] = self.nome_gest
        dic_cadastro['lst_contas'] = self.lst_contas.to_db()
        dic_cadastro['descr'] = self.descr
        return (dic_cadastro)


class c_conta:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.id_ger = kwargs.get('id_ger', None)
        self.agencia = kwargs.get('agencia', '')
        self.numero = kwargs.get('numero', '')
        self.cod_banco = kwargs.get('cod_banco', '')
        self.nome = kwargs.get('nome', 'Conta não declarada')
        self._saldo = self.__set_saldo__(kwargs.get('saldo', 0))
        self.tipo = kwargs.get('tipo', 'abstrata')
        self.taxa_mensal = kwargs.get('taxa_mensal', 0)
        self.extrato = kwargs.get('extrato', [])

        if self.extrato is not []:
            lst_aux = []
            for elem in self.extrato:
                pass
            self.extrato = lst_aux

    def __set_saldo__(self, saldo):
        #self.saldo = float(saldo)
        self.saldo = round(float(saldo), 2)

    def __str__(self):
        return str(self.__dict__)

    def move(self, valor):
        self.saldo = self.saldo + valor


    def update(self, **kwargs):
        self.id_ger = kwargs.get('id_ger', self.id_ger)
        self.nome = kwargs.get('nome', self.nome)
        self.saldo = kwargs.get('saldo', self.saldo)
        self.tipo = kwargs.get('__tipo', self.tipo)
        self.taxa_mensal = kwargs.get('taxa_mensal', 0)
        self.extrato = kwargs.get('extrato', self.extrato)


    def to_treeView(self, **kwargs):
        tipo = kwargs.get('__tipo', '')

        dic_treeView = {}
        if tipo == '':
            dic_treeView['idd'] = self.idd
            dic_treeView['text'] = self.nome
            dic_treeView['values'] = [self.tipo, self.saldo]
            return (dic_treeView)

        elif tipo == 'extrato':
            lst = []
            for elem in self.extrato:
                dic_treeView = elem.to_treeView()
                lst.append(dic_treeView)
            return lst

    def to_comboBox(self):
        return self.nome


    def append_move(self, move):
        # TODO LEMBRAR DE VERIFICAR INSTANCIA
        self.extrato.append(move)

    def m_idd(self):
        return self.idd

    def m_nome(self):
        return self.nome

    def m_tipo(self):
        return self.nome

    def m_saldo(self):
        return self.saldo

    def m_id_ger(self):
        return self.id_ger

    def m_tax_mens(self):
        return self.taxa_mensal

    def m_retorna_tipo(self):
        return self.tipo

    def m_retorna_nome(self):
        return self.nome

    def m_retorna_saldo(self):
        return self.saldo


class CompraItemServ(transac):
    def __init__(self, **kwargs):
        super().__init__()
        self.tipo = 'compra de itens/serviços'
        self.__estab = self.__set_estab__(kwargs.get('estab', Estab()))
        self.compras_list = kwargs.get('compras_list', MyCollection())


    def __set_estab__(self, estabIn: Estab):
        if isinstance(estabIn, Estab):
            self.__estab = estabIn
            self.conta_fav = self.__estab.conta_generica

    @property
    def estab(self):
        return self.__estab

    @estab.setter
    def estab(self, estabIn):
        if isinstance(estabIn, Estab):
            self.__estab = estabIn
            self.conta_fav = estabIn.conta_generica

    def append(self, model_obj: ItemServCompra):
        if isinstance(model_obj, ItemServCompra) is False:
            raise Exception('Interface de classe errada, precisa ser: itemServLst')
        else:
            self.compras_list.append(model_obj)
            self.valor = float(self.valor)+float(model_obj.valor_total)

    def to_treeView(self):
        lst = []
        for obj in self.compras_list:
            lst.append(obj.to_treeView())
        return lst


class TribServ:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.__tipo = self.__set_tipo__(kwargs.get('__tipo', None))
        self.nome = ''
        self.descr = ''
        self.valor = 0
        self.__venc_dat = None
        self.taxaJuros = 0
        self.moraMulta = 0

    def __set_tipo__(self, tipo: Categ):
        if isinstance(tipo, Categ):
            return tipo
        else:
            pass
    @property
    def venc_dat(self):
        return self.__venc_dat

    @venc_dat.setter
    def venc_dat(self, dat):
        if isinstance(dat, date):
            self.__venc_dat = dat


class AgendServ:
    def __init__(self):
        self.serv = None
        self.dataHora = None
        self.cliente = None
        self.status = None


class pessoaTransac:
    def __init__(self, **kwargs):
        self.ident = kwargs.get('ident')
        self.conta = kwargs.get('conta')
        self.tipo_pessoa = self.ident.tipo

    @property
    def id_ident(self):
        return self.ident.idd

    @property
    def id_conta(self):
        return self.conta.idd


class LstTransac(list):
    def __init__(self):
        super().__init__()

    def append(self, obj_transac: transac):
        if isinstance(obj_transac, transac):
            super().append(obj_transac)
        else:
            raise Exception('erro no append() LstTransac')


class MyCollection(dict):
    def __init__(self):
        super().__init__()
        self._idd = 1
        self.elem_type = None

    def append(self, model_obj):
        """
        :type model_obj: object
        """
        self.elem_type = type(model_obj)
        try:
            idd = model_obj.idd
            if idd is None:
                self[self._idd] = model_obj
                self._idd = self._idd + 1
            else:
                self[idd] = model_obj

        except Exception as expt:
            print(expt)
            raise Exception("An error occurred while trying to append the object!")

    def to_treeView(self):
        lst = []
        for obj in self.values():
            lst.append(obj.to_treeView())
        return lst

    def to_comboBox(self):
        lst = []
        for obj in self.values():
            lst.append(obj.to_comboBox())
        return lst

    def to_db(self):
        lst = []
        for obj in self.values():
            lst.append(obj.to_db())
        return lst

    def search_name(self, name):
        for obj in self.values():
            if obj.nome == name:
                return obj


class MyList(list):
    def __init__(self):
        super().__init__()
        self._idd = 1
        self.elem_type = None

    def append(self, model_obj):
        """
        :type model_obj: object
        """
        # CONSIDERAR A VERIFICAÇÃO DE TIPO DURANTE A INSERÇÃO NA LISTA!
        self.elem_type = type(model_obj)
        super().append(model_obj)

    def to_treeView(self):
        lst = []
        for obj in self:
            lst.append(obj.to_treeView())
        return lst

    def to_comboBox(self):
        lst = []
        for obj in self:
            lst.append(obj.to_comboBox())
        return lst

    def to_db(self):
        lst = []
        for obj in self:
            lst.append(obj.to_db())
        return lst

    def search_name(self, name):
        for obj in self:
            if obj.nome == name:
                return obj

    def search_id(self, idd):
        for obj in self:
            if obj.idd == idd:
                return obj


class extrato_conta(MyList):
    def __init__(self):
        super().__init__()
        self.idd_conta = None
        self.date_ref_inic = None
        self.date_ref_fin = None

    def append(self, model_obj):
        if isinstance(model_obj, transac):
            super().append(model_obj)
        else:
            raise Exception('Erro no append da classe extrato_conta')


class vendasLst(MyCollection):
    def __init__(self):
        super().__init__()
        self.valor_total = 0

    def append(self, model_obj: itemVenda):
        if isinstance(model_obj, itemVenda) is False:
            raise Exception('Interface errada, precisa ser: itemVenda')
        else:
            if self.get(model_obj.idd) is None:
                super().append(model_obj)
                self.valor_total = self.valor_total + itemVenda.valor_total
            else:
                pass


class MyDate:
    def __init__(self):
        self.data = None
        self.hoje = date.today()
        self.dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        self.meses = (
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
        'Dezembro')


    def __str__(self):
        return str(self.data.day)+'-'+self.meses[self.hoje.month]+'-'+str(self.data.year)

    @property
    def mes_atual(self):
        return self.meses[self.hoje.month]

    @property
    def dia_semana(self):
        return self.dias[self.hoje.weekday]