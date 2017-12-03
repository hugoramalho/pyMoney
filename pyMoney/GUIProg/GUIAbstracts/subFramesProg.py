from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

import os
import codecs

from tkinter import *
from tkinter import ttk
from time import sleep



class sub_CBox:
    def __init__(self, framePai, **kwargs):
        #kwargs:
        self.tit_CBox_text = kwargs.get('tit_CBox', 'Título')
        self.set_CBox_text = kwargs.get('set_CBox_default', '')
        self.CBox_state = kwargs.get('CBox_state', 'readonly')
        self.CBox_values = kwargs.get('CBox_values',['Opção 1', 'Opção 2'])
        self.width = kwargs.get('width', 20)
        
        
        self.frameLocal = Frame(framePai)
        
        self.tit_CBox = Label(self.frameLocal, text = self.tit_CBox_text)
        self.tit_CBox.grid(row=0, column=0, sticky = W)
        
        self.var_CBox = StringVar()
        
        self.CBox = ttk.Combobox(self.frameLocal, textvariable = self.var_CBox, values = self.CBox_values, width = self.width)
        self.CBox.grid(row = 1, column = 0)
        
        self.CBox.set(self.set_CBox_text)
        self.CBox.config(state = self.CBox_state)
    
    
    
    

    def pointer_CBox(self):
        return(self.CBox)

    def pointer_tit_Cbox(self):
        return(self.tit_CBox)

    def config_CBox(self, **kwargs):
        self.CBox.config(kwargs)
    
    def config_Label(self, **kwargs):
        self.tit_CBox.config(kwargs)

    def add_value_CBox(self, lst):
        self.CBox.config(state = "normal")
        list_values = list(self.CBox["values"])
        list_values.append(lst)
        self.CBox["values"] = list_values
        self.CBox.config(state = "readonly")

    def define_values_CBox(self, lst):
        self.CBox["values"] = lst

    def retorna_escolha_CBox(self):
        return(self.var_CBox.get())
    
    def set_CBox_default(self, tit):
        if self.CBox['state'] != 'normal':
            state = self.CBox['state']
            self.CBox.config(state = 'normal')
            self.CBox.set(tit)
            self.CBox.config(state = state)
        else:
            self.CBox.set(tit)
        

    def config_CBox_state(self, estado):
        self.CBox.config(state = estado)
        
    def config_tit_CBox(self, titulo):
        self.tit_CBox.config(text = titulo)
    
    def finaliza(self):
        self.frameLocal.destroy()
        
    def grid_frame(self, **kwargs):
        #kwargs:
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)
        
        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def insere_nova_CBox(self, CBox):
        self.CBox.destroy()
        self.CBox = CBox(self.frameLocal)
        self.CBox.grid(row = 2, column = 3, padx = 5)



