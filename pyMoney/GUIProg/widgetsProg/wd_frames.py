from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo, askyesno
from tkinter import *
from .calendario_3 import *
import datetime, calendar


class wd_CBox(Frame):
    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.tit_CBox_text = kwargs.get('tit_CBox', 'Título')
        self.set_CBox_text = kwargs.get('set_CBox_default', '')
        self.CBox_state = kwargs.get('CBox_state', 'readonly')
        self.CBox_values = kwargs.get('CBox_values', ['Opção 1', 'Opção 2'])
        self.width = kwargs.get('width', 20)

        self.frameLocal = Frame(self)
        self.frameLocal.grid()

        self.tit_CBox = Label(self.frameLocal, text=self.tit_CBox_text)
        self.tit_CBox.grid(row=0, column=0, sticky=W)

        self.var_CBox = StringVar()
        self.CBox = ttk.Combobox(self.frameLocal, textvariable=self.var_CBox, values=self.CBox_values, width=self.width)
        self.CBox.grid(row=1, column=0, sticky='W')

        self.CBox.set(self.set_CBox_text)
        self.CBox.config(state=self.CBox_state)

    def config_CBox(self, **kwargs):
        self.CBox.config(kwargs)

    def config_Label(self, **kwargs):
        self.tit_CBox.config(kwargs)

    def add_value_CBox(self, lst):
        self.CBox.config(state="normal")
        list_values = list(self.CBox["values"])
        list_values.append(lst)
        self.CBox["values"] = list_values
        self.CBox.config(state="readonly")

    def define_values_CBox(self, lst):
        self.CBox["values"] = lst

    def get_choice(self):
        return (self.var_CBox.get())

    def set_CBox_default(self, tit):
        if self.CBox['state'] != 'normal':
            state = self.CBox['state']
            self.CBox.config(state='normal')
            self.CBox.set(tit)
            self.CBox.config(state=state)
        else:
            self.CBox.set(tit)

    def config_CBox_state(self, estado):
        self.CBox.config(state=estado)

    def config_tit_CBox(self, titulo):
        self.tit_CBox.config(text=titulo)

    def finaliza(self):
        self.frameLocal.destroy()

    def grid_frame(self, **kwargs):
        # kwargs:
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()



