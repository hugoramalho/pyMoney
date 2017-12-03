from datetime import datetime
import os



## if not isinstance(objeto, classe): 
    #raise Exception('Bad interface')

class MyDateTime(datetime):
    def __init__(self):
        super().__init__(self)
        self.now = self.now()
        #self.data_hora.isoformat(' ')
        #self.data_hora = datetime.strptime(kwargs.get('data_hora', ''), isoformat)


def f_data_hora():
    #Essa função retorna uma string contendo a data e hora do momento requisitado
    tempo = datetime.now()
    a = str(tempo.year)
    me = str(tempo.month)
    d = str(tempo.day)
    h = str(tempo.hour)
    mi = str(tempo.minute)
    s = str(tempo.second)
    
    data = str(a+'_'+me+'_'+d+'_'+h+'_'+mi+'_'+s)
    return(data)


class c_primaria:
    '''PENSAR NO CASO DE CRIAR UMA CLASSE ABSTRATA PRIMÁRIA'''
    def __init__(self):
        pass
        
    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_primaria'
        return(dic_cadastro)
    
    def __str__(self):
        return(self.m_dic_cadastro())


class c_gerencia:        
    
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.tipo = kwargs.get('tipo', None)
        self.nome_ger = kwargs.get('nome_ger', '')
        self.nome_gest = kwargs.get('nome_gest', '')
        self.descr = kwargs.get('descr', '')


    def m_re_init(self, **kwargs):
        self.tipo = kwargs.get('tipo', self.tipo)
        self.nome_ger = kwargs.get('nome_ger', '')
        self.nome_gest = kwargs.get('nome_gest', '')
        self.descr = kwargs.get('descr', '')

    def __str__(self):
        return(self.m_dic_cadastro())

    def m_kwargs_treeView(self, **kwargs):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.saldo] 
        return(dic_treeView)

    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_gerencia'
        dic_cadastro['nome_ger'] = self.nome_ger
        dic_cadastro['nome_gest'] = self.nome_gest
        dic_cadastro['descr'] = self.descr
        return(dic_cadastro)

    def m_tupl_cadastro(self):
        tupl_cadastro_ = (self.nome_ger, self.nome_gest, self.descr)
        print("\n"+str(tupl_cadastro_))
        return(tupl_cadastro_)


class c_conta:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.id_ger = kwargs.get('id_ger', '')
        self.nome = kwargs.get('nome', 'Conta não declarada')
        self.saldo = kwargs.get('saldo', 0)
        self.tipo = kwargs.get('tipo', 'desconhecida')
        self.taxa_mensal = kwargs.get('taxa_mensal', 0)

    def m_re_init(self, **kwargs):
        self.idd = kwargs.get('idd', self.idd)
        self.id_ger = kwargs.get('id_ger', self.id_ger)
        self.nome = kwargs.get('nome', self.nome)
        self.saldo = kwargs.get('saldo', self.saldo)
        self.tipo = kwargs.get('tipo', self.tipo)
        self.taxa_mensal = kwargs.get('taxa_mensal', 0)

    def m_kwargs_treeView(self, **kwargs):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.saldo] 
        
        return(dic_treeView)
        
    def m_lst_treeView(self, **kwargs):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.saldo] 
        return(dic_treeView)

    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_conta'
        dic_cadastro['idd'] = self.idd
        dic_cadastro['id_ger'] = self.id_ger
        dic_cadastro['tipo'] = self.tipo
        dic_cadastro['nome'] = self.nome
        dic_cadastro['saldo'] = self.saldo
        dic_cadastro['taxa_mensal'] = self.taxa_mensal
        return(dic_cadastro)

    def m_tupl_cadastro(self):
        tupl_cadastro_ = (self.id_ger, self.tipo, self.nome, self.saldo, self.taxa_mensal)
        print("\n class c_conta "+str(tupl_cadastro_))
        return(tupl_cadastro_)

    def m_idd(self):
        return(self.idd)
    
    def m_nome(self):
        return(self.nome)
        
    def m_tipo(self):
        return(self.nome)
        

    def m_saldo(self):
        return(self.saldo)
        
    def m_id_ger(self):
        return(self.id_ger)
        
    def m_tax_mens(self):
        return(self.taxa_mensal)

    def m_retorna_tipo(self):
        return(self.tipo)

    def m_retorna_nome(self):
        return(self.nome)

    def m_retorna_saldo(self):
        return(self.saldo)
        
    def m_mov(self, mov):
        self.saldo = self.saldo + mov

    def m_define_saldo(self, novo_saldo):
        self.saldo = novo_saldo



