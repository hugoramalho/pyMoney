from pyMoney.DataBaseServices.SqliteServer import ConnDB as sqliteDB
from pyMoney.DataBaseServices.SqliteServer import ConnDBEnder as sqliteEnderDB
from pyMoney.Models.models import *


class DAO:
    def __init__(self):
        self.conDB = sqliteDB()

    def __select_fetchone__(self, sql = '', tupl = ''):
        dict_feedback = self.conDB.select_fetchone(sql, tupl)
        return dict_feedback

    def __execute_commit__(self, sql='', tupl=''):
        dict_feedback = self.conDB.execute_commit(sql, tupl)
        return dict_feedback

    def __execute_fetchall__(self, sql='', tupl=''):
        dict_feedback = self.conDB.execute_fetchall(sql, tupl)
        return dict_feedback

    def __lastrowid__(self):
        return self.conDB.lastrowid()


class estoqueDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_item:item):
        id_item = str(obj_item.idd)
        print(id_item)
        quant = str(obj_item.quant)

        tupl = (quant, id_item)
        sql = 'INSERT INTO estoque(QUANTIDADE, ID_ITEM) VALUES (?, ?);'
        self.__execute_commit__(sql, tupl)

    def load(self, obj_item:item):
        id_item = str(obj_item.idd)
        sql = 'SELECT QUANTIDADE FROM estoque WHERE ID_ITEM = '+id_item+';'
        quant = int(self.__select_fetchone__(sql))
        return quant

    def loadAll(self):
        sql = 'SELECT itens.ID, itens.NOME, itens.DESCRICAO, itens.CODIGO, itens.ID_ESPECIE, estoque.QUANTIDADE FROM estoque INNER JOIN itens ON (estoque.ID_ITEM = itens.ID);'
        lst_db = self.__execute_fetchall__(sql)
        print(lst_db)
        dic_item = {}
        lst_estoque = MyCollection()
        if lst_db is not None:
            for elem in lst_db:
                dic_item['idd'] = elem[0]
                dic_item['nome'] = elem[1]
                dic_item['descr'] = elem[2]
                dic_item['codigo'] = elem[3]
                # TODO PRECISO RESOLVER O PROBLEMA DA ESPECIE DO ITEM
                dic_estoq = {}
                dic_estoq['item'] = item(**dic_item)
                dic_estoq['quantidade'] = elem[5]
                estoque_aux = itemEstoque(**dic_estoq)
                lst_estoque.append(estoque_aux)
            return lst_estoque
        else:
            return lst_estoque

    def update(self, obj_item:item):
        id_item = str(obj_item.quant)
        quantidade = str(obj_item.quant)
        sql = 'UPDATE estoque SET QUANTIDADE = '+quantidade+' WHERE ID_ITEM = '+id_item+';'
        self.__execute_commit__(sql)


class itemDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_item:item):
        nome = obj_item.nome
        descricao = obj_item.descr
        codigo = obj_item.codigo
        id_espec = obj_item.id_especie

        tupl = (nome, descricao, codigo, id_espec)
        sql = 'INSERT INTO itens(NOME, DESCRICAO, CODIGO, ID_ESPECIE) VALUES(?, ?, ?, ?);'
        self.__execute_commit__(sql, tupl)

        obj_item.idd = self.__lastrowid__()
        estoque_DAO = estoqueDAO()
        estoque_DAO.insert(obj_item)

        self.__execute_commit__(sql, tupl)

    def update(self, obj_item:item):
        idd = str(obj_item.idd)
        nome = obj_item.nome
        descricao = obj_item.descr
        codigo = obj_item.codigo
        id_espec = str(obj_item.id_especie)

        sql = 'UPDATE itens SET NOME = "'+nome+'", DESCRICAO = "'+descricao+'", CODIGO = "'+codigo+'", ID_ESPECIE = '+id_espec+' WHERE ID = '+idd
        self.__execute_commit__(sql)

    def loadAll(self):
        sql = 'SELECT itens.ID, itens.NOME, itens.DESCRICAO, itens.CODIGO, itens.ID_ESPECIE, estoque.QUANTIDADE FROM estoque INNER JOIN itens ON (estoque.ID_ITEM = itens.ID);'
        # sql = 'SELECT itens.id, itens.nome, itens.descricao, marcas.nome, id_subcateg,
        # subcateg_serv_item.subcategoria, id_marca FROM itens INNER JOIN marcas ON(marcas.id = id_marca) INNER JOIN
        # subcateg_serv_item ON(subcateg_serv_item.id = id_subcateg);'
        lst_db = self.__execute_fetchall__(sql)

        lst_itens = MyCollection()
        if lst_db is not None:
            for elem_tupl in lst_db:
                # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
                dic_item = {}
                dic_item['idd'] = elem_tupl[0]
                dic_item['nome'] = elem_tupl[1]
                dic_item['descr'] = elem_tupl[2]
                dic_item['codigo'] = elem_tupl[3]
                dic_item['quant'] = elem_tupl[5]

                item_aux = item(**dic_item)
                lst_itens.append(item_aux)
        return lst_itens


    def search_name(self, name_like):
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM itens WHERE NOME LIKE "' + name_like + '%";'
        lst_db = self.__execute_fetchall__(sql)
        lst_itens = MyCollection()
        if lst_db is not None:
            for elem_tupl in lst_db:
                # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
                dic_item = {}
                dic_item['idd'] = elem_tupl[0]
                dic_item['nome'] = elem_tupl[1]
                dic_item['descr'] = elem_tupl[2]
                dic_item['codigo'] = elem_tupl[3]

                item_aux = item(**dic_item)
                lst_itens.append(item_aux)
        return lst_itens

    def search_code(self, code):
        code = str(code)
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM itens WHERE CODIGO = "' + code + '";'
        tupl_db = self.__select_fetchone__(sql)
        lst_itens = MyCollection()
        if tupl_db is not None:
            # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
            dic_item = {}
            dic_item['idd'] = tupl_db[0]
            dic_item['nome'] = tupl_db[1]
            dic_item['descr'] = tupl_db[2]
            dic_item['codigo'] = tupl_db[3]
            item_aux = item(**dic_item)
            lst_itens.append(item_aux)
        return lst_itens

    def load(self, id_item = None):
        id_item = str(id_item)
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM itens WHERE ID = "' + id_item + '";'
        tupl_db = self.__select_fetchone__(sql)
        lst_itens = MyCollection()
        if tupl_db is not None:
            # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
            dic_item = {}
            dic_item['idd'] = tupl_db[0]
            dic_item['nome'] = tupl_db[1]
            dic_item['descr'] = tupl_db[2]
            dic_item['codigo'] = tupl_db[3]
            item_aux = item(**dic_item)
            lst_itens.append(item_aux)
        return lst_itens

    def delete(self, id_item = None):
        pass


class servDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_serv: serv):
        nome = obj_serv.nome
        descricao = obj_serv.descr
        codigo = obj_serv.codigo
        id_especie = obj_serv.id_especie

        tupl = (nome, descricao, codigo, id_especie)
        sql = 'INSERT INTO servicos(NOME, DESCRICAO, CODIGO, ID_ESPECIE) VALUES(?, ?, ?, ?);'
        self.__execute_commit__(sql, tupl)

    def update(self, obj_serv: serv):
        idd = str(obj_serv.idd)
        nome = obj_serv.nome
        descricao = obj_serv.descr
        codigo = obj_serv.codigo
        id_especie = str(obj_serv.id_especie)

        sql = 'UPDATE servicos SET nome = "' + nome + '", DESCRICAO = "' + descricao + '", CODIGO = "'+codigo+'", ID_ESPECIE = ' + id_especie + ' WHERE ID = ' + idd
        self.__execute_commit__(sql)

    def loadAll(self):
        # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA LOS NO SERVICO
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM servicos;'
        lst_db = self.__execute_fetchall__(sql)
        lst_servs = MyCollection()
        if lst_db is not None:
            for elem_tuple in lst_db:
                dic_serv = {}
                dic_serv['idd'] = elem_tuple[0]
                dic_serv['nome'] = elem_tuple[1]
                dic_serv['descr'] = elem_tuple[2]
                dic_serv['codigo'] = elem_tuple[3]

                serv_aux = serv(**dic_serv)
                lst_servs.append(serv_aux)
        return lst_servs

    def search_name(self, name_like):
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM servicos WHERE NOME LIKE "' + name_like + '%";'
        lst_db = self.__execute_fetchall__(sql)
        lst_serv = MyCollection()

        if lst_db is not None:
            for elem_tupl in lst_db:
                # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
                dic_item = {}
                dic_item['idd'] = elem_tupl[0]
                dic_item['nome'] = elem_tupl[1]
                dic_item['descr'] = elem_tupl[2]
                dic_item['codigo'] = elem_tupl[3]
                item_aux = serv(**dic_item)
                lst_serv.append(item_aux)
        return lst_serv

    def search_code(self, code):
        code = str(code)
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM servicos WHERE CODIGO = "' + code + '";'
        tupl_db = self.__select_fetchone__(sql)
        lst_serv = MyCollection()
        if tupl_db is not None:
            # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
            dic_item = {}
            dic_item['idd'] = tupl_db[0]
            dic_item['nome'] = tupl_db[1]
            dic_item['descr'] = tupl_db[2]
            dic_item['codigo'] = tupl_db[3]
            item_aux = serv(**dic_item)
            lst_serv.append(item_aux)
        return lst_serv

    def load(self, id_item:int)->dict:
        id_item = str(id_item)
        sql = 'SELECT ID, NOME, DESCRICAO, CODIGO, ID_ESPECIE FROM servicos WHERE ID = "' + id_item + '";'
        tupl_db = self.__select_fetchone__(sql)
        lst_serv = MyCollection()
        if tupl_db is not None:
            # TODO CRIAR OS DAOs DAS CLASSES DE ESPECIE, SUBCATEGORIA E CATEGORIA E ENTAO CARREGA-LOS NO ITEM
            dic_item = {}
            dic_item['idd'] = tupl_db[0]
            dic_item['nome'] = tupl_db[1]
            dic_item['descr'] = tupl_db[2]
            dic_item['codigo'] = tupl_db[3]
            item_aux = serv(**dic_item)
            lst_serv.append(item_aux)
        return lst_serv

    def delete(self, id_item=None):
        pass


class moveDAO:
    def __init__(self):
        self.conDB = sqliteDB()

    def insert(self, obj_move):
        pass

    def update(self, obj_move):
        pass

    def loadAll(self):
        pass

    def load(self, id_move = None):
        pass

    def delete(self, id_move):
        pass

    def __execute_commit__(self, sql = '', tupl = ''):
        dict_feedback = self.conDB.execute_commit(sql, tupl)
        return dict_feedback

    def __execute_fetchall__(self, sql = '', tupl = ''):
        dict_feedback = self.conDB.execute_fetchall(sql, tupl)
        return dict_feedback


class fornecDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_fornec: fornec):
        # PRIMEIRO OCORRE A INSERÃO DO CONTATO NA TABELA CONTATO
        obj_contato = obj_fornec.contato # O OBJETO CONTATO É CAPTURADO E SEUS ATRIBUTOS COLHIDOS:
        tel1 = obj_contato.tel1
        tel2 = obj_contato.tel2
        cel1 = obj_contato.cel1
        cel2 = obj_contato.cel2
        email1 = obj_contato.email1
        email2 = obj_contato.email2
        tupl = (tel1, tel2, cel1, cel2, email1, email2)
        sql = 'INSERT INTO contatos(TEL1, TEL2, CEL1, CEL2, EMAIL1, EMAIL2) VALUES(?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl) # A TABELA CONTATO RECEBE OS ATRIBUTOS DO OBJETO
        id_contato = self.__lastrowid__() # A ID DO CONTATO REGISTRADO É CAPTURADA E SERVIRÁ DE CHAVE EXTRANGEIRA


        # SEGUNDO, OCORRE A INSERCÃO DO ENDERECO NA TABELA ENDERECOS
        obj_ender = obj_fornec.ender
        numero = obj_ender.numero
        tipo_resid = obj_ender.tipo_resid
        num_apart = obj_ender.num_apart
        bloco = obj_ender.bloco
        referencia = obj_ender.referencia
        edificio = obj_ender.edificio
        num_sala = obj_ender.num_sala
        cep = obj_ender.cep
        tipo_logradouro = obj_ender.tipo_logra
        logradouro = obj_ender.logradouro
        bairro = obj_ender.bairro
        cidade = obj_ender.cidade
        estado = obj_ender.estado
        uf = obj_ender.uf

        tupl = (numero, tipo_resid, num_apart, referencia, edificio, num_sala, cep, bloco, tipo_logradouro, logradouro, bairro, cidade, estado, uf)
        sql = 'INSERT INTO enderecos(NUMERO, TIPO_RESID, NUMERO_APART, REFERENCIA, EDIFICIO, NUMERO_SALA, CEP, BLOCO, TIPO_LOGRADOURO, LOGRADOURO, BAIRRO, CIDADE, ESTADO, UF) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)  # A TABELA ENDEREÇOS RECEBE OS ATRIBUTOS DO OBJETO
        id_ender = self.__lastrowid__()  # A ID DO ENDEREÇO REGISTRADO É CAPTURADA E SERVIRÁ DE CHAVE EXTRANGEIRA

        # TODO INSERÇÃO DE LISTA DE CONTAS
        lst_contas = obj_fornec.lst_contas

        # ABAIXO O CLIENTE É FINALMENTE REGISTRADO COM AS DEVIDAS CHAVES EXTRANGEIRAS NECESSÁRIAS:
        nome = obj_fornec.nome
        cnpj = obj_fornec.cnpj
        raz_soc = obj_fornec.raz_soc
        ramo = obj_fornec.ramo
        descricao = obj_fornec.descr
        id_ger = obj_fornec.id_ger
        tupl = (nome, cnpj, raz_soc, ramo, descricao, id_contato, id_ender, id_ger)
        sql = 'INSERT INTO fornecedores(nome, cnpj, raz_soc, ramo, descricao, id_contato, id_ender, id_ger) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)

    def load(self, id_fornec):
        sql = 'SELECT id, nome, cnpj, raz_soc, ramo, descricao, id_contato, id_ender, id_ger FROM fornecedores WHERE id = '+ id_fornec+';'
        tupl_fornec = self.__execute_fetchall__(sql)
        if tupl_fornec is not None:
            dic_fornec = {}
            dic_fornec['idd'] = tupl_fornec[0]
            dic_fornec['nome'] = tupl_fornec[1]
            dic_fornec['cnpj'] = tupl_fornec[2]
            dic_fornec['raz_soc'] = tupl_fornec[3]
            dic_fornec['ramo'] = tupl_fornec[4]
            dic_fornec['descricao'] = tupl_fornec[5]
            id_contato = tupl_fornec[6]
            id_ender = tupl_fornec[7]
            dic_fornec['id_ger'] = tupl_fornec[8]
            contato_DAO = contatoDAO()
            dic_fornec['contato'] = contato_DAO.load(id_contato)
            endereco_DAO = enderIdentDAO()
            dic_fornec['ender'] = endereco_DAO.load(id_ender)

            return fornec(**dic_fornec)
        else:
            return None

    def loadAll(self):
        sql = 'SELECT id, nome, cnpj, raz_soc, ramo, descricao, id_contato, id_ender, id_ger FROM fornecedores;'
        lst_db = self.__execute_fetchall__(sql)
        lst_fornec = MyCollection()

        if lst_db is not None:
            for elem in lst_db:
                dic_fornec = {}
                dic_fornec['idd'] = elem[0]
                dic_fornec['nome'] = elem[1]
                dic_fornec['cnpj'] = elem[2]
                dic_fornec['raz_soc'] = elem[3]
                dic_fornec['ramo'] = elem[4]
                dic_fornec['descricao'] = elem[5]
                id_contato = elem[6]
                id_ender = elem[7]
                dic_fornec['id_ger'] = elem[8]
                contato_DAO = contatoDAO()
                dic_fornec['contato'] = contato_DAO.load(id_contato)
                endereco_DAO = enderIdentDAO()
                dic_fornec['ender'] = endereco_DAO.load(id_ender)

                fornec_aux = fornec(**dic_fornec)
                lst_fornec.append(fornec_aux)

        return lst_fornec

    def update(self, obj_fornec:fornec):
        contato = obj_fornec.contato
        contato_DAO = contatoDAO()
        contato_DAO.update(contato)

        ender = obj_fornec.ender
        ender_DAO = enderIdentDAO()
        ender_DAO.update(ender)

        raz_soc = obj_fornec.raz_soc
        nome = obj_fornec.nome
        cnpj = obj_fornec.cnpj
        ramo = obj_fornec.ramo
        idd = str(obj_fornec.idd)
        descricao = obj_fornec.descr

        print(obj_fornec)
        sql = 'UPDATE fornecedores SET NOME = "'+nome+'", CNPJ = "'+cnpj +'", RAMO = "'+ramo+'", DESCRICAO = "'+descricao+'", RAZ_SOC = "'+raz_soc+'" WHERE id = '+idd
        print(sql)
        self.conDB.execute_commit(sql)

    def delete(self, client_id):
        pass