class wd_DateCbox(LabelFrame):
    def __init__(self, framePai, **kwargs):
        text = kwargs.get('text', '')
        relief = kwargs.get('relief', FLAT)
        choice = kwargs.get('choice', True)
        self.date = kwargs.get('date', None)
        language = kwargs.get('language', 'Portuguese')

        self.ano_escolha = None
        self.dia_escolha = None
        self.mes_escolha = None

        if self.date is not None:
            self.ano_escolha = self.date.year
            self.dia_escolha = self.date.day
            self.mes_escolha = self.date.month

        super().__init__(framePai, text=text, relief=relief)
        self.grid()
        self.tempo_agora = datetime.datetime.now()

        self.lst_meses = self.mesList()
        #self.lst_dias = self.diasList(mes)
        self.lst_anos = self.anoList()

        self.ano_var = StringVar()
        self.CBox3 = ttk.Combobox(self, textvariable=self.ano_var, values=self.lst_anos, width=10, state = 'readonly')
        if self.date is not None:
            self.CBox3.set(self.date.year)
        else:
            self.CBox3.set('Ano')
        self.CBox3.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.CBox3.bind('<<ComboboxSelected>>', lambda event: self.bind_ano_Cbox())

        self.mes_var = StringVar()
        self.CBox1 = ttk.Combobox(self, textvariable=self.mes_var, values=self.lst_meses, state='readonly', width=10)
        if self.date is not None:
            mes = self.date.strftime('%B')
            mes = self.toPortuguese(mes)
            self.CBox1.set(mes)
        else:
            self.CBox1.set('Mês')
        self.CBox1.bind('<<ComboboxSelected>>', lambda event: self.bind_mes_Cbox())
        self.CBox1.grid(row=0, column=1, sticky='w', padx=5, pady=5)

        self.dia_var = StringVar()
        self.CBox2 = ttk.Combobox(self, textvariable=self.dia_var, width=10)
        if self.date is not None:
            self.CBox2.set(self.date.day)
        else:
            self.CBox2.set('Dia')
        self.CBox2.config(state='disabled')
        self.CBox2.grid(row=0, column=2, sticky='w', padx=5, pady=8)
        self.CBox2.bind('<<ComboboxSelected>>', lambda event: self.bind_dia_Cbox())

        if choice is False:
            self.CBox1.config(state='disabled')
            self.CBox2.config(state='disabled')
            self.CBox3.config(state='disabled')

    def update_dias(self):
        mes = self.mes_escolha
        if mes is not None:
            lst_dias = self.diasList(mes)
            self.CBox2.config(state = 'readonly', values = lst_dias)

    def bind_dia_Cbox(self):
        self.dia_escolha = self.dia_var.get()

    def bind_ano_Cbox(self):
        self.ano_escolha = self.ano_var.get()
        self.CBox1.config(state = 'readonly')
        self.update_dias()

    def bind_mes_Cbox(self):
        self.mes_escolha = self.mes_var.get()
        lst_dias = self.diasList(self.mes_escolha)
        self.CBox2.config(state = 'readonly', values = lst_dias)

    def getMes(self):
        return self.mes_escolha

    def getAno(self):
        return self.ano_escolha

    def getDia(self):
        return self.dia_escolha

    def get_date(self):
        print(self.dia_escolha, self.mes_escolha, self.ano_escolha)
        if self.mes_escolha is not None and self.dia_escolha is not None:
            if self.ano_escolha is None:
                ano = 1
            else:
                ano = self.ano_escolha

            mes_int = int(self.numeroMes(self.mes_escolha))

            return datetime.datetime(int(ano), mes_int, int(self.dia_escolha))

        elif self.mes_escolha is None and self.dia_escolha is None and self.ano_escolha is None:
            return datetime.datetime(1, 1, 1)

    def diasList(self, mes):
        if self.ano_escolha is None:
            ano = 1992 # POR SER ANO BISSEXTO
        else:
            ano = int(self.ano_escolha)

        num_mes = self.numeroMes(mes)
        quant_dias = calendar.monthrange(ano, num_mes)[1]
        lst_dias = []
        for dia in range(1, quant_dias+1):
            lst_dias.append(str(dia))
        return lst_dias

    def mesList(self):
        lst_meses = []
        ano_atual = self.tempo_agora.year
        for i in range(1, 13):
            mes = datetime.date(ano_atual, i, 1).strftime('%B')
            mes = self.toPortuguese(mes)
            lst_meses.append(mes)
        return lst_meses

    def anoList(self):
        ano_atual = self.tempo_agora.year
        ano_list = []
        for ano in range(1900, ano_atual+1):
            ano_list.append(str(ano))
        ano_list.reverse()
        return ano_list

    def numeroMes(self, string):
        print(string)
        num = 0
        if string == 'January' or string == 'Janeiro':
            num = 1
        elif string == 'February' or string == 'Fevereiro':
            num = 2
        elif string == 'March' or string == 'Março':
            num = 3
        elif string == 'April' or string == 'Abril':
            num = 4
        elif string == 'May' or string == 'Maio':
            num = 5
        elif string == 'June' or string == 'Junho':
            num = 6
        elif string == 'July' or string == 'Julho':
            num = 7
        elif string == 'August' or string == 'Agosto':
            num = 8
        elif string == 'September' or string == 'Setembro':
            num = 9
        elif string == 'October' or string == 'Outubro':
            num = 10
        elif string == 'November' or string == 'Novembro':
            num = 11
        elif string == 'December'or string == 'Dezembro':
            num = 12
        return num

    def toPortuguese(self, string):
        if string == 'Month':
            string = 'Mês'
        elif string == 'January':
            string = 'Janeiro'
        elif string == 'February':
            string = 'Fevereiro'
        elif string == 'March':
            string = 'Março'
        elif string == 'April':
            string = 'Abril'
        elif string == 'May':
            string = 'Maio'
        elif string == 'June':
            string = 'Junho'
        elif string == 'July':
            string = 'Julho'
        elif string == 'August':
            string = 'Agosto'
        elif string == 'September':
            string = 'Setembro'
        elif string == 'October':
            string = 'Outubro'
        elif string == 'November':
            string = 'Novembro'
        elif string == 'December':
            string = 'Dezembro'
        return string

    def config_wd(self, **kwargs):
        choice = kwargs.get('choice', None)
        if choice is True:
            self.CBox1.config(state='enabled')
            self.CBox2.config(state='enabled')
            self.CBox3.config(state='enabled')
        elif choice is False:
            self.CBox1.config(state='disabled')
            self.CBox2.config(state='disabled')
            self.CBox3.config(state='disabled')