class c_move:

    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')
        self.refe = kwargs.get('refe', c_refe())
        self.tipo = kwargs.get('tipo', '')
        self.data = kwargs.get('data', '')
        self.id_refe = kwargs.get('id_refe', None)
        self.descr = kwargs.get('descr', '')
        self.valor = float(kwargs.get('valor', 0))
        self.conta_fav = kwargs.get('conta_fav', c_conta())
        self.conta_ced = kwargs.get('conta_ced', c_conta())
        self.status_mov = kwargs.get('status_mov', False)
        self.__verf_contas__()


    def m_re_init(self, **kwargs):
        
        self.id_refe = kwargs.get('id_refe', self.id_refe)
        self.nome = kwargs.get('nome', self.nome)
        self.refe = kwargs.get('refe', self.refe)
        self.data = kwargs.get('data', self.data)
        self.tipo = kwargs.get('tipo', self.tipo)
        self.descr = kwargs.get('descr', self.descr)
        self.valor = float(kwargs.get('valor', self.valor))
        self.conta_fav = kwargs.get('conta_fav', self.conta_fav)
        self.conta_ced = kwargs.get('conta_ced', self.conta_ced)
        self.status_mov = kwargs.get('status_mov', self.status_mov)
        self.__verf_contas__()




    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = self.idd
        dic_cadastro['idd'] = 'c_move'
        dic_cadastro['nome'] = self.nome
        dic_cadastro['refe'] = self.refe.m_dic_cadastro()
        dic_cadastro['id_refe'] = self.id_refe
        dic_cadastro['data'] = self.data
        dic_cadastro['tipo'] = self.tipo
        dic_cadastro['valor'] = self.valor
        dic_cadastro['conta_fav'] = self.conta_fav.m_dic_cadastro()
        dic_cadastro['conta_ced'] = self.conta_ced.m_dic_cadastro()
        dic_cadastro['status_mov'] = self.status_mov
        dic_cadastro['descr'] = self.descr
        
        return(dic_cadastro)

    def m_tupl_cadastro(self):
        tupl_cadastro = (self.id_refe, self.data, self.tipo, self.valor, self.conta_fav, self.conta_ced, self.status_mov)
        return(tupl_cadastro)

    def m_data(self):
        return(self.data)

    def m_tipo(self):
        return(self.tipo)

    def m_id_refe(self):
        return(self.id_refe)

    def m_descr(self):
        return(self.descr)

    def m_conta_ced(self):
        return(self.conta_ced)

    def m_conta_fav(self):
        return(self.conta_fav)

    def m_status_move(self):
        return(self.status_exe)

    def m_valor(self, tipo = 'string'):
        if tipo == 'float':
            return(self.valor)
        else:
            return(str(self.valor))

    def __verf_contas__(self):
        if isinstance(self.conta_ced, c_conta) and isinstance(self.conta_fav, c_conta): 
            return(True)
        else:
            raise Exception('c_conta: Bad interface')

    def m_executa_move(self):
        if(self.__verf_contas__()):
            valor_out = (-1)*float(self.valor)
            self.conta_ced.m_mov(valor_out)
            valor_in =  float(self.valor)
            self.conta_fav.m_mov(valor_in)
            self.status_mov = True
            self.refe.status_mov = True
        else:
            raise Exception('Contas não declaradas.')





class c_refe:

    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.id_fornec = kwargs.get('id_fornec', None)
        self.valor = float(kwargs.get('valor', 0))
        self.nome = kwargs.get('nome', 'Não informado')
        self.id_mov = kwargs.get('id_mov', 0)
        self.status_mov = kwargs.get('status_mov', False)
        self.lst_items = kwargs.get('lst_items', c_list())
        self.cn_fornec = kwargs.get('cn_fornec', '')
        self.nome_fornec = kwargs.get('nome_fornec', '')
        self.tipo = kwargs.get('tipo', None)
        
        #Abaixo é verificada se a lista de items é do tipo valida:
        self.__verf_instance__(tipo = 'lst_items', obj = self.lst_items)

    def m_re_init(self, **kwargs):
        self.nome = kwargs.get('nome', 'Não informado')
        self.id_fornec = kwargs.get('id_fornec', self.id_fornec)
        self.valor = float(kwargs.get('valor', self.valor))
        self.lst_items = kwargs.get('lst_items', self.lst_items)
        self.cn_fornec = kwargs.get('cn_fornec', self.cn_fornec)
        self.nome_fornec = kwargs.get('nome_fornec', self.nome_fornec)
        self.tipo = kwargs.get('tipo', self.tipo)
        self.status_mov = kwargs.get('status_mov', self.status_mov)
        self.id_mov = kwargs.get('id_mov', 0)
        
        
        #Abaixo é verificada se a lista de items é do tipo valida:
        self.__verf_instance__(tipo = 'lst_items', obj = self.lst_items)


    def __verf_instance__(self, **kwargs):
        #Função recebe o tipo de comparação a ser feita e objeto a ser comparado
        tipo = kwargs.get('tipo', None)
        obj = kwargs.get('obj', None)
        
        if tipo == 'lst_items':
            if not isinstance(obj, c_list) and not isinstance(obj, type(None)):
                raise Exception('Interface de classe inválida para c_refe. Esperado um objeto da classe c_list')
        else: 
            return(True)
        
        

    def m_lst_treeView(self, **kwargs):
        tipo = kwargs.get('tipo', 'lista_itemServ')
        
        if tipo == 'lista_itemServ':
            return(self.lst_items.m_lst_treeView())
                    
        elif tipo == 'referente':
            #~ dic_treeView = {}
            #~ dic_treeView['idd'] = m_idd()
            #~ dic_treeView['lst_treeView'] = [self.nome_fornec, self.tipo, self.preco_total]
            #~ return(dic_treeView)
            lst_treeView = [self.nome_fornec, self.tipo, self.valor]
            return(lst_treeView)
        


    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_refe'
        dic_cadastro['idd'] = self.idd
        dic_cadastro['id_fornec'] = self.id_fornec
        dic_cadastro['tipo'] = self.tipo
        dic_cadastro['valor'] = self.valor
        dic_cadastro['lst_items'] = self.lst_items.m_lst_cadastro(tipo = 'dict')
        dic_cadastro['nome_fornec'] = self.nome_fornec
        dic_cadastro['cn_fornec'] = self.cn_fornec
        dic_cadastro['status_mov'] = self.status_mov
        dic_cadastro['id_mov'] = self.id_mov

        return(dic_cadastro)



    def m_status_move(self):
        return(self.status_mov)
    
    def m_nome(self):
        return(self.nome)
    
    def m_id_fornec(self):
        return(self.id_fornec)

    def m_tupl_cadastro(self):
        tupl_cadastro = (self.id_fornec, self.tipo, self.valor, self.lst_items, self.nome_fornec, self.cn_fornec, self.status_mov)
        return(tupl_cadastro)

    def m_tipo(self):
        return(self.tipo)
        
    def m_valor(self):
        return(self.valor)
        
    def m_cn_fornec(self):
        return(self.cn_fornec)

    def m_idd(self):
        return(self.idd)
    
    def m_lst_refe(self):
        return(self.lst_items)

    def m_append_item(self, item):
        self.lst_items.m_append_item(item)
        
    def m_nome_fornec(self):
        return(self.nome_fornec)
        
    def m_busca_item(self, item_id):
        contador = 0
        while contador < len(self.lst_items):
            if self.lst_items[contador].m_item_id() == item_id:
                
                return(self.lst_items[contador])
                break
            else:
                contador = contador + 1

    









