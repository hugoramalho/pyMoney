from pyMoney.modelsProg.models import *
from pyMoney.modelsProg.DAOs import *
from pyMoney.GUIProg.UIFrames import *
from .exceptions import AppException


class App_controller(Tk):
    def __init__(self):
        super().__init__()
        self.ger_atv = None
        self.main_window = MainWindow(self, self)
        self.mainFrame = self.main_window.main_frame
        self.show_frame('MenuInic')

    def show_frame(self, page_name):
        if page_name == 'MenuInic':
            self.main_window.destroi_framesFilhos_cent()
            frame = MenuInic(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        if page_name == 'frame_carrega_ger':
            self.main_window.destroi_framesFilhos_cent()
            frame = CarregaGerFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        if page_name == 'StatusGeralFrame':
            self.main_window.destroi_framesFilhos_cent()
            frame = StatusGeralFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'banco_itens_frame':
            self.main_window.destroi_framesFilhos_cent()
            frame = ItemServFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'FornecFrame':
            self.main_window.destroi_framesFilhos_cent()
            frame = FornecFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'banco_refs_constr':
            frame = ins_compras_list_frame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'insere_refe_frame':
            self.main_window.destroi_framesFilhos_cent()
            frame = ins_compras_list_frame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'ClientesFrame':
            self.main_window.destroi_framesFilhos_cent()
            frame = ClientesFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'ins_move_frame':
            self.main_window.destroi_framesFilhos_cent()
            frame = ins_move_frame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            # frame.tkraise()

        elif page_name == 'NovaGerFrame':
            self.main_window.destroi_framesFilhos_cent()
            frame = NovaGerFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)

        elif page_name == 'AlteraGerFrame':
            frame = AlteraGerFrame(self.mainFrame, self)

        elif page_name == 'EstoqServFrame':
            self.main_window.destroi_framesFilhos_cent()
            frame = EstoqServFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)

        elif page_name == 'EstabFrame':
            self.main_window.destroi_framesFilhos_cent()
            frame = EstabFrame(self.mainFrame, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)

        elif page_name == 'AlteraContaFrame':
            frame = AlteraContaFrame(self.mainFrame, self)

        elif page_name == 'InsConta':
            frame = InsConta(self.mainFrame, self)

    def search_name_item(self, name):
        item_dao = itemDAO()
        lst_item = item_dao.search_name(name)
        return lst_item

    def search_name_serv(self, name):
        serv_dao = servDAO()
        lst_serv = serv_dao.search_name(name)
        return lst_serv

    def search_code_item(self, code):
        item_dao = itemDAO()
        return item_dao.search_code(code)

    def search_code_serv(self, code):
        serv_dao = servDAO()
        return serv_dao.search_code(code)

    def search_CEP(self, cep):
        cep_dao = enderDAO()
        ender = cep_dao.search_cep(cep)
        return ender

    def load_CIDADES(self, UF):
        cep_dao = enderDAO()
        ender = cep_dao.load_CIDADES(UF)
        return ender

    def load_BAIRROS(self, CIDADE):
        cep_dao = enderDAO()
        ender = cep_dao.load_BAIRROS(CIDADE)
        return ender

    def load_UF(self):
        cep_dao = enderDAO()
        ender = cep_dao.load_UF()
        return ender

    def loadAll_model(self, model_obj):
        if type(model_obj) is gerencia:
            geren_DAO = gerenDAO()
            lst_ger = geren_DAO.loadAll()
            return lst_ger

        elif type(model_obj) is cliente:
            cliente_DAO = clienteDAO()
            lst_clientes = cliente_DAO.loadAll()
            return lst_clientes

        elif type(model_obj) is fornec:
            fornec_DAO = fornecDAO()
            lst_fornecs = fornec_DAO.loadAll()
            return lst_fornecs

        elif type(model_obj) is c_conta:
            conta_DAO = contaDAO()
            lst_contas = conta_DAO.loadAll(id_ger=self.ger_atv.idd)
            return lst_contas

        elif type(model_obj) is item:
            item_DAO = itemDAO()
            lst_item = item_DAO.loadAll()
            return lst_item

        elif type(model_obj) is serv:
            serv_DAO = servDAO()
            lst_servs = serv_DAO.loadAll()
            return lst_servs

        elif type(model_obj) is CategEstab:
            categEstab_DAO = categEstabDAO()
            lst_categs = categEstab_DAO.loadAll()
            return lst_categs

        elif type(model_obj) is Estab:
            estab_DAO = estabDAO()
            lst_estabs = estab_DAO.loadAll()
            return lst_estabs

        elif type(model_obj) is Categ:
            #categ_DAO = categDAO()
            #lst_categs = categ_DAO.loadAll()
            #return lst_categs
            pass

        elif type(model_obj) is SubCateg:
            #subcateg_DAO = subcategDAO()
            #lst_subcateg = subcateg_DAO.loadAll()
            #return lst_subcateg
            pass

        elif type(model_obj) is Especie:
            #especie_DAO = especieDAO()
            #lst_espec = especie_DAO.loadAll()
            #return lst_espec
            pass

    def load_model(self, model_obj):
        if type(model_obj) is gerencia:
            geren_DAO = gerenDAO()
            lst_ger = geren_DAO.load()
            return lst_ger

        elif type(model_obj) is cliente:
            cliente_DAO = clienteDAO()
            lst_clientes = cliente_DAO.load()
            return lst_clientes

        elif type(model_obj) is fornec:
            fornec_DAO = fornecDAO()
            lst_fornecs = fornec_DAO.load()
            return lst_fornecs

        elif type(model_obj) is c_conta:
            conta_DAO = contaDAO()
            lst_contas = conta_DAO.load(id_ger=self.ger_atv.idd)
            return lst_contas

    def update_model(self, model_obj):
        try:
            if type(model_obj) is gerencia:
                geren_dao = gerenDAO()
                geren_dao.update(model_obj)

            elif type(model_obj) is cliente:
                cliente_dao = clienteDAO()
                cliente_dao.update(model_obj)

            elif type(model_obj) is fornec:
                fornec_DAO = fornecDAO()
                fornec_DAO.update(model_obj)

            elif type(model_obj) is c_conta:
                conta_DAO = contaDAO()
                conta_DAO.update(model_obj)

            elif type(model_obj) is CategEstab:
                CategEstab_DAO = categEstabDAO()
                CategEstab_DAO.update(model_obj)

            elif type(model_obj) is Estab:
                estab_DAO = estabDAO()
                estab_DAO.update(model_obj)

            elif type(model_obj) is Categ:
                #categ_DAO = categDAO()
                #categ_DAO.update(model_obj)
                pass

            elif type(model_obj) is SubCateg:
                #subcateg_DAO = subcategDAO()
                #subcateg_DAO.update(model_obj)
                pass

            elif type(model_obj) is Especie:
                #especie_DAO = especieDAO()
                #especie_DAO.update(model_obj)
                pass

            return 0

        except Exception as Expt:
            print(Expt)

    def insert_model(self, model_obj):
        try:
            if type(model_obj) is gerencia:
                geren_DAO = gerenDAO()
                geren_DAO.insert(model_obj)

            elif type(model_obj) is cliente:
                cliente_DAO = clienteDAO()
                cliente_DAO.insert(model_obj)

            elif type(model_obj) is fornec:
                fornec_DAO = fornecDAO()
                fornec_DAO.insert(model_obj)

            elif type(model_obj) is c_conta:
                conta_DAO = contaDAO()
                conta_DAO.insert(model_obj)

            elif type(model_obj) is item:
                item_DAO = itemDAO()
                item_DAO.insert(model_obj)

            elif type(model_obj) is serv:
                serv_DAO = servDAO()
                serv_DAO.insert(model_obj)

            elif type(model_obj) is CategEstab:
                categEstab_DAO = categEstabDAO()
                categEstab_DAO.insert(model_obj)

            elif type(model_obj) is Estab:
                estab_DAO = estabDAO()
                estab_DAO.insert(model_obj)


            elif type(model_obj) is transac:
                print('Caiu aqui controller')
                transac_DAO = transacDAO()
                transac_DAO.insert(model_obj)

            return 0

        except Exception as Expt:
            self.catch_Exception(Expt)

    def inic_session(self, ger_atv):
        self.ger_atv = ger_atv
        self.main_window.sideMenu.ativa_todos_Rbs()
        self.main_window.destroi_framesFilhos_cent()
        self.show_frame('StatusGeralFrame')

    def efetivaCompra(self, compra: CompraItemServ):
        try:
            compra_DAO = compraItemServDAO()
            compra_DAO.insert(compra)
            return 0
        except Exception as Expt:
            self.catch_Exception(Expt)
            return 1

    def loadExtrato(self, obj_conta: c_conta, tempoInic: datetime, tempoFim: datetime):
        try:
            transac_DAO = transacDAO()
            transac_DAO.getExtratoConta(obj_conta, tempoInic, tempoFim)
            return obj_conta
        except Exception as Expt:
            self.catch_Exception(Expt)

    def catch_Exception(self, Exp):
        t = AppException(Exp)