class sub_LFrame_3CBox:
    def __init__(self, framePai, **kwargs):
        #kwargs:
        self.width = kwargs.get('width', 7)
        self.frame_text = kwargs.get('frame_text', 'Teste')
        self.relief = kwargs.get('relief', FLAT)
            #CBox1 options:
        self.set_CBox1_text = kwargs.get('set_CBox1_default', '')
        self.CBox1_state = kwargs.get('CBox1_state', 'readonly')
        self.CBox1_values = kwargs.get('CBox1_values',['Opção 1', 'Opção 2'])
            #Cbox2 options:
        self.set_CBox2_text = kwargs.get('set_CBox2_default', '')
        self.CBox2_state = kwargs.get('CBox2_state', 'readonly')
        self.CBox2_values = kwargs.get('CBox2_values',['Opção 1', 'Opção 2'])
            #Cbox3 options:
        self.set_CBox3_text = kwargs.get('set_CBox3_default', '')
        self.CBox3_state = kwargs.get('CBox3_state', 'readonly')
        self.CBox3_values = kwargs.get('CBox3_values',['Opção 1', 'Opção 2'])
        
        self.frameLocal = LabelFrame(framePai, text = self.frame_text, relief = self.relief)

        self.var_CBox1 = StringVar()
        self.CBox1 = ttk.Combobox(self.frameLocal, textvariable = self.var_CBox1, values = self.CBox1_values, width = self.width)
        self.CBox1.set(self.set_CBox1_text)
        self.CBox1.config(state = self.CBox1_state)

        self.var_CBox2 = StringVar()
        self.CBox2 = ttk.Combobox(self.frameLocal, textvariable = self.var_CBox2, values = self.CBox2_values, width = self.width)
        self.CBox2.set(self.set_CBox2_text)
        self.CBox2.config(state = self.CBox2_state)

        self.var_CBox3 = StringVar()
        self.CBox3 = ttk.Combobox(self.frameLocal, textvariable = self.var_CBox3, values = self.CBox3_values, width = self.width)
        self.CBox3.set(self.set_CBox3_text)
        self.CBox3.config(state = self.CBox3_state)

    def config_tit_frame(self, tit):
        self.frameLocal.config(text = tit)

    def pointer_CBox1(self):
        return(self.CBox1)

    def pointer_CBox2(self):
        return(self.CBox2)
        
    def pointer_CBox3(self):
        return(self.CBox3)

    def config_CBox1(self, **kwargs):
        self.CBox1.config(kwargs)
        
    def config_CBox2(self, **kwargs):
        self.CBox2.config(kwargs)
        
    def config_CBox3(self, **kwargs):
        self.CBox3.config(kwargs)
        

    def add_value_CBox1(self, lst):
        self.CBox1.config(state = "normal")
        list_values = list(self.CBox["values"])
        list_values.append(lst)
        self.CBox1["values"] = list_values
        self.CBox1.config(state = "readonly")
        
    def add_value_CBox1(self, lst):
        self.CBox2.config(state = "normal")
        list_values = list(self.CBox2["values"])
        list_values.append(lst)
        self.CBox2["values"] = list_values
        self.CBox2.config(state = "readonly")
        
    def add_value_CBox3(self, lst):
        self.CBox3.config(state = "normal")
        list_values = list(self.CBox3["values"])
        list_values.append(lst)
        self.CBox3["values"] = list_values
        self.CBox3.config(state = "readonly")

    def define_values_CBox1(self, lst):
        self.CBox1["values"] = lst

    def define_values_CBox2(self, lst):
        self.CBox2["values"] = lst
        
    def define_values_CBox1(self, lst):
        self.CBox3["values"] = lst

    def retorna_escolha_CBox1(self):
        return(self.var_CBox1.get())

    def retorna_escolha_CBox2(self):
        return(self.var_CBox2.get())
        
    def retorna_escolha_CBox3(self):
        return(self.var_CBox3.get())
    
    def set_CBox1_default(self, tit):
        self.CBox1.set(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set(tit)
        
    def set_CBox3_default(self, tit):
        self.CBox3.set(tit)


    def config_CBox1_state(self, estado):
        self.CBox1.config(state = estado)

    def config_CBox3_state(self, estado):
        self.CBox3.config(state = estado)

    def config_CBox3_state(self, estado):
        self.CBox3.config(state = estado)



    def finaliza(self):
        self.frameLocal.destroy()
        
    def grid_frame(self, **kwargs):
        #kwargs:
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 1)
        padx = kwargs.get('padx', 1)
        
        self.CBox1.grid(row = 0, column = 0, sticky = 'w', padx = 5, pady = 5)
        self.CBox2.grid(row = 0, column = 1, sticky = 'we', padx = 5, pady = 5)
        self.CBox3.grid(row = 0, column = 2, sticky = 'e', padx = 5, pady = 5)
        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()



class sub_Menu:
    def __init__(self, framePai, **kwargs):
        self.nome_op1 = kwargs.get('nome_B1', 'Opção 1')
        self.nome_op2 = kwargs.get('nome_B2', 'Opção 2')

        self.framePai = framePai
        
        self.menu = Menu(self.framePai, tearoff=0)
        self.menu.add_command(label = self.nome_op1, command = None)
        self.menu.add_command(label= self.nome_op2, command = None)
        
        #~ self.bind(self.framePai)0

    def config_nome_B1(self, tit):
        #index_B1 = self.menu.index(self.nome_op1)
        self.menu.entryconfig(0, label = tit)
    
    def config_nome_B2(self, tit):
        #index_B2 = self.menu.index(self.nome_op2)
        self.menu.entryconfig(1, label = tit)

    def config_comando_B1(self, comando):
        #index_B1 = self.menu.index(self.nome_op1)
        self.menu.entryconfig(0, command = comando)
        
    def config_comando_B2(self, comando):
        #index_B2 = self.menu.index(self.nome_op2)
        self.menu.entryconfig(1, command = comando)

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def bind(self, pointer):
        pointer.bind("<Button-3>", self.popup)