class c_itemServ_ref:
    def __init__(self, **kwargs):
        self._idd = kwargs.get('idd', None)
        self._itemServ_idd = kwargs.get('itemServ_idd', None)
        self._nome = kwargs.get('nome', '')
        self._preco_unit = float(kwargs.get('preco_unit', 0))
        self._quant = float(kwargs.get('quant', 0))
        self._preco_total = float(kwargs.get('preco_total', 0))
        self.idd_ref = kwargs.get('idd_ref', None)


    def m_re_init(self, **kwargs):
        self._itemServ_idd = kwargs.get('itemServ_idd', self._itemServ_idd)
        self._nome = kwargs.get('nome', self._nome )
        self._preco_unit = float(kwargs.get('preco_unit', self._preco_unit))
        self._quant = float(kwargs.get('quant', self._quant))
        self._preco_total = float(kwargs.get('preco_total', self._preco_total))
        self.idd_ref = kwargs.get('idd_ref', self.idd_ref)
        
    

    def __verf_null__(self, atrb):
        if atrb == None:
            return(True)
        else:
            return(False)

    def m_idd(self):
        return(self._idd)
        
    def m_idd_ref(self):
        return(self.idd_ref)

    def m_preco_total(self):
        return(self._preco_total)

    def m_itemServ_idd(self):
        return(self._itemServ_idd)
        
    def m_preco_unit(self):
        return(self._preco_unit)
        
    def m_nome(self):
        return(self._nome)
        
    def m_quant(self):
        return(self._quant)
        

    def m_tupl_cadastro(self):
        if self.__verf_null__(self._itemServ_idd) != True:
            tupl_cadastro = (self._itemServ_idd, self._nome, self._preco_unit, self._quant, self._preco_total)
            return(tupl_cadastro)
        else:
            raise Exception('O item não foi informado!')

    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_itemServ_ref'
        dic_cadastro['idd'] = self._idd
        dic_cadastro['nome'] = self._nome
        dic_cadastro['itemServ_idd'] = self._itemServ_idd
        dic_cadastro['preco_unit'] = self._preco_unit
        dic_cadastro['quant'] = self._quant
        dic_cadastro['preco_total'] = self._preco_total
        return(dic_cadastro)
        
    def m_kwargs_treeView(self, **kwargs):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['lst_treeView'] = [self._nome, self._quant, self._preco_unit, self._preco_total]
        return(dic_treeView)

    def m_lst_treeView(self, **kwargs):
        lst_treeView = [self._nome, self._quant, self._preco_unit, self._preco_total]
        return(lst_treeView)



