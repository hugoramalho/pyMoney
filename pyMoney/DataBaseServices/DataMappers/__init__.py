import sqlite3


def conecta():
    con = sqlite3.connect('BD_prog.db')
    cur = con.cursor()

    return (con, cur)


def catalogando_categoria(con, cur):
    sql = 'create table if not exists categ_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria VARCHAR(25), __tipo VARCHAR(11));'
    cur.executescript(sql)
    con.commit()

    sql = '''
    create table if not exists categ_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria VARCHAR(25), __tipo VARCHAR(11));


    INSERT INTO categ_serv_item VALUES (NULL, "Alimento", "Item" );
    INSERT INTO categ_serv_item VALUES (NULL, "Eletrônicos", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Ferramentas", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Cosmético", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Higiene", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Vestiário", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Móveis", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Decoração", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, 'Produtos de limpeza', "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Escritório", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, 'Utensílios domésticos', "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "Automóvel", "Item");
    INSERT INTO categ_serv_item VALUES (NULL, "PetShop", "Item");

    '''
    try:
        con.execute('pragma foreign_keys=ON');
        cur.executescript(sql)
        con.commit()
        print("Categorias cadastradas.\nSem erro.")
    except Exception as Expt:
        print(str(Expt))
        return (str(Expt))


def catalogando_subcategoria(con, cur):
    sql = 'create table if not exists subcateg_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, id_pai INTEGER, subcategoria VARCHAR(30), FOREIGN KEY (id_pai) REFERENCES categ_serv_item(id));'
    cur.executescript(sql)
    con.commit()

    sql = '''               

    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Condimentos");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Carnes");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Bebibas alcólicas");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Bebidas");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Padaria");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Horti fruti");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Óleos");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Graos e cereais");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Alimento"), "Embutidos");


    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Automóvel"), "Combustível");


    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Eletrônicos"),"Informática");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Eletrônicos"),"Telefonia");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Eletrônicos"),"Eletrodomésticos");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Eletrônicos"),"Iluminação");


    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Cosmético"),"Perfumaria");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Cosmético"),"Maquiagem");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Cosmético"),"Estética pessoal");


    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Ferramentas"),"Alvenaria");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Ferramentas"),"Marcenaria");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Ferramentas"),"Ferramentas Elétricas");


    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Escritório"), "Leitura");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Escritório"), "Utensílios");

    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Produtos de limpeza"),"Limpeza geral");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Produtos de limpeza"),"Lavanderia");

    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Utensílios domésticos"),"Limpeza");

    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "Higiene"),"Higiene Pessoal");


    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "PetShop"), "Caninos\felinos");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "PetShop"), "Aves");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "PetShop"), "Roedores");
    INSERT INTO subcateg_serv_item VALUES (NULL, (SELECT id FROM categ_serv_item WHERE categoria = "PetShop"), "Peixes");
    '''
    try:
        cur.executescript(sql)
        con.commit()
        print("Subcategorias cadastradas.\nSem erro.")
    except Exception as Expt:
        print(str(Expt))
        return (str(Expt))