class sub_Menu:
    def __init__(self, framePai, **kwargs):
        self.nome_op1 = kwargs.get('nome_B1', 'Opção 1')
        self.nome_op2 = kwargs.get('nome_B2', 'Opção 2')

        self.framePai = framePai

        self.menu = Menu(self.framePai, tearoff=0)
        self.menu.add_command(label=self.nome_op1, command=None)
        self.menu.add_command(label=self.nome_op2, command=None)

        # ~ self.bind(self.framePai)0

    def config_nome_B1(self, tit):
        # index_B1 = self.menu.index(self.nome_op1)
        self.menu.entryconfig(0, label=tit)

    def config_nome_B2(self, tit):
        # index_B2 = self.menu.index(self.nome_op2)
        self.menu.entryconfig(1, label=tit)

    def config_comando_B1(self, comando):
        # index_B1 = self.menu.index(self.nome_op1)
        self.menu.entryconfig(0, command=comando)

    def config_comando_B2(self, comando):
        # index_B2 = self.menu.index(self.nome_op2)
        self.menu.entryconfig(1, command=comando)

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def bind(self, pointer):
        pointer.bind("<Button-3>", self.popup)


class wd_Entry:
    def __init__(self, framePai, **kwargs):
        self.label = kwargs.get('label', 'Título')
        self.tit_Entry_text = kwargs.get('entry_Label', self.label)
        self.set_Entry_default = kwargs.get('set_Entry_default', '')
        self.state_Entry = kwargs.get('state', 'enabled')
        self.state_Entry = kwargs.get('state_Entry', self.state_Entry )
        self.width_Entry = kwargs.get('width', 20)

        self.frameLocal = Frame(framePai)
        self.entry_Label = Label(self.frameLocal, text=self.tit_Entry_text)
        self.var_Entry = StringVar()
        self.entry = ttk.Entry(self.frameLocal, textvariable=self.var_Entry, width=self.width_Entry,
                               state=self.state_Entry)
        self.insert_text(self.set_Entry_default)

    def wd_state(self, state):
        self.entry.config(state = state)

    def config_Entry(self, **kwargs):
        self.entry.config(kwargs)

    def get_text(self):
        return self.var_Entry.get()

    def insert_text(self, txt):
        if self.entry['state'] != 'enabled':
            state = self.entry['state']
            self.entry.config(state='enabled')
            self.limpa_entr()
            self.entry.delete(0, "end")
            self.entry.insert('end', txt)
            self.entry.config(state=state)
        else:
            self.limpa_entr()
            self.entry.insert('end', txt)

    def config_Entry_state(self, estado):
        self.entry.config(state=estado)

    def config_tit_Entry(self, titulo):
        self.entry_Label.config(text=titulo)

    def finaliza(self):
        self.frameLocal.destroy()

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 2)
        padx = kwargs.get('padx', 2)

        self.entry_Label.grid(row=0, column=0, sticky=W, columnspan=columnspan)
        self.entry.grid(row=1, column=0, sticky=sticky, columnspan=columnspan)
        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)

    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def limpa_entr(self):
        self.entry.delete(0, "end")


class wd_TelEntry(Frame):
    def __init__(self, frameMaster, **kwargs):
        super().__init__(frameMaster)
        label = kwargs.get('label', 'Título')
        self.set_Entry_default = kwargs.get('default', '')
        self.state_Entry = kwargs.get('state', 'enabled')
        self.width_Entry = kwargs.get('width', 20)

        self.entry_Label = Label(self, text=label)
        self.entry_Label.grid(row=0, column=0)

        self.var_Entry = StringVar()

        self.entry = ttk.Entry(self, textvariable=self.var_Entry, width=self.width_Entry, state=self.state_Entry)
        self.entry.bind('<KeyRelease>', lambda event: self.__pattern__())
        self.entry.grid(row=1, column=0)
        self.insert(self.set_Entry_default)

    def __pattern__(self):
        text = self.get_text()
        if len(text) == 1:
            if text == ' ' or text.isdigit() is False:
                self.var_Entry = StringVar()
        else:
            if len(text) !=0:
                if (' ' in text) or text[len(text)-1].isdigit() is False:
                    if len(text) == 1:
                        self.var_Entry.set('(' +text)
                    elif len(text) == 2:
                        self.var_Entry.set('(' +text + ')')
                    elif len(text) == 0:
                        self.var_Entry = StringVar()
                else:
                    self.var_Entry.set(text[:(len(text))])

    def grid_frame(self, **kwargs):
        self.grid(**kwargs)

    def retorna_entr(self):
        return self.get_text()

    def get_text(self):
        return self.var_Entry.get()

    def insert(self, txt):
        if self.entry['state'] != 'enabled':
            state = self.entry['state']
            self.entry.config(state='enabled')
            self.delete()
            self.entry.delete(0, "end")
            self.entry.insert('end', txt)
            self.entry.config(state=state)
        else:
            self.delete()
            self.entry.insert('end', txt)

    def insert_Entry(self, text):
        self.insert(text)

    def limpa_entr(self):
        self.delete()

    def wd_state(self, state):
        self.entry.config(state = state)

    def delete(self, index1=0, index2='end'):
        self.entry.delete(index1, index2)