class c_ident:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')
        self.cn = kwargs.get('cn', '')
        self.descr = kwargs.get('descr', '')
        self.genero = kwargs.get('genero', '')
        self.tel1 = kwargs.get('tel1', '')
        self.tel2 = kwargs.get('tel2', '')
        self.email1 = kwargs.get('email1', '')
        self.email2 = kwargs.get('email2', '')
        self.uf = kwargs.get('uf', '')
        self.cidade = kwargs.get('cidade', '')
        self.bairro = kwargs.get('bairro', '')
        self.logradouro = kwargs.get('logradouro', '')
        self.num_resid = kwargs.get('num_resid', '')
        self.tipo_resid = kwargs.get('tipo_resid', '')
        self.num_ape = kwargs.get('num_ape', '')
        self.nome_cond = kwargs.get('nome_cond', '')
        self.cep =  kwargs.get('cep', '')
        self.dia_nasc = kwargs.get('dia_nasc', '')
        self.mes_nasc = kwargs.get('mes_nasc', '')
        self.ano_nasc = kwargs.get('ano_nasc', '')
        self.banco = kwargs.get('banco')
        self.agencia = kwargs.get('agencia')
        self.conta = kwargs.get('conta')

    def m_re_init(self, **kwargs):
        self.idd = kwargs.get('idd', self.idd)
        self.nome = kwargs.get('nome', self.nome)
        self.cn = kwargs.get('cn', self.cn)
        self.descr = kwargs.get('descr', self.descr)
        self.genero = kwargs.get('genero', self.genero)
        self.tel1 = kwargs.get('tel1', self.tel1)
        self.tel2 = kwargs.get('tel2', self.tel2)
        self.email1 = kwargs.get('email1', self.email1)
        self.email2 = kwargs.get('email2', self.email2)
        self.uf = kwargs.get('uf', self.uf)
        self.cidade = kwargs.get('cidade', self.cidade)
        self.bairro = kwargs.get('bairro', self.bairro)
        self.logradouro = kwargs.get('logradouro', self.logradouro)
        self.num_resid = kwargs.get('num_resid', self.num_resid)
        self.tipo_resid = kwargs.get('tipo_resid', self.tipo_resid)
        self.num_ape = kwargs.get('num_ape', self.num_ape)
        self.nome_cond = kwargs.get('nome_cond', self.nome_cond)
        self.cep =  kwargs.get('cep', self.cep)
        self.dia_nasc = kwargs.get('dia_nasc', self.dia_nasc)
        self.mes_nasc = kwargs.get('mes_nasc', self.mes_nasc)
        self.ano_nasc = kwargs.get('ano_nasc', self.ano_nasc)
        self.num_banco = kwargs.get('banco', self.banco)
        self.num_agencia = kwargs.get('agencia', self.agencia)
        self.num_conta = kwargs.get('conta', self.conta)

    def __verf_null__(self, atrib):
        if atrib == None or atrib == '' or atrib == '\n' or atrib == 'Escolha a opção':
            return('Não informado')
        else:
            return(atrib)

    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_ident'
        dic_cadastro['idd'] = self.idd
        dic_cadastro['nome'] = self.nome
        dic_cadastro['cn'] = self.cn
        dic_cadastro['genero'] = self.genero
        dic_cadastro['dia_nasc'] = self.dia_nasc
        dic_cadastro['mes_nasc'] = self.mes_nasc
        dic_cadastro['ano_nasc'] = self.ano_nasc
        dic_cadastro['descr'] = self.descr
        dic_cadastro['tel1'] = self.tel1
        dic_cadastro['tel2'] = self.tel2
        dic_cadastro['email1'] = self.email1
        dic_cadastro['email2'] = self.email2
        dic_cadastro['uf'] = self.uf
        dic_cadastro['cidade'] = self.cidade
        dic_cadastro['bairro'] = self.bairro
        dic_cadastro['logradouro'] = self.logradouro
        dic_cadastro['num_resid'] = self.num_resid
        dic_cadastro['tipo_resid'] = self.tipo_resid
        dic_cadastro['num_ape'] = self.num_ape
        dic_cadastro['nome_cond'] = self.nome_cond
        dic_cadastro['cep'] = self.cep
        dic_cadastro['banco'] = self.num_banco
        dic_cadastro['agencia'] = self.agencia
        dic_cadastro['conta'] = self.conta
        return(dic_cadastro)

    def m_idd(self):
        return(self.idd)

    def m_nome(self):
        return(self.nome)

    def m_descr(self):
        self.descr = self.__verf_null__(self.descr)
        return(self.descr)
        
    def m_genero(self):
        self.genero =  self.__verf_null__(self.genero)
        return(self.genero)
    
    def m_cn(self):
        self.cn =  self.__verf_null__(self.cn)
        return(self.cn)
    
    def m_email1(self):
        self.email1 =  self.__verf_null__(self.email1)
        return(self.email1)
        
    def m_email2(self):
        self.email2 =  self.__verf_null__(self.email2)
        return(self.email2)
        
    def m_tel1(self):
        self.tel1 =  self.__verf_null__(self.tel1)
        return(self.tel1)
        
    def m_tel2(self):
        self.tel2 =  self.__verf_null__(self.tel2)
        return(self.tel2)

    def m_uf(self):
        self.uf =  self.__verf_null__(self.uf)
        return(self.uf)
        
    def m_cidade(self):
        self.cidade =  self.__verf_null__(self.cidade)
        return(self.cidade)

    def m_bairro(self):
        self.bairro =  self.__verf_null__(self.bairro)
        return(self.bairro)
        
    def m_logradouro(self):
        self.logradouro =  self.__verf_null__(self.logradouro)
        return(self.logradouro)
        
    def m_num_resid(self):
        self.num_resid =  self.__verf_null__(self.num_resid)
        return(self.num_resid)
    
    def m_tipo_resid(self):
        self.tipo_resid =  self.__verf_null__(self.tipo_resid)
        return(self.tipo_resid)
    
    def m_num_ape(self):
        self.num_ape =  self.__verf_null__(self.num_ape)
        return(self.num_ape)
    
    def m_nome_cond(self):
        self.nome_cond =  self.__verf_null__(self.nome_cond)
        return(self.nome_cond)
    
    def m_cep(self):
        self.cep =  self.__verf_null__(self.cep)
        return(self.cep)

    def m_banco(self):
        self.banco =  self.__verf_null__(self.banco)
        return(self.banco)

    def m_agencia(self):
        self.agencia =  self.__verf_null__(self.agencia)
        return(self.agencia)

    def m_conta(self):
        self.conta =  self.__verf_null__(self.conta)
        return(self.conta)