class sub_Entry:
    def __init__(self, framePai, **kwargs):
        self.tit_Entry_text = kwargs.get('tit_Entry', 'Título')
        self.set_Entry_default = kwargs.get('set_Entry_default', 'Opções')
        self.state_Entry = kwargs.get('state_Entry', 'enabled')
        self.width_Entry = kwargs.get('width', 20)


        self.frameLocal = Frame(framePai)
        self.tit_Entry = Label(self.frameLocal, text = self.tit_Entry_text)
        self.var_Entry = StringVar()
        self.Entry = ttk.Entry(self.frameLocal, textvariable = self.var_Entry, width = self.width_Entry, state = self.state_Entry)


    def config_Label(self, **kwargs):
        self.tit_Entry.config(kwargs)
    
    def config_Entry(self, **kwargs):
        self.Entry.config(kwargs)

    def pointer_Entry(self):
        return(self.Entry)
        
    def pointer_tit_Entry(self):
        return(self.tit_Entry)
        

    def retorna_entr(self):
        return(self.var_Entry.get())
    
    '''
    DEPRECIADA
    def set_Entry_default(self, tit):
        self.Entry.set(tit)
    '''
        
    def insert_Entry(self, txt):
        print('AQUI>', txt, type(txt))
        if self.Entry['state'] != 'enabled':
            state = self.Entry['state']
            self.Entry.config(state = 'enabled')
            self.limpa_entr()
            self.Entry.delete(0, "end")
            self.Entry.insert('end', txt)
            self.Entry.config(state = state)
        else:
            self.limpa_entr()
            self.Entry.insert('end', txt)

    def config_Entry_state(self, estado):
        self.Entry.config(state = estado)
        
    def config_tit_Entry(self, titulo):
        self.tit_Entry.config(text = titulo)
    
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
        

        self.tit_Entry.grid(row=0, column=0, sticky = W, columnspan = columnspan)
        self.Entry.grid(row = 1, column = 0, sticky = sticky, columnspan = columnspan)
        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def limpa_entr(self):
        self.Entry.delete(0, "end")
        
        
    def insere_nova_Entry(self, Entry_):
        self.Entry.destroy()
        self.Entry = Entry_(self.frameLocal)
        self.Entry.grid(row = 2, column = 3, padx = 5)



class sub_Text:

    def __init__(self, framePai, **kwargs):
        self.tit = kwargs.get('tit', 'Título')
        self.state = kwargs.get('state', NORMAL)
        self.width = kwargs.get('width', 50)
        self.height = kwargs.get('height', 4)
        self.scrollbarx = kwargs.get('scrollbarx', True)
        self.scrollbary = kwargs.get('scrollbary', True)
        self.bd = kwargs.get('bd', 3)

        #Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frameLocal = Frame(framePai)


        self.tit_text = ttk.Label(self.frameLocal, text = self.tit )
        self.tit_text.grid(row = 0, column = 0, sticky = W)
        
        self.blocoText = Text(self.frameLocal, insertborderwidth = 5, bd = self.bd, font = "Arial 9", wrap = WORD, width = self.width, height = self.height, state = self.state, autoseparators=True)
        self.blocoText.grid(row = 1, column = 0)


        self.__scrollbar_constr__()


        #~ self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        #~ self.separador1.grid(row = 5, column = 0, columnspan = 5, sticky = "we")


    def config_Text(self, **kwargs):
        self.blocoText.config(kwargs)

    def return_text(self):
        text = self.blocoText.get(1.0, "end")
        return (text)

    def config_tit_text(self, text):
        self.tit_text.config(text = text)
        

    def __scrollbar_constr__(self):
        if self.scrollbarx == True:
            self.scrollbarX = Scrollbar(self.frameLocal, command = self.blocoText.xview, orient = HORIZONTAL)
            self.scrollbarX.grid(row= 2, column = 0, sticky = E+W)
            self.blocoText.config(xscrollcommand = self.scrollbarX.set)
            
            
        if self.scrollbary == True:
            self.scrollbarY = Scrollbar(self.frameLocal, command = self.blocoText.yview, orient = VERTICAL)
            self.scrollbarY.grid(row = 1, column = 1,sticky=N+S)
            self.blocoText.config(yscrollcommand = self.scrollbarY.set)


    def insert_text(self, txtStr):
        self.blocoText.config(state = NORMAL)
        self.blocoText.delete(1.0, END)
        self.blocoText.insert(1.0, txtStr)
        self.blocoText.config(state = DISABLED)
    
    def clear_text(self):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete('1.0', END)
        self.blocoText.config(state=DISABLED)


    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def destroy_frame(self):
        
        self.frameLocal.destroy()


