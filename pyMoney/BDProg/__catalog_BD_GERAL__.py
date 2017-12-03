import sqlite3

'''
    sql = 'create table if not exists contas_cred(id INTEGER PRIMARY KEY, id_ger INTEGER, nome_conta VARCHAR(55), descricao VARCHAR(100), id_refe, FOREIGN KEY (id_ger) REFERENCES gerencias (id), FOREIGN KEY (id_refe) REFERENCES referente_cred (id))'
    cur.execute(sql)

    sql = 'create table if not exists referente_cred(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), descricao VARCHAR(100), tipo VARCHAR(20), referente INTEGER, cedente INTEGER, FOREIGN KEY (referente) REFERENCES referentes (id), FOREIGN KEY (cedente) REFERENCES contas_cred (id))'
    cur.execute(sql)
    con.commit()
'''

def iniciaBD_prog():
    # Cria uma conexão e um cursor
    con = sqlite3.connect('BD_prog.db')
    con.execute('pragma foreign_keys=ON')
    cur = con.cursor()

    #Criamos uma string de nome sql pela qual encapsulamos as sentenças para o sqlite:
    sql = ''
    sql = 'CREATE TABLE IF NOT EXISTS gerencias(id INTEGER PRIMARY KEY, nome_ger VARCHAR(35), nome_gest VARCHAR(35), descricao VARCHAR(100))'
    cur.execute(sql)


    #~ sql = 'DROP TABLE IF EXISTS contas'
    #~ cur.execute(sql)
    #~ con.commit()
    #~ print('droped')

    sql = 'CREATE TABLE IF NOT EXISTS contas(id INTEGER PRIMARY KEY, id_ger INTEGER, tipo VARCHAR(8), nome VARCHAR(55), saldo , taxa_mensal FLOAT,  FOREIGN KEY (id_ger) REFERENCES gerencias (id))'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS vendas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), tipo VARCHAR(20), id_move_NE INTEGER, id_cliente INTEGER, FOREIGN KEY (id_cliente) REFERENCES clientes (id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS vendas_list(id INTEGER PRIMARY KEY AUTOINCREMENT, id_refe, id_item_serv, quantidade FLOAT, valor_unit DOUBLE PRECISION, valor_total DOUBLE PRECISION, FOREIGN KEY (id_refe) REFERENCES referentes (id), FOREIGN KEY (id_item_serv) REFERENCES itens_servs (id))'
    cur.execute(sql)
    con.commit()


    sql = 'DROP TABLE IF EXISTS move'
    cur.execute(sql)
    con.commit()
    print('droped')

    #~ #Criando tabela de transacoes:
    #~ sql = CREATE TABLE transac(id INTEGER PRIMARY KEY, nome VARCHAR(55), descricao VARCHAR[65], dat DATE(11), tipo VARCHAR(20), id_conta_ced INTEGER, id_conta_fav INTEGER, valor DOUBLE PRECISION, id_fornec INTEGER, FOREIGN KEY(id_conta_fav) REFERENCES contas(id), FOREIGN KEY (id_conta_ced) REFERENCES contas(id), FOREIGN KEY (id_fornec) REFERENCES fornecs(id))'
    #~ cur.execute(sql)
    #~ con.commit()
  
    #Criando tabela de movimentações:
    sql = 'CREATE TABLE IF NOT EXISTS move(id INTEGER PRIMARY KEY, nome VARCHAR(55), descricao TEXT, data DATE(11), tipo VARCHAR(20), id_conta_ced INTEGER, id_conta_fav INTEGER, valor DOUBLE PRECISION, id_refe INTEGER, FOREIGN KEY(id_refe) REFERENCES referentes(id), FOREIGN KEY(id_conta_fav) REFERENCES contas(id), FOREIGN KEY (id_conta_ced) REFERENCES contas(id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS compras(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), tipo VARCHAR(20), id_move_NE INTEGER, id_fornec INTEGER, FOREIGN KEY (id_fornec) REFERENCES fornecs (id))'
    cur.execute(sql)
    con.commit()


    #~ sql = 'DROP TABLE IF EXISTS compras_list'
    #~ cur.execute(sql)
    #~ con.commit()
    #~ print('droped')

    sql = 'CREATE TABLE IF NOT EXISTS compras_list(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(40), id_refe, id_item_serv, quantidade FLOAT, valor_unit DOUBLE PRECISION, valor_total DOUBLE PRECISION, FOREIGN KEY (id_refe) REFERENCES referentes (id), FOREIGN KEY (id_item_serv) REFERENCES itens_servs (id))'
    cur.execute(sql)
    con.commit()
    
    
   # sql = 'DROP TABLE IF EXISTS referentes'
   # cur.execute(sql)
   # con.commit()
   # print('droped')

    sql = 'CREATE TABLE IF NOT EXISTS referentes(id INTEGER PRIMARY KEY, nome VARCHAR(55), nome_fornec VARCHAR(40), id_fornec INTEGER, tipo VARCHAR(20), subtipo VARCHAR(20), valor FLOAT, id_lst_items INTEGER,  status_mov BOOLEAN, id_mov INTEGER,  FOREIGN KEY (id_fornec) REFERENCES fornecs (id), FOREIGN KEY (id_mov) REFERENCES move (id))'
    cur.execute(sql)
    con.commit()


    #Criando tabela de categoria de serviços:
    sql = 'CREATE TABLE IF NOT EXISTS categ_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria VARCHAR(25), tipo VARCHAR(12))'
    cur.execute(sql)
    con.commit()

    #Criando tabela de Sub_categorias de serviços:
    sql = 'CREATE TABLE IF NOT EXISTS subcateg_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, id_categ INTEGER, subcategoria VARCHAR(22) UNIQUE, FOREIGN KEY (id_categ) REFERENCES categ_serv_item(id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS espec_item_serv(id INTEGER PRIMARY KEY AUTOINCREMENT, id_pai INTEGER, especie VARCHAR(30), FOREIGN KEY (id_pai) REFERENCES subcateg_serv_item(id));'
    cur.execute(sql)
    con.commit()


    #Criando tabela de categorias de fornecedores:
    sql = 'CREATE TABLE IF NOT EXISTS categ_fornec(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria VARCHAR(25) UNIQUE)'
    cur.execute(sql)
    con.commit()

    #Criando tabela de Sub_categorias  de fornecedores:
    sql = 'CREATE TABLE IF NOT EXISTS subcateg_fornec(id INTEGER PRIMARY KEY AUTOINCREMENT, id_categ INTEGER, subcategoria VARCHAR(22) UNIQUE, FOREIGN KEY (id_categ) REFERENCES categ_fornec(id))'
    cur.execute(sql)
    con.commit()
    

    #Criando tabela de clientes:
    sql = 'CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), cn INTEGER, genero VARCHAR(15), dia_nasc VARCHAR(3), mes_nasc VARCHAR(3), ano_nasc VARCHAR(5), descricao VARCHAR(100), tel1 VARCHAR(18), tel2 VARCHAR(18), email1 VARCHAR(25), email2 VARCHAR(25), uf VARCHAR(3), cidade VARCHAR(25), bairro VARCHAR(25), logradouro VARCHAR(30), num_resid VARCHAR(8), tipo_resid VARCHAR(18), num_ape VARCHAR(8), nome_cond VARCHAR(25), cep VARCHAR(21))'
    cur.execute(sql)
    con.commit()

    #Criando tabela de Fornecedores:
    sql = 'CREATE TABLE IF NOT EXISTS fornecs(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), descricao VARCHAR(100), categoria VARCHAR(20), subcategoria VARCHAR(20), uf VARCHAR(3), cidade VARCHAR(25), email VARCHAR(30), tel1 INTEGER, tel2 INTEGER, cnpj INTEGER)'
    cur.execute(sql)
    con.commit()

    #Criando tabela de Funcionários:
    sql = 'CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), descricao VARCHAR(100), categoria VARCHAR(20), subcategoria VARCHAR(20), cidade VARCHAR(25), email VARCHAR(30), tel1 INTEGER, tel2 INTEGER, cpf INTEGER)'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS itens_servs_2(id INTEGER PRIMARY KEY AUTOINCREMENT, tipo VARCHAR(11), nome VARCHAR(55), descricao VARCHAR(100), id_subcateg INTEGER, marca VARCHAR(35))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS estoq(id INTEGER PRIMARY KEY AUTOINCREMENT, id_item INTEGER, valor_unit_pago FLOAT, id_compra, FOREIGN KEY (id_item) REFERENCES itens_servs(id), FOREIGN KEY (id_compra) REFERENCES compras(id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXIST tabl_vendas_itens(id INTEGER PRIMARY AUTOINCREMENT, id_item INTEGER, quant INTEGER, valor_unit DOUBLE PRECISION, FOREIGN KEY (id_item) REFERENCES estoq(id))'
    sql = 'CREATE TABLE IF NOT EXIST tabl_vendas_servs(id INTEGER PRIMARY AUTOINCREMENT, id_serv INTEGER, valor DOUBLE PRECISION, FOREIGN KEY (itens_servs) REFERENCES estoq(id))'

    con.close()
    del(con, cur, sql)



def main(args):
    iniciaBD_prog()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