class c_cliente:

    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', '')
        self.cn = kwargs.get('cn', '')
        self.descr = kwargs.get('descr', '')
        self.genero = kwargs.get('genero', '')
        self.tel1 = kwargs.get('tel1', '')
        self.tel2 = kwargs.get('tel2', '')
        self.email1 = kwargs.get('email1', '')
        self.email2 = kwargs.get('email2', '')
        self.uf = kwargs.get('uf', '')
        self.cidade = kwargs.get('cidade', '')
        self.bairro = kwargs.get('bairro', '')
        self.logradouro = kwargs.get('logradouro', '')
        self.num_resid = kwargs.get('num_resid', '')
        self.tipo_resid = kwargs.get('tipo_resid', '')
        self.num_ape = kwargs.get('num_ape', '')
        self.nome_cond = kwargs.get('nome_cond', '')
        self.cep =  kwargs.get('cep', '')
        self.dia_nasc = kwargs.get('dia_nasc', '')
        self.mes_nasc = kwargs.get('mes_nasc', '')
        self.ano_nasc = kwargs.get('ano_nasc', '')
        self.banco = kwargs.get('banco', '')
        self.agencia = kwargs.get('agencia', '')
        self.conta = kwargs.get('conta', '')


    def m_re_init(self, **kwargs):
        self.idd = kwargs.get('idd', self.idd)
        self.nome = kwargs.get('nome', self.nome)
        self.cn = kwargs.get('cn', self.cn)
        self.descr = kwargs.get('descr', self.descr)
        self.genero = kwargs.get('genero', self.genero)
        self.tel1 = kwargs.get('tel1', self.tel1)
        self.tel2 = kwargs.get('tel2', self.tel2)
        self.email1 = kwargs.get('email1', self.email1)
        self.email2 = kwargs.get('email2', self.email2)
        self.uf = kwargs.get('uf', self.uf)
        self.cidade = kwargs.get('cidade', self.cidade)
        self.bairro = kwargs.get('bairro', self.bairro)
        self.logradouro = kwargs.get('logradouro', self.logradouro)
        self.num_resid = kwargs.get('num_resid', self.num_resid)
        self.tipo_resid = kwargs.get('tipo_resid', self.tipo_resid)
        self.num_ape = kwargs.get('num_ape', self.num_ape)
        self.nome_cond = kwargs.get('nome_cond', self.nome_cond)
        self.cep =  kwargs.get('cep', self.cep)
        self.dia_nasc = kwargs.get('dia_nasc', self.dia_nasc)
        self.mes_nasc = kwargs.get('mes_nasc', self.mes_nasc)
        self.ano_nasc = kwargs.get('ano_nasc', self.ano_nasc)
        self.banco = kwargs.get('banco', self.num_banco)
        self.agencia = kwargs.get('agencia', self.num_agencia)
        self.conta = kwargs.get('conta', self.num_conta)



    def __verf_null__(self, atrib):
        if atrib == None or atrib == '' or atrib == '\n' or atrib == 'Escolha a opção':
            return('Não informado')
        else:
            return(atrib)


    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_cliente'
        dic_cadastro['idd'] = self.idd
        dic_cadastro['nome'] = self.nome
        dic_cadastro['cn'] = self.cn
        dic_cadastro['genero'] = self.genero
        dic_cadastro['dia_nasc'] = self.dia_nasc
        dic_cadastro['mes_nasc'] = self.mes_nasc
        dic_cadastro['ano_nasc'] = self.ano_nasc
        dic_cadastro['descr'] = self.descr
        dic_cadastro['tel1'] = self.tel1
        dic_cadastro['tel2'] = self.tel2
        dic_cadastro['email1'] = self.email1
        dic_cadastro['email2'] = self.email2
        dic_cadastro['uf'] = self.uf
        dic_cadastro['cidade'] = self.cidade
        dic_cadastro['bairro'] = self.bairro
        dic_cadastro['logradouro'] = self.logradouro
        dic_cadastro['num_resid'] = self.num_resid
        dic_cadastro['tipo_resid'] = self.tipo_resid
        dic_cadastro['num_ape'] = self.num_ape
        dic_cadastro['nome_cond'] = self.nome_cond
        dic_cadastro['cep'] = self.cep
        dic_cadastro['num_banco'] = self.num_banco
        dic_cadastro['num_agencia'] = self.num_agencia
        dic_cadastro['num_conta'] = self.num_conta
        return(dic_cadastro)


    def m_tupl_cadastro(self):
        tupl_cadastro = (self.nome, self.cn, self.genero, self.dia_nasc, self.mes_nasc, self.ano_nasc, self.descr, self.tel1, self.tel2, self.email1, self.email2, self.uf, self.cidade, self.bairro, self.logradouro, self.num_resid, self.tipo_resid, self.num_ape, self.nome_cond, self.cep)
        return(tupl_cadastro)

    def m_kwargs_treeView(self, **kwargs):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.tel1, self.email1, self.logradouro, self.cidade, self.uf, self.cep] 
        return(dic_treeView)

    def m_lst_treeView(self, **kwargs):
        try:
            lst_treeView = [self.m_nome(), self.m_tel1(), self.m_email1(), self.m_logradouro(), self.m_cidade(), self.m_uf(), self.m_cep()]
        except Exception as Expt:
            print(str(Expt))
        return(lst_treeView)

    def m_idd(self):
        return(self.idd)

    def m_nome(self):
        return(self.nome)

    def m_descr(self):
        self.descr = self.__verf_null__(self.descr)
        return(self.descr)
        
    def m_genero(self):
        self.genero =  self.__verf_null__(self.genero)
        return(self.genero)

    def m_cn(self):
        self.cn =  self.__verf_null__(self.cn)
        return(self.cn)
    
    def m_email1(self):
        self.email1 =  self.__verf_null__(self.email1)
        return(self.email1)
        
    def m_email2(self):
        self.email2 =  self.__verf_null__(self.email2)
        return(self.email2)
        
    def m_tel1(self):
        self.tel1 =  self.__verf_null__(self.tel1)
        return(self.tel1)
        
    def m_tel2(self):
        self.tel2 =  self.__verf_null__(self.tel2)
        return(self.tel2)

    def m_uf(self):
        self.uf =  self.__verf_null__(self.uf)
        return(self.uf)
        
    def m_cidade(self):
        self.cidade =  self.__verf_null__(self.cidade)
        return(self.cidade)

    def m_bairro(self):
        self.bairro =  self.__verf_null__(self.bairro)
        return(self.bairro)
        
    def m_logradouro(self):
        self.logradouro =  self.__verf_null__(self.logradouro)
        return(self.logradouro)
        
    def m_num_resid(self):
        self.num_resid =  self.__verf_null__(self.num_resid)
        return(self.num_resid)
    
    def m_tipo_resid(self):
        self.tipo_resid =  self.__verf_null__(self.tipo_resid)
        return(self.tipo_resid)
    
    def m_num_ape(self):
        self.num_ape =  self.__verf_null__(self.num_ape)
        return(self.num_ape)
    
    def m_nome_cond(self):
        self.nome_cond =  self.__verf_null__(self.nome_cond)
        return(self.nome_cond)
    
    def m_cep(self):
        self.cep =  self.__verf_null__(self.cep)
        return(self.cep)