def catalogando_especie(con, cur):
    sql = 'create table if not exists espec_item_serv(id INTEGER PRIMARY KEY AUTOINCREMENT, id_pai INTEGER, especie VARCHAR(30), FOREIGN KEY (id_pai) REFERENCES subcateg_serv_item(id));'
    cur.executescript(sql)
    con.commit()
    sql = '''
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Combustível'), "Gasolina comum");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Combustível'), "Gasolina especial");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Combustível'), "Álcool veicular");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Combustível'), "Diesel");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Combustível'), "Gás veicular");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Combustível'), "Querosene");



    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Óleos"), "Azeite de oliva");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Óleos"), "Óleo de soja");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Óleos"), "Óleo de canola");

    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Sabão em barra");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Alvejante");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Desengordurante");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Limpa alumínio");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Detergente comum");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Desinfetante");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Lustra móveis");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lipeza geral"), "Álcool de limpeza");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lavanderia"),"Sabão em pó");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lavanderia"),"Sabão líquido");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lavanderia"),"Sabão em cápsula");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lavanderia"),"Alvejante de roupas");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Lavanderia"),"Amaciante de roupas");




    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Aveia");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Gérmen de trigo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Chia");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Castanha");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Amendoim");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Arroz");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Feijão");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Soja");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Graos e cereais"), "Ervilha");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Embutidos"), "Milho em lata");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Embutidos"), "Ervilha em lata");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Embutidos"), "Salsicha em lata");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Embutidos"), "Carne em lata");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Embutidos"), "Sardinha em lata");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Embutidos"), "Atum em lata");



    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Manteiga");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Margarina");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Pão de hamburguer");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Pão caseiro");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Pão de forma");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Pó de café");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Biscoito doce");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Biscoito salgado");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Padaria"),"Pizza");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Carnes"),"Carne de frango");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Carnes"),"Carne suína");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Carnes"),"Mortadela");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Carnes"),"Linguiça");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Carnes"),"Carne bovina");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Horti fruti"), "Fruta");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Horti fruti"), "Folhosos");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Horti fruti"), "Legumes ou verduras");



    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas"),"Chá em caixa\garrafa");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas"),"Suco em caixa\garrafa");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas alcólicas"),"Cerveja lata");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas alcólicas"),"Cerveja garrafa");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas alcólicas"),"Vinho");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas alcólicas"),"Vodka");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas alcólicas"),"Cachaça");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Bebibas alcólicas"),"Tekila");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Sabonete barra");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Sabonete líquido");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Shampoo\Condicionador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Papel higiênico");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Pasta de dente");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Fio dental");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Enxaguante bucal");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Barbeador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = 'Higiene Pessoal'),"Escova de dente");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Perfumaria"),"Perfume masculino");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Perfumaria"),"Perfume feminino");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Lápis/lapiseira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Caneta");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Borracha");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Apagador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Quadro branco");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Grampeador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Clip/grampo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Porta treco");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Pasta");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Organizador de arquivo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Utensílios"),"Caixa arquivo");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Leitura"),"Livro");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Leitura"),"Revista");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Leitura"),"Gibi");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Alvenaria"),"Tijolo\lajota");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Alvenaria"),"Cimento");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Alvenaria"),"Massa corrida");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Alvenaria"),"Massa mista de secagem");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Alvenaria"),"Azulejo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Alvenaria"),"Azulejo __tipo pastilha");

    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Martelo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Marreta");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Prego");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Parafuso");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Serrilha");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Alicate");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Marcenaria"),"Alicate de corte");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Ferramentas elétricas"),"Furadeira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Ferramentas elétricas"),"Parafusadeira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Ferramentas elétricas"),"Serra elétrica");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Ferramentas elétricas"),"Aplainadora");

    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Vassoura");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Rodo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Escova");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Balde/bacia");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Esfregão");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Pá");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Pregador de roupa");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Varal portátil");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Limpeza/lavanderia"),"Varal de teto");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Geladeira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Televisão");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Foguão");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Máquina de lavar");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Liquidificador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Cafeteira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Misteira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Grill");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Microondas");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Forno elétrico");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Ar condicionado");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Ventilador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Eletrodomésticos"),"Aspirador de pó");

    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Iluminação"),"Abajour");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Iluminação"),"Lâmpada");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Iluminação"),"Lanterna");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Tablet");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"PenDrive");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"HD");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"GPU");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Placa mãe");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Gabinete");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Mouse");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Teclado");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Monitor");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Processador");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Memória RAM");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"HD externo");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"SSD");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"chip SSD");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Cooler");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Watercooler");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Leitor de DVD");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Adaptador wireless");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Impressora");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Tinta de impressora");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Informática"),"Roteador");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Telefonia"),"Celular");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Telefonia"),"Telefone");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Telefonia"),"Capa protetora");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Telefonia"),"Tela protetora");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Telefonia"),"Chip");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Telefonia"),"Cabo\\carregagor");

    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Ração");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Petisco");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Areia higiênica");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Brinquedinho");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Caixa higiênica");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Tijela alimentar");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Shampoo/perfume animal");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Coleira");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Caninos\felinos"),"Caixa transportadora");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Aves"),"Ave (Animal)");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Aves"),"Gaiola aviária");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Aves"),"Ração aviária");


    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Roedores"),"Roedor (Animal)");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Roedores"),"Gaiola de roedor");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Roedores"),"Ração de roedor");

    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Peixes"),"Peixe (Animal)");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Peixes"),"Ração para peixe");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Peixes"),"Aquário");
    INSERT INTO espec_item_serv VALUES (NULL, (SELECT id FROM subcateg_serv_item WHERE subcategoria = "Peixes"),"Decorativo de aquário");
    '''

    try:
        cur.executescript(sql)
        con.commit()
        print("Espécies cadastradas.\nSem erro.")
    except Exception as Expt:
        print(str(Expt))
        return (str(Expt))


def main(args):
    con, cur = conecta()

    catalogando_categoria(con, cur)
    catalogando_subcategoria(con, cur)
    catalogando_especie(con, cur)


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


##################################################################################################

import sqlite3

