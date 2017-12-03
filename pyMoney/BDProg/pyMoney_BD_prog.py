import os
import sqlite3
from random import *




'''




SELECT transac.nome, transac.valor, fornecs.nome, transac.descricao, dat, contas.nome FROM transac INNER JOIN fornecs ON (transac.id_fornec = fornecs.id)  INNER JOIN contas ON (transac.id_conta_fav= contas.id) 



INSERT INTO transac (nome, descricao, dat , tipo , id_conta_ced , id_conta_fav , valor , id_fornec) VALUES ('teste1', 'esta é uma transação de teste','teste' , '01/01/2018', 1, 2, 1000, 1)




SELECT id_espec from transac WRERE id = id

compras_list (id, id_transac , id_item_serv , valor_unit, quantidade)
transac(id , nome , descricao , dat , tipo , id_conta_ced , id_conta_fav , valor  , id_fornec) 
itens_servs(id , nome, descricao, id_espec, id_fornec)



'''

class conexao_BD_prog:

    def __init__(self):
        try:
            self.conn = sqlite3.connect("BD_prog.db")
            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            #self.data = self.cursor.fetchone()
            self.conn.close()
            self.con_status = False
    
        except Exception as Expt:
            self.__expt_msg__(Expt)


    def __conect_BD__(self):
        try:
            if(self.con_status == False):
                self.conn = sqlite3.connect("BD_prog.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()
                #self.data = self.cursor.fetchone()
            else:
                raise Exception('Conexão indisponível ou já em uso')
                pass
        except Exception as Expt:
            self.__expt_msg__(Expt)


    def __disconect_BD__(self):
        self.con_status = False
        self.conn.close()


    def __select_fetchone__(self, sql):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)

    def __lastrowid__(self):
        return(self.cursor.lastrowid)
        

    def __execute_fetchone__(self, sql):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)



    def __select_fetchall__(self, sql,  tpl = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)


    def __execute_fetchall__(self, sql,  tpl = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)
            
            

    def __execute_commit__(self, sql = '', tpl  = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()#Conexão fechada com o BD!
        
        except Exception as Expt:
            self.__expt_msg__(Expt)




    def finaliza_conexao(self):
        self.__disconect_BD__()
   



    def __expt_msg__(self, Expt):
        self.finaliza_conexao()
        print(str(Expt))
        return(None)



########################################################################################################################################################################
########################################################################################################################################################################
################# MÉTODOS DE INSERÇÃO:




    def ins_tupl_ger(self, tupla):
        sql = 'DROP TABLE IF EXISTS gerencia_carregada'
        self.__execute_commit__(sql, tupla)
        sql = "insert into gerencias (nome_ger, nome_gest, descricao) VALUES(?, ?, ?)"
        self.__execute_commit__(sql, tupla)
        print("Gerência salva no banco de dados!")






    def ins_gerencia_carregada(self, idd): 
        sql = 'CREATE TABLE IF NOT EXISTS gerencia_carregada(id_ger_carregada INTEGER)'
        self.__execute_commit__(sql)

        tupl_idd = (idd,)
        sql = 'INSERT INTO gerencia_carregada VALUES (?)'
        self.__execute_commit__(sql, tupl_idd)




    def ins_tupl_cliente(self, tupla):
        sql = 'INSERT INTO clientes(nome, cn, genero, dia_nasc, mes_nasc, ano_nasc, descricao, tel1, tel2, email1, email2, uf, cidade, bairro, logradouro, num_resid, tipo_resid, num_ape, nome_cond, cep) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.__execute_commit__(sql, tupla)
        
 



    def ins_tupl_conta(self, tupla):
            sql = "INSERT INTO contas(id_ger, tipo, nome, saldo, taxa_mensal) VALUES(?, ?, ?, ?, ?)"
            self.__execute_commit__(sql, tupla)
            print("Conta salva no banco de dados!")





    def ins_tupl_item_serv(self, tupla):
            sql = "INSERT INTO itens_servs(tipo, nome , descricao, id_subcateg, marca) VALUES( ?, ?, ?, ?, ?)"
            self.__execute_commit__(sql, tupla)





    def ins_tupl_fornecs(self, tupla):
            sql = 'INSERT INTO fornecs(nome, descricao, categoria, subcategoria, uf, cidade, email, tel1, tel2, cnpj) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self.__execute_commit__(sql, tupla)






    def ins_lst_item_serv(self, lst):
            try:
                self.__conect_BD__() 
                sql = "INSERT INTO itens_servs(tipo, nome , descricao, categoria, subcategoria) VALUES( ?, ?, ?, ?, ?)"
                
                for tupla in lst:
                    self.cursor.execute(sql, tupla)
                    self.conn.commit()
                print("Salvo no banco de dados!")
                self.__disconect_BD__()
            
            except Exception as Expt:
                self.__expt_msg__(Expt)
                
    
    def ins_refe(self, **kwargs):
        tipo = kwargs.get('tipo', 'dict')
        arg_ins = kwargs.get('insert', None)
        
        if tipo == 'dict':
            nome = arg_ins.get('nome', 'Sem nome')
            nome_fornec = arg_ins.get('nome_fornec', None)
            id_fornec = arg_ins.get('id_fornec', None)
            tipo = arg_ins.get('tipo', None)
            valor = arg_ins.get('valor', None)
            lst_items = arg_ins.get('lst_items', None)
            id_mov = arg_ins.get('id_mov', 0)
            
            status_mov = arg_ins.get('status_mov', False)
            if status_mov == False:
                status_mov = '0'
            elif status_mov == True:
                status_mov = '1'

            
            
            #Gera uma id aleatória:
            #~ idd_ref = randrange(100000)
            #~ tupl_ref = (idd_ref, nome, nome_fornec, id_fornec, tipo, valor, status_mov, id_mov)
            
            
            tupl_ref = (nome, nome_fornec, id_fornec, tipo, valor, status_mov, id_mov)
            #~ sql = 'INSERT INTO referentes(id, nome, nome_fornec, id_fornec, tipo, valor, status_mov, id_mov) VALUES( ?, ?, ?, ?, ?, ?, ?, ?)'
            
            sql = 'INSERT INTO referentes(nome, nome_fornec, id_fornec, tipo, valor, status_mov, id_mov) VALUES( ?, ?, ?, ?, ?, ?, ?)'
            self.__execute_commit__(sql, tupl_ref)
            idd_ref = self.__lastrowid__()
            print('\n Referente parcialmente salvo 1 de 2. . . ')
            
            
            for elem in lst_items:
                #Lembrando que lista lst_items é uma "lista cadastro"
                #Ou seja, uma lista de dicionários cadastros
                #Dessa forma, o loop varre os elementos do dicionário
                #Colocando-os em uma tupla e executando o INSERT
            
                nome_item = elem.get('nome', '')
                itemServ_idd = elem.get('itemServ_idd', '')
                preco_unit = elem.get('preco_unit', '')
                quant = elem.get('quant', '')
                preco_total = elem.get('preco_total', '')
                
                tupl_comprasList = (nome_item, itemServ_idd, preco_unit, quant, preco_total, idd_ref)
                
                
                sql = 'INSERT INTO compras_list(nome, id_item_serv, valor_unit, quantidade, valor_total, id_refe) VALUES ( ? , ? , ? , ? , ? , ?)'
                self.__execute_commit__(sql, tupl_comprasList)
                
                
                sql = 'SELECT id, nome FROM compras_list WHERE id_refe = ' + str(idd_ref) +';'
                lst = self.__select_fetchall__(sql)
                
                #~ print('\n Referente parcialmente salvo 2 de 2. . .')
            #~ print('\n Referente salvo com sucesso!')
            
        else:
            raise Exception("ins_refe() precisa receber como tipo um 'dict'")



    def ins_move(self, **kwargs):
        tipo = kwargs.get('tipo', 'dict')
        arg_ins = kwargs.get('insert', None)

        if tipo == 'dict':
            refe = arg_ins.get('refe')
            #~ Class = arg_ins.get('class')
            nome = arg_ins.get('nome')
            #Lembrando que a chave 'refe' guarda um dicionário também
            refe = arg_ins.get('refe')
            data = arg_ins.get('data')
            tipo = arg_ins.get('tipo')
            valor = arg_ins.get('valor')
            #Lembrando que a chave 'conta_fav' e 'conta_ced' guardam dicionários também
            conta_fav = arg_ins.get('conta_fav')
            conta_ced = arg_ins.get('conta_ced')
            descr = arg_ins.get('descr')            
            id_conta_fav = conta_fav['idd']
            id_conta_ced = conta_ced['idd']
            status_mov = arg_ins.get('status_mov', False)
            if status_mov == False:
                status_mov = '0'
            elif status_mov == True:
                status_mov = '1'
            

            self.update_conta(**conta_fav)
            self.update_conta(**conta_ced)
            

            #Gera uma id aleatória:
            #~ id_mov = randrange(100000)
            #~ refe['id_mov'] = id_mov
            #~ tupl_mov = (id_mov, nome, descr, data, tipo, id_conta_ced , id_conta_fav, valor)
            #~ sql = 'INSERT INTO move(id, nome, descricao, data, tipo, id_conta_ced , id_conta_fav, valor) VALUES( ?, ?, ?, ?, ?, ?, ?. ?)'
            
            tupl_mov = (nome, descr, data, tipo, id_conta_ced , id_conta_fav, valor)
            sql = 'INSERT INTO move(nome, descricao, data, tipo, id_conta_ced , id_conta_fav, valor) VALUES(?, ?, ?, ?, ?, ?. ?)'
            self.__execute_commit__(sql, tupl_mov)
            id_mov = self.__lastrowid__()
            refe['id_mov'] = id_mov
            print('\n Movimentação parcialmente salva 1 de 2. . .\nSalvando referente da movimentação . . . ')
            self.ins_refe(insert = refe)
            print('Movimentação salva com sucesso!')




########################################################################################################################################################################
########################################################################################################################################################################
#############   MÉTODOS DE COLETA: (FETCH)##############################################################################################################################




    def select_conta_ger(self):
        id_ger = self.fetch_ger_carregada()

        if id_ger != None:
            id_ger = str(id_ger)
            sql = "SELECT nome, tipo, saldo FROM contas WHERE id_ger = '" + id_ger + "'"
            lst_contas =  self.__execute_fetchall__(sql)
            return(lst_contas)
        else:
            return(None)


    def fetchall_contas(self, **kwargs):
        ret_type = kwargs.get('return_type', 'list_dict')
        id_ger = self.fetch_ger_carregada()
        if id_ger != None:
            id_ger = str(id_ger)
            '''ABAIXO O SELECT QUE DEVERÁ SER FEITO APÓS ATUALIZAR O BD'''
            #~ sql = "SELECT id, nome_conta, tipo, saldo, id_ger, taxa_mensal FROM contas WHERE id_ger = '" + id_ger + "'"
            sql = "SELECT id, nome, tipo, saldo, id_ger, taxa_mensal FROM contas WHERE id_ger = '" + id_ger + "'"
            lst_contas = self.__execute_fetchall__(sql)            
            if ret_type == 'list_tuple':
                return(lst_contas)
            
            elif ret_type == 'list_dict':
                lst_ret = []
                for tupl in lst_contas:
                    dict_ret = {}
                    dict_ret['idd'] = tupl[0]
                    dict_ret['nome'] = tupl[1]
                    dict_ret['tipo'] = tupl[2]
                    dict_ret['saldo'] = tupl[3]
                    dict_ret['id_ger'] = tupl[4]
                    dict_ret['taxa_mensal'] = tupl[5]
                    print(dict_ret)
                    lst_ret.append(dict_ret)
                return(lst_ret)
                
        else:
            return(None)


    def fetchall_ref(self, **kwargs):
        tipo = kwargs.get('tipo', 'dict')
        cond = kwargs.get('cond', 'all')
        print(cond)
        lst_ref = []
        dic_ref = {}

        if cond == 'status_move = True':
            sql = 'SELECT id, nome, nome_fornec, id_fornec, tipo, valor, status_mov FROM referentes WHERE status_mov'
            print('\n **** status_move = True ')
        else:
            sql = 'SELECT id, nome, nome_fornec, id_fornec, tipo, valor, status_mov FROM referentes'

        lst_refs = self.__select_fetchall__(sql)
        
        if tipo == 'dict':
            for tupl in lst_refs:
                dic_ref = {}
                dic_ref['idd'] = int(tupl[0])
                dic_ref['nome'] = tupl[1]
                
                #LEMBRAR QUE O IDEAL É BUSCAR O NOME DO FORNECEDOR NA TABELA DE FORNECEDORES
                dic_ref['nome_fornec'] = tupl[2]
                
                if tupl[3] != None:
                    dic_ref['id_fornec'] = int(tupl[3])
                else:
                    dic_ref['id_fornec'] = tupl[3]
                    
                dic_ref['tipo'] = tupl[4]
                dic_ref['valor'] = tupl[5]
                dic_ref['status_mov'] = tupl[6]
                        
                
                id_refe = str(dic_ref['idd'])
                sql = 'SELECT id, nome, id_item_serv, valor_unit, quantidade, valor_total FROM compras_list WHERE id_refe = ' + id_refe + ';'
                lst_itemServ = self.__select_fetchall__(sql)
                
                lst_itens = []
                for elem in lst_itemServ:
                    dic_item = {}
                    dic_item['idd'] = int(elem[0])
                    dic_item['idd_ref'] = int(dic_ref['idd'])
                    
                    #LEMBRAR QUE O IDEAL É BUSCAR O NOME DO ITEM/SERVIÇO NA TABELA DE ITEM/SERVIÇO
                    dic_item['nome'] = elem[1]
                    
                    dic_item['itemServ_idd'] = elem[2]
                    
                    dic_item['preco_unit'] = float(elem[3])
                    dic_item['quant'] = float(elem[4])
                    dic_item['preco_total'] = float(elem[5])
                    lst_itens.append(dic_item)
                
                
                dic_ref['lst_items'] = lst_itens
                lst_ref.append(dic_ref)
                
            return(lst_ref)
        
        elif tipo == 'tuple':
            pass





    def fetch_id_ger(self, nome_ger):
        sql = "SELECT id FROM gerencias WHERE nome_ger = '" + nome_ger+ "'"
        id_ger = self.__execute_fetchone__(sql)
        id_ger = self.__strip_id__(id_ger)
        return(id_ger)





    def fetch_ger_carregada(self):
        sql = 'SELECT id_ger_carregada FROM gerencia_carregada'
        id_ger = self.__execute_fetchone__(sql)
        id_ger = self.__strip_id__(id_ger)
        return(id_ger)





    def __strip_lst_varchar__(self, lst_varchar):
        n = 0
        while n < len(lst_varchar):
            lst_varchar[n] = str(lst_varchar[n])
            lst_varchar[n] = lst_varchar[n].strip( ')' )
            lst_varchar[n] = lst_varchar[n].strip( '(' )
            lst_varchar[n] = lst_varchar[n].strip( "," )
            lst_varchar[n] = lst_varchar[n].strip( "'" )
            n = n+1
        return(lst_varchar)




    def fetchall_categ_str(self, tipo):
        if tipo == 'Item' or tipo == 'Serviço':
            sql = "SELECT categoria FROM categ_serv_item WHERE tipo =  '" + tipo + "'"
            tabl_lst = self.__execute_fetchall__(sql)
            tabl_lst = self.__strip_lst_varchar__(tabl_lst)
            return(tabl_lst)
        else:
            return('Erro: Tipo inválido')




    def fetchall_ger(self):
        sql = "SELECT nome_ger, nome_gest FROM gerencias"
        lst_ger = self.__execute_fetchall__(sql)
        return(lst_ger)




    def __select_id__(self, **kwargs):
        """Função abaixo retorna o id do elemento que satisfaz uma condição dada"""
        table = kwargs.get('table', '')
        cond = kwargs.get('cond', '')
        id_type = kwargs.get('id_type', 'str')
        
        if table == '':
            return(None)
        else:
            if cond == '':
                sql = 'SELECT id FROM ' + table + ';'
            else:
                sql = 'SELECT id FROM ' + table + ' WHERE ' + cond

            idd = self.__execute_fetchone__(sql)
            idd = self.__strip_id__(idd, id_type)
            return(idd)




    def __strip_id__(self, idd, tipo = 'int'):
        idd = str(idd)
        idd = idd.strip(')').strip( '(' ).strip( "," )
        
        if tipo == 'int':
            idd = int(idd)
            return(idd)
        elif tipo == 'str':
            return(idd)
        else:
            raise Exception('Argumento: ', tipo, ' não reconhecido, precisa ser "str" ou "int"')




    def fetchall_subcateg_str(self, tipo, categ_pai):
        sql = "SELECT id FROM categ_serv_item WHERE categoria = '" + categ_pai + "' AND tipo = '" + tipo + "' ;"
        id_pai = self.__execute_fetchone__(sql)
        id_pai = self.__strip_id__(id_pai, 'str')

        sql = "SELECT subcategoria FROM subcateg_serv_item WHERE id_categ = " + id_pai
        tabl_lst = self.__execute_fetchall__(sql)
        tabl_lst = self.__strip_lst_varchar__(tabl_lst)

        return(tabl_lst)


    def fetchall_espec_str(self, tipo, subcateg_pai):
        table_ = 'subcateg_serv_item'
        cond_ = 'subcategoria = "' + subcateg_pai +  '" ;'
        id_pai = self.__select_id__(table = table_, cond = cond_)

        sql = "SELECT especie FROM espec_item_serv WHERE id_pai = " + id_pai + ";"
        tabl_lst = self.__execute_fetchall__(sql)
        tabl_lst = self.__strip_lst_varchar__(tabl_lst)
        return(tabl_lst)


    def fetchall_transac(self):
        sql = 'SELECT transac.nome, transac.valor, fornecs.nome, transac.descricao, dat, contas.nome, id_conta_fav FROM transac INNER JOIN fornecs ON (transac.id_fornec = fornecs.id)  INNER JOIN contas ON (transac.id_conta_ced= contas.id) '
        tupl_lst = self.__execute_fetchall__(sql)
        
  
        
        lst_dic = [] #Lista de dicionários que guardará as transações carregadas
        for elem_tupl in tupl_lst:
            dic_transac = {}
            dic_transac['nome'] = elem_tupl[0]
            dic_transac['valor'] = elem_tupl[1]
            dic_transac['nome_fornec'] = elem_tupl[2]            
            dic_transac['descricao'] = elem_tupl[3]
            dic_transac['data'] = elem_tupl[4]
            dic_transac['nome_conta_ced'] = elem_tupl[5]
            
            id_conta_fav = self.__strip_id__(elem_tupl[6], tipo = 'str')
            sql = 'SELECT nome FROM contas WHERE id = ' + id_conta_fav+ ';'
            nome_conta_fav = self.__execute_fetchone__(sql)
            dic_transac['nome_conta_fav'] = nome_conta_fav[0]
            
            lst_dic.append(dic_transac)
    
        return(lst_dic)


    def fetch_compras_list(self, id_transac):
        id_transac = self.__strip_id__(id_transac, tipo = 'str')
        print('id_transac ',id_transac)
        sql = 'SELECT itens_servs.nome, quantidade, valor_unit, id_item_serv FROM compras_list INNER JOIN itens_servs ON (compras_list.id_item_serv = itens_servs.id) WHERE compras_list.id_transac = ' + id_transac + ';'
        print(sql)

        tupl_lst = self.__execute_fetchall__(sql)
        print(tupl_lst)
       
        lst_dic = []
        for elem_tupl in tupl_lst:
            dic_compras_list = {}
            dic_compras_list['nome'] = elem_tupl[0]
            dic_compras_list['quantidade'] = elem_tupl[1]
            dic_compras_list['valor_unit'] = elem_tupl[2]
            valor_pago = float(elem_tupl[2]) * float(elem_tupl[1])
            dic_compras_list['valor_pago'] = valor_pago
            dic_compras_list['id_item_serv'] = elem_tupl[3]
            lst_dic.append(dic_compras_list)

        return(lst_dic)
        


    def fetchall_table(self, nome_table):
        sql = "SELECT * FROM " + nome_table
        tabela = self.__execute_fetchall__(sql)
        return (tabela)

    def fetchall_itens_servs(self, tipo='', return_tp='tuple', like='', **kwargs):
        tipo = tipo
        return_tp = return_tp
        like = like
        
        if tipo != '':

	
            sql = "SELECT id, nome, descricao, marca, tipo FROM itens_servs WHERE tipo = '" + tipo + "'"
            lst_itens_servs = self.__execute_fetchall__(sql)


            if return_tp == 'tuple':
                return(lst_itens_servs)

            elif return_tp == 'dict':
                lst_aux = []
                for elem_aux in lst_itens_servs:
                    dic_itemServ = {}
                    dic_itemServ['idd'] = elem_aux[0]
                    dic_itemServ['nome'] = elem_aux[1]
                    dic_itemServ['descricao'] = elem_aux[2]
                    dic_itemServ['marca'] = elem_aux[3]
                    dic_itemServ['tipo'] = elem_aux[4]
                    lst_aux.append(dic_itemServ)
                lst_itens_servs = lst_aux
                return(lst_itens_servs)
            elif return_tp != 'tuple' and return_tp == 'dict':
                raise Exception('fetchall_itens_servs(): Erro de argumento, deve ser "dict" ou "tuple"\n','O argumento: ', return_tp,' é inválido.')

        elif tipo == '':

            sql = "SELECT id, nome, descricao, marca, tipo FROM itens_servs"
            lst_itens_servs = self.__execute_fetchall__(sql)

            if return_tp == 'tuple':
                return(lst_itens_servs)
            elif return_tp == 'dict':
                lst_aux = []
                for elem_aux in lst_itens_servs:
                    dic_itemServ = {}
                    dic_itemServ['idd'] = elem_aux[0]
                    dic_itemServ['nome'] = elem_aux[1]
                    dic_itemServ['descricao'] = elem_aux[2]
                    dic_itemServ['marca'] = elem_aux[3]
                    dic_itemServ['tipo'] = elem_aux[4]
                    lst_aux.append(dic_itemServ)
                lst_itens_servs = lst_aux
                return(lst_itens_servs)
            elif return_tp != 'tuple' and return_tp == 'dict':
                raise Exception('fetchall_itens_servs(): Erro de argumento, deve ser "dict" ou "tuple"\n','O argumento: ', return_tp,' é inválido.')

        else:
            return(None)


    def fetchall_clientes(self, **kwargs):
        return_tp = kwargs.get('return_tp', 'tuple')

        sql = "SELECT id, nome, cn, genero, dia_nasc, mes_nasc, ano_nasc, descricao, tel1, tel2, email1, email2, uf, cidade, bairro, logradouro, num_resid, tipo_resid, num_ape, nome_cond, cep FROM clientes"
        lst_clients = self.__execute_fetchall__(sql)

        if return_tp == 'tuple':
            return(lst_clients)
        elif return_tp == 'dict':
            lst_aux = []
            for elem_aux in lst_clients:
                dic_clients = {}
                dic_clients['idd'] = elem_aux[0]
                dic_clients['nome'] = elem_aux[1]
                dic_clients['cn'] = elem_aux[2]
                dic_clients['genero'] = elem_aux[3]
                dic_clients['dia_nasc'] = elem_aux[4]
                dic_clients['mes_nasc'] = elem_aux[5]
                dic_clients['ano_nasc'] = elem_aux[6]
                dic_clients['descricao'] = elem_aux[7]
                dic_clients['tel1'] = elem_aux[8]
                dic_clients['tel2'] = elem_aux[9]
                dic_clients['email1'] = elem_aux[10]
                dic_clients['email2'] = elem_aux[11]
                dic_clients['uf'] = elem_aux[12]
                dic_clients['cidade'] = elem_aux[13]
                dic_clients['bairro'] = elem_aux[14]
                dic_clients['logradouro'] = elem_aux[15]
                dic_clients['num_resid'] = elem_aux[16]
                dic_clients['tipo_resid'] = elem_aux[17]
                dic_clients['num_ape'] = elem_aux[18]
                dic_clients['nome_cond'] = elem_aux[19]
                dic_clients['cep'] = elem_aux[20]
                lst_aux.append(dic_clients)
            lst_clients = lst_aux
            return(lst_clients)
        elif return_tp != 'tuple' and return_tp == 'dict':
            raise Exception('fetchall_clientes(): Erro de argumento, deve ser "dict" ou "tuple"\n','O argumento: ', return_tp,' é inválido.')






    def fetchall_fornec(self, **kwargs):
        """Método que retorna todos os fornecedores"""

        return_tp = kwargs.get('return_tp', 'tuple')
        like = kwargs.get('like', '')
        
        if like == '':
            sql = "SELECT id, nome, descricao, categoria, subcategoria, uf, cidade, email, tel1, tel2 , cnpj FROM fornecs"
            lst_fornecs = self.__execute_fetchall__(sql)

            if return_tp == 'tuple':
                return(lst_fornecs)

            elif return_tp == 'dict':
                lst_aux = []
                for elem_aux in lst_fornecs:
                    dic_fornecs = {}
                    dic_fornecs['idd'] = elem_aux[0]
                    dic_fornecs['nome'] = elem_aux[1]
                    dic_fornecs['descricao'] = elem_aux[2]
                    dic_fornecs['categoria'] = elem_aux[3]
                    dic_fornecs['subcategoria'] = elem_aux[4]
                    dic_fornecs['uf'] = elem_aux[5]
                    dic_fornecs['cidade'] = elem_aux[6]
                    dic_fornecs['email'] = elem_aux[7]
                    dic_fornecs['tel1'] = elem_aux[8]
                    dic_fornecs['tel2'] = elem_aux[9]
                    dic_fornecs['cnpj'] = elem_aux[10]
                    lst_aux.append(dic_fornecs)
                lst_fornecs = lst_aux
                return(lst_fornecs)
            elif return_tp != 'tuple' and return_tp == 'dict':
                raise Exception('fetchall_fornec(): Erro de argumento, deve ser "dict" ou "tuple"\n','O argumento: ', return_tp,' é inválido.')

        else:

            like = like + '%'
            sql = 'SELECT id, nome, descricao, categoria, subcategoria, uf, cidade, email, tel1, tel2 , cnpj FROM fornecs WHERE nome  LIKE "' + like + '" ;'
            lst_fornecs = self.__execute_fetchall__(sql)

            if return_tp == 'tuple':
                return(lst_fornecs)

            elif return_tp == 'dict':
                lst_aux = []
                for elem_aux in lst_fornecs:
                    dic_fornecs = {}
                    dic_fornecs['idd'] = elem_aux[0]
                    dic_fornecs['nome'] = elem_aux[1]
                    dic_fornecs['descricao'] = elem_aux[2]
                    dic_fornecs['categoria'] = elem_aux[3]
                    dic_fornecs['subcategoria'] = elem_aux[4]
                    dic_fornecs['uf'] = elem_aux[5]
                    dic_fornecs['cidade'] = elem_aux[6]
                    dic_fornecs['email'] = elem_aux[7]
                    dic_fornecs['tel1'] = elem_aux[8]
                    dic_fornecs['tel2'] = elem_aux[9]
                    dic_fornecs['cnpj'] = elem_aux[10]
                    lst_aux.append(dic_fornecs)
                lst_fornecs = lst_aux
                return(lst_fornecs)
            elif return_tp != 'tuple' and return_tp == 'dict':
                raise Exception('fetchall_fornec(): Erro de argumento, deve ser "dict" ou "tuple"\n','O argumento: ', return_tp,' é inválido.')





    def fetch_id_fornec(self, nome):
        sql = "SELECT id FROM fornec WHERE nome = " + nome
        id_fornec = self.__execute_fetchone__(sql)
        id_fornec = self.__strip_id__(id_fornec)
        return(id_fornec)


    
    
    
    def fetch_id_itens_servs(self, nome, tipo):
            sql = "SELECT id FROM itens_servs WHERE nome = " + nome + " AND tipo = " + tipo
            id_itens_servs = self.__execute_fetchone__(sql)
            id_itens_servs = self.__strip_id__(id_itens_servs)
            return(id_itens_servs)



########################################################################################################################################################################
########################################################################################################################################################################
##############       MÉTODOS DE EXCLUSÃO: (DROP)########################################################################################################################
########################################################################################################################################################################


    #Dispensando a tabela da gerencia carregada - REVER ESSA METODOLOGIA
    def drop_gerencia_carregada(self):
        sql = 'DROP TABLE IF EXISTS gerencia_carregada'
        self.__execute_commit__(sql)




    #Deletando algum cliente
    def delete_cliente(self, client_id):
        if type(client_id) != str:
            client_id = str(client_id)

        #sql = 'DELETE FROM clientes WHERE id = ?'
        #self.cursor.execute(sql, client_id)
        sql = 'DELETE FROM clientes WHERE id = ' + client_id + ';'
        self.__execute_commit__(sql)


    #Deletando algum fornecedor
    def delete_fornec(self, fornec_id):
        if type(fornec_id) != str:
            fornec_id = str(fornec_id) + ';'

        #~ sql = 'DELETE FROM fonecs WHERE id = ?;'
        #~ self.cursor.execute(sql, fornec_id)
        sql = 'DELETE FROM fonecs WHERE id = ' + fornec_id + ';'
        self.__execute_commit__(sql)



    #Deletando algum fornecedor
    def delete_itemServ(self, itemServ_id):
        if type(itemServ_id) != str:
            itemServ_id = str(itemServ_id)

        #~ sql = 'DELETE FROM itens_servs WHERE id = ?;'
        #~ self.cursor.execute(sql, itemServ_id)
        sql = 'DELETE FROM itens_servs WHERE id = ' + itemServ_id + ';'
        self.__execute_commit__(sql)


########################################################################################################################################################################
########################################################################################################################################################################
#############   MÉTODOS DE MODIFICAÇÃO: (UPDATE)

    #Modificação de item ou serviço
    def update_conta(self, **kwargs):
        
        print(kwargs)
        
        idd = str(kwargs.get('idd'))
        nome = kwargs.get('nome', '')
        id_ger = str(kwargs.get('id_ger', ''))
        saldo = str(kwargs.get('saldo', ''))
        taxa_mensal = str(kwargs.get('taxa_mensal', ''))
        tipo = kwargs.get('tipo', '')
        
        print('\n\n\n', idd,nome , id_ger,saldo ,taxa_mensal ,tipo )
        
        
        strAux = ''
        if id_ger != '' and id_ger != None:
            strAux = strAux + ' id_ger = ' + id_ger + ','
        
        if saldo != '' and saldo != None:
            strAux = strAux + ' saldo = ' + saldo + ','
        
        if taxa_mensal != '' and taxa_mensal != '' :
            strAux = strAux + ' taxa_mensal = ' + taxa_mensal + ','
        
        if tipo != '' and tipo != '':
            strAux = strAux + ' tipo = "' + tipo + '",'
        
        if nome != '' and nome != '' :
            strAux = strAux + ' nome = "' + nome + '",'
        

        if strAux != '':
            strAux = strAux.strip(', ')
            
        sql = 'UPDATE contas SET ' + strAux + ' WHERE id = ' + idd + ';'
        print(sql)
        self.__execute_commit__(sql)




    #Modificação de item ou serviço
    def update_itemServ(self, itemServ_id, **kwargs):
        if type(itemServ_id) != str:
            itemServ_id = str(itemServ_id)
        
        strAux = ''
        nome = kwargs.get('nome', '')
        if nome != '':
            strAux = strAux + ' nome = "' + nome + '",'
        tipo = kwargs.get('tipo', '')
        if tipo != '':
            strAux = strAux + ' tipo = "' + tipo + '",'
        
        descr = kwargs.get('descr', '')
        if descr != '':
            strAux = strAux + ' descricao = "' + descr + '",'
        
        categoria = kwargs.get('categoria', '')
        if categoria != '':
            strAux = strAux + ' categoria = "' + categoria + '",'
        
        subcategoria = kwargs.get('subcategoria', '')
        if subcategoria != '':
            strAux = strAux + ' subcategoria = "' + subcategoria + '",'
        
        marca = kwargs.get('marca', '')
        if marca != '':
            strAux = strAux + ' marca = "' + marca + '",'

        if strAux != '':
            strAux = strAux.strip(', ')
            
        try:
            sql = 'UPDATE itens_servs SET ' + strAux + ' WHERE id = ' + itemServ_id + ';'
            self.__conect_BD__()#Conexão aberta com o BD!
            self.cursor.execute(sql)
            self.conn.commit()
            self.__disconect_BD__()#Conexão fechada com o BD!
        except Exception as Expt:
            self.__expt_msg__(Expt)
            


    #Modificação cliente
    def update_cliente(self, cliente_id, **kwargs):
        if type(cliente_id) != str:
            cliente_id = str(cliente_id)
        strAux = ''
        nome = kwargs.get('nome', '')
        if nome != '':
            strAux = strAux + ' nome = "' + nome + '",'
        
        cn = kwargs.get('cn', '')
        if cn != '':
            strAux = strAux + ' cn = "' + cn + '",'
            
        genero = kwargs.get('genero', '')
        if genero != '':
            strAux = strAux + ' genero = "' + genero + '",'
        
        dia_nasc = kwargs.get('dia_nasc', '')
        if dia_nasc != '':
            strAux = strAux + ' dia_nasc = "' + dia_nasc + '",'
        
        mes_nasc = kwargs.get('mes_nasc', '')
        if mes_nasc != '':
            strAux = strAux + ' mes_nasc = "' + mes_nasc + '",'
        
        ano_nasc = kwargs.get('ano_nasc', '')
        if ano_nasc != '':
            strAux = strAux + ' ano_nasc = "' + ano_nasc + '",'
        
        descr = kwargs.get('descr', '')
        if descr != '':
            strAux = strAux + ' descricao = "' + descr + '",'
        
        tel1 = kwargs.get('tel1', '')
        if tel1 != '':
            strAux = strAux + ' tel1 = "' + tel1 + '",'
        
        tel2 = kwargs.get('tel2', '')
        if tel2 != '':
            strAux = strAux + ' tel2 = "' + tel2 + '",'
        
        email1 = kwargs.get('email1', '')
        if email1 != '':
            strAux = strAux + ' email1 = "' + email1 + '",'
        
        email2 = kwargs.get('email2', '')
        if email2 != '':
            strAux = strAux + ' email2 = "' + email2 + '",'
        
        uf = kwargs.get('uf', '')
        if uf != '':
            strAux = strAux + ' uf = "' + uf + '",'
        
        cidade = kwargs.get('cidade', '')
        if cidade != '':
            strAux = strAux + ' cidade = "' + cidade + '",'
        
        bairro = kwargs.get('bairro', '')
        if bairro != '':
            strAux = strAux + ' bairro = "' + bairro + '",'
        
        logradouro = kwargs.get('logradouro', '')
        if logradouro != '':
            strAux = strAux + ' logradouro = "' + logradouro + '",'
        
        num_resid = kwargs.get('num_resid', '')
        if num_resid != '':
            strAux = strAux + ' num_resid = "' + num_resid + '",'
        
        tipo_resid = kwargs.get('tipo_resid', '')
        if tipo_resid != '':
            strAux = strAux + ' tipo_resid = "' + tipo_resid + '",'
        
        num_ape = kwargs.get('num_ape', '')
        if num_ape != '':
            strAux = strAux + ' num_ape = "' + num_ape + '",'
        
        nome_cond = kwargs.get('nome_cond', '')
        if nome_cond != '':
            strAux = strAux + ' nome_cond = "' + nome_cond + '",'
        
        cep = kwargs.get('cep', '')
        if cep != '':
            strAux = strAux + ' cep = "' + cep + '", '
        
        if strAux != '':
            strAux = strAux.strip(', ')
        
        
        sql = 'UPDATE clientes SET ' + strAux + ' WHERE id = ' + cliente_id + ';'
        self.__execute_commit__(sql)




    #######################################
    #Modificação cliente
    def update_fornec(self, fornec_id, **kwargs):
        if type(fornec_id) != str:
            fornec_id = str(fornec_id)
        
        strAux = ''
        nome = kwargs.get('nome', '')
        if nome != '':
            strAux = strAux + ' nome = "' + nome + '",'
        
        cnpj = kwargs.get('cnpj', '')
        if cnpj != '':
            strAux = strAux + ' cnpj = "' + cnpj + '",'
            
        categoria = kwargs.get('categoria', '')
        if categoria != '':
            strAux = strAux + ' categoria = "' + categoria + '",'
        
        subcategoria = kwargs.get('subcategoria', '')
        if subcategoria != '':
            strAux = strAux + ' subcategoria = "' + subcategoria + '",'
        
        descr = kwargs.get('descr', '')
        if descr != '':
            strAux = strAux + ' descricao = "' + descr + '",'
        
        tel1 = kwargs.get('tel1', '')
        if tel1 != '':
            strAux = strAux + ' tel1 = "' + tel1 + '",'
        
        tel2 = kwargs.get('tel2', '')
        if tel2 != '':
            strAux = strAux + ' tel2 = "' + tel2 + '",'
        
        
        #PRECISO VER COMO FAREI COM O EMAIL!
        #AQUI TEM 2 EMAILS E NO BD SÓ TEM 1
        
        email1 = kwargs.get('email1', '')
        if email1 != '':
            strAux = strAux + ' email = "' + email1 + '",'
        
        email2 = kwargs.get('email2', '')
        if email2 != '':
            strAux = strAux + ' email2 = "' + email2 + '",'
        
        uf = kwargs.get('uf', '')
        if uf != '':
            strAux = strAux + ' uf = "' + uf + '",'
        
        cidade = kwargs.get('cidade', '')
        if cidade != '':
            strAux = strAux + ' cidade = "' + cidade + '",'
        
        bairro = kwargs.get('bairro', '')
        if bairro != '':
            strAux = strAux + ' bairro = "' + bairro + '",'
        
        logradouro = kwargs.get('logradouro', '')
        if logradouro != '':
            strAux = strAux + ' logradouro = "' + logradouro + '",'
        
        num_resid = kwargs.get('num_resid', '')
        if num_resid != '':
            strAux = strAux + ' num_resid = "' + num_resid + '",'
        
        tipo_resid = kwargs.get('tipo_resid', '')
        if tipo_resid != '':
            strAux = strAux + ' tipo_resid = "' + tipo_resid + '",'
        
        num_ape = kwargs.get('num_ape', '')
        if num_ape != '':
            strAux = strAux + ' num_ape = "' + num_ape + '",'
        
        nome_cond = kwargs.get('nome_cond', '')
        if nome_cond != '':
            strAux = strAux + ' nome_cond = "' + nome_cond + '",'
        
        cep = kwargs.get('cep', '')
        if cep != '':
            strAux = strAux + ' cep = "' + cep + '", '
        
        if strAux != '':
            strAux = strAux.strip(', ')
        
  
        sql = 'UPDATE fornecs SET ' + strAux + ' WHERE id = ' + fornec_id + ';'
        self.__execute_commit__(sql)



#######################################################################################################################################
#######################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################



class conexao_BD_ender:

    def __init__(self):
        try:
            self.conn = sqlite3.connect("BD_ender.db")
            self.con_status = True
            self.conn.commit()
            self.cursor = self.conn.cursor()
            self.conn.close()
            self.con_status = False
    
        except Exception as Expt:
            self.__expt_msg__(Expt)




    def __conect_BD__(self):
        try:
            if(self.con_status == False):
                self.conn = sqlite3.connect("BD_ender.db")
                self.con_status = True
                self.conn.commit()
                self.cursor = self.conn.cursor()
                
        except Exception as Expt:
            self.__expt_msg__(Expt)




    def __disconect_BD__(self):
        self.con_status = False
        self.conn.close()




    def finaliza_conexao(self):
        self.__disconect_BD__()




    def __select_fetchone__(self, sql):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            elem = self.cursor.fetchone()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(elem)
        except Exception as Expt:
            self.__expt_msg__(Expt)




    def __select_fetchall__(self, sql):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            self.cursor.execute(sql)
            lst = self.cursor.fetchall()
            self.__disconect_BD__()#Conexão fechada com o BD!
            return(lst)
        except Exception as Expt:
            self.__expt_msg__(Expt)




    def __execute_commit__(self, sql, tpl = ''):
        self.__conect_BD__()#Conexão aberta com o BD!
        try:
            if tpl == '':
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, tpl)
            self.conn.commit()
            self.__disconect_BD__()#Conexão fechada com o BD!
        
        except Exception as Expt:
            self.__expt_msg__(Expt)




    def __expt_msg__(self, Expt):
        self.finaliza_conexao()
        print(str(Expt))
        return(None)




    def fetch_ender_rua(self, rua):
        if type(rua) != str:
            rua = str(rua)

        lst_ender = [] # Lista que será retornada pelo método. Lista de dicionários contendo os endereços
        
        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE RUA =  "' + rua + '" ;'
        lst_tupl = self.__select_fetchall__(sql) #lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['tipo'] = elem_tupl[3]
            lst_ender.append(dic_ender)

        for elem_dic in lst_ender:
            id_bairro = elem_dic['id_bairro']
            del(elem_dic['id_bairro']) #Exclui essa posição, não mais necessária
            
            sql = 'SELECT ID_CIDADES, BAIRROS FROM TB_BAIRROS WHERE ID = ' + id_bairro + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_cidade'] = str(tupla_ender[0])
            elem_dic['bairro'] = tupla_ender[1]
            
        for elem_dic in lst_ender:
            id_cidade = elem_dic['id_cidade']
            del(elem_dic['id_cidade']) #Exclui essa posição, não mais necessária
            
            sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID = ' + id_cidade + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_estado'] = str(tupla_ender[0])
            elem_dic['cidade'] = tupla_ender[1]
            
        for elem_dic in lst_ender:
            id_estado = elem_dic['id_estado']
            del(elem_dic['id_estado'])
            
            sql = 'SELECT ESTADO, UF FROM TB_ESTADOS WHERE ID = ' + id_estado + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['estado'] = tupla_ender[0]
            elem_dic['uf'] = tupla_ender[1]
            elem_dic['pais'] = 'Brasil'

        return(lst_ender)




    def fetch_ender_cep(self, cep):
        cep = str(cep)
        dic_ender = {} #Dicionário que será retornado pelo método, contendo o endereço
        
        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE CEP = ' + cep + ';'
        tupla_ender = self.__select_fetchone__(sql)
        if tupla_ender != None:
            id_bairro = str(tupla_ender[0])
            dic_ender['rua'] = tupla_ender[1]
            dic_ender['cep'] = str(tupla_ender[2])
            dic_ender['tipo'] = tupla_ender[3]
            
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
            
            return(dic_ender)
        else:
            return(None)
        
      




    def fetch_ender_rua_like(self, rua):
        if type(rua) != str:
            rua = str(rua)
        rua = rua + '%'
        lst_ender = [] # Lista que será retornada pelo método. Lista de dicionários contendo os endereços
        
        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE RUA LIKE  "' + rua + '" ;'
        lst_tupl = self.__select_fetchall__(sql) #lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['tipo'] = elem_tupl[3]
            lst_ender.append(dic_ender)

        for elem_dic in lst_ender:
            id_bairro = elem_dic['id_bairro']
            del(elem_dic['id_bairro']) #Exclui essa posição, não mais necessária
            
            sql = 'SELECT ID_CIDADES, BAIRROS FROM TB_BAIRROS WHERE ID = ' + id_bairro + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_cidade'] = str(tupla_ender[0])
            elem_dic['bairro'] = tupla_ender[1]
            
        for elem_dic in lst_ender:
            id_cidade = elem_dic['id_cidade']
            del(elem_dic['id_cidade']) #Exclui essa posição, não mais necessária
            
            sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID = ' + id_cidade + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_estado'] = str(tupla_ender[0])
            elem_dic['cidade'] = tupla_ender[1]
            
        for elem_dic in lst_ender:
            id_estado = elem_dic['id_estado']
            del(elem_dic['id_estado'])
            
            sql = 'SELECT ESTADO, UF FROM TB_ESTADOS WHERE ID = ' + id_estado + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['estado'] = tupla_ender[0]
            elem_dic['uf'] = tupla_ender[1]
            elem_dic['pais'] = 'Brasil'

        return(lst_ender)


    def fetch_ender_cep_like(self, cep):
        cep = str(cep)
        cep = cep + '%'
        lst_ender = [] # Lista que será retornada pelo método. Lista de dicionários contendo os endereços
        sql = 'SELECT ID_BAIRRO, RUA, CEP, TIPO FROM TB_RUAS WHERE CEP LIKE  "' + cep + '" ;'
        lst_tupl = self.__select_fetchall__(sql) #lst_tupl guarda a lista de tuplas retornada pela __select_fetchall__()
        for elem_tupl in lst_tupl:
            dic_ender = {}
            dic_ender['id_bairro'] = str(elem_tupl[0])
            dic_ender['rua'] = elem_tupl[1]
            dic_ender['cep'] = str(elem_tupl[2])
            dic_ender['tipo'] = elem_tupl[3]
            lst_ender.append(dic_ender)

        for elem_dic in lst_ender:
            id_bairro = elem_dic['id_bairro']
            del(elem_dic['id_bairro']) #Exclui essa posição, não mais necessária
            
            sql = 'SELECT ID_CIDADES, BAIRROS FROM TB_BAIRROS WHERE ID = ' + id_bairro + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_cidade'] = str(tupla_ender[0])
            elem_dic['bairro'] = tupla_ender[1]
            
        for elem_dic in lst_ender:
            id_cidade = elem_dic['id_cidade']
            del(elem_dic['id_cidade']) #Exclui essa posição, não mais necessária
            
            sql = 'SELECT ID_ESTADO, CIDADE FROM TB_CIDADES WHERE ID = ' + id_cidade + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['id_estado'] = str(tupla_ender[0])
            elem_dic['cidade'] = tupla_ender[1]
            
        for elem_dic in lst_ender:
            id_estado = elem_dic['id_estado']
            del(elem_dic['id_estado'])
            
            sql = 'SELECT ESTADO, UF FROM TB_ESTADOS WHERE ID = ' + id_estado + ';'
            tupla_ender = self.__select_fetchone__(sql)
            elem_dic['estado'] = tupla_ender[0]
            elem_dic['uf'] = tupla_ender[1]
            elem_dic['pais'] = 'Brasil'

        return(lst_ender)


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
            
        return(lst_ender)

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
            return(None)
        else:
            if cep != '':
                dic_ender = self.fetch_ender_cep(cep)
            else:
                dic_ender = self.fetch_ender_rua(rua)
                
            return(dic_ender)