class c_fornec:
    def __init__(self, **kwargs):
        self.idd = kwargs.get('idd', None)
        self.nome = kwargs.get('nome', None)
        self.cn = kwargs.get('cn', None)
        self.descr = kwargs.get('descr', None)
        self.categ = kwargs.get('categoria', None)
        self.subcateg = kwargs.get('subcategoria', None)
        self.tel1 = kwargs.get('tel1', None)
        self.tel2 = kwargs.get('tel2', None)
        self.email = kwargs.get('email', None)
        self.uf = kwargs.get('uf', None)
        self.cidade = kwargs.get('cidade', None)
        self.banco = kwargs.get('banco', None)
        self.agencia = kwargs.get('agencia', None)
        self.num_conta = kwargs.get('num_conta', None)
        
    def m_re_init(self, **kwargs):
        self.nome = kwargs.get('nome', self.nome)
        self.cn = kwargs.get('cn', self.cn)
        self.descr = kwargs.get('descr', self.descr)
        self.categ = kwargs.get('categoria', self.categ)
        self.subcateg = kwargs.get('subcategoria', self.subcateg)
        self.tel1 = kwargs.get('tel1', self.tel1)
        self.tel2 = kwargs.get('tel2', self.tel2)
        self.email = kwargs.get('email', self.email)
        self.uf = kwargs.get('uf', self.uf)
        self.cidade = kwargs.get('cidade', self.cidade)
        self.banco = kwargs.get('banco', None)
        self.agencia = kwargs.get('agencia', None)
        self.num_conta = kwargs.get('num_conta', None)

    def __verf_null__(self, atrib):
        if atrib == None or atrib == '' or atrib == '\n' or atrib == 'Escolha a opção':
            return('Não informado')
        else:
            return(atrib)


    def __append_obj_dic__(self):
        self.__class__.dic_fornec[self.idd] = self
    

    def m_lst_treeView(self, **kwargs):
        try:
            lst_treeView = [self.m_nome(), self.m_tel1(), self.m_email(), self.m_cidade(), self.m_uf()]
            return(lst_treeView)
        except Exception as Expt:
            print(str(Expt))
    
    
    def m_kwargs_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        dic_treeView['values'] = [self.categ, self.tel1, self.email, self.cidade] 
        return(dic_treeView)

    
    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_fornec'
        dic_cadastro['idd'] = self.idd
        dic_cadastro['nome'] = self.nome
        dic_cadastro['descr'] = self.descr
        dic_cadastro['categ'] = self.categ
        dic_cadastro['subcateg'] = self.subcateg
        dic_cadastro['uf'] = self.uf
        dic_cadastro['cidade'] = self.cidade
        dic_cadastro['email'] = self.email
        dic_cadastro['tel1'] = self.tel1
        dic_cadastro['tel2'] = self.tel2
        dic_cadastro['cn'] = self.cn
        return(dic_cadastro)


    def m_tupl_cadastro(self):
        tupl_cadastro_ = (self.nome, self.descr, self.categ, self.subcateg, self.uf, self.cidade, self.email, self.tel1, self.tel2, self.cn)
        print(tupl_cadastro_)
        return(tupl_cadastro_)


    def m_nome(self):
        self.nome = self.__verf_null__(self.nome)
        return(self.nome)
            
    def m_descr(self):
        self.descr = self.__verf_null__(self.descr)
        return(self.descr)
        
    def m_categ(self):
        self.categ = self.__verf_null__(self.categ)
        return(self.categ)
        
    def m_subcateg(self):
        self.subcateg = self.__verf_null__(self.subcateg)
        return(self.subcateg)
    
    def m_cn(self):
        self.cn = self.__verf_null__(self.cn)
        return(self.cn)
    
    def m_email(self):
        self.email = self.__verf_null__(self.email)
        return(self.email)
        
    def m_tel1(self):
        self.tel1 = self.__verf_null__(self.tel1)
        return(self.tel1)
        
    def m_tel2(self):
        self.tel2 = self.__verf_null__(self.tel2)
        return(self.tel2)
    
    def m_cidade(self):
        self.cidade = self.__verf_null__(self.cidade)
        return(self.cidade)
    
    def m_uf(self):
        self.uf = self.__verf_null__(self.uf)
        return(self.uf)

    def m_local(self):
        if self.m_cidade() != 'Não informado' and self.m_uf() != 'Não informado':
            local =  self.m_cidade() + ', ' + self.m_uf()
            return(local)
        else:
            return('Não informado')

    def m_idd(self):
        return(self.idd)