class wd_Text(Frame):

    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.tit = kwargs.get('label', 'Título')
        self.state = kwargs.get('state', NORMAL)
        self.width = kwargs.get('width', 50)
        self.height = kwargs.get('height', 4)
        self.scrollbarx = kwargs.get('scrollbarx', True)
        self.scrollbary = kwargs.get('scrollbary', True)
        self.bd = kwargs.get('bd', 3)

        # Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frameLocal = Frame(framePai)

        self.text_Label = ttk.Label(self.frameLocal, text=self.tit)
        self.text_Label.grid(row=0, column=0, sticky=W)

        self.text = Text(self.frameLocal, insertborderwidth=5, bd=self.bd, font="Arial 9", wrap=WORD,
                         width=self.width, height=self.height, state=self.state, autoseparators=True)
        self.text.grid(row=1, column=0)

        self.__scrollbar_constr__()

        # ~ self.separator1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        # ~ self.separator1.grid(row = 5, column = 0, columnspan = 5, sticky = "we")

    def config_Text(self, **kwargs):
        self.text.config(kwargs)

    def get_text(self):
        text = self.text.get(1.0, "end")
        return (text)

    def wd_state(self, state):
        self.text.config(state = state)


    def __scrollbar_constr__(self):
        if self.scrollbarx == True:
            self.scrollbarX = Scrollbar(self.frameLocal, command=self.text.xview, orient=HORIZONTAL)
            self.scrollbarX.grid(row=2, column=0, sticky=E + W)
            self.text.config(xscrollcommand=self.scrollbarX.set)

        if self.scrollbary == True:
            self.scrollbarY = Scrollbar(self.frameLocal, command=self.text.yview, orient=VERTICAL)
            self.scrollbarY.grid(row=1, column=1, sticky=N + S)
            self.text.config(yscrollcommand=self.scrollbarY.set)

    def delete(self, index1 = 1, index2 = END):
        self.text.delete(index1, index2)

    def insert_text(self, txtStr):
    # TODO ALTERAR O METODO PARA RECEBER OS DOIS PARAMETROS:
    # def insert_text(self, param = 1, txtStr):
        if self.text['state'] != NORMAL:
            state = self.text['state']
            self.text.config(state=NORMAL)
            self.text.delete(1.0, END)
            self.text.insert(1.0, txtStr)
            self.text.config(state=DISABLED)
            self.text.config(state=state)
        else:
            self.text.delete(1.0, END)
            self.text.insert(1.0, txtStr)

    def clear_text(self):
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.config(state=DISABLED)

    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=pady, padx=padx,
                             sticky=sticky)


