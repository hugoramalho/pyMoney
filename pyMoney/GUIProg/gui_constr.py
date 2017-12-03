from tkinter import Tk
from . import *
from .GUIAbstracts.frames_prog import *


class App_controller(Tk):
    # todo:  TODAS AS CLASSES ABSTRATAS DA INTERFACE PRECISAM HERDAR DE tkinter.Frame
    def __init__(self, con_bd):
        super().__init__()
        self.id_ger = None
        self.con_bd = con_bd

        self.main_frame = main_frame(self)

    def inic_session(self, **kwargs):
        self.id_ger = kwargs.get('id_ger')
        lst_something = self.con_bd.load_ger(**kwargs)

    def show_frame(self, page_name):
        '''Constrói o frame cujo nome foi dado'''
        self.destroi_frames_filhos()

        if page_name == 'frame_carrega_ger':
            frame = carrega_ger_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        if page_name == 'statusGeral_frame':
            frame = statusGeral_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'banco_itens_frame':
            frame = banco_itens_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'fornec_frame':
            frame = fornec_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'banco_refs_constr':
            frame = banco_refs_constr(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'insere_refe_frame':
            frame = InsFornecFrame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'clientes_frame':
            frame = clientes_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'insere_move_frame':
            frame = insere_move_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'insere_move_frame':
            frame = insere_move_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()

        elif page_name == 'menu_inic':
            frame = menu_inic_frame(self, self)
            frame.grid(row=0, column=0, sticky="nsew", padx=25, pady=25)
            frame.tkraise()




    def destroi_frames_filhos(self):
        if self.winfo_children() != []:
            # O método abaixo retorna uma lista com os frames-filhos do frame atual:
            lst_frames = self.winfo_children()
            # O loop abaixo percorre a lista e os destrói:
            for elem_frame in lst_frames:
                elem_frame.destroy()
        else:
            return None

    def load_custommers(self):
        lst = self.con_bd.fetchall_clients()
        return(lst)

    def load_accounts(self):
        lst = self.con_bd.fetchall_contas()

    def load_ger(self, id_ger):
        lst = self.con_bd.fetch_ger_carregada(id_ger)