class c_item_serv(object):

    def __init__(self, **kwargs):
        #A IDD ABAIXO CARACTERIZA QUE O ITEM INSTANCIADO VEIO DO BANCO DE DADOS
        self.idd = kwargs.get('idd', None)
        self.tipo = kwargs.get('tipo', None)
        self.nome = kwargs.get('nome', None)
        self.descr = kwargs.get('descr', None)
        self.categ = kwargs.get('categ', None)
        self.subcateg = kwargs.get('subcateg', None)
        self.marca = kwargs.get('marca', None)

    def m_re_init(self, **kwargs):
        self.tipo = kwargs.get('tipo', self.tipo)
        self.nome = kwargs.get('nome', self.nome)
        self.descr = kwargs.get('descr', self.descr)
        self.categ = kwargs.get('categ', self.categ)
        self.subcateg = kwargs.get('subcateg', self.subcateg)
        self.marca = kwargs.get('marca', self.marca)

    def m_idd(self):
        return(self.idd)

    def m_dic_cadastro(self):
        dic_cadastro = {}
        dic_cadastro['class'] = 'c_item_serv'
        dic_cadastro['idd'] = self.idd
        dic_cadastro['tipo'] = self.tipo
        dic_cadastro['nome'] = self.nome
        dic_cadastro['descr'] = self.descr
        dic_cadastro['categ'] = self.categ
        dic_cadastro['subcateg'] = self.subcateg
        dic_cadastro['marca'] = self.marca
        return(dic_cadastro)

    def m_tupl_cadastro(self):
        tupl_cadastro= (self.tipo, self.nome, self.descr, self.subcateg, self.marca)
        print(tupl_cadastro)
        return(tupl_cadastro)

    def __verf_null__(self, atrib):
        if atrib == None or atrib == '' or atrib == '\n' or atrib == 'Escolha a opção':
            return('Não informado')
        else:
            return(atrib)

    def m_lst_treeView(self, **kwargs):
        if self.tipo == 'Item':
            return([self.m_nome(), self.m_categ(), self.m_subcateg(), self.m_marca()])
        else:
            return([self.m_nome(), self.m_categ(), self.m_subcateg()])

    def m_kwargs_treeView(self):
        dic_treeView = {}
        dic_treeView['idd'] = self.idd
        dic_treeView['text'] = self.nome
        if self.tipo == 'Item':
            dic_treeView['values'] = [self.categ, self.subcateg, self.marca] 
        else:
            dic_treeView['values'] = [self.categ, self.subcateg] 
        return(dic_treeView)
    
    def m_tipo(self):
        self.tipo = self.__verf_null__(self.tipo)
        return(self.tipo)
        
    def m_nome(self):
        self.nome = self.__verf_null__(self.nome)
        return(self.nome)
            
    def m_descr(self):
        self.descr = self.__verf_null__(self.descr)
        return(self.descr)
        
    def m_categ(self):
        self.categ = self.__verf_null__(self.categ)
        return(self.categ)
        
    def m_subcateg(self):
        self.subteg = self.__verf_null__(self.subcateg)
        return(self.subcateg)
    
    def m_marca(self):
        if self.tipo == 'Serviço':
            return(None)
        else:
            self.marca = self.__verf_null__(self.marca)
            return(self.marca)



class c_list():

    def __init__(self, obj_item = None):
        self.tipo_lst = None
        self.idd_item = 0
        self.dic_itens = {}
        
        """
        ABAIXO, CASO O ARGUMENTO SEJA DIFERENTE DE NONE, O OBJETO RECEBIDO (obj_item) 
        É ENVIADO PARA A FUNÇÃO QUE VERIFICARÁ SUA INSTANCIA(INTERFACE DE CLASSE)
        E EM SEGUIDA, ADICIONADA À LISTA, CASO A INSTANCIA SEJA COMPÁTIVEL
        """
        if obj_item != None:
                #HUGO, A PRINCÍPIO NAO SERÁ NECESSÁRIA A FUNÇÃO ABAIXO PORQUE A __append_item__() JÁ CHAMA A __verf_instance__()
                #self.__verf_instance__(obj_item)
                self.__append_item__(obj_item)
        else:
            pass

    def __done__(self):
        del(self.idd_item)
        del(self.dic_itens)
        del(self.tipo_lst)

    """
    A FUNÇÃO ABAIXO VERIFICA SE O OBJETO RECEBIDO PELA PRESENTE CLASSE PERTENCE À ALGUMA CLASSE COMPÁTIVEL
    OU SEJA, VERIFICA SE A INTERFACE DE CLASE ESTÁ CORRETA!
    """
    def __verf_instance__(self, obj_item):
        pass
        #~ if not isinstance(obj_item, c_item_serv) and not isinstance(obj_item, c_fornec) and not isinstance(obj_item, c_cliente) and not isinstance(obj_item, c_itemServ_ref) and not isinstance(obj_item, c_refe): 
            #~ raise Exception('Interface de classe incorreta!\nA classe deve ser algum do conjunto: c_item_serv, c_cliente, c_fornec, c_itemServ_ref, c_refe')
        #~ else:
            #~ pass

    def __append_item__(self, obj_item):
            self.__verf_instance__(obj_item)
            self.__verf_idd__(obj_item)
            if obj_item.m_idd() == None:
                self.idd_item = self.idd_item + 1
                self.dic_itens[self.idd_item] = obj_item
            else:
                self.idd_item = obj_item.m_idd()
                self.dic_itens[self.idd_item] = obj_item

                
    def __verf_idd__(self, obj_item):
        if self.idd_item == 0:
            """
            CASO O OBJETO NÃO TENHA UMA IDD, SIGNIFICA QUE NÃO FOI CARREGADO DE UM BANCO DE DADOS
            NESTE CASO, TRATA-SE DE UM OBJETO SENDO INSCRITO NO PROGRAMA
            """
            if obj_item.m_idd() == None:
                self.tipo_lst = 'Inscrição'
            else:
                """
                CASO O OBJETO TENHA O ATRIBUTO IDD, SIGNIFICA QUE FOI CARREGADO DE UMA BANCO DE DADOS
                """
                self.tipo_lst = 'Banco_de_dados'
        else:
            if obj_item.m_idd() == None:
                if self.tipo_lst == 'Banco_de_dados':
                    raise Exception('Objeto em dissonância com o tipo de lista iniciada!')
                else:
                    pass
            else:
                if self.tipo_lst == 'Inscrição':
                    raise Exception('Objeto em dissonância com o tipo de lista iniciada!')
                else:
                    pass

    def m_item(self, index):
        return(self.dic_itens[index])

    def m_dic_itens(self):
        return(self.dic_itens)
        
    def m_lst_treeView(self, **kwargs):
        #~ num_cols = kwargs.get('num_cols', 3)
        #~ tipo = kwargs.get('tipo', 1)
        
        lst_elems = self.__lst_itens__()
        lst_treeView = []
        for elem in lst_elems:
            try:
                dic_treeView = {}
                dic_treeView['idd'] = elem.m_idd()
                dic_treeView['lst_treeView'] = elem.m_lst_treeView(**kwargs)
                lst_treeView.append(dic_treeView)
            except:
                pass
        return(lst_treeView)



    def m_dic_nome_id(self):
        lst_elems = self.__lst_itens__()
        dic = {}
        for elem in lst_elems:
            dic[elem.m_nome()] = elem.m_idd()       
        return(dic)


    def m_cls_dic(self):
        del(self.dic_itens)
        self.dic_itens = {}
        self.idd_item = 0
        self.tipo_lst = None

    def m_append_item(self, obj_item):
        self.__verf_instance__(obj_item)
        self.__append_item__(obj_item)

    def m_del_item(self, idd):
        del(self.dic_itens[self.idd])

    def __lst_itens__(self):
        return(list(self.dic_itens.values()))

    def m_itens(self):
        lst = self.__lst_itens__()
        return(lst)

    def m_len_lst(self):
        return(len(self.dic_itens))



    def m_lst_cadastro(self, tipo = 'tuple'):
        lst = self.__lst_itens__()
        lst_cadastro = []        
        
        for item in lst:
            if tipo == 'tuple':
                tupla_cadastro = item.m_tupl_cadastro()
                lst_cadastro.append(tupla_cadastro)
            if tipo == 'dict':
                dic_cadastro = item.m_dic_cadastro()
                lst_cadastro.append(dic_cadastro)
        
        return(lst_cadastro)



