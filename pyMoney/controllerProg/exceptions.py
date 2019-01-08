import sqlite3
from tkinter.messagebox import showerror, showwarning, showinfo


class AppException(Exception):
    def __init__(self, Exp: Exception):
    # A EXCEÇÃO RECEBIDA É DEVIDAMENTE IDENTIFICADA E TRATADA:

        if isinstance(Exp, sqlite3.IntegrityError):
            if str(Exp) == 'UNIQUE constraint failed: itens.CODIGO':
                showwarning('Atenção!', 'Algum item já possui esse código!\nPor favor defina outro código.')

        elif isinstance(Exp, sqlite3.Error):
            showwarning('Atenção!', 'Falha na comunicação com o banco de dados!\n'+str(Exp))