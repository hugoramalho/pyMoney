from pyMoney.DataBaseServices.sqlite_APIs import *

BDProg = ConnDB()


def load_all(class_name, **kwargs):
    if class_name == 'c_item':
        lst = BDProg.fetchall_itens(**kwargs)
        return lst

    if class_name == 'c_serv':
        lst = BDProg.fetchall_servs(**kwargs)
        return lst

    elif class_name == 'c_cliente':
        lst_customers = BDProg.fetchall_clientes(**kwargs)
        return lst_customers

    elif class_name == 'gerencia':
        lst_ger = BDProg.fetchall_ger()
        return lst_ger

    elif class_name == 'c_conta':
        lst_contas = BDProg.fetchall_contas(**kwargs)
        return lst_contas

    elif class_name == 'c_move':
        pass
    elif class_name == 'referente':
        pass
    elif class_name == 'c_itemServ_ref':
        pass



    elif class_name == 'c_estab':
        lst_estabs = BDProg.fetchall_estabs(**kwargs)
        return lst_estabs


    elif class_name == 'c_fornec':
        lst_fornec = BDProg.fetchall_fornec(**kwargs)
        return lst_fornec

    elif class_name == 'c_comprasList':
        lst_comprasList = BDProg.fetch_compras_list(**kwargs)
        return lst_comprasList

    elif class_name == '':
        pass
    elif class_name == '':
        pass
    elif class_name == '':
        pass


def update(class_name, **kwargs):
    if class_name == 'c_item_serv':
        BDProg.update_itemServ(**kwargs)

    elif class_name == 'c_cliente':
        BDProg.update_cliente(**kwargs)

    elif class_name == 'gerencia':
        pass

    elif class_name == 'c_conta':
        BDProg.update_conta(**kwargs)

    elif class_name == 'c_move':
        pass
    elif class_name == 'referente':
        pass
    elif class_name == 'c_itemServ_ref':
        pass
    elif class_name == 'c_ident':
        pass
    elif class_name == 'c_cliente':
        pass

    elif class_name == 'c_fornec':
        BDProg.update_fornec(**kwargs)


def delete(class_name, **kwargs):
    if class_name == 'c_item_serv':
        pass
    elif class_name == 'c_cliente':
        pass
    elif class_name == 'gerencia':
        pass
    elif class_name == 'c_conta':
        pass
    elif class_name == 'c_move':
        pass
    elif class_name == 'referente':
        pass
    elif class_name == 'c_itemServ_ref':
        pass
    elif class_name == 'c_ident':
        pass
    elif class_name == 'c_cliente':
        pass
    elif class_name == 'c_fornec':
        pass


def save(class_name, **kwargs):
    if class_name == 'c_item_serv':
        pass
    elif class_name == 'c_cliente':
        pass
    elif class_name == 'gerencia':
        id_ger = BDProg.ins_ger(**kwargs)
        return id_ger


    elif class_name == 'c_conta':
        pass

    elif class_name == 'c_move':
        BDProg.ins_move(**kwargs)

    elif class_name == 'referente':
        pass
    elif class_name == 'c_itemServ_ref':
        pass
    elif class_name == 'c_ident':
        pass
    elif class_name == 'c_cliente':
        pass
    elif class_name == 'c_fornec':
        pass


def search(class_name, **kwargs):
    if class_name == 'c_item_serv':
        pass
    elif class_name == 'c_cliente':
        pass
    elif class_name == 'gerencia':
        pass
    elif class_name == 'c_conta':
        pass
    elif class_name == 'c_move':
        pass
    elif class_name == 'referente':
        pass
    elif class_name == 'c_itemServ_ref':
        pass
    elif class_name == 'c_ident':
        pass
    elif class_name == 'c_cliente':
        pass
    elif class_name == 'c_fornec':
        pass