'''
    sql = 'create table if not exists contas_cred(id INTEGER PRIMARY KEY, id_ger INTEGER, nome_conta VARCHAR(55), descricao VARCHAR(100), id_refe, FOREIGN KEY (id_ger) REFERENCES gerencias (id), FOREIGN KEY (id_refe) REFERENCES referente_cred (id))'
    cur.execute(sql)

    sql = 'create table if not exists referente_cred(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), descricao VARCHAR(100), __tipo VARCHAR(20), referente INTEGER, cedente INTEGER, FOREIGN KEY (referente) REFERENCES referentes (id), FOREIGN KEY (cedente) REFERENCES contas_cred (id))'
    cur.execute(sql)
    con.commit()
'''


def iniciaBD_prog():
    # Cria uma conexão e um cursor
    con = sqlite3.connect('BD_prog.db')
    con.execute('pragma foreign_keys=ON')
    cur = con.cursor()

    # Criamos uma string de nome sql pela qual encapsulamos as sentenças para o sqlite:
    sql = ''
    sql = 'CREATE TABLE IF NOT EXISTS gerencias(id INTEGER PRIMARY KEY, nome_ger VARCHAR(35), nome_gest VARCHAR(35), descricao VARCHAR(100))'
    cur.execute(sql)

    # ~ sql = 'DROP TABLE IF EXISTS contas'
    # ~ cur.execute(sql)
    # ~ con.commit()
    # ~ print('droped')

    sql = 'CREATE TABLE IF NOT EXISTS contas(id INTEGER PRIMARY KEY, id_ger INTEGER, __tipo VARCHAR(8), nome VARCHAR(55), saldo , taxa_mensal FLOAT,  FOREIGN KEY (id_ger) REFERENCES gerencias (id))'
    cur.execute(sql)

    sql = 'CREATE TABLE IF NOT EXISTS vendas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), __tipo VARCHAR(20), id_move_NE INTEGER, id_cliente INTEGER, FOREIGN KEY (id_cliente) REFERENCES clientes (id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS vendas_list(id INTEGER PRIMARY KEY AUTOINCREMENT, id_refe, id_item_serv, quantidade FLOAT, valor_unit DOUBLE PRECISION, valor_total DOUBLE PRECISION, FOREIGN KEY (id_refe) REFERENCES referentes (id), FOREIGN KEY (id_item_serv) REFERENCES itens_servs (id))'
    cur.execute(sql)
    con.commit()

    sql = 'DROP TABLE IF EXISTS move'
    cur.execute(sql)
    con.commit()
    print('droped')

    # ~ #Criando tabela de transacoes:
    # ~ sql = CREATE TABLE transac(id INTEGER PRIMARY KEY, nome VARCHAR(55), descricao VARCHAR[65], dat DATE(11), __tipo VARCHAR(20), id_conta_ced INTEGER, id_conta_fav INTEGER, valor DOUBLE PRECISION, id_fornec INTEGER, FOREIGN KEY(id_conta_fav) REFERENCES contas(id), FOREIGN KEY (id_conta_ced) REFERENCES contas(id), FOREIGN KEY (id_fornec) REFERENCES fornecs(id))'
    # ~ cur.execute(sql)
    # ~ con.commit()

    # Criando tabela de movimentações:
    sql = 'CREATE TABLE IF NOT EXISTS move(id INTEGER PRIMARY KEY, nome VARCHAR(55), descricao TEXT, data DATE(11), __tipo VARCHAR(20), id_conta_ced INTEGER, id_conta_fav INTEGER, valor DOUBLE PRECISION, id_refe INTEGER, FOREIGN KEY(id_refe) REFERENCES referentes(id), FOREIGN KEY(id_conta_fav) REFERENCES contas(id), FOREIGN KEY (id_conta_ced) REFERENCES contas(id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS compras(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), __tipo VARCHAR(20), id_move_NE INTEGER, id_fornec INTEGER, FOREIGN KEY (id_fornec) REFERENCES fornecs (id))'
    cur.execute(sql)
    con.commit()

    # ~ sql = 'DROP TABLE IF EXISTS compras_list'
    # ~ cur.execute(sql)
    # ~ con.commit()
    # ~ print('droped')

    sql = 'CREATE TABLE IF NOT EXISTS compras_list(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(40), id_refe, id_item_serv, quantidade FLOAT, valor_unit DOUBLE PRECISION, valor_total DOUBLE PRECISION, FOREIGN KEY (id_refe) REFERENCES referentes (id), FOREIGN KEY (id_item_serv) REFERENCES itens_servs (id))'
    cur.execute(sql)
    con.commit()

    # sql = 'DROP TABLE IF EXISTS referentes'
    # cur.execute(sql)
    # con.commit()
    # print('droped')

    sql = 'CREATE TABLE IF NOT EXISTS referentes(id INTEGER PRIMARY KEY, nome VARCHAR(55), nome_fornec VARCHAR(40), id_fornec INTEGER, __tipo VARCHAR(20), subtipo VARCHAR(20), valor FLOAT, id_lst_items INTEGER,  status_mov BOOLEAN, id_mov INTEGER,  FOREIGN KEY (id_fornec) REFERENCES fornecs (id), FOREIGN KEY (id_mov) REFERENCES move (id))'
    cur.execute(sql)
    con.commit()

    # Criando tabela de categoria de serviços:
    sql = 'CREATE TABLE IF NOT EXISTS categ_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria VARCHAR(25), __tipo VARCHAR(12))'
    cur.execute(sql)
    con.commit()

    # Criando tabela de Sub_categorias de serviços:
    sql = 'CREATE TABLE IF NOT EXISTS subcateg_serv_item(id INTEGER PRIMARY KEY AUTOINCREMENT, id_categ INTEGER, subcategoria VARCHAR(22) UNIQUE, FOREIGN KEY (id_categ) REFERENCES categ_serv_item(id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS espec_item_serv(id INTEGER PRIMARY KEY AUTOINCREMENT, id_pai INTEGER, especie VARCHAR(30), FOREIGN KEY (id_pai) REFERENCES subcateg_serv_item(id));'
    cur.execute(sql)
    con.commit()

    # Criando tabela de categorias de fornecedores:
    sql = 'CREATE TABLE IF NOT EXISTS categ_fornec(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria VARCHAR(25) UNIQUE)'
    cur.execute(sql)
    con.commit()

    # Criando tabela de Sub_categorias  de fornecedores:
    sql = 'CREATE TABLE IF NOT EXISTS subcateg_fornec(id INTEGER PRIMARY KEY AUTOINCREMENT, id_categ INTEGER, subcategoria VARCHAR(22) UNIQUE, FOREIGN KEY (id_categ) REFERENCES categ_fornec(id))'
    cur.execute(sql)
    con.commit()

    # Criando tabela de clientes:
    sql = 'CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), cn INTEGER, genero VARCHAR(15), dia_nasc VARCHAR(3), mes_nasc VARCHAR(3), ano_nasc VARCHAR(5), descricao VARCHAR(100), tel1 VARCHAR(18), tel2 VARCHAR(18), email1 VARCHAR(25), email2 VARCHAR(25), uf VARCHAR(3), cidade VARCHAR(25), bairro VARCHAR(25), logradouro VARCHAR(30), num_resid VARCHAR(8), tipo_resid VARCHAR(18), num_ape VARCHAR(8), nome_cond VARCHAR(25), cep VARCHAR(21))'
    cur.execute(sql)
    con.commit()

    # Criando tabela de Fornecedores:
    sql = 'CREATE TABLE IF NOT EXISTS fornecs(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), descricao VARCHAR(100), categoria VARCHAR(20), subcategoria VARCHAR(20), uf VARCHAR(3), cidade VARCHAR(25), email VARCHAR(30), tel1 INTEGER, tel2 INTEGER, cnpj INTEGER)'
    cur.execute(sql)
    con.commit()

    # Criando tabela de Funcionários:
    sql = 'CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), descricao VARCHAR(100), categoria VARCHAR(20), subcategoria VARCHAR(20), cidade VARCHAR(25), email VARCHAR(30), tel1 INTEGER, tel2 INTEGER, cpf INTEGER)'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS itens_servs_2(id INTEGER PRIMARY KEY AUTOINCREMENT, __tipo VARCHAR(11), nome VARCHAR(55), descricao VARCHAR(100), id_subcateg INTEGER, marca VARCHAR(35))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXISTS estoq(id INTEGER PRIMARY KEY AUTOINCREMENT, id_item INTEGER, valor_unit_pago FLOAT, id_compra, FOREIGN KEY (id_item) REFERENCES itens_servs(id), FOREIGN KEY (id_compra) REFERENCES compras(id))'
    cur.execute(sql)
    con.commit()

    sql = 'CREATE TABLE IF NOT EXIST tabl_vendas_itens(id INTEGER PRIMARY AUTOINCREMENT, id_item INTEGER, quant INTEGER, valor_unit DOUBLE PRECISION, FOREIGN KEY (id_item) REFERENCES estoq(id))'
    sql = 'CREATE TABLE IF NOT EXIST tabl_vendas_servs(id INTEGER PRIMARY AUTOINCREMENT, id_serv INTEGER, valor DOUBLE PRECISION, FOREIGN KEY (itens_servs) REFERENCES estoq(id))'

    con.close()
    del (con, cur, sql)


#def main(args):
    #iniciaBD_prog()
    #return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