class sub_Treeview:

    def __init__(self, framePai, **kwargs):
        self.quantCol =  kwargs.get('num_cols', 4)
        self.tit = kwargs.get('tit', 'Título')
        self.height = kwargs.get('height', 4)
        self.selectmode = kwargs.get('selectmode', 'browse')
        
        self.frameLocal = Frame(framePai)
        
        self.tit_treeView = Label(self.frameLocal, text = self.tit)
        self.tit_treeView.grid(row = 0, column = 0, sticky = W)
        
        
        columnTuple = self.__column_tuple__()
        self.treeView = ttk.Treeview(self.frameLocal, height = self.height, style = "Treeview", selectmode='browse', columns = columnTuple)
        self.treeView.grid(row = 1, column = 0)
        
        self.__column_constr__()
        
        
        
            #Bloco das Scrollbars(barras de rolagem):
        self.scrollbarY= Scrollbar(self.frameLocal, command = self.treeView.yview)
        self.scrollbarY.grid(row = 1, column = 1,sticky = N+S)
            #Bloco  Declaradas a Scrollbar, treeView1 é configurado a recebê-las:
        self.treeView.config(yscrollcommand = self.scrollbarY.set)

    def pointer_treeView(self):
        return(self.treeView)

    def config_treeView(self, **kwargs):
        self.treeView.config(kwargs)
    
    def config_Label(self, **kwargs):
        self.tit_treeView(self, **kwargs)
        
        
    def config_tit_treeView(self, tit):
        self.tit_treeView.config(text = tit)


    def config_tit_col_treeView(self, col, titulo):
        if type(col) != str:
            col = str(col)
        if col == '0':
            col = '#0'
        self.treeView.heading(col, text = titulo)

    def selection_treeView(self):
        
        return(self.treeView.selection())

    def idd_selection_treeView(self):
        return(int(self.treeView.selection()[0]))


    def item_treeView(self, idd):
        return(self.treeView.item(idd))

    def __column_tuple__(self):
        
        lstAux = []
        if self.quantCol == 1:
            columnTuple = tuple(lstAux)
        
        else:
            n = 0
            while n < (self.quantCol-1):
                quant = n + 1
                columnAux = str(quant)
                lstAux.append(columnAux)
                n = n + 1
            
            columnTuple = tuple(lstAux)
        
        return(columnTuple)


    def config_heading(self, index, **kwargs):
        if index == 0 or index == '0':
            index = '#0'
            
        self.treeView.heading(index, **kwargs)
        

    def config_column(self, index, **kwargs):
            if index == 0 or index == '0':
                index = '#0'
            self.treeView.column("#0", **kwargs)


    def __column_constr__(self):
        self.treeView.heading("#0", text = "text")
        self.treeView.column("#0", width = 245, stretch = 0)
        
        n = 1
        while n < (self.quantCol):
            columnAux = str(n)
            self.treeView.heading(columnAux, text="coluna 1")
            self.treeView.column(columnAux, width=100, stretch = 0)
            n = n + 1


    def insert_kwargs_treeView(self, **kwargs):
        idd = kwargs.get('idd', None)
        text = kwargs.get('text', None)
        values = kwargs.get('values', None)
        
        self.treeView.insert('', 0, iid = idd, text = text, values = values)


    def insere_elem_treeView(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = '', **kwargs):
        idd = kwargs.get('idd', None)
        elems = (value1, value2, value3, value4)
        self.treeView.insert('', 0, iid = idd, text = value0, values = elems)
        #~ print('Dentro do insere:', *self.treeView.get_children())

    def insere_lst_elem_treeView(self, *lst_args, **kwargs):
        lst_itens = lst_args[0] #Desempacotando o argumento
        #~ print('\nTESTE empacotado', lst_itens)
        #~ print('\nTESTE desempacotado', lst_itens[0])
        idd = kwargs.get('idd', None)#Adquirindo a id do elemento
        self.treeView.insert('', 0, iid = idd, text = lst_itens[0], values = lst_itens[1:])

    def insert_lst_treeView(self, lst_treeView):
        for elem in lst_treeView:
            lst = elem.get('lst_treeView', [''])
            idd = elem.get('idd', None)
            self.insere_lst_elem_treeView(lst, idd = idd)
        
        
    def grid_frame(self, **kwargs):
        row = kwargs.get('row', 0)
        column = kwargs.get('column', 0)
        sticky = kwargs.get('sticky', W)
        columnspan = kwargs.get('columnspan', 1)
        rowspan = kwargs.get('rowspan', 1)
        pady = kwargs.get('pady', 5)
        padx = kwargs.get('padx', 5)

        self.frameLocal.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan, pady = pady, padx = padx, sticky = sticky)

    def clear_treeView(self):
        self.treeView.delete(*self.treeView.get_children())

    def destroy_frame(self):
        self.treeView.destroy()
        self.frameLocal.destroy()