class gerenDAO(DAO):
    def __init__(self):
        super().__init__()


    def loadAll(self):
        sql = "SELECT id, nome_ger, nome_gest, descricao FROM gerencias"
        lst_tupl = self.__execute_fetchall__(sql)

        lst_ger = MyCollection()
        for elem_tupl in lst_tupl:
            dic_ger = {}
            dic_ger['idd'] = elem_tupl[0]
            dic_ger['nome_ger'] = elem_tupl[1]
            dic_ger['nome_gest'] = elem_tupl[2]
            dic_ger['descr'] = elem_tupl[3]

            conta_DAO = contaDAO()
            lst_contas = conta_DAO.loadAll(id_ger=elem_tupl[0])
            dic_ger['lst_contas'] = lst_contas

            obj_ger = gerencia(**dic_ger)
            lst_ger.append(obj_ger)
        return lst_ger

    def load(self, id_ger = None):
        if id_ger is None:
            #return Exception('ERROR')
            pass
        else:
            id_ger = str(id_ger)
            sql = 'SELECT id, nome_ger, nome_gest, descricao FROM gerencias WHERE id =  '+ id_ger + ';'
            lst_tupl = self.__execute_fetchall__(sql)
            lst_ger = []
            for elem_tupl in lst_tupl:
                dic_ger = {}
                dic_ger['idd'] = elem_tupl[0]
                dic_ger['nome_ger'] = elem_tupl[1]
                dic_ger['nome_gest'] = elem_tupl[2]
                dic_ger['descr'] = elem_tupl[3]
                lst_ger.append(dic_ger)
            return lst_ger

    def update(self, obj_geren: gerencia):
        idd = str(obj_geren.idd)
        nome_ger = obj_geren.nome_ger
        nome_gest = obj_geren.nome_gest
        descr = obj_geren.descr

        # TODO IMPLEMENTAR O UPDATE DA LISTA DE CONTAS
        # lst_contas = obj_geren.lst_contas

        sql = 'UPDATE gerencias SET nome_ger = "'+nome_ger+'", nome_gest = "'+nome_gest+'", descricao = "'+descr+'" WHERE id = '+ idd + ';'
        self.__execute_commit__(sql)



    def insert(self, obj_ger):
        kwargs = obj_ger.to_db()

        nome_ger = kwargs.get('nome_ger', '')
        nome_gest = kwargs.get('nome_gest', '')
        descricao = kwargs.get('descr', '')
        lst_contas = kwargs.get('lst_contas', [])

        tupla = (nome_ger, nome_gest, descricao)
        sql = "insert into gerencias (nome_ger, nome_gest, descricao) VALUES(?, ?, ?)"
        self.__execute_commit__(sql, tupla)

        # Abaixo, a id da gerência recem salva é obtida
        id_ger = self.__lastrowid__()
        for elem in lst_contas:
            # Como essas contas devem possuir a chave estrangeira da gerencia,
            # a lista é percorrida e atribuida a sua id_ger que servirá de chave estranageira
            elem['id_ger'] = id_ger

        # Finalmente, a lista de contas é salva:
        conta_dao = contatoDAO()
        conta_dao.insert(lst_contas)

        print("Gerência salva no banco de dados!")
        return id_ger

    def delete(self, obj_ger):
        pass