class c_lst_BD(c_list):
    def __init__(self, *lst_bd, **kwargs):
        if lst_bd != None and len(lst_bd) != 0:
            c_list.__init__(self)
            self.tipo = kwargs.get('tipo', None)
            self.__init_list__(*lst_bd)
        else:
            pass

    def m_carrega_lst(self, *lst_bd, **kwargs):
        if lst_bd != None and len(lst_bd) != 0:
            c_list.__init__(self)
            self.tipo = kwargs.get('tipo', None)
            lst_bd = lst_bd[0]
            self.__init_list__(lst_bd)
            
        else:
            return(None)

    def __init_list__(self, *lst_bd):
        '''PRECISO ESQUEMATIZAR FUNÇÕES CONSTRUTORAS!'''
        
        self.__verf_tipo__()
        
        lst_bd = lst_bd[0] #Desempacotando o argumento
        if self.tipo == 'fornec' or self.tipo == 'fornecedores':
            for elem in lst_bd:
                obj = c_fornec(idd = elem[0], nome = elem[1], descr = elem[2],categoria = elem[3], subcategoria = elem[4], uf = elem[5],cidade = elem[6], email = elem[7], tel1 = elem[8], tel2 = elem[9], cn = elem[10])
                self.m_append_item(obj)
        
        elif self.tipo == 'item_serv' or self.tipo == 'item' or self.tipo == 'serv' or self.tipo == 'serviço' or self.tipo == 'iten':
            for elem in lst_bd: 
                obj = c_item_serv(idd = elem[0], nome = elem[1], descr = elem[2], subcateg = elem[3], marca = elem[4])
                self.m_append_item(obj)
        
        elif self.tipo == 'cliente' or self.tipo == 'client' or self.tipo == 'clientes':
            for elem in lst_bd:
                obj = c_cliente(idd = elem[0], nome = elem[1], cn = elem[2], genero = elem[3], dia_nasc = elem[4], mes_nasc = elem[5], ano_nasc = elem[6], descr = elem[7], tel1 = elem[8], tel2 = elem[9], email1 = elem[10], email2 = elem[11], uf = elem[12], cidade = elem[13], bairro = elem[14], logradouro = elem[15], num_resid = elem[16], tipo_resid = elem[17], num_ape = elem[18], nome_cond = elem[19], cep = elem[20])
                self.m_append_item(obj)
        
        
        elif self.tipo == 'ref' or self.tipo == 'refe' or self.tipo == 'referente':
            for elem_dic in lst_bd:
                
                lst_itemServ_ref = c_list()
                for elem in elem_dic['lst_items']:
                    itemServ_ref = c_itemServ_ref(**elem)
                    lst_itemServ_ref.m_append_item(itemServ_ref) 
                
                elem_dic['lst_items'] = lst_itemServ_ref
                
                obj = c_refe(**elem_dic)
                self.m_append_item(obj)
        
        elif self.tipo == 'conta' or self.tipo == 'cont' or self.tipo == 'contas':
            ''' PRECISO ESQUEMATIZAR FUNÇÕES CONSTRUTORAS '''
            for elem_dic in lst_bd:
                obj = c_conta(**elem_dic)
                self.m_append_item(obj)
                
                
        elif self.tipo == 'mov' or self.tipo == 'move' or self.tipo == 'movimentacao':
            pass
            ''' PRECISO ESQUEMATIZAR FUNÇÕES CONSTRUTORAS '''
            
            #~ for elem_dic in lst_bd:
                
                #~ lst_itemServ_ref = c_list()
                #~ for elem in elem_dic['lst_items']:
                    #~ itemServ_ref = c_itemServ_ref(**elem)
                    #~ lst_itemServ_ref.m_append_item(itemServ_ref) 
                
                #~ elem_dic['lst_items'] = lst_itemServ_ref
                
                #~ obj = c_refe(**elem_dic)
                #~ self.m_append_item(obj)

        else:
            raise Exception('Tipo:',self.tipo,' especificado não existe!')

    def __verf_tipo__(self):
        if self.tipo == None:
            raise Exception('Tipo não especificado para a classe c_lst_BD.')
        else:
            pass