class wd_Treeview(Frame):
    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.quantCol = kwargs.get('num_cols', 4)
        self.tit = kwargs.get('label', '')
        self.height = kwargs.get('height', 4)
        self.selectmode = kwargs.get('selectmode', 'browse')

        self.tit_treeView = Label(self, text=self.tit, font = 'VERDANA')
        self.tit_treeView.grid(row=0, column=0, sticky=W)

        columnTuple = self.__column_tuple__()
        self.treeView = ttk.Treeview(self, height=self.height, style="Treeview", selectmode='browse',
                                     columns=columnTuple)
        self.treeView.grid(row=1, column=0)

        self.__column_constr__()

        # Bloco das Scrollbars(barras de rolagem):
        self.scrollbarY = Scrollbar(self, command=self.treeView.yview)
        self.scrollbarY.grid(row=1, column=1, sticky=N + S)
        # Bloco  Declaradas a Scrollbar, treeView2 é configurado a recebê-las:
        self.treeView.config(yscrollcommand=self.scrollbarY.set)


    def headingText(self, col, titulo):
        if type(col) is not str:
            col = str(col)
        if col == '0':
            col = '#0'
        self.treeView.heading(col, text=titulo)

    def selection_treeView(self):
        return (self.treeView.selection())

    def idd_selection_treeView(self):
        if self.treeView.selection() is not ():
            return int(self.treeView.selection()[0])
        else:
            return None

    def item_treeView(self, idd):
        return (self.treeView.item(idd))

    def __column_tuple__(self):
        lstAux = []
        if self.quantCol == 1:
            columnTuple = tuple(lstAux)

        else:
            n = 0
            while n < (self.quantCol - 1):
                quant = n + 1
                columnAux = str(quant)
                lstAux.append(columnAux)
                n = n + 1

            columnTuple = tuple(lstAux)

        return (columnTuple)

    def config_heading(self, index, **kwargs):
        if type(index) is not str:
            index = str(index)
        if index == 0 or index == '0':
            index = '#0'
        self.treeView.heading(index, **kwargs)

    def config_column(self, index, **kwargs):
        if index == 0 or index == '0':
            index = '#0'
        elif type(index) is int:
            index = str(index)
        self.treeView.column(index, **kwargs)

    def __column_constr__(self):
        self.treeView.heading("#0", text="text")
        self.treeView.column("#0", width=245, stretch=0)
        n = 1
        while n < (self.quantCol):
            columnAux = str(n)
            self.treeView.heading(columnAux, text="coluna 1")
            self.treeView.column(columnAux, width=100, stretch=0)
            n = n + 1

    def insert_kwargs_treeView(self, **kwargs):
        idd = kwargs.get('idd', None)
        text = kwargs.get('text', None)
        values = kwargs.get('values', None)

        self.treeView.insert('', 'end', iid=idd, text=text, values=values)

    def insert(self, arg):
        if type(arg) is list:
            for elem in arg:
                self.insert_kwargs_treeView(**elem)
        elif type(arg) is dict:
            self.insert_kwargs_treeView(**arg)

    def grid(self, **kwargs):
        pady = kwargs.get('pady')
        if pady is None:
            kwargs['pady'] = 10
        padx = kwargs.get('padx')
        if padx is None:
            kwargs['padx'] = 10
        super().grid(**kwargs)

    def clear_treeView(self):
        self.treeView.delete(*self.treeView.get_children())


class wd_calendario(Frame):
    def __init__(self, framePai, **kwargs):
        super().__init__(framePai)
        self.calendario = Calendar(self, firstweekday=calendar.SUNDAY)
        self.calendario.grid(row=0, column=0, sticky=N+S+W+E)

    def selection(self):
        return self.calendario.selection()


class ScrolledWindow(Frame):
    """
    1. Master widget gets scrollbars and a canvas. Scrollbars are connected
    to canvas scrollregion.

    2. self.scrollwindow is created and inserted into canvas

    Usage Guideline:
    Assign any widgets as children of <ScrolledWindow instance>.scrollwindow
    to get them inserted into canvas

    __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs)
    docstring:
    Parent = master of scrolled window
    canv_w - width of canvas
    canv_h - height of canvas

    """

    def __init__(self, parent, canv_w=400, canv_h=400, *args, **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        # creating a scrollbars
        self.xscrlbr = ttk.Scrollbar(self.parent, orient='horizontal')
        self.xscrlbr.grid(column=0, row=1, sticky='ew', columnspan=2)
        self.yscrlbr = ttk.Scrollbar(self.parent)
        self.yscrlbr.grid(column=1, row=0, sticky='ns')
        # creating a canvas
        self.canv = Canvas(self.parent)
        self.canv.config(relief='flat',
                         width=10,
                         heigh=10, bd=2)
        # placing a canvas into frame
        self.canv.grid(column=0, row=0, sticky='nsew')
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command=self.canv.xview)
        self.yscrlbr.config(command=self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = ttk.Frame(self.parent)

        self.canv.create_window(0, 0, window=self.scrollwindow, anchor='nw')

        self.canv.config(xscrollcommand=self.xscrlbr.set,
                         yscrollcommand=self.yscrlbr.set,
                         scrollregion=(0, 0, 100, 100))

        self.yscrlbr.lift(self.scrollwindow)
        self.xscrlbr.lift(self.scrollwindow)
        self.scrollwindow.bind('<Configure>', self._configure_window)
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)

        return

    def _bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canv.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
        self.canv.config(scrollregion='0 0 %s %s' % size)
        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canv.config(width=self.scrollwindow.winfo_reqwidth())
        if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
            # update the canvas's width to fit the inner frame
            self.canv.config(height=self.scrollwindow.winfo_reqheight())