class contaDAO(DAO):
    def __init__(self):
        super().__init__()

    def loadAll(self, **kwargs):
        id_ger = kwargs.get('id_ger')
        if id_ger is None:
            #TODO IMPLEMENTAR UM ERRO CASO A ID DADA SEJA NULA
            #return Exception('ERROR')
            pass
        else:
            id_ger = str(id_ger)
            id_ger = str(id_ger)
            sql = "SELECT id, nome, tipo, saldo, id_ger, taxa_mensal FROM contas WHERE id_ger = '" + id_ger + "' AND tipo != 'abstrata';"
            lst_BD = self.__execute_fetchall__(sql)

            lst_contas = MyCollection()
            for tupl in lst_BD:
                dict_conta = {}
                dict_conta['idd'] = tupl[0]
                dict_conta['nome'] = tupl[1]
                dict_conta['tipo'] = tupl[2]
                dict_conta['saldo'] = tupl[3]
                dict_conta['id_ger'] = tupl[4]
                dict_conta['taxa_mensal'] = tupl[5]
                #dict_ret['extrato'] = self.fetchall_moves(id_ger = tupl[4], id_conta=tupl[0])
                #print(dict_ret)
                conta = c_conta(**dict_conta)
                lst_contas.append(conta)
            return lst_contas

    def insert(self, obj_conta: c_conta):
        nome = obj_conta.nome
        tipo = obj_conta.tipo
        id_ger = obj_conta.id_ger
        taxa_mensal = obj_conta.taxa_mensal
        saldo = obj_conta.saldo
        tupl = (nome, tipo, saldo, id_ger, taxa_mensal)
        sql = 'INSERT INTO contas(nome, tipo, saldo, id_ger, taxa_mensal) VALUES (?, ?, ?, ?, ?);'
        self.__execute_commit__(sql, tupl)
        #return self.__lastrowid__()

    def load(self, **kwargs):
        id_ger = kwargs.get('id_ger', None)
        id_conta = kwargs.get('id_conta', None)

        if id_ger is None or id_conta is None:
            #TODO INVOCAR UM ERRO CASO ALGUMAS DAS CONDIÇÕES ACIMA SATISFAÇAM-SE
            #return Exception('ERROR')
            pass

        else:
            id_ger, id_conta = str(id_ger), str(id_conta)
            sql = 'SELECT id, nome, tipo, saldo, id_ger, taxa_mensal FROM contas WHERE id_ger = ' + id_ger + ' AND id = ' + id_conta + ';'
            conta = self.__select_fetchone__(sql)

            #ABAIXO, A VERIFICAÇÃO OCORRE PORQUE NO MOMENTO DA CODIFICAÇÃO NÃO FICOU CLARO SE O MÉTODO __execute_fetchone__()
            #RETORNA UMA LISTA OU UMA TUPLA
            if type(conta) is list:
                lst_contas = MyCollection()
                for tupl in conta:
                    conta_aux = c_conta()
                    conta_aux.idd = tupl[0]
                    conta_aux.nome = tupl[1]
                    conta_aux.tipo = tupl[2]
                    conta_aux.saldo = tupl[3]
                    conta_aux.id_ger = tupl[4]
                    conta_aux.taxa_mensal = tupl[5]
                    lst_contas.append(conta_aux)
                return lst_contas

            elif type(conta) is tuple:
                conta_aux = c_conta()
                conta_aux.idd = conta[0]
                conta_aux.nome = conta[1]
                conta_aux.tipo = conta[2]
                conta_aux.saldo = conta[3]
                conta_aux.id_ger = conta[4]
                conta_aux.taxa_mensal= conta[5]
                return conta_aux

    def update(self, obj_conta:c_conta):
        idd = str(obj_conta.idd)
        nome = obj_conta.nome
        id_ger = str(obj_conta.id_ger)
        saldo = str(obj_conta.saldo)
        taxa_mensal = str(obj_conta.taxa_mensal)
        tipo = obj_conta.tipo

        #print('\n\n\n', idd, nome, id_ger, saldo, taxa_mensal, tipo)
        strAux = ''
        if id_ger != '' and id_ger != None:
            strAux = strAux + ' id_ger = ' + id_ger + ','

        if saldo != '' and saldo != None:
            strAux = strAux + ' saldo = ' + saldo + ','

        if taxa_mensal != '' and taxa_mensal != '':
            strAux = strAux + ' taxa_mensal = ' + taxa_mensal + ','

        if tipo != '' and tipo != '':
            strAux = strAux + ' tipo = "' + tipo + '",'

        if nome != '' and nome != '':
            strAux = strAux + ' nome = "' + nome + '",'

        if strAux != '':
            strAux = strAux.strip(', ')

        sql = 'UPDATE contas SET ' + strAux + ' WHERE id = ' + idd + ';'
        print(sql)
        self.__execute_commit__(sql)

    def delete(self, conta_id):
        if type(conta_id) != str:
            client_id = str(conta_id)
        # sql = 'DELETE FROM clientes WHERE id = ?'
        # self.cursor.execute(sql, client_id)
        sql = 'DELETE FROM contas WHERE id = ' + conta_id + ';'
        self.__execute_commit__(sql)


class contatoDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_contato: contato):
        # TODO PRECISO VER SE ISSO É VÁLIDO, JÁ QUE A INSERÇÃO GERA UMA ID QUE SERVIRÁ DE CHAVE EXTRANGEIRA
        tel1 = obj_contato.tel1
        tel2 = obj_contato.tel2
        cel1 = obj_contato.cel1
        cel2 = obj_contato.cel2
        email1 = obj_contato.email1
        email2 = obj_contato.email2
        tupl = (tel1, tel2, cel1, cel2, email1, email2)
        sql = 'INSERT INTO contatos(TEL1, TEL2, CEL1, CEL2, EMAIL1, EMAIL2) VALUES(?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl) # A TABELA CONTATO RECEBE OS ATRIBUTOS DO OBJETO

    def load(self, ID):
        ID = str(ID)
        dic_contato = {}  # Dicionário que será retornado enviado para instanciar um enderecoIdent()
        sql = 'SELECT ID, TEL1, TEL2, CEL1, CEL2, EMAIL1, EMAIL2 FROM contatos WHERE ID = ' + ID + ';'
        tupl_ender = self.__select_fetchone__(sql)
        if tupl_ender is not None:
            # DICIONÁRIO É PREENCHIDO:
            dic_contato['idd'] = tupl_ender[0]
            dic_contato['tel1'] = tupl_ender[1]
            #dic_contato['tel2'] = tupl_ender[2]
            dic_contato['cel1'] = tupl_ender[3]
            #dic_contato['cel2'] = tupl_ender[4]
            dic_contato['email1'] = tupl_ender[5]
            #dic_contato['email2'] = tupl_ender[6]

            contat = contato(**dic_contato)
            return contat
        else:
            return contato()

    def update(self, obj_contato: contato):

        kwargs = obj_contato.to_db()
        print(kwargs)
        idd = str(kwargs.get('idd'))
        tel1 = kwargs.get('tel1', '')
        tel2 = None # str(kwargs.get('tel2', ''))
        cel1 = str(kwargs.get('cel1', ''))
        cel2 = None # str(kwargs.get('cel2', ''))
        email1 = kwargs.get('email1', '')
        email2 = None # str(kwargs.get('email2', ''))

        strAux = ''
        if tel1 != '' and tel1 is not None:
            strAux = strAux + ' TEL1 = "' + tel1 + '",'

        if tel2 != '' and tel2 is not None:
            strAux = strAux + ' TEL2 = "' + tel2 + '",'

        if cel1 != '' and cel1 is not None:
            strAux = strAux + ' CEL1 = "' + cel1 + '",'

        if cel2 != '' and cel2 is not None:
            strAux = strAux + ' CEL2 = "' + cel2 + '",'

        if email1 != '' and email1 is not None:
            strAux = strAux + ' EMAIL1 = "' + email1 + '",'

        if email2 != '' and email2 is not None:
            strAux = strAux + ' EMAIL2 = "' + email2 + '",'

        if strAux != '':
            strAux = strAux.strip(', ')

        sql = 'UPDATE contatos SET ' + strAux + ' WHERE ID = ' + idd + ';'
        print(sql)
        self.__execute_commit__(sql)

    def delete(self, obj_contato: contato):
        ID = str(obj_contato.idd)
        sql = 'DELETE FROM contatos WHERE ID = ' + ID + ';'
        self.__execute_commit__(sql)


