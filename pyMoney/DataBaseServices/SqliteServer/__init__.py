import sqlite3

'''
SELECT transac.nome, transac.valor, fornecs.nome, transac.descricao, dat, contas.nome FROM transac INNER JOIN fornecs ON (transac.id_fornec = fornecs.id)  INNER JOIN contas ON (transac.id_conta_fav= contas.id) 


compras_list (id, id_transac , id_item_serv , valor_unit, quantidade)
transac(id , nome , descricao , dat , __tipo , id_conta_ced , id_conta_fav , valor  , id_fornec) 
itens_servs(id , nome, descricao, id_espec, id_fornec)
'''


class ConnDB:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(".\data_base\BD_prog.db")
            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            # self.data = self.cursor.fetchone()
            self.conn.close()
            self.con_status = False

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __conect_BD__(self):
        try:
            if (self.con_status == False):
                self.conn = sqlite3.connect(".\data_base\BD_prog.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()
                # self.data = self.cursor.fetchone()
            else:
                raise Exception('Conexão indisponível ou já em uso')

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __disconect_BD__(self):
        self.con_status = False
        self.conn.close()

    def __select_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return elem
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __lastrowid__(self):
        return (self.cursor.lastrowid)

    def __execute_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return elem
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __select_fetchall__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __execute_fetchall__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return lst
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __execute_commit__(self, sql='', tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def execute_commit(self, sql='', tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def execute_fetchone(self, sql, tupl):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql, tupl)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return elem
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def execute_fetchall(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return lst
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def select_fetchone(self, sql, tupl):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql, tupl)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return elem
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def lastrowid(self):
        return self.cursor.lastrowid

    def finaliza_conexao(self):
        self.__disconect_BD__()

    def __expt_msg__(self, Expt):
        self.finaliza_conexao()
        print(Expt, ' ', type(Expt))
        print(isinstance(Expt,sqlite3.IntegrityError))
        raise Expt

    def __strip_lst_varchar__(self, lst_varchar):
        n = 0
        while n < len(lst_varchar):
            lst_varchar[n] = str(lst_varchar[n])
            lst_varchar[n] = lst_varchar[n].strip(')')
            lst_varchar[n] = lst_varchar[n].strip('(')
            lst_varchar[n] = lst_varchar[n].strip(",")
            lst_varchar[n] = lst_varchar[n].strip("'")
            n = n + 1
        return lst_varchar

    def fetchall_categ_str(self, tipo):
        if tipo == 'Item' or tipo == 'Serviço':
            sql = "SELECT categoria FROM categ_serv_item WHERE __tipo =  '" + tipo + "'"
            tabl_lst = self.__execute_fetchall__(sql)
            tabl_lst = self.__strip_lst_varchar__(tabl_lst)
            return (tabl_lst)
        else:
            return ('Erro: Tipo inválido')

    def __strip_id__(self, idd, tipo='int'):
        idd = str(idd)
        idd = idd.strip(')').strip('(').strip(",")

        if tipo == 'int':
            idd = int(idd)
            return (idd)
        elif tipo == 'str':
            return (idd)
        else:
            raise Exception('Argumento: ', tipo, ' não reconhecido, precisa ser "str" ou "int"')

    def fetchall_subcateg_str(self, tipo, categ_pai):
        sql = "SELECT id FROM categ_serv_item WHERE categoria = '" + categ_pai + "' AND __tipo = '" + tipo + "' ;"
        id_pai = self.__execute_fetchone__(sql)
        id_pai = self.__strip_id__(id_pai, 'str')

        sql = "SELECT subcategoria FROM subcateg_serv_item WHERE id_categ = " + id_pai
        tabl_lst = self.__execute_fetchall__(sql)
        tabl_lst = self.__strip_lst_varchar__(tabl_lst)

        return (tabl_lst)

    def fetchall_espec_str(self, tipo, subcateg_pai):
        table_ = 'subcateg_serv_item'
        cond_ = 'subcategoria = "' + subcateg_pai + '" ;'
        id_pai = self.__select_id__(table=table_, cond=cond_)

        sql = "SELECT especie FROM espec_item_serv WHERE id_pai = " + id_pai + ";"
        tabl_lst = self.__execute_fetchall__(sql)
        tabl_lst = self.__strip_lst_varchar__(tabl_lst)
        return (tabl_lst)


class ConnDBEnder:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("BD_ender.db")
            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            #self.conn.close()
            self.con_status = False

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __conect_BD__(self):
        try:
            if (self.con_status == False):
                self.conn = sqlite3.connect("BD_ender.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __disconect_BD__(self):
        self.con_status = False
        #self.conn.close()

    def finaliza_conexao(self):
        self.__disconect_BD__()

    def __select_fetchone__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __select_fetchall__(self, sql):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __execute_commit__(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __expt_msg__(self, Expt):
        self.finaliza_conexao()
        print(str(Expt))
        return (None)


    def execute_commit(self, sql='', tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()  # Conexão fechada com o BD!

        except Exception as Expt:
            self.__expt_msg__(Expt)

    def execute_fetchone(self, sql='', tupl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql, tupl)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def execute_fetchall(self, sql, tpl=''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def select_fetchone(self, sql = '', tupl = ''):
        self.__conect_BD__()  # Conexão aberta com o BD!
        try:
            self.cursor.execute(sql, tupl)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()  # Conexão fechada com o BD!
            return (elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def lastrowid(self):
        return (self.cursor.lastrowid)


    def fetch_ender_rua(self, rua):
        if type(rua) != str:
            rua = str(rua)

        lst_ender = []  # Lista que será retornada pelo método. Lista de dicionários contendo os endereços

        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE RUA =  "' + rua + '" ;'
        lst_tupl = self.__select_fetchall__(
            sql)  # lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['__tipo'] = elem_tupl[3]
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

        return (lst_ender)

    def fetch_ender_cep(self, cep):
        cep = str(cep)
        dic_ender = {}  # Dicionário que será retornado pelo método, contendo o endereço

        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE CEP = ' + cep + ';'
        tupla_ender = self.__select_fetchone__(sql)
        if tupla_ender != None:
            id_bairro = str(tupla_ender[0])
            dic_ender['rua'] = tupla_ender[1]
            dic_ender['cep'] = str(tupla_ender[2])
            dic_ender['__tipo'] = tupla_ender[3]

            sql = 'SELECT ID_CIDADES, BAIRROS FROM TB_BAIRROS WHERE ID = ' + id_bairro + ';'
            tupla_ender = self.__select_fetchone__(sql)
            id_cidade = str(tupla_ender[0])
            dic_ender['bairro'] = tupla_ender[1]

            sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID = ' + id_cidade + ';'
            tupla_ender = self.__select_fetchone__(sql)
            id_estado = str(tupla_ender[0])
            dic_ender['cidade'] = tupla_ender[1]

            sql = 'SELECT ESTADO, UF FROM TB_ESTADOS WHERE ID = ' + id_estado + ';'
            tupla_ender = self.__select_fetchone__(sql)
            dic_ender['estado'] = tupla_ender[0]
            dic_ender['uf'] = tupla_ender[1]
            dic_ender['pais'] = 'Brasil'

            return (dic_ender)
        else:
            return (None)

    def fetch_ender_rua_like(self, rua):
        if type(rua) != str:
            rua = str(rua)
        rua = rua + '%'
        lst_ender = []  # Lista que será retornada pelo método. Lista de dicionários contendo os endereços

        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE RUA LIKE  "' + rua + '" ;'
        lst_tupl = self.__select_fetchall__(
            sql)  # lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['__tipo'] = elem_tupl[3]
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

    def fetch_ender_cep_like(self, cep):
        cep = str(cep)
        cep = cep + '%'
        lst_ender = []  # Lista que será retornada pelo método. Lista de dicionários contendo os endereços
        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE CEP LIKE  "' + cep + '" ;'
        lst_tupl = self.__select_fetchall__(
            sql)  # lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['__tipo'] = elem_tupl[3]
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

        return (lst_ender)

    def fetch_cidade(self, cidade):
        lst_ender = []
        cidade = cidade + '%'
        sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE CIDADE LIKE "' + cidade + '";'
        lst_tupl = self.__select_fetchall__(sql)
        for elem in lst_tupl:
            dic_cidade = {}
            dic_cidade['id_estado'] = str(elem[0])
            dic_cidade['cidade'] = elem[1]
            lst_ender.append(dic_cidade)

        return (lst_ender)

    def fetch_estados(self):
        pass

    def fetch_cidades(self, estado):
        pass

    def fetch_bairros(self, estado, cidade):
        pass

    def fetch_ruas(self, estado, cidade, bairro):
        pass

    def fetch_ender(self, **kwargs):
        cep = kwargs.get(cep, '')
        rua = kwargs.get(rua, '')
        like_search = kwargs.get(like_search, False)

        if cep != '' and rua != '':
            raise Exception('fetch_ender() deve receber ou "cep" ou "rua" como argumento, e não os dois ao mesmo tempo.')
        elif cep == '' and rua == '':
            return None
        else:
            if cep != '':
                dic_ender = self.fetch_ender_cep(cep)
            else:
                dic_ender = self.fetch_ender_rua(rua)
            return dic_ender