class clienteDAO(DAO):
    def __init__(self, obj_cliente = None):
        super().__init__()

    def insert(self, obj_cliente: cliente):
        # PRIMEIRO OCORRE A INSERÃO DO CONTATO NA TABELA CONTATO
        obj_contato = obj_cliente.contato # O OBJETO CONTATO É CAPTURADO E SEUS ATRIBUTOS COLHIDOS:
        tel1 = obj_contato.tel1
        tel2 = obj_contato.tel2
        cel1 = obj_contato.cel1
        cel2 = obj_contato.cel2
        email1 = obj_contato.email1
        email2 = obj_contato.email2
        tupl = (tel1, tel2, cel1, cel2, email1, email2)
        sql = 'INSERT INTO contatos(TEL1, TEL2, CEL1, CEL2, EMAIL1, EMAIL2) VALUES(?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl) # A TABELA CONTATO RECEBE OS ATRIBUTOS DO OBJETO
        id_contato = self.__lastrowid__() # A ID DO CONTATO REGISTRADO É CAPTURADA E SERVIRÁ DE CHAVE EXTRANGEIRA

        # SEGUNDO, OCORRE A INSERCÃO DO ENDERECO NA TABELA ENDERECOS
        obj_ender = obj_cliente.ender
        numero = obj_ender.numero
        tipo_resid = obj_ender.tipo_resid
        num_apart = obj_ender.num_apart
        bloco = obj_ender.bloco
        referencia = obj_ender.referencia
        edificio = obj_ender.edificio
        num_sala = obj_ender.num_sala
        cep = obj_ender.cep
        tipo_logradouro = obj_ender.tipo_logra
        logradouro = obj_ender.logradouro
        bairro = obj_ender.bairro
        cidade = obj_ender.cidade
        estado = obj_ender.estado
        uf = obj_ender.uf

        tupl = (numero, tipo_resid, num_apart, referencia, edificio, num_sala, cep, bloco, tipo_logradouro, logradouro, bairro, cidade, estado, uf)
        sql = 'INSERT INTO enderecos(NUMERO, TIPO_RESID, NUMERO_APART, REFERENCIA, EDIFICIO, NUMERO_SALA, CEP, BLOCO, TIPO_LOGRADOURO, LOGRADOURO, BAIRRO, CIDADE, ESTADO, UF) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)  # A TABELA ENDEREÇOS RECEBE OS ATRIBUTOS DO OBJETO
        id_ender = self.__lastrowid__()  # A ID DO ENDEREÇO REGISTRADO É CAPTURADA E SERVIRÁ DE CHAVE EXTRANGEIRA

        # TODO INSERÇÃO DE LISTA DE CONTAS
        lst_contas = obj_cliente.lst_contas

        # ABAIXO O CLIENTE É FINALMENTE REGISTRADO COM AS DEVIDAS CHAVES EXTRANGEIRAS NECESSÁRIAS:
        nome = obj_cliente.nome
        cpf = obj_cliente.cpf
        rg = obj_cliente.rg
        genero = obj_cliente.genero
        dataNasc = obj_cliente.dataNasc
        descricao = obj_cliente.descr
        id_ger = obj_cliente.id_ger
        tupl = (nome, cpf, rg, genero, dataNasc, descricao, id_contato, id_ender, id_ger)
        sql = 'INSERT INTO clientes(nome, cpf, rg, genero, dataNasc, descricao, id_contato, id_ender, id_ger) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)

    def load(self, id_cliente = None):
        sql = 'SELECT id, nome, cpf, rg, genero, dataNasc, descricao, id_contato, id_ender, id_ger FROM clientes WHERE id = ' + id_cliente +';'
        tupl_client = self.__select_fetchone__(sql)

        dic_client = {}
        dic_client['idd'] = tupl_client[0]
        dic_client['nome'] = tupl_client[1]
        dic_client['cpf'] = tupl_client[2]
        dic_client['rg'] = tupl_client[3]
        dic_client['genero'] = tupl_client[4]
        dic_client['dataNasc'] = tupl_client[5]
        dic_client['descricao'] = tupl_client[6]
        id_contato = tupl_client[7]
        id_ender = tupl_client[8]
        dic_client['id_ger'] = tupl_client[9]

        contato_DAO = contatoDAO()
        dic_client['contato'] = contato_DAO.load(id_contato)
        endereco_DAO = enderIdentDAO()
        dic_client['ender'] = endereco_DAO.load(id_ender)
        return cliente(**dic_client)

    def loadAll(self):
        sql = 'SELECT id, nome, cpf, rg, genero, dataNasc, descricao, id_contato, id_ender, id_ger FROM clientes'
        lst_db = self.__execute_fetchall__(sql)
        lst_clientes = MyCollection()
        if lst_db is not None:

            for elem in lst_db:
                dic_client = {}
                dic_client['idd'] = elem[0]
                dic_client['nome'] = elem[1]
                dic_client['cpf'] = elem[2]
                dic_client['rg'] = elem[3]
                dic_client['genero'] = elem[4]
                dic_client['dataNasc'] = elem[5]
                dic_client['descricao'] = elem[6]
                id_contato = elem[7]
                id_ender = elem[8]
                dic_client['id_ger'] = elem[9]
                contato_DAO = contatoDAO()
                dic_client['contato'] = contato_DAO.load(id_contato)
                endereco_DAO = enderIdentDAO()
                dic_client['ender'] = endereco_DAO.load(id_ender)

                cliente_aux = cliente(**dic_client)
                lst_clientes.append(cliente_aux)
            return lst_clientes
        else:
            return lst_clientes

    def update(self, obj_cliente: cliente):
        dataNasc = obj_cliente.dataNasc
        contato = obj_cliente.contato
        ender = obj_cliente.ender
        nome = obj_cliente.nome
        cpf = str(obj_cliente.cpf)
        genero = obj_cliente.genero
        idd = str(obj_cliente.idd)

        contato_DAO = contatoDAO()
        contato_DAO.update(contato)

        ender_DAO = enderIdentDAO()
        ender_DAO.update(ender)

        sql = 'UPDATE clientes SET NOME = "'+nome+'", CPF = "'+cpf +'", GENERO = "'+genero+'", dataNasc = "'+str(dataNasc)+'" WHERE id = '+idd
        print(sql)
        print(dataNasc)
        self.conDB.execute_commit(sql)

    def delete(self, client_id):
        pass


class enderIdentDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_ender: enderecoIdent):
        # TODO PRECISO VER SE ISSO É VÁLIDO, JÁ QUE A INSERÇÃO GERA UMA ID QUE SERVIRÁ DE CHAVE EXTRANGEIRA
        numero = obj_ender.numero
        tipo_resid = obj_ender.tipo_resid
        num_apart = obj_ender.num_apart
        bloco = obj_ender.bloco
        referencia = obj_ender.referencia
        edificio = obj_ender.edificio
        num_sala = obj_ender.num_sala
        cep = obj_ender.cep
        tipo_logradouro = obj_ender.tipo_logra
        logradouro = obj_ender.logradouro
        bairro = obj_ender.bairro
        cidade = obj_ender.cidade
        estado = obj_ender.estado
        uf = obj_ender.uf

        tupl = (numero, tipo_resid, num_apart, referencia, edificio, num_sala, cep, bloco, tipo_logradouro, logradouro, bairro, cidade, estado, uf)
        sql = 'INSERT INTO enderecos(NUMERO, TIPO_RESID, NUMERO_APART, REFERENCIA, EDIFICIO, NUMERO_SALA, CEP, BLOCO, TIPO_LOGRADOURO, LOGRADOURO, BAIRRO, CIDADE, ESTADO, UF) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)  # A TABELA ENDEREÇOS RECEBE OS ATRIBUTOS DO OBJETO


    def load(self, ID):
        ID = str(ID)
        dic_ender = {}  # Dicionário que será retornado enviado para instanciar um enderecoIdent()
        sql = 'SELECT ID, NUMERO, TIPO_RESID, EDIFICIO, NUMERO_APART, BLOCO, NUMERO_SALA, CEP, REFERENCIA, ' \
              'TIPO_LOGRADOURO, LOGRADOURO, BAIRRO, CIDADE, ESTADO, UF FROM enderecos WHERE ID = ' + ID + ';'

        tupl_ender = self.__select_fetchone__(sql)
        if tupl_ender is not None:
            # DICIONÁRIO É PREENCHIDO:
            dic_ender['idd'] = tupl_ender[0]
            dic_ender['numero'] = tupl_ender[1]
            dic_ender['tipo_resid'] = tupl_ender[2]
            dic_ender['edificio'] = tupl_ender[3]
            dic_ender['num_apart'] = tupl_ender[4]
            dic_ender['bloco'] = tupl_ender[5]
            dic_ender['num_sala'] = tupl_ender[6]
            dic_ender['cep'] = tupl_ender[7]
            dic_ender['referencia'] = tupl_ender[8]
            dic_ender['tipo'] = tupl_ender[9]
            dic_ender['logradouro'] = tupl_ender[10]
            dic_ender['bairro'] = tupl_ender[11]
            dic_ender['cidade'] = tupl_ender[12]
            dic_ender['estado'] = tupl_ender[13]
            dic_ender['uf'] = tupl_ender[14]

            ender = enderecoIdent(**dic_ender)
            return ender
        else:
            return enderecoIdent()


    def update(self, obj_ender: enderecoIdent):
        print(obj_ender)
        idd = str(obj_ender.idd)
        numero = obj_ender.numero
        tipo_resid = obj_ender.tipo_resid
        edificio = obj_ender.edificio
        num_apart = obj_ender.num_apart
        bloco = obj_ender.bloco
        num_sala = obj_ender.num_sala
        referencia = obj_ender.referencia
        cep = obj_ender.cep
        tipo  = obj_ender.tipo_logra
        logradouro = obj_ender.logradouro
        bairro = obj_ender.bairro
        cidade = obj_ender.cidade
        estado = obj_ender.estado
        uf = obj_ender.uf

        sql = 'UPDATE enderecos SET NUMERO = "'+numero+\
              '", TIPO_RESID = "'+tipo_resid+\
              '", EDIFICIO = "'+edificio +\
              '", NUMERO_APART = "'+ num_apart+\
              '", BLOCO = "'+bloco +\
              '", NUMERO_SALA = "'+ num_sala+\
              '", CEP = "'+cep+\
              '", REFERENCIA ="'+referencia + \
              '", TIPO_LOGRADOURO="' + tipo + \
              '", LOGRADOURO="' + logradouro + \
              '", BAIRRO="' + bairro + \
              '", CIDADE="' + cidade + \
              '", ESTADO="' + estado + \
              '", UF="' + uf + \
              '" WHERE ID = ' + idd
        print(sql)
        self.__execute_commit__(sql)


class enderDAO:
    def __init__(self):
        # REPARE QUE O PRESENTE DAO ABRE OUTRO BD:
        self.conDB = sqliteEnderDB()

    def search_cep(self, cep):
        cep = str(cep)
        dic_ender = {}  # Dicionário que será retornado pelo método, contendo o endereço

        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE CEP = ' + cep + ';'
        tupla_ender = self.__select_fetchone__(sql)
        if tupla_ender != None:
            id_bairro = str(tupla_ender[0])
            dic_ender['id_bairro'] = id_bairro
            dic_ender['logradouro'] = tupla_ender[1]
            dic_ender['cep'] = str(tupla_ender[2])
            dic_ender['tipo'] = tupla_ender[3]

            sql = 'SELECT ID_CIDADES, BAIRROS FROM TB_BAIRROS WHERE ID = ' + id_bairro + ';'
            tupla_ender = self.__select_fetchone__(sql)
            id_cidade = str(tupla_ender[0])
            dic_ender['id_cidade'] = id_cidade
            dic_ender['bairro'] = tupla_ender[1]

            sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID = ' + id_cidade + ';'
            tupla_ender = self.__select_fetchone__(sql)
            id_estado = str(tupla_ender[0])
            dic_ender['id_estado'] = id_estado
            dic_ender['cidade'] = tupla_ender[1]

            sql = 'SELECT ESTADO, UF FROM TB_ESTADOS WHERE ID = ' + id_estado + ';'
            tupla_ender = self.__select_fetchone__(sql)
            dic_ender['estado'] = tupla_ender[0]
            dic_ender['uf'] = tupla_ender[1]
            dic_ender['pais'] = 'Brasil'

            ender = endereco(**dic_ender)
            return ender
        else:
            return None

    def search_rua(self, rua):
    # TODO NAO ESTA PRONTO O PRESENTE METODO
        if type(rua) != str:
            rua = str(rua)

        lst_ender = []  # Lista que será retornada pelo método. Lista de dicionários contendo os endereços

        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE RUA =  "' + rua + '" ;'
        lst_tupl = self.__execute_fetchall__(sql)  # lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['tipo'] = elem_tupl[3]
            lst_ender.append(dic_ender)

        for elem_dic in lst_ender:
            id_bairro = elem_dic['id_bairro']
            del (elem_dic['id_bairro'])  # Exclui essa posição, não mais necessária

            sql = 'SELECT ID_CIDADES, BAIRROS FROM TB_BAIRROS WHERE ID = ' + id_bairro + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_cidade'] = str(tupla_ender[0])
            elem_dic['bairro'] = tupla_ender[1]

        for elem_dic in lst_ender:
            id_cidade = elem_dic['id_cidade']
            del (elem_dic['id_cidade'])  # Exclui essa posição, não mais necessária

            sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID = ' + id_cidade + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_estado'] = str(tupla_ender[0])
            elem_dic['cidade'] = tupla_ender[1]

        for elem_dic in lst_ender:
            id_estado = elem_dic['id_estado']
            del (elem_dic['id_estado'])

            sql = 'SELECT ESTADO, UF FROM TB_ESTADOS WHERE ID = ' + id_estado + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['estado'] = tupla_ender[0]
            elem_dic['uf'] = tupla_ender[1]
            elem_dic['pais'] = 'Brasil'

        return lst_ender

    def load_UF(self):
        lst_UF = []  # Lista que será retornada pelo método.

        sql = 'SELECT ID, ESTADO, UF, IBGE_ESTADO FROM TB_ESTADOS;'
        lst_tupl = self.__execute_fetchall__(sql)  # lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            str_estado = str(elem_tupl[1])
            lst_UF.append(str_estado)
        return lst_UF

    def load_CIDADES(self, UF):
        UF = str(UF)
        sql = 'SELECT ID FROM TB_ESTADOS WHERE ESTADO = "'+UF+'";'
        ID_ESTADO = str(self.__select_fetchone__(sql)[0])

        sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID_ESTADO = '+ID_ESTADO+';'
        lst_bd = self.__execute_fetchall__(sql)
        lst_cidades = []
        for elem in lst_bd:
            str_cidade = elem[1]
            lst_cidades.append(str_cidade)
        return lst_cidades

    def load_BAIRROS(self, CIDADE):
        CIDADE = str(CIDADE)
        sql = 'SELECT ID FROM TB_CIDADES WHERE CIDADE = "'+CIDADE+'";'
        ID_CIDADES = str(self.__select_fetchone__(sql)[0])

        sql = 'SELECT ID, BAIRROS FROM TB_BAIRROS WHERE ID_CIDADES = '+ID_CIDADES+';'
        lst_bd = self.__execute_fetchall__(sql)
        lst_bairros = []
        for elem in lst_bd:
            str_bairro = elem[1]
            lst_bairros.append(str_bairro)
        return lst_bairros


    def __select_fetchone__(self, sql = '', tupl = ''):
        dict_feedback = self.conDB.select_fetchone(sql, tupl)
        return dict_feedback

    def __execute_commit__(self, sql='', tupl=''):
        dict_feedback = self.conDB.execute_commit(sql, tupl)
        return dict_feedback

    def __execute_fetchall__(self, sql='', tupl=''):
        dict_feedback = self.conDB.execute_fetchall(sql, tupl)
        return dict_feedback

    def __lastrowid__(self):
        return self.conDB.lastrowid()


class estabDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_estab: Estab):
        # PRIMEIRO OCORRE A INSERÃO DO CONTATO NA TABELA CONTATO
        obj_contato = obj_estab.contato # O OBJETO CONTATO É CAPTURADO E SEUS ATRIBUTOS COLHIDOS:
        tel1 = obj_contato.tel1
        tel2 = obj_contato.tel2
        cel1 = obj_contato.cel1
        cel2 = obj_contato.cel2
        email1 = obj_contato.email1
        email2 = obj_contato.email2
        tupl = (tel1, tel2, cel1, cel2, email1, email2)
        sql = 'INSERT INTO contatos(TEL1, TEL2, CEL1, CEL2, EMAIL1, EMAIL2) VALUES(?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl) # A TABELA CONTATO RECEBE OS ATRIBUTOS DO OBJETO
        id_contato = self.__lastrowid__() # A ID DO CONTATO REGISTRADO É CAPTURADA E SERVIRÁ DE CHAVE EXTRANGEIRA

        # SEGUNDO, OCORRE A INSERCÃO DO ENDERECO NA TABELA ENDERECOS
        obj_ender = obj_estab.ender
        numero = obj_ender.numero
        tipo_resid = obj_ender.tipo_resid
        num_apart = obj_ender.num_apart
        bloco = obj_ender.bloco
        referencia = obj_ender.referencia
        edificio = obj_ender.edificio
        num_sala = obj_ender.num_sala
        cep = obj_ender.cep
        tipo_logradouro = obj_ender.tipo_logra
        logradouro = obj_ender.logradouro
        bairro = obj_ender.bairro
        cidade = obj_ender.cidade
        estado = obj_ender.estado
        uf = obj_ender.uf

        tupl = (numero, tipo_resid, num_apart, referencia, edificio, num_sala, cep, bloco, tipo_logradouro, logradouro, bairro, cidade, estado, uf)
        sql = 'INSERT INTO enderecos(NUMERO, TIPO_RESID, NUMERO_APART, REFERENCIA, EDIFICIO, NUMERO_SALA, CEP, BLOCO, TIPO_LOGRADOURO, LOGRADOURO, BAIRRO, CIDADE, ESTADO, UF) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)  # A TABELA ENDEREÇOS RECEBE OS ATRIBUTOS DO OBJETO
        id_ender = self.__lastrowid__()  # A ID DO ENDEREÇO REGISTRADO É CAPTURADA E SERVIRÁ DE CHAVE EXTRANGEIRA

        # ABAIXO A CONTA É REGISTRADA NO BANCO DE DADOS:
        id_ger = obj_estab.id_ger
        conta_ident = obj_estab.conta_generica
        tipo = conta_ident.tipo
        saldo = conta_ident.saldo
        taxa_mensal = conta_ident.taxa_mensal
        nome = conta_ident.nome
        tupl = (nome, saldo, taxa_mensal, tipo, id_ger)
        sql = 'INSERT INTO contas(NOME, SALDO, TAXA_MENSAL, TIPO, ID_GER) VALUES(?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)
        id_conta = self.__lastrowid__()
        # CONSIDERAR FAZER DESSE JEITO:
        # conta_DAO = contaDAO()
        # conta_DAO.insert(conta_ident)

        # ABAIXO O ESTABELECIMENTO É FINALMENTE REGISTRADO COM AS DEVIDAS CHAVES EXTRANGEIRAS NECESSÁRIAS:
        nome = obj_estab.nome
        id_categ = obj_estab.categ.idd
        descricao = obj_estab.descr
        id_ger = obj_estab.id_ger
        tupl = (nome, descricao, id_categ, id_contato, id_ender, id_ger, id_conta)
        sql = 'INSERT INTO estabelecimentos(nome, descricao, id_categ, id_contato, id_ender, id_ger, id_conta) VALUES (?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupl)

    def load(self, idd):
        idd = str(idd)
        sql = 'SELECT id, nome, descricao, id_categ, id_contato, id_ender, id_ger FROM estabelecimentos WHERE id = ' + idd
        tupl_db = self.__select_fetchone__(sql)

        if tupl_db is not None and tupl_db != ():
            estab = Estab()
            estab.idd = tupl_db[0]
            estab.nome = tupl_db[1]
            estab.descr = tupl_db[2]
            estab.id_ger = tupl_db[6]
            # ABAIXO AS IDs EXTRANGEIRAS SÃO RECUPERADAS
            # PODER-SE-IA FAZÊ-LO POR INNER JOIN
            id_categ = tupl_db[3]
            id_contato = tupl_db[4]
            id_ender = tupl_db[5]
            # E CADA DAO SE ENCARREGA DE BUSCAR OS OBJETOS
            contato_DAO = contatoDAO()
            estab.contato = contato_DAO.load(id_contato)

            endereco_DAO = enderIdentDAO()
            estab.ender = endereco_DAO.load(id_ender)

            categ_DAO = categEstabDAO()
            estab.categ = categ_DAO.load(id_categ)
            return estab
        else:
            return None

    def loadAll(self):
        sql = 'SELECT id, nome, descricao, id_categ, id_contato, id_ender, id_ger, id_conta FROM estabelecimentos'
        lst_db = self.__execute_fetchall__(sql)
        lst_estabs = MyCollection()
        if lst_db is not None:
            for elem in lst_db:
                estab_aux = Estab()
                estab_aux.idd = elem[0]
                estab_aux.nome = elem[1]
                estab_aux.descr = elem[2]
                estab_aux.id_ger = elem[6]
                id_ger = elem[6]
                id_conta = elem[7]
                # ABAIXO AS IDs EXTRANGEIRAS SÃO RECUPERADAS
                # PODER-SE-IA FAZÊ-LO POR INNER JOIN
                id_categ = elem[3]
                id_contato = elem[4]
                id_ender = elem[5]

                # E CADA DAO SE ENCARREGA DE BUSCAR OS OBJETOS
                contato_DAO = contatoDAO()
                estab_aux.contato = contato_DAO.load(id_contato)

                endereco_DAO = enderIdentDAO()
                estab_aux.ender = endereco_DAO.load(id_ender)

                categ_DAO = categEstabDAO()
                estab_aux.categ = categ_DAO.load(id_categ)

                conta_DAO = contaDAO()
                estab_aux.conta_generica = conta_DAO.load(id_ger=id_ger, id_conta=id_conta)


                lst_estabs.append(estab_aux)




            return lst_estabs
        else:
            return lst_estabs

    def update(self, obj_estab: Estab):
        idd = str(obj_estab.idd)
        nome = obj_estab.nome
        descricao = obj_estab.descr

        id_categ = str(obj_estab.categ.idd)
        contato = obj_estab.contato
        ender = obj_estab.ender

        contato_DAO = contatoDAO()
        contato_DAO.update(contato)

        ender_DAO = enderIdentDAO()
        ender_DAO.update(ender)

        sql = 'UPDATE estabelecimentos SET nome = "'+nome+'", descricao = "'+descricao +'", id_categ = '+id_categ+' WHERE id = '+idd
        self.__execute_commit__(sql)

    def delete(self, obj_estab: Estab):
        pass


class categEstabDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_categ: CategEstab):
        nome = obj_categ.nome
        tupl = (nome,)
        sql = 'INSERT INTO categ_estab(nome) VALUES(?)'
        self.__execute_commit__(sql, tupl) # A TABELA CONTATO RECEBE OS ATRIBUTOS DO OBJETO

    def load(self, id_categ):
        id_categ = str(id_categ)
        sql = 'SELECT id, nome FROM categ_estab WHERE id = ' + id_categ + ';'
        tupl_categ = self.__select_fetchone__(sql)

        if tupl_categ is not None and tupl_categ != ():
            categ_estab = CategEstab()
            categ_estab.idd = tupl_categ[0]
            categ_estab.nome = tupl_categ[1]
            return categ_estab
        else:
            return None

    def loadAll(self):
        sql = 'SELECT id, nome FROM categ_estab'
        lst_db = self.__execute_fetchall__(sql)
        lst_categs = MyCollection()
        if lst_db is not None and lst_db != []:
            for elem in lst_db:
                categ_aux = CategEstab()
                categ_aux.idd = elem[0]
                categ_aux.nome = elem[1]
                lst_categs.append(categ_aux)
        return lst_categs

    def update(self, obj_categ: CategEstab):
        nome = obj_categ.nome
        idd = str(obj_categ.idd)
        sql = 'UPDATE categ_estab SET nome = "' + nome + '" WHERE id = ' + idd
        self.__execute_commit__(sql)

    def delete(self, obj_categ: CategEstab):
        idd = str(obj_categ.idd)
        sql = 'DELETE FROM categ_estab WHERE idd = '+idd
        #self.__execute_commit__(sql)


class transacDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_transac: transac):
        print('chegou aqui 1')
        data_ = obj_transac.data.data
        print('chegou aqui 2')


        id_conta_ced = obj_transac.conta_ced.idd
        id_conta_fav = obj_transac.conta_fav.idd
        valor = obj_transac.valor
        tipo = obj_transac.tipo

        print('chegou aqui')
        tupl = (data_, id_conta_ced, id_conta_fav, valor, tipo)
        sql = 'INSERT INTO transacs(DATA_, ID_CONTA_CED, ID_CONTA_FAV, VALOR, TIPO) VALUES (?, ?, ?, ?, ?)'
        print(sql)
        print(tupl)
        self.__execute_commit__(sql, tupl)

        conta_DAO = contaDAO()
        conta_DAO.update(obj_transac.conta_ced)
        conta_DAO.update(obj_transac.conta_fav)



    def loadAll(self):
        pass

    def load(self, idd):
        pass

    def getExtratoConta(self, obj_conta: c_conta, tempoInic: datetime, tempoFin: datetime):
        idd = str(obj_conta.idd)
        idd_ger = obj_conta.id_ger
        lst_transac = extrato_conta()
        lst_transac.date_ref_inic = tempoInic
        lst_transac.date_ref_fin = tempoFin
        lst_transac.idd_conta = idd

        sql = 'SELECT ID, DATA_, ID_CONTA_CED, ID_CONTA_FAV, VALOR, TIPO FROM transacs WHERE ID_CONTA_CED =  '+idd+' AND DATA_ >= "'+str(tempoInic)+'" AND DATA_ <= "'+str(tempoFin)+'" ORDER BY DATA_;'
        print(sql)
        lst_bd = self.__execute_fetchall__(sql)
        print(lst_bd)

        conta_DAO = contaDAO()
        for elem in lst_bd:
            transac_aux = transac()
            transac_aux.idd = elem[0]
            transac_aux.conta_ced = obj_conta
            transac_aux.data = datetime.strptime(elem[1], '%Y-%m-%d %H:%M:%S').date()
            transac_aux.conta_fav = conta_DAO.load(id_conta=elem[3], id_ger=idd_ger)
            transac_aux.valor = elem[4]
            transac_aux.tipo = elem[5]
            lst_transac.append(transac_aux)

        obj_conta.extrato = lst_transac
        return obj_conta


    def update(self, obj_transac: transac):
        pass


class compraItemServDAO(DAO):
    def __init__(self):
        super().__init__()

    def insert(self, obj_compra: CompraItemServ):
        # ATRIBUTOS GENERICOS DA CLASSE PAI transac:
        idd = obj_compra.idd
        data = obj_compra.data
        id_conta_fav = obj_compra.conta_fav.idd
        id_conta_ced = obj_compra.conta_ced.idd
        valor = obj_compra.valor
        tipo = obj_compra.tipo

        # ABAIXO ATRIBUTOS ESPECÍFICOS DO CompraItemServ:
        tupl = (data, id_conta_ced, id_conta_fav, valor, tipo)
        sql = 'INSERT INTO transacs(DATA_, ID_CONTA_CED, ID_CONTA_FAV, VALOR, TIPO) VALUES (?, ?, ?, ?, ?);'
        self.__execute_commit__(sql, tupl)

        id_estab = obj_compra.estab.idd
        tupl = (id_estab, valor)
        sql = 'INSERT INTO compras(ID_ESTAB, VALOR_TOTAL) VALUES (?, ?);'
        self.__execute_commit__(sql, tupl)
        # ABAIXO A ID DA COMPRA É RESGATADA E SERVIRÁ DE CHAVE EXTRANGEIRA PARA A LISTA DE ITENSERVS COMPRADOS
        id_compra = self.__lastrowid__()
        # ABAIXO O LOOP PERCORRE A LISTA DE COMPRAS INSERINDO NO BD COM SUA RESPECTIVA CHAVE EXTRANGEIRA ACIMA OBTIDA

        lst_compras = obj_compra.compras_list.values()
        print('AQUI HAHAH ', lst_compras)
        for elem in lst_compras:
            id_itemServ = elem.itemServ.idd
            valor_unit = elem.valor_unit
            quant = elem.quant
            tupl = (id_compra, id_itemServ, valor_unit, quant)
            sql = 'INSERT INTO compras_list(ID_COMPRA, ID_ITEMSERV, VALOR_UNIT, QUANT) VALUES (?, ?, ?, ?)'
            self.__execute_commit__(sql, tupl)

        # ABAIXO AS CONTAS SÃO ATUALIZADAS, DE MODO A TEREM SEUS SALDOS ALTERADOS E PERSISTIDOS NO BD
        conta_DAO = contaDAO()
        # CONTA CEDENTE:
        contaCed = obj_compra.conta_ced
        conta_DAO.update(contaCed)
        # CONTA FAVORECIDA:
        #contaFav = obj_compra.conta_fav
        #conta_DAO.update(contaFav)

    def loadAll(self):
        pass

    def load(self, idd):
        pass

    def loadFor(self):
        # PODE NAO SER ÚTIL...
        pass

    def update(self, obj_compra: CompraItemServ):
        pass

    def delete(self):
        pass


def main():
    dao = enderDAO()

    myender = dao.search_cep('')

    #print(ender.bairro, ' ', ender.tipo_logra, ' ', ender.logradouro)
    print(myender)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())