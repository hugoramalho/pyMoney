'''
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

import os
import codecs

from tkinter import *
from tkinter import ttk
from time import sleep
'''

from .subFramesProg import *
from .calendario_3 import *



class frame_1T_3abas:
    
    def __init__ (self, framePai, **kwargs):
        
        #Blobo (1): Configurando frame que conterá as abas, o frameAbas:
        self.frameLocal = LabelFrame(framePai, text = '', relief=GROOVE,  padx = 15, pady = 15)

        
        
        #Bloco (2): O título do frame que contém abas é declarado abaixo, e recebe a variável titulo dado no __init__:
        self.tit1 = Label(self.frameLocal, text = "Título", font = 'Verdana' ,pady = 5, padx = 3, anchor = CENTER)
        self.tit1.grid(row=0, column = 0, sticky = E+W)
        

        #Bloco (3): Aqui, é instanciado o tipo Notebook, que na verdade é um frame que conterá as abas:
        self.abasBarra = ttk.Notebook(self.frameLocal)
        self.abasBarra.grid(row = 1, column = 0, sticky = E+W)
        

        #Bloco (4): Abaixo, cada aba é instanciada, cujo frame pai é o "Abas":
        self.aba1 = ttk.Frame(self.abasBarra)   
        self.abasBarra.add(self.aba1, text = "Aba 1")
        
        self.aba2 = ttk.Frame(self.abasBarra)  
        self.abasBarra.add(self.aba2, text = "Aba 2")
        
        self.aba3 = ttk.Frame(self.abasBarra)  
        self.abasBarra.add(self.aba3, text = "Aba 3")


        
    def pointer_frame_aba1(self):
        return(self.aba1)
        
    def pointer_frame_aba2(self):
        return(self.aba2)

    def pointer_frame_aba3(self):
        return(self.aba3)


    def config_tit1(self, titulo):
        self.tit1.config(text = titulo)

    def config_nome_aba1(self, titulo):
        self.abasBarra.tab(self.aba1, text = titulo)
        
    def config_nome_aba2(self, titulo):
        self.abasBarra.tab(self.aba2, text = titulo)
    
    def config_nome_aba3(self, titulo):
        self.abasBarra.tab(self.aba3, text = titulo)


    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()

class frame_1T_5abas:
    
    def __init__ (self, framePai, titulo = ' Menu em abas', frame1Titulo = 'Aba 1', frame2Titulo ='Aba 2', frame3Titulo='Aba 3', frame4Titulo='Aba 4', frame5Titulo='Aba 5'):
        
        #Blobo (1): Configurando frame que conterá as abas, o frameAbas:
        self.frameLocal = LabelFrame(framePai, text = 'Titulo', relief=GROOVE, padx = 15, pady = 15)
        #self.frameLocal.grid(row = 0, column = 0, sticky = E+W+N+S)
        
        
        
        #Bloco (2): O título do frame que contém abas é declarado abaixo, e recebe a variável titulo dado no __init__:
        self.tit2 = Label(self.frameLocal, text = titulo, font = 'Verdana' , anchor = CENTER)
        self.tit2.grid(row=0, column = 0, pady = 10, sticky = E+W)
        

        #Bloco (3): Aqui, é instanciado o tipo Notebook, que na verdade é um frame que conterá as abas:
        self.abasBarra = ttk.Notebook(self.frameLocal)
        self.abasBarra.grid(row = 1, column = 0, sticky = E+W)
        

        #Bloco (4): Abaixo, cada aba é instanciada, cujo frame pai é o "Abas":
        self.aba1 = ttk.Frame(self.abasBarra)   
        self.abasBarra.add(self.aba1, text = frame1Titulo)
        
        self.aba2 = ttk.Frame(self.abasBarra)  
        self.abasBarra.add(self.aba2, text = frame2Titulo)
        
        self.aba3 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba3, text =frame3Titulo)
        
        self.aba4 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba4, text = frame4Titulo)
        
        self.aba5 = ttk.Frame(self.abasBarra)
        self.abasBarra.add(self.aba5, text = frame5Titulo)

        
    def pointer_frame_aba1(self):
        return(self.aba1)
        
    def pointer_frame_aba2(self):
        return(self.aba2)
        
    def pointer_frame_aba3(self):
        return(self.aba3)
        
    def pointer_frame_aba4(self):
        return(self.aba4)
        
    def pointer_frame_aba5(self):
        return(self.aba5)
        

    def config_tit1(self, titulo):
        self.frameLocal.config(text = titulo)

    def config_tit2(self, titulo):
        self.tit2.config(text = titulo)


    def config_nome_aba1(self, titulo):
        self.abasBarra.tab(self.aba1, text = titulo)
        
    def config_nome_aba2(self, titulo):
        self.abasBarra.tab(self.aba2, text = titulo)
    
    def config_nome_aba3(self, titulo):
        self.abasBarra.tab(self.aba3, text = titulo)
                
    def config_nome_aba4(self, titulo):
        self.abasBarra.tab(self.aba4, text = titulo)

    def config_nome_aba5(self, titulo):
        self.abasBarra.tab(self.aba5, text = titulo)
                        
    
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    
    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_clientes_cadastrados:
    
    def __init__(self, framePai, **kwargs):

        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, relief = FLAT, text ='', padx ="8", pady = "8")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        self.tit2 = Label(self.frameLocal, text = 'Banco de serviços e ítens')
        self.tit2.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = W)
        
        #Frame que conterá as Combobox 2, 3, e 4:
        self.frame_CBox2_3_4 = ttk.LabelFrame(self.frameLocal, text = 'Filtrar por:')
        self.frame_CBox2_3_4.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 3)
        #Bloco CBox2:
        self.CBox2 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Categoria", CBox_state = 'readonly')
        self.CBox2.grid_frame(row = 0, column = 0, sticky = W)
        #Bloco CBox3:
        self.CBox3 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Subcategoria", CBox_state = 'readonly')
        self.CBox3.grid_frame(row = 0, column = 1, sticky = W)
        #Bloco CBox4:
        self.CBox4 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Espécie", CBox_state = 'readonly')
        self.CBox4.grid_frame(row = 0, column = 2, sticky = W)

        #Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 7, height = 8)
        self.treeView1.grid_frame(row = 2, column = 0, columnspan = 5, padx = 5, pady = 5)
        self.config_tit_col_treeView1(0, 'Nome')
        self.config_tit_col_treeView1(1, 'Telefone')
        self.config_tit_col_treeView1(2, 'Email')
        self.config_tit_col_treeView1(3, 'Endereço')
        self.config_tit_col_treeView1(4, 'Cidade')
        self.config_tit_col_treeView1(5, 'Estado')
        self.config_tit_col_treeView1(6, 'CEP')


        self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador1.grid(row = 3, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = 'we')
        
        self.entr1 = sub_Entry(self.frameLocal, tit_Entry = 'Nome:', state_Entry = 'readonly', width = 55)
        self.entr1.grid_frame(row = 4, column = 0, columnspan = 2)

        self.entr2 = sub_Entry(self.frameLocal, tit_Entry = 'Gênero:', state_Entry = 'readonly', width = 26)
        self.entr2.grid_frame(row = 4, column = 2)
        
        self.entr3 = sub_Entry(self.frameLocal, tit_Entry = 'Telefone principal:', state_Entry = 'readonly', width = 26)
        self.entr3.grid_frame(row = 4, column = 3)


        self.entr4 = sub_Entry(self.frameLocal, tit_Entry = 'Telefone alternativo:', state_Entry = 'readonly', width = 26)
        self.entr4.grid_frame(row = 4, column = 4)

        self.entr5 = sub_Entry(self.frameLocal, tit_Entry = 'CPF/CNPJ:', state_Entry = 'readonly', width = 26)
        self.entr5.grid_frame(row = 5, column = 2)
        
        self.entr6 = sub_Entry(self.frameLocal, tit_Entry = 'E-mail principal:', state_Entry = 'readonly', width = 26)
        self.entr6.grid_frame(row = 5, column = 3)
        
        self.entr7 = sub_Entry(self.frameLocal, tit_Entry = 'E-mail alternativo:', state_Entry = 'readonly', width = 26)
        self.entr7.grid_frame(row = 5, column = 4)
        
        self.entr8 = sub_Entry(self.frameLocal, tit_Entry = 'Número:', state_Entry = 'readonly', width = 26)
        self.entr8.grid_frame(row = 6, column = 2)

        self.entr9 = sub_Entry(self.frameLocal, tit_Entry = 'CEP:', state_Entry = 'readonly', width = 26)
        self.entr9.grid_frame(row = 6, column = 3)
        
        self.entr10 = sub_Entry(self.frameLocal, tit_Entry = 'Data de nascimento:', state_Entry = 'readonly', width = 26)
        self.entr10.grid_frame(row = 6, column = 4)
        
        self.entr11 = sub_Entry(self.frameLocal, tit_Entry = 'UF:', state_Entry = 'readonly', width = 26)
        self.entr11.grid_frame(row = 5, column = 0)
        
        self.entr12 = sub_Entry(self.frameLocal, tit_Entry = 'Cidade:', state_Entry = 'readonly', width = 26)
        self.entr12.grid_frame(row = 5, column = 1)
        
        self.entr13 = sub_Entry(self.frameLocal, tit_Entry = 'Bairro:', state_Entry = 'readonly', width = 26)
        self.entr13.grid_frame(row = 6, column = 0)
        
        self.entr14 = sub_Entry(self.frameLocal, tit_Entry = 'logradouro:', state_Entry = 'readonly', width = 26)
        self.entr14.grid_frame(row = 6, column = 1)
        
        self.entr15 = sub_Entry(self.frameLocal, tit_Entry = 'Tipo de residência:', state_Entry = 'readonly', width = 26)
        self.entr15.grid_frame(row = 7, column = 0)
        
        self.entr16 = sub_Entry(self.frameLocal, tit_Entry = 'Nome do edifício/condomínio:', state_Entry = 'readonly', width = 26)
        self.entr16.grid_frame(row = 7, column = 1)
        
        self.entr17 = sub_Entry(self.frameLocal, tit_Entry = 'Número do apartamento:', state_Entry = 'readonly', width = 26)
        self.entr17.grid_frame(row = 7, column = 2)





        self.menu_RC = sub_Menu(self.frameLocal)

        self.text1 = sub_Text(self.frameLocal, tit = 'Titulo texto', state = DISABLED, width = 40, scrollbarx = False)
        #~ self.text1.grid_frame(row = 5, colum = 0, columnspan = 2, rowspan = 3)
        
        #~ #Bloco botao1:
        #~ self.botao1 = ttk.Button(self.frameLocal, text = "Enviar")#, padding = "1 10 1 10")
        #~ self.botao1.grid(row = 5, column = 1,  sticky = W+E,padx = 7)


    def config_tit_Frame_Cbox(self, tit):
        self.frame_CBox2_3_4.config(text = tit)

    def config_tit_entr1(self, tit):
        self.entr1.config_tit_Entry(tit)
    
    def config_tit_entr2(self, tit):
        self.entr2.config_tit_Entry(tit)
        
    def config_tit_entr3(self, tit):
        self.entr3.config_tit_Entry(tit)
        
    def config_tit_entr4(self, tit):
        self.entr4.config_tit_Entry(tit)
        
    def config_tit_entr5(self, tit):
        self.entr5.config_tit_Entry(tit)
        
    def config_tit_entr6(self, tit):
        self.entr6.config_tit_Entry(tit)
        
    def config_tit_entr7(self, tit):
        self.entr7.config_tit_Entry(tit)
    
    def config_tit_entrN(self, n, tit):
        if n == 1:
            self.entr1.config_tit_Entry(tit)
            
        elif n == 2:
            self.entr2.config_tit_Entry(tit)
        
        elif n == 3:
            self.entr3.config_tit_Entry(tit)
            
        elif n == 4:
            self.entr4.config_tit_Entry(tit)
        
        elif n == 5:
            self.entr5.config_tit_Entry(tit)
        
        elif n == 6:
            self.entr6.config_tit_Entry(tit)
        
        elif n == 7:
            self.entr7.config_tit_Entry(tit)

        elif n == 8:
            self.entr8.config_tit_Entry(tit)

        elif n == 9:
            self.entr9.config_tit_Entry(tit)

        elif n == 10:
            self.entr10.config_tit_Entry(tit)

        elif n == 11:
            self.entr11.config_tit_Entry(tit)
        
        elif n == 12:
            self.entr12.config_tit_Entry(tit)
        
        elif n == 13:
            self.entr13.config_tit_Entry(tit)
        
        elif n == 14:
            self.entr14.config_tit_Entry(tit)
        
        elif n == 15:
            self.entr15.config_tit_Entry(tit)
        
        elif n == 16:
            self.entr16.config_tit_Entry(tit)
        
        elif n == 17:
            self.entr17.config_tit_Entry(tit)

    def popup_menu(self, event):
        self.menu_RC.popup(event)

    def limpa_entr1(self):
        self.entr1.limpa_entr()
        
    def limpa_entr2(self):
        self.entr2.limpa_entr()

    def limpa_entr3(self):
        self.entr3.limpa_entr()
        
    def limpa_entr4(self):
        self.entr4.limpa_entr()
        
    def limpa_entr5(self):
        self.entr5.limpa_entr()

    def limpa_entr6(self):
        self.entr6.limpa_entr()
        
    def limpa_entr7(self):
        self.entr7.limpa_entr()

    def insert_entr1(self, txt):
        self.entr1.insert_Entry(txt)

    def insert_entr2(self, txt):
        self.entr2.insert_Entry(txt)

    def insert_entr3(self, txt):
        self.entr3.insert_Entry(txt)

    def insert_entr4(self, txt):
        self.entr4.insert_Entry(txt)

    def insert_entr5(self, txt):
        self.entr5.insert_Entry(txt)

    def insert_entr6(self, txt):
        self.entr6.insert_Entry(txt)

    def insert_entr7(self, txt):
        self.entr7.insert_Entry(txt)

    def insert_entrN(self, n, tit):
        if n == 1:
            self.entr1.insert_Entry(tit)
            
        elif n == 2:
            self.entr2.insert_Entry(tit)
        
        elif n == 3:
            self.entr3.insert_Entry(tit)
            
        elif n == 4:
            self.entr4.insert_Entry(tit)
        
        elif n == 5:
            self.entr5.insert_Entry(tit)
        
        elif n == 6:
            self.entr6.insert_Entry(tit)
        
        elif n == 7:
            self.entr7.insert_Entry(tit)

        elif n == 8:
            self.entr8.insert_Entry(tit)

        elif n == 9:
            self.entr9.insert_Entry(tit)

        elif n == 10:
            self.entr10.insert_Entry(tit)

        elif n == 11:
            self.entr11.insert_Entry(tit)
            
        elif n == 12:
            self.entr12.insert_Entry(tit)
        
        elif n == 13:
            self.entr13.insert_Entry(tit)
        
        elif n == 14:
            self.entr14.insert_Entry(tit)
        
        elif n == 15:
            self.entr15.insert_Entry(tit)
        
        elif n == 16:
            self.entr16.insert_Entry(tit)
        
        elif n == 17:
            self.entr17.insert_Entry(tit)

    def config_entr1(self, **kwargs):
        self.entr1.config_Entry(**kwargs)

    def insert_text1(self, txtStr):
        self.text1.insert_text(txtStr)

    def pointer_treeView1(self):
        return(self.treeView1.pointer_treeView())

    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', **kwargs):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, **kwargs)

    def insere_lst_elem_treeView1(self, *lst_itens, **kwargs):
        self.treeView1.insere_lst_elem_treeView(*lst_itens, **kwargs)

    def clear_treeView1(self):
        self.treeView1.clear_treeView()
    
    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)

    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))

    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)
    
    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())

    def idd_selection_treeView1(self):
        return(self.treeView1.idd_selection_treeView())

    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())

    def pointer_CBox2(self):
        return(self.CBox2.pointer_CBox())
        
    def pointer_CBox3(self):
        return(self.CBox3.pointer_CBox())

    def config_tit_CBox1(self, titulo):
        self.tit_CBox1.config_tit_CBox(titulo)

    def config_tit_CBox2(self, titulo):
        self.tit_CBox2.config_tit_CBox(titulo)

    def config_tit_CBox3(self, titulo):
        self.tit_CBox3.config_tit_CBox(titulo)

    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)

    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)
        
    def define_values_CBox3(self, lst):
        self.CBox3.define_values_CBox(lst)
    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
        
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())
        
    def retorna_escolha_CBox3(self):
        return(self.CBox3.retorna_escolha_CBox())
        
    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set_CBox_default(tit)
        
    def config_CBox3_state(self, estado):
        self.CBox3.config_CBox_state(estado)
    
    def pointer_frameLocal(self):
        return(self.frameLocal)
        
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_fornec_cadastrados:
    
    def __init__(self, framePai, **kwargs):
        
        
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, relief = FLAT, text ='', padx ="8", pady = "8")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        
        self.tit2 = Label(self.frameLocal, text = 'Banco de serviços e ítens')
        self.tit2.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = W)
        
        
        #Frame que conterá a Combobox 1
        self.frame_CBox1 = ttk.LabelFrame(self.frameLocal, text = 'Selecione o tipo:')
        self.frame_CBox1.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        #Bloco CBox1:
        self.CBox1 = sub_CBox(self.frame_CBox1, tit_CBox = '', set_CBox_default = "Item/Serviço", CBox_state = 'readonly')
        self.CBox1.grid_frame(row = 0, column = 0, sticky = S)
        
        
        #Frame que conterá as Combobox 2, 3, e 4:
        self.frame_CBox2_3_4 = ttk.LabelFrame(self.frameLocal, text = 'Filtrar por:')
        self.frame_CBox2_3_4.grid(row = 1, column = 1, padx = 5, pady = 5, columnspan = 3)
        #Bloco CBox2:
        self.CBox2 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Categoria", CBox_state = 'readonly')
        self.CBox2.grid_frame(row = 0, column = 0, sticky = W)
        #Bloco CBox3:
        self.CBox3 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Subcategoria", CBox_state = 'readonly')
        self.CBox3.grid_frame(row = 0, column = 1, sticky = W)
        #Bloco CBox4:
        self.CBox4 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Espécie", CBox_state = 'readonly')
        self.CBox4.grid_frame(row = 0, column = 2, sticky = W)



        #Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 5, height = 8)
        self.treeView1.grid_frame(row = 2, column = 0, columnspan = 5, padx = 5, pady = 5)

        self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador1.grid(row = 3, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = 'we')
        
        self.entr1 = sub_Entry(self.frameLocal, tit_Entry = 'entr1', state_Entry = 'readonly', width = 49)
        self.entr1.grid_frame(row = 4, column = 0, columnspan = 3)

        self.entr2 = sub_Entry(self.frameLocal, tit_Entry = 'entr2', state_Entry = 'readonly')
        self.entr2.grid_frame(row = 4, column = 2)
        
        self.entr3 = sub_Entry(self.frameLocal, tit_Entry = 'entr3', state_Entry = 'readonly')
        self.entr3.grid_frame(row = 4, column = 3)


        self.entr4 = sub_Entry(self.frameLocal, tit_Entry = 'entr4', state_Entry = 'readonly')
        self.entr4.grid_frame(row = 5, column = 3)

        self.entr5 = sub_Entry(self.frameLocal, tit_Entry = 'entr5', state_Entry = 'readonly')
        self.entr5.grid_frame(row = 5, column = 2)
        
        self.entr6 = sub_Entry(self.frameLocal, tit_Entry = 'entr6', state_Entry = 'readonly')
        self.entr6.grid_frame(row = 6, column = 2)
        
        self.entr7 = sub_Entry(self.frameLocal, tit_Entry = 'entr7', state_Entry = 'readonly')
        self.entr7.grid_frame(row = 6, column = 3)
        
        self.text1 = sub_Text(self.frameLocal, tit = 'Titulo texto', state = DISABLED, width = 40, scrollbarx = False)
        self.text1.grid_frame(row = 5, colum = 0, columnspan = 2, rowspan = 3)
        
        #~ #Bloco botao1:
        #~ self.botao1 = ttk.Button(self.frameLocal, text = "Enviar")#, padding = "1 10 1 10")
        #~ self.botao1.grid(row = 5, column = 1,  sticky = W+E,padx = 7)


        ## ATENÇÃO LEMBRAR DE SETAR OS VALORES JUNTO ÀS INSTANCIAÇÕES:
        self.define_values_CBox1(['Pessoa', 'Estabelecimento'])
        self.set_CBox1_default('Pessoa\Estabelecimento')

        self.config_tit_treeView1('')
        self.config_tit_col_treeView1(0, "Nome:")
        self.config_tit_col_treeView1(1, "Categoria:")
        self.config_tit_col_treeView1(2, "Telefone:")
        self.config_tit_col_treeView1(3, "Email:")
        self.config_tit_col_treeView1(4, "Cidade:")

        self.config_tit_entr1('Nome:')
        self.config_tit_entr2('Categoria:')
        self.config_tit_entr3('Telefone principal:')
        self.config_tit_entr4('Telefone alternativo:')
        self.config_tit_entr5('Email:')
        self.config_tit_entr6('CNPJ:')
        self.config_tit_entr7('Localidade:')

        self.menu_RC = sub_Menu(self.frameLocal)


    def config_tit_entr1(self, tit):
        self.entr1.config_tit_Entry(tit)
    
    def config_tit_entr2(self, tit):
        self.entr2.config_tit_Entry(tit)
        
    def config_tit_entr3(self, tit):
        self.entr3.config_tit_Entry(tit)
        
    def config_tit_entr4(self, tit):
        self.entr4.config_tit_Entry(tit)
        
    def popup_menu(self, event):
        self.menu_RC.popup(event)

    def config_tit_entr5(self, tit):
        self.entr5.config_tit_Entry(tit)
        
        
    def config_tit_entr6(self, tit):
        self.entr6.config_tit_Entry(tit)
        
    def config_tit_entr7(self, tit):
        self.entr7.config_tit_Entry(tit)

    def limpa_entr1(self):
        self.entr1.limpa_entr()
        
    def limpa_entr2(self):
        self.entr2.limpa_entr()

    def limpa_entr3(self):
        self.entr3.limpa_entr()
        
    def limpa_entr4(self):
        self.entr4.limpa_entr()
        
    def limpa_entr5(self):
        self.entr5.limpa_entr()

    def limpa_entr6(self):
        self.entr6.limpa_entr()
        
    def limpa_entr7(self):
        self.entr7.limpa_entr()

    def insert_entr1(self, txt):
        self.entr1.insert_Entry(txt)

    def insert_entr2(self, txt):
        self.entr2.insert_Entry(txt)

    def insert_entr3(self, txt):
        self.entr3.insert_Entry(txt)

    def insert_entr4(self, txt):
        self.entr4.insert_Entry(txt)

    def insert_entr5(self, txt):
        self.entr5.insert_Entry(txt)

    def insert_entr6(self, txt):
        self.entr6.insert_Entry(txt)

    def insert_entr7(self, txt):
        self.entr7.insert_Entry(txt)


    def config_entr1(self, **kwargs):
        self.entr1.config_Entry(**kwargs)


    def insert_text1(self, txtStr):
        self.text1.insert_text(txtStr)


    def pointer_treeView1(self):
        return(self.treeView1.pointer_treeView())

    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', **kwargs):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, **kwargs)

    def insere_lst_elem_treeView1(self, lst_itens, **kwargs):
        self.treeView1.insere_lst_elem_treeView(lst_itens, **kwargs)

    def clear_treeView1(self):
        self.treeView1.clear_treeView()
    
    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)

    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))


    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)
    
    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())
        
        

    def idd_selection_treeView1(self):
        return(self.treeView1.idd_selection_treeView())



    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())

    def pointer_CBox2(self):
        return(self.CBox2.pointer_CBox())
        
    def pointer_CBox3(self):
        return(self.CBox3.pointer_CBox())

    def config_tit_CBox1(self, titulo):
        self.tit_CBox1.config_tit_CBox(titulo)

    def config_tit_CBox2(self, titulo):
        self.tit_CBox2.config_tit_CBox(titulo)

    def config_tit_CBox3(self, titulo):
        self.tit_CBox3.config_tit_CBox(titulo)

    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)

    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)
        
    def define_values_CBox3(self, lst):
        self.CBox3.define_values_CBox(lst)
        
    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
        
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())
        
    def retorna_escolha_CBox3(self):
        return(self.CBox3.retorna_escolha_CBox())
        
    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set_CBox_default(tit)
        
    def config_CBox3_state(self, estado):
        self.CBox3.config_CBox_state(estado)
    
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_itens_cadastrados:
    
    def __init__(self, framePai, **kwargs):
        
        
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, relief = FLAT, text ='', padx ="8", pady = "8")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        
        self.tit2 = Label(self.frameLocal, text = 'Banco de serviços e ítens')
        self.tit2.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = W)
        
        
        #Frame que conterá a Combobox 1
        self.frame_CBox1 = ttk.LabelFrame(self.frameLocal, text = 'Selecione o tipo:')
        self.frame_CBox1.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        #Bloco CBox1:
        self.CBox1 = sub_CBox(self.frame_CBox1, tit_CBox = '', set_CBox_default = "ítem/Serviço", CBox_state = 'readonly')
        self.CBox1.grid_frame(row = 0, column = 0, sticky = S)
        
        
        
        #Frame que conterá as Combobox 2, 3, e 4:
        self.frame_CBox2_3_4 = ttk.LabelFrame(self.frameLocal, text = 'Filtrar por:')
        self.frame_CBox2_3_4.grid(row = 1, column = 1, padx = 5, pady = 5, columnspan = 3)
        #Bloco CBox2:
        self.CBox2 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Categoria", CBox_state = 'readonly')
        self.CBox2.grid_frame(row = 0, column = 0, sticky = W)
        #Bloco CBox3:
        self.CBox3 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Subcategoria", CBox_state = 'readonly')
        self.CBox3.grid_frame(row = 0, column = 1, sticky = W)
        #Bloco CBox4:
        self.CBox4 = sub_CBox(self.frame_CBox2_3_4, tit_CBox = '', set_CBox_default = "Espécie", CBox_state = 'readonly')
        self.CBox4.grid_frame(row = 0, column = 2, sticky = W)



        #Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 4, height = 8)
        self.treeView1.grid_frame(row = 2, column = 0, columnspan = 5, padx = 5, pady = 5)

        self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador1.grid(row = 3, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = 'we')
        
        self.entr1 = sub_Entry(self.frameLocal, tit_Entry = 'entr1', state_Entry = 'readonly', width = 49)
        self.entr1.grid_frame(row = 4, column = 0, columnspan = 3)

        self.entr2 = sub_Entry(self.frameLocal, tit_Entry = 'entr2', state_Entry = 'readonly')
        self.entr2.grid_frame(row = 4, column = 2)
        
        self.entr3 = sub_Entry(self.frameLocal, tit_Entry = 'entr3', state_Entry = 'readonly')
        self.entr3.grid_frame(row = 4, column = 3)


        self.entr4 = sub_Entry(self.frameLocal, tit_Entry = 'entr4', state_Entry = 'readonly')
        self.entr4.grid_frame(row = 5, column = 3)

        self.entr5 = sub_Entry(self.frameLocal, tit_Entry = 'entr5', state_Entry = 'readonly')
        self.entr5.grid_frame(row = 5, column = 2)
        
        self.entr6 = sub_Entry(self.frameLocal, tit_Entry = 'entr6', state_Entry = 'readonly')
        self.entr6.grid_frame(row = 6, column = 2)
        
        self.entr7 = sub_Entry(self.frameLocal, tit_Entry = 'entr7', state_Entry = 'readonly')
        self.entr7.grid_frame(row = 6, column = 3)
        
        self.text1 = sub_Text(self.frameLocal, tit = 'Titulo texto', state = DISABLED, width = 40, scrollbarx = False)
        self.text1.grid_frame(row = 5, colum = 0, columnspan = 2, rowspan = 3)
        
        #~ #Bloco botao1:
        #~ self.botao1 = ttk.Button(self.frameLocal, text = "Enviar")#, padding = "1 10 1 10")
        #~ self.botao1.grid(row = 5, column = 1,  sticky = W+E,padx = 7)
        self.menu_RC = sub_Menu(self.frameLocal)

    def popup_menu(self, event):
        self.menu_RC.popup(event)
        
    def config_tit_entr1(self, tit):
        self.entr1.config_tit_Entry(tit)
    
    def config_tit_entr2(self, tit):
        self.entr2.config_tit_Entry(tit)
        
    def config_tit_entr3(self, tit):
        self.entr3.config_tit_Entry(tit)
        
    def config_tit_entr4(self, tit):
        self.entr4.config_tit_Entry(tit)
        
        
    def config_tit_entr5(self, tit):
        self.entr5.config_tit_Entry(tit)
        
        
    def config_tit_entr6(self, tit):
        self.entr6.config_tit_Entry(tit)
        
        
    def config_tit_entr7(self, tit):
        self.entr7.config_tit_Entry(tit)


    def limpa_entr1(self):
        self.entr1.limpa_entr()
        
    def limpa_entr2(self):
        self.entr2.limpa_entr()

    def limpa_entr3(self):
        self.entr3.limpa_entr()
        
    def limpa_entr4(self):
        self.entr4.limpa_entr()
        
    def limpa_entr5(self):
        self.entr5.limpa_entr()

    def limpa_entr6(self):
        self.entr6.limpa_entr()
        
    def limpa_entr7(self):
        self.entr7.limpa_entr()

    def insert_entr1(self, txt):
        self.entr1.insert_Entry(txt)


    def insert_entr2(self, txt):
        self.entr2.insert_Entry(txt)

    def insert_entr3(self, txt):
        self.entr3.insert_Entry(txt)

    def insert_entr4(self, txt):
        self.entr4.insert_Entry(txt)

    def insert_entr5(self, txt):
        self.entr5.insert_Entry(txt)

    def insert_entr6(self, txt):
        self.entr6.insert_Entry(txt)

    def insert_entr7(self, txt):
        self.entr7.insert_Entry(txt)
    
    def config_tit_text1(self, tit):
        self.text1.config_tit_text(tit)

    def config_entr1(self, **kwargs):
        self.entr1.config_Entry(**kwargs)
    
    def config_text1(self, **kwargs):
        self.text1.config_Text(**kwargs)

    def insert_text1(self, txtStr):
        self.text1.insert_text(txtStr)


    def pointer_treeView1(self):
        return(self.treeView1.pointer_treeView())

    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', **kwargs):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, **kwargs)

    def insere_lst_elem_treeView1(self, lst_itens, **kwargs):
        self.treeView1.insere_lst_elem_treeView(lst_itens, **kwargs)

    def clear_treeView1(self):
        self.treeView1.clear_treeView()
    
    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)

    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))


    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)
    
    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())

    def idd_selection_treeView1(self):
        return(self.treeView1.idd_selection_treeView())



    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())

    def pointer_CBox2(self):
        return(self.CBox2.pointer_CBox())
        
    def pointer_CBox3(self):
        return(self.CBox3.pointer_CBox())

    def config_tit_CBox1(self, titulo):
        self.tit_CBox1.config_tit_CBox(titulo)

    def config_tit_CBox2(self, titulo):
        self.tit_CBox2.config_tit_CBox(titulo)

    def config_tit_CBox3(self, titulo):
        self.tit_CBox3.config_tit_CBox(titulo)

    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)

    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)
        
    def define_values_CBox3(self, lst):
        self.CBox3.define_values_CBox(lst)
        
    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
        
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())
        
    def retorna_escolha_CBox3(self):
        return(self.CBox3.retorna_escolha_CBox())
        
    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set_CBox_default(tit)
        
    def config_CBox3_state(self, estado):
        self.CBox3.config_CBox_state(estado)
    
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_resumoGer:
    
    def __init__(self, framePai, **kwargs):
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = Frame(framePai, padx ="8", pady = "8")
        
        #Bloco 2, instanciando o frame que conterá a treeview1
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 3)
        self.treeView1.grid_frame(row = 0, column = 0)


        self.treeView2 = sub_Treeview(self.frameLocal, num_cols = 3)
        self.treeView2.grid_frame(row = 1, column = 0)



        self.treeView3 = sub_Treeview(self.frameLocal, num_cols = 3)
        self.treeView3.grid_frame(row = 2, column = 0)



        self.treeView4 = sub_Treeview(self.frameLocal, num_cols = 3)
        self.treeView4.grid_frame(row = 0, column = 1)

        # TODO SETAR OS PARAMETROS ABAXO NA INSTANCIAÇÃO
        self.config_tit_col_treeView1(0, 'Nome da conta:')
        self.config_tit_col_treeView1(1, 'Tipo:')
        self.config_tit_col_treeView1(2, 'Saldo atual:')


    def pointer_treeView1(self):
        return(self.treeView1)

    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView1(self, lst_itens):
        self.treeView1.insere_lst_elem_treeView(lst_itens)
    
    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())
        
    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))
    
    def clear_treeView1(self):
        self.treeView1.clear_treeView()


    def pointer_treeView2(self):
        return(self.treeView2)

    def config_tit_col_treeView2(self, col, titulo):
        self.treeView2.config_tit_col_treeView(col, titulo)

    def insere_elem_treeView2(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView2.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView2(self, lst_itens):
        self.treeView2.insere_lst_elem_treeView(lst_itens)
    
    def selection_treeView2(self):
        return(self.treeView2.selection_treeView())
        
    def item_treeView2(self, idd):
        return(self.treeView2.item_treeView(idd))
    
    def clear_treeView2(self):
        self.treeView2.clear_treeView()


    def pointer_treeView3(self):
        return(self.treeView1)

    def config_tit_col_treeView3(self, col, titulo):
        self.treeView3.config_tit_col_treeView(col, titulo)

    def insere_elem_treeView3(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView3.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView3(self, lst_itens):
        self.treeView3.insere_lst_elem_treeView(lst_itens)
    
    def selection_treeView3(self):
        return(self.treeView3.selection_treeView())
        
    def item_treeView3(self, idd):
        return(self.treeView3.item_treeView(idd))
    
    def clear_treeView3(self):
        self.treeView3.clear_treeView()

    def pointer_treeView4(self):
        return(self.treeView4)

    def config_tit_col_treeView4(self, col, titulo):
        self.treeView4.config_tit_col_treeView(col, titulo)

    def insere_elem_treeView4(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView4.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView4(self, lst_itens):
        self.treeView4.insere_lst_elem_treeView(lst_itens)
    
    def selection_treeView4(self):
        return(self.treeView4.selection_treeView())
        
    def item_treeView4(self, idd):
        return(self.treeView4.item_treeView(idd))
    
    def clear_treeView4(self):
        self.treeView4.clear_treeView()



    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_nova_gerencia:
    #APLICAR MUDANÇAS À CLASSE frame_6T_2E_3B_1Tex_1Cbox_1Tview
    def __init__(self, framePai, **kwargs):
        
        
        
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, text = "Titulo 1", relief=GROOVE, borderwidth=2, padx ="8", pady = "8")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)
        


        #Bloco entr1:
        self.entr1 = sub_Entry(self.frameLocal)
        self.entr1.grid_frame(row = 0, column = 0,  padx = 5)


        
        #Bloco entr2:
        self.entr2 = sub_Entry(self.frameLocal)
        self.entr2.grid_frame(row = 1, column = 0, padx = 5)


        #Separador 1:
        self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador1.grid(row = 2, column = 0, pady = 6, columnspan = 3, sticky = 'we')


        #Bloco do título ?:
        self.tit2 = Label(self.frameLocal, text = 'Título 2')
        self.tit2.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = W)

        #Bloco CBox1:
        self.CBox1 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox1.grid_frame(row = 4, column = 0, padx = 5, pady = 5)

        #Bloco entr3:
        self.entr3 = sub_Entry(self.frameLocal)
        self.entr3.grid_frame(row = 4, column = 1, padx = 5, pady = 5)


        #Bloco entr4:
        self.entr4 = sub_Entry(self.frameLocal)
        self.entr4.grid_frame(row = 4, column = 2, padx = 5, pady = 5)





        #Bloco botao1:
        self.botao1 = ttk.Button(self.frameLocal, text = "Botão 1" )
        self.botao1.grid(row = 5, column = 0, pady = 5, padx = 5, sticky = W+E)


        #Separador 2:
        self.separador2 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador2.grid(row = 6, column = 0, pady = 6, columnspan = 3, sticky = 'we')


        #Bloco botao2:
        self.botao2 = ttk.Button(self.frameLocal, text = "Botão 2" )
        self.botao2.grid(row = 7, column = 0, pady = 5, padx = 5, sticky = W+E)

        #Bloco botao3:
        self.botao3 = ttk.Button(self.frameLocal, text = "Botão 3" )
        self.botao3.grid(row = 7, column = 1, columnspan = 2, pady = 5, padx = 5, sticky = W+E)


        #Bloco do Text1:
        self.blocoText = sub_Text(self.frameLocal, width = 35, height = 4, tit = "Descrição:")
        self.blocoText.grid_frame(row = 0, column = 1, rowspan = 2, columnspan = 2, sticky = E+N+N, padx = 11, pady = 12)


        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 3, height = 11, rowspan = 13)
        self.treeView1.grid_frame(row = 0, column = 3, rowspan = 8, sticky = N+S, columnspan = 2, padx = 9)

        ####################################################################################################
        # TODO SETAR OS ATRIBUTOS ABAIXO EM CADA INSTANCIAÇÃO
        self.config_nome_tit1('Incluir nova gerência')
        self.config_tit_entr1('Nome da gerência:')
        self.config_tit_entr2('Nome do gestor:')
        self.config_tit_text1('Descrição da gerência')

        self.config_nome_tit2('Incluir contas:')
        self.config_tit_CBox1('Tipo de conta:')
        self.set_CBox1_default('Escolha a opção:')
        self.define_values_CBox1(['Conta corrente', 'Conta poupança', 'Cartão de crédito', 'Carteira', 'Caixa'])
        self.config_tit_entr3('Nome da conta:')
        self.config_tit_entr4('Saldo inicial: ')

        self.config_tit_col_treeView1(0, 'Nome da conta:')
        self.config_tit_col_treeView1('1', 'Tipo:')
        self.config_tit_col_treeView1('2', 'Saldo inicial: (R$)')

        self.config_text_B1('Enviar conta')
        self.config_text_B2('Voltar ao menu')
        self.config_text_B3('Salvar gerência')
        ####################################################################################################

    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView1(self, lst_itens):
        self.treeView1.insere_lst_elem_treeView(lst_itens)
        
    def clear_treeView1(self):
        self.treeView1.clear_treeView()
        
    def config_nome_tit1(self, titulo):
        self.frameLocal.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)


    def retorna_entr1(self):
        return(self.entr1.retorna_entr())
        
    def retorna_entr2(self):
        return(self.entr2.retorna_entr())

    def retorna_entr3(self):
        return(self.entr3.retorna_entr())

    def retorna_entr4(self):
        return(self.entr4.retorna_entr())

    def config_entr1_state(self, estado):
        self.entr1.config_Entry_state(estado)

    def config_entr2_state(self, estado):
        self.entr2.config_Entry_state(estado)
        
    def config_entr3_state(self, estado):
        self.entr3.config_Entry_state(estado)

    def config_entr4_state(self, estado):
        self.entr4.config_Entry_state(estado)

    def limpa_entr1(self):
        self.entr1.limpa_entr()

    def limpa_entr2(self):
        self.entr2.limpa_entr()

    def limpa_entr3(self):
        self.entr3.limpa_entr()

    def limpa_entr4(self):
        self.entr4.limpa_entr()

    def config_tit_entr1(self, titulo):
        self.entr1.config_tit_Entry(titulo)
        
    def config_tit_entr2(self, titulo):
        self.entr2.config_tit_Entry(titulo)

    def config_tit_entr3(self, titulo):
        self.entr3.config_tit_Entry(titulo)
        
    def config_tit_entr4(self, titulo):
        self.entr4.config_tit_Entry(titulo)

    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())
        
    def config_tit_CBox1(self, titulo):
        self.CBox1.config_tit_CBox(titulo)

    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)

    def config_tit_text1(self, titulo):
        self.blocoText.config_tit_text(titulo)
    
    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def config_comando_B2(self, comando):
        self.botao2.config(command = comando)

    def config_comando_B3(self, comando):
        self.botao3.config(command = comando)

    def config_text_B1(self, nome):
        self.botao1.config(text = nome)

    def config_text_B2(self, nome):
        self.botao2.config(text = nome)
    
    def config_text_B3(self, nome):
        self.botao3.config(text = nome)


    def insere_nova_CBox1(self, CBox):
        self.CBox1.insere_nova_CBox(CBox)


    def add_value_CBox1(self, lst):
        self.CBox1.add_value_CBox(lst)

    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)
    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
    
    
    def insert_text1(self, txtStr):
        self.blocoText.insert_text(txtStr)

    def clear_text1(self):
        self.blocoText.clear_text()

    def return_text1(self):
        text = self.blocoText.return_text()
        return (text)

    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_carrega_ger:

    def __init__(self, framePai):
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, text = "Titulo 1", relief=GROOVE, borderwidth=2, padx ="8", pady = "8")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)


        #Bloco do título 2:
        self.tit2 = Label(self.frameLocal, text = 'Título 2')
        self.tit2.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 2, height = 4)
        self.treeView1.grid_frame(row = 1, column = 0, sticky = N+S, padx = 9)

        #Bloco botao1:
        self.botao1 = ttk.Button(self.frameLocal, text = "Botão 1" )
        self.botao1.grid(row = 2, column = 0, pady = 5, padx = 5, sticky = W+E)

        #Bloco botao2:
        self.botao2 = ttk.Button(self.frameLocal, text = "Botão 2" )
        self.botao2.grid(row = 3, column = 0, pady = 5, padx = 5, sticky = W+E)

        #Bloco do Text1:
        self.blocoText = sub_Text(self.frameLocal, width = 35, height = 6, tit = "Descrição:")
        self.blocoText.grid_frame(row = 1, column = 1, columnspan = 2, sticky = E+N+N, padx = 11, pady = 12)


    def pointer_treeView1(self):
        return(self.treeView1)

    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView1(self, lst_itens):
        self.treeView1.insere_lst_elem_treeView(lst_itens)
    
    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())
        
    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))
    
    def clear_treeView1(self):
        self.treeView1.clear_treeView()
        
    def config_nome_tit1(self, titulo):
        self.frameLocal.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)

    def config_tit_text1(self, titulo):
        self.blocoText.config_tit_text(titulo)
    
    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)
        
    def config_comando_B2(self, comando):
        self.botao2.config(command = comando)

    def config_text_B1(self, nome):
        self.botao1.config(text = nome)
        
    def config_text_B2(self, nome):
        self.botao2.config(text = nome)

    def insert_text1(self, txtStr):
        self.blocoText.insert_text(txtStr)

    def clear_text1(self):
        self.blocoText.clear_text()

    def return_text1(self):
        text = self.blocoText.return_text()
        return (text)

    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_ref_cadastrados(Frame):
    def __init__(self, framePai, **kwargs):
        
       
        Frame.__init__(self, framePai)
        self.grid(row = 0, column = 0, sticky = W+E+S+N)   
        self.subFrame1 = Frame(self, padx = 5, pady = 5)
        self.subFrame1.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        self.tit1 = ttk.Label(self.subFrame1, text = 'Título 2')
        self.tit1.grid(row = 0, column = 0, padx = 5, sticky = W)
        
        self.treeView1 = sub_Treeview(self.subFrame1, num_cols = 3, height = 11, rowspan = 13)
        self.treeView1.grid_frame(row = 1, column = 0, sticky = N, columnspan = 2, padx = 9)

        #O frame subFrame2 conterá a a treeview2
        #Preciso ver se é necessário haver um subFrame1 -> FOI NECESSÁRIO
        self.subFrame2 = Frame(self, padx = 5, pady = 5)
        self.subFrame2.grid(row = 0, column = 2, sticky = W+E+S+N)
        
        self.separador1 = ttk.Separator(self.subFrame2, orient = VERTICAL)
        self.separador1.grid(row = 0, column = 0, rowspan = 40, pady = 10, padx = 10, sticky = "sn")
        
        self.entr1 = sub_Entry(self.subFrame2, width = 51, tit_Entry = 'entr8')
        self.entr1.grid_frame(row=0, column=1, sticky = W, padx = 5)


        self.treeView2 = sub_Treeview(self.subFrame2, num_cols = 4, height = 17)
        self.treeView2.grid_frame(row = 1, column = 1, sticky = W, padx = 5, pady = 5, columnspan = 4, num_cols = 4)
        
        #~ self.botao2 = ttk.Button(self.subFrame2, text = "Enviar")
        #~ self.botao2.grid(row = 20, column = 1, sticky = W, pady = 10)





    def insert_lst_treeView1(self, lst_treeView):
        self.treeView1.insert_lst_treeView(lst_treeView)

    def insert_lst_treeView2(self, lst_treeView):
        self.treeView2.insert_lst_treeView(lst_treeView)
    

    def pointer_treeView1(self):
        return(self.treeView1)
        
    def pointer_treeView2(self):
        return(self.treeView2)

    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)


    def config_treeView1(self, **kwargs):
        self.treeView1.config_treeView(**kwargs)
        
    def config_label_treeView1(self, **kwargs):
        self.treeView1.config_Label(**kwargs)
    
    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, value4)
    
    def insere_lst_elem_treeView1(self, lst_itens):
        self.treeView1.insere_lst_elem_treeView(lst_itens)


    def idd_selection_treeView1(self):
        return(self.treeView1.idd_selection_treeView())

    def idd_selection_treeView2(self):
        return(self.treeView2.idd_selection_treeView())
        
        
    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))
    
    def item_treeView2(self, idd):
        return(self.treeView2.item_treeView(idd))
        
    def clear_treeView1(self):
        self.treeView1.clear_treeView()
        
    def clear_treeView2(self):
        self.treeView2.clear_treeView()
        
    
    def grid_frame(self):
        self.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.grid_forget()
    
    def finaliza(self):
        self.destroy()


class c_frame_ref(Frame):
    def __init__(self, framePai, **kwargs):
        
        
        Frame.__init__(self, framePai)
        self.grid(row = 0, column = 0, sticky = W+E+S+N) 
        
        #Bloco (3): Aqui, é instanciado o tipo Notebook, que na verdade é um frame que conterá as abas:
        self.abasBarra = ttk.Notebook(self)
        self.abasBarra.grid(row = 0, column = 0, sticky = E+W)
        

        #Bloco (4): Abaixo, cada aba é instanciada, cujo frame pai é o "Abas":
        self.aba1 = ttk.Frame(self.abasBarra)   
        self.abasBarra.add(self.aba1, text = "Aba 1")


        self.aba2 = ttk.Frame(self.abasBarra)  
        self.abasBarra.add(self.aba2, text = "Aba 2")



    def pointer_frame_aba1(self):
        return(self.aba1)
        
    def pointer_frame_aba2(self):
        return(self.aba2)
        

    def config_nome_aba1(self, titulo):
        self.abasBarra.tab(self.aba1, text = titulo)
        
    def config_nome_aba2(self, titulo):
        self.abasBarra.tab(self.aba2, text = titulo)

    def grid_frame(self):
        self.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.grid_forget()
    
    def finaliza(self):
        self.destroy()


class c_frame_insere_item_serv:
    #APLICAR MUDANÇAS TAMBÉM À CLASSE:  frame_6T_1E_1Tex_3Cbox_1Tview
    
    
    def __init__(self, framePai, **kwargs):
        
        
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, text = "Titulo 1", relief=FLAT, borderwidth=2, padx ="10", pady = "10")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        
        #Bloco (2): Configurando o título d, que receberá variável "tit2":
        self.tit2 = Label(self.frameLocal, text= "Titulo 2", pady = 5)
        self.tit2.grid(row=0, column=0, columnspan = 3, sticky = W+N)

        self.CBox1 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox1.grid_frame(row = 1, column = 0, padx = 5)
        
        self.CBox2 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox2.grid_frame(row = 1, column = 1, padx = 5)
        
        self.CBox3 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox3.grid_frame(row = 1, column = 2, padx = 5)

        self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador1.grid(row = 3, column = 0, columnspan = 5, sticky = "we", pady = 10)

        self.caixa_entr1 = sub_Entry(self.frameLocal, width = 51)
        self.caixa_entr1.grid_frame( column = 0, row = 4, padx = 5, columnspan = 3, sticky = W+E)

        self.CBox4 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox4.grid_frame(row = 4, column = 2, padx = 5)


        
        #Bloco botao1:
        self.botao1 = ttk.Button(self.frameLocal, text = "Botão 1", padding = "30 5 30 5")
        self.botao1.grid(row = 5, column = 2, columnspan = 2)



        #self.blocoText = sub_Text(self.frameLocal, row = 4, column = 0, columnspan = 2, sticky = W+E, padx = 10, pady = 5)

        
        #Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frame_blocoText = Frame(self.frameLocal)
        self.frame_blocoText.grid(row = 5, column = 0, columnspan = 2, sticky = W+E, padx = 10, pady = 5)
        
        self.tit_text = ttk.Label(self.frame_blocoText, text = "Descrição:")
        self.tit_text.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self.blocoText = Text(self.frame_blocoText, insertborderwidth = 5, bd = 3, font = "Arial 9", wrap = WORD, width = 50, height = 4, state = NORMAL, autoseparators=True)
        self.blocoText.grid(row = 1, column = 0)
        

            #Bloco (3.2): Instanciando as Scrollbars(barras de rolagem):
        self.scrollbarY = Scrollbar(self.frame_blocoText, command=self.blocoText.yview)
        self.scrollbarY.grid(row = 1, column = 2,sticky=N+S)
        
        self.scrollbarX = Scrollbar(self.frame_blocoText, command=self.blocoText.xview, orient = HORIZONTAL)
        self.scrollbarX.grid(row= 2, column = 0, sticky = E+W)
            
            #Bloco (3.3): Declaradas as Scrollbars, o blocoText é configurado a recebê-las:
        self.blocoText.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
        
        
        self.separador2 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador2.grid(row = 6, column = 0, columnspan = 5, sticky = "we")
        
        #Bloco do frame da Treeview:
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 5, height = 5)
        self.treeView1.grid_frame(row = 7, column = 0, columnspan = 8)


        #Bloco do botão2:
        self.botao2 = ttk.Button(self.frameLocal, text = "Botão 2")
        self.botao2.grid(row = 8, column = 0, padx = 8, pady = 6, sticky = W+E)
        
        #BLoco do botão3:
        self.botao3 = ttk.Button(self.frameLocal, text = "Botão 3")
        self.botao3.grid(row = 8, column = 1, padx = 8, pady = 6, sticky = W+E)
        ################################
        #TODO CONFIGURAR OS PARAMETROS EM CADA INSTANCIAÇÃO

        # Abaixo, são configuradas as instâncias da interface:
        self.config_nome_tit1("Cadastro de itens/serviços")
        self.config_nome_tit2("Especifique os dados:")

        # Configurações iniciais da combobox1:
        self.config_tit_CBox1("Tipo:")
        self.set_CBox1_default("Escolha a opção:")
        self.define_values_CBox1(["Item", "Serviço"])

        # Configurações iniciais da combobox2:
        self.config_tit_CBox2("Categoria:")
        self.config_CBox2_state('disabled')

        # Configurações iniciais da combobox3:
        self.config_tit_CBox3("Subcategoria:")
        self.config_CBox3_state('disabled')

        # Configurações iniciais da combobox4:
        self.config_tit_CBox4("Espécie:")
        self.config_CBox4_state('disabled')

        # Configurando o título da entrada do nome:
        self.config_tit_entr1("Nome:")

        self.config_tit_treeView1("Itens a cadastrar:")
        self.config_tit_col_treeView1(0, "Nome:")
        self.config_tit_col_treeView1(1, "Tipo:")
        self.config_tit_col_treeView1(2, "Categoria:")
        self.config_tit_col_treeView1(3, "Subcategoria:")
        self.config_tit_col_treeView1(4, "Marca")

        self.config_tit_B1("Enviar para a lista:")
        self.config_tit_B2("Cancelar cadastro")
        self.config_tit_B3("Salvar cadastro")
        ##############

    def pointer_treeView1(self):
        return(self.treeView1.pointer_treeView())
        
    def config_nome_tit1(self, titulo):
        self.frameLocal.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)
        
    def config_tit_B1(self, titulo):
        self.botao1.config(text = titulo)
        
    def config_tit_B2(self, titulo):
        self.botao2.config(text = titulo)
    
    def config_tit_B3(self, titulo):
        self.botao3.config(text = titulo)


    def config_B1(self, **kwargs):
        self.botao1.config(kwargs)
        
    def config_B2(self, **kwargs):
        self.botao2.config(kwargs)
        
    def config_B3(self, **kwargs):
        self.botao3.config(kwargs)


    def retorna_text1(self):
        text1 = self.blocoText.get(1.0, "end")
        print(text1)
        return (text1)
    
    def retorna_entr1(self):
        return(self.caixa_entr1.retorna_entr())
    
    
    def config_tit_entr1(self, tit):
        self.caixa_entr1.config_tit_Entry(tit)

    
    def config_tit_entr2(self, titulo):
        self.tit_entr2.config(text = titulo)
        
    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)
        
        
    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)



    def insere_lst_elem_treeView1(self, lst_itens, **kwargs):
        self.treeView1.insere_lst_elem_treeView(lst_itens, **kwargs)

    def clear_treeView1(self):
        self.treeView1.clear_treeView()

    def selection_treeView1(self):
        return(self.treeView1.selection_treeView())



    def config_tit_text(self, titulo):
        self.tit_text.config(text = titulo)
    
    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def config_comando_B2(self, comando):
        self.botao2.config(command = comando)
        
    def config_comando_B3(self, comando):
        self.botao3.config(command = comando)



    def config_tit_CBox1(self, tit):
        self.CBox1.config_tit_CBox(tit)

    def config_tit_CBox2(self, tit):
        self.CBox2.config_tit_CBox(tit)

    def config_tit_CBox3(self, tit):
        self.CBox3.config_tit_CBox(tit)
        
    def config_tit_CBox4(self, tit):
        self.CBox4.config_tit_CBox(tit)

    def insere_nova_CBox1(self, CBox):
        self.CBox1.insere_nova_CBox(CBox)

    def insere_nova_CBox2(self, CBox):
        self.CBox2.insere_nova_CBox(CBox)

    def insere_nova_CBox3(self, CBox):
        self.CBox3.insere_nova_CBox(CBox)
        
    def insere_nova_CBox4(self, CBox):
        self.CBox4.insere_nova_CBox(CBox)


    
    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)

    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)

    def define_values_CBox3(self, lst):
        self.CBox3.define_values_CBox(lst)
    
    def define_values_CBox4(self, lst):
        self.CBox4.define_values_CBox(lst)

    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
    
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())
    
    def retorna_escolha_CBox3(self):
        return(self.CBox3.retorna_escolha_CBox())
        
    def retorna_escolha_CBox4(self):
        return(self.CBox4.retorna_escolha_CBox())

    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())
        
    def pointer_CBox2(self):
        return(self.CBox2.pointer_CBox())
        
    def pointer_CBox3(self):
        return(self.CBox3.pointer_CBox())
        
    def pointer_CBox4(self):
        return(self.CBox4.pointer_CBox())


    '''
    DEPRECIADA:
    def CBox1_bind(self, comando):
        self.CBox1.bind("<<ComboboxSelected>>", comando)
    '''
    
    '''
    DEPRECIADA:
    def CBox2_bind(self, bind_tuple):
        self.CBox2.bind(bind_tuple)
    '''
    
    '''
    DEPRECIADA:
    def CBox3_bind(self, comando):
        self.CBox3.bind('<<ComboboxSelected>>', comando)
    '''
    
    def config_CBox1_state(self, estado):
        self.CBox1.config_CBox_state(estado)
    
    def config_CBox2_state(self, estado):
        self.CBox2.config_CBox_state(estado)

    def config_CBox3_state(self, estado):
        self.CBox3.config_CBox_state(estado)

    def config_CBox4_state(self, estado):
        self.CBox4.config_CBox_state(estado)
        
    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set_CBox_default(tit)
        
    def set_CBox3_default(self, tit):
        self.CBox3.set_CBox_default(tit)
        
    def set_CBox4_default(self, tit):
        self.CBox4.set_CBox_default(tit)



    def insereTexto(self, txtStr):
        self.blocoText.config(state=NORMAL)
        self.blocoText.insert(1.0, txtStr)
        #~ self.blocoText.config(state=DISABLED)

    def limpa_CaixaTexto(self):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete('1.0', END)
        #~ self.blocoText.config(state=DISABLED)
        
    def limpa_entr1(self):
        self.caixa_entr1.limpa_entr()
        
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E, padx = 10, pady = 20)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_insere_cliente:

    def __init__(self, framePai, **kwargs):
        
        
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, text = "Titulo 1", relief=FLAT, borderwidth=2, padx ="10", pady = "10")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        
        #Bloco (2): Configurando o título d, que receberá variável "tit2":
        self.tit2 = Label(self.frameLocal, text= "Titulo 2", pady = 5)
        self.tit2.grid(row=0, column=0, columnspan = 3, sticky = W+N)
        
        
        
        self.entr1 = sub_Entry(self.frameLocal, width = 47, tit_Entry = 'entr1')
        self.entr1.grid_frame(row = 1, column = 0, padx = 5, columnspan = 3, sticky = W+E)

        self.CBox1 = sub_CBox(self.frameLocal, set_CBox_default = '', width = 21)
        self.CBox1.grid_frame(row = 1, column = 3, padx = 5)
        
        
        self.CBox2 = sub_CBox(self.frameLocal, set_CBox_default = '', width = 21)
        self.CBox2.grid_frame(row = 2, column = 0, padx = 5)

        
        self.CBox3 = sub_CBox(self.frameLocal, set_CBox_default = '', width = 21)
        self.CBox3.grid_frame(row = 2, column = 1, padx = 5)


        self.CBox4 = sub_CBox(self.frameLocal, set_CBox_default = '', width = 21)
        self.CBox4.grid_frame(row = 3, column = 0, padx = 5)
        
        self.entr2 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr2')
        self.entr2.grid_frame(row = 2, column = 2, padx = 5, sticky = W+E)
        
        self.entr3 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr3')
        self.entr3.grid_frame(row = 2, column = 3, padx = 5, sticky = W+E)
        
        self.entr4 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr4')
        self.entr4.grid_frame(row = 3, column = 2, padx = 5, sticky = W+E)
        
        self.entr5 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr5')
        self.entr5.grid_frame(row = 1, column = 2, padx = 5, sticky = W+E)
        
        self.entr6 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr6')
        self.entr6.grid_frame(row = 3, column = 3, padx = 5, sticky = W+E)
        
        
        self.entr7 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr7')
        self.entr7.grid_frame(row = 3, column = 1, padx = 5, sticky = W+E)
        
        
        self.CBox5 = sub_CBox(self.frameLocal, set_CBox_default = '', width = 21)
        self.CBox5.grid_frame(row = 4, column = 0, padx = 5)
        
        self.entr8 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr8')
        self.entr8.grid_frame(row = 4, column = 1, padx = 5, sticky = W+E)
        
        self.entr9 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr9')
        self.entr9.grid_frame(row = 5, column = 0, padx = 5, sticky = W+E)
        
        
        self.entr10 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr10')
        self.entr10.grid_frame(row = 5, column = 1, padx = 5, sticky = W+E)
        
        self.entr11 = sub_Entry(self.frameLocal, width = 24, tit_Entry = 'entr11')
        self.entr11.grid_frame(row = 4, column = 2, padx = 5, sticky = W+E)

        self.frame_3CBox = sub_LFrame_3CBox(self.frameLocal)
        self.frame_3CBox.grid_frame(row = 5, column = 3, columnspan = 3, sticky = W+E)
        
        #Bloco botao1:
        self.botao1 = ttk.Button(self.frameLocal, text = "Botão 1", padding = '20 5 20 5')
        self.botao1.grid(row = 5, column = 2, sticky = W)


        #Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frame_blocoText = Frame(self.frameLocal)

        
        self.tit_text = ttk.Label(self.frame_blocoText, text = "Descrição:")
        self.tit_text.grid(row = 0, column = 0, columnspan = 2, sticky = W+S)
        
        

        self.blocoText = Text(self.frame_blocoText, insertborderwidth = 5, bd = 3, font = "Arial 9", wrap = WORD, width = 50, height = 4, state = NORMAL, autoseparators=True)
        #~ self.blocoText.grid(row = 1, column = 0)


        #Bloco do frame da Treeview:
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 7)
        self.treeView1.grid_frame(row = 6, column = 0, sticky = W, columnspan = 7, padx = 5, pady = 5)
        

        
        #Bloco do botão2:
        self.botao2 = ttk.Button(self.frameLocal, text = "Botão 2")
        self.botao2.grid(row = 7, column = 0, padx = 8, pady = 6, sticky = W+E)
        
        #BLoco do botão3:
        self.botao3 = ttk.Button(self.frameLocal, text = "Botão 3")
        self.botao3.grid(row = 7, column = 1, padx = 8, pady = 6, sticky = W+E)

        self.botao4 = ttk.Button(self.frameLocal, text = "Botão 4", padding = '20 5 20 5')
        self.botao4.grid(row = 4, column = 3, columnspan = 3, padx = 8, pady = 6, sticky = W + S)
        self.config_nome_tit1("Cadastro de Clientes")
        self.config_nome_tit2("Especifique os dados:")

        # Configurações iniciais da combobox1:
        self.config_tit_CBox1("Genero:")
        self.set_CBox1_default("Não especificado")
        self.define_values_CBox1(["Feminino", "Masculino"])
        self.config_CBox1_state('readonly')

        # Configurações iniciais da combobox2:
        self.config_tit_CBox2("Estado:")
        self.set_CBox2_default("Escolha a opção")
        self.config_CBox2_state('readonly')

        # Configurações iniciais da combobox3:
        self.config_tit_CBox3("Cidade:")
        self.set_CBox3_default("Escolha a opção")
        self.config_CBox3_state('readonly')

        # Configurações iniciais da combobox4:
        self.config_tit_CBox4("Bairro:")
        self.set_CBox4_default("Escolha a opção")
        self.config_CBox4_state('readonly')

        # Configurações iniciais da combobox5:
        self.config_tit_CBox5("Tipo:")
        self.set_CBox5_default("Escolha a opção")
        self.config_CBox5_state('readonly')

        # Configurando o título da entrada do nome:
        self.config_tit_entr1("Nome/Nome fantasia:")
        self.config_tit_entr2("Telefone principal:")
        self.config_tit_entr3("Telefone alternativo:")
        self.config_tit_entr4("E-mail:")
        self.config_tit_entr5("CNPJ/CPF:")
        self.config_tit_entr6("E-mail alternativo:")
        self.config_tit_entr7("Logradouro:")
        self.config_tit_entr8("Número:")
        self.config_tit_entr9("Nome do edifício/condomínio:")
        self.config_tit_entr10("Número do apartamento:")
        self.config_tit_entr11("CEP:")

        self.config_label_frame_3CBox('Data de nascimento')

        self.config_tit_treeView1("Clientes a cadastrar:")
        self.config_tit_col_treeView1(0, "Nome:")
        self.config_tit_col_treeView1(1, "Telefone:")
        self.config_tit_col_treeView1(2, "E-mail")
        self.config_tit_col_treeView1(3, "Endereço")
        self.config_tit_col_treeView1(4, "Cidade:")
        self.config_tit_col_treeView1(5, "Estado:")
        self.config_tit_col_treeView1(6, "CEP:")

        self.config_tit_B1("Enviar para a lista:")
        self.config_tit_B2("Cancelar cadastro")
        self.config_tit_B3("Salvar cadastro")
        self.config_tit_B4("Pesquisar CEP")
        
    def config_B1(self, **kwargs):
        self.botao1.config(kwargs)
        
    def config_B2(self, **kwargs):
        self.botao2.config(kwargs)
        
    def config_B3(self, **kwargs):
        self.botao3.config(kwargs)
    
    def config_label_frame_3CBox(self, text):
        self.frame_3CBox.config_tit_frame(text)

    def config_nome_tit1(self, titulo):
        self.frameLocal.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)
        
    def config_tit_B1(self, titulo):
        self.botao1.config(text = titulo)
        
    def config_tit_B2(self, titulo):
        self.botao2.config(text = titulo)
    
    def config_tit_B3(self, titulo):
        self.botao3.config(text = titulo)
        
    def config_tit_B4(self, titulo):
        self.botao4.config(text = titulo)
    
    
    def retorna_text1(self):
        text1 = self.blocoText.get(1.0, "end")
        print(text1)
        return (text1)

    def messagebox_info(self, tit, msg):
        messagebox.showinfo(tit, msg)



    def insert_CBoxN(self, n, tit):
        if n == 1:
            self.CBox1.set_CBox1_default(tit)
            
        elif n == 2:
            self.CBox2.set_CBox2_default(tit)
        
        elif n == 3:
            self.CBox3.set_CBox3_default(tit)
            
        elif n == 4:
            self.CBox4.set_CBox_default(tit)
        
        elif n == 5:
            self.CBox5.set_CBox5_default(tit)
        
        elif n == 6:
            self.CBox6.set_CBox6_default(tit)
        
        elif n == 7:
            self.CBox7.set_CBox7_default(tit)
            


    def insert_entrN(self, n, tit):
        if n == 1:
            self.entr1.insert_Entry(tit)
            
        elif n == 2:
            self.entr2.insert_Entry(tit)
        
        elif n == 3:
            self.entr3.insert_Entry(tit)
            
        elif n == 4:
            self.entr4.insert_Entry(tit)
        
        elif n == 5:
            self.entr5.insert_Entry(tit)
        
        elif n == 6:
            self.entr6.insert_Entry(tit)
        
        elif n == 7:
            self.entr7.insert_Entry(tit)

        elif n == 8:
            self.entr8.insert_Entry(tit)

        elif n == 9:
            self.entr9.insert_Entry(tit)

        elif n == 10:
            self.entr10.insert_Entry(tit)

        elif n == 11:
            self.entr11.insert_Entry(tit)
            


    def retorna_entr1(self):
        return(self.entr1.retorna_entr())

    def retorna_entr2(self):
        return(self.entr2.retorna_entr())
        
    def retorna_entr3(self):
        return(self.entr3.retorna_entr())

    def retorna_entr4(self):
        return(self.entr4.retorna_entr())
        
    def retorna_entr5(self):
        return(self.entr5.retorna_entr())
        
    def retorna_entr6(self):
        return(self.entr6.retorna_entr())
        
    def retorna_entr7(self):
        return(self.entr7.retorna_entr())
    
    def retorna_entr8(self):
        return(self.entr8.retorna_entr())

    def retorna_entr9(self):
        return(self.entr9.retorna_entr())

    def retorna_entr10(self):
        return(self.entr10.retorna_entr())
    
    def retorna_entr11(self):
        return(self.entr11.retorna_entr())

    def config_tit_entrN(self, n, tit):
        if n == 1:
            self.entr1.config_tit_Entry(tit)
            
        elif n == 2:
            self.entr2.config_tit_Entry(tit)
        
        elif n == 3:
            self.entr3.config_tit_Entry(tit)
            
        elif n == 4:
            self.entr4.config_tit_Entry(tit)
        
        elif n == 5:
            self.entr5.config_tit_Entry(tit)
        
        elif n == 6:
            self.entr6.config_tit_Entry(tit)
        
        elif n == 7:
            self.entr7.config_tit_Entry(tit)

        elif n == 8:
            self.entr8.config_tit_Entry(tit)

        elif n == 9:
            self.entr9.config_tit_Entry(tit)

        elif n == 10:
            self.entr10.config_tit_Entry(tit)

        elif n == 11:
            self.entr11.config_tit_Entry(tit)
        '''
        elif n == 12:
            self.entr12.config_tit_Entry(tit)
        
        elif n == 13:
            self.entr13.config_tit_Entry(tit)
        
        elif n == 14:
            self.entr14.config_tit_Entry(tit)
        
        elif n == 15:
            self.entr15.config_tit_Entry(tit)
        
        elif n == 16:
            self.entr16.config_tit_Entry(tit)
        
        elif n == 17:
            self.entr17.config_tit_Entry(tit)
        '''

    def limpa_todas_entr(self):
        self.limpa_entr1()
        self.limpa_entr2()
        self.limpa_entr3()
        self.limpa_entr4()
        self.limpa_entr5()
        self.limpa_entr6()
        self.limpa_entr7()
        self.limpa_entr8()
        self.limpa_entr9()
        self.limpa_entr10()
        self.limpa_entr11()
        
    def limpa_entr1(self):
        self.entr1.limpa_entr()
        
    def limpa_entr2(self):
        self.entr2.limpa_entr()

    def limpa_entr3(self):
        self.entr3.limpa_entr()
        
    def limpa_entr4(self):
        self.entr4.limpa_entr()
        
    def limpa_entr5(self):
        self.entr5.limpa_entr()

    def limpa_entr6(self):
        self.entr6.limpa_entr()
        
    def limpa_entr7(self):
        self.entr7.limpa_entr()

    def limpa_entr8(self):
        self.entr8.limpa_entr()
    
    def limpa_entr9(self):
        self.entr9.limpa_entr()
    
    def limpa_entr10(self):
        self.entr10.limpa_entr()
        
    def limpa_entr11(self):
        self.entr11.limpa_entr()

    def config_tit_entr1(self, tit):
        self.entr1.config_tit_Entry(tit)

    def config_tit_entr2(self, tit):
        self.entr2.config_tit_Entry(tit)

    def config_tit_entr3(self, tit):
        self.entr3.config_tit_Entry(tit)

    def config_tit_entr4(self, tit):
        self.entr4.config_tit_Entry(tit)

    def config_tit_entr5(self, tit):
        self.entr5.config_tit_Entry(tit)
        
    def config_tit_entr6(self, tit):
        self.entr6.config_tit_Entry(tit)
        
    def config_tit_entr7(self, tit):
        self.entr7.config_tit_Entry(tit)

    def config_tit_entr8(self, tit):
        self.entr8.config_tit_Entry(tit)

    def config_tit_entr9(self, tit):
        self.entr9.config_tit_Entry(tit)

    def config_tit_entr10(self, tit):
        self.entr10.config_tit_Entry(tit)
        
    def config_tit_entr11(self, tit):
        self.entr11.config_tit_Entry(tit)

    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)

    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)
    
    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = '', **kwargs):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, value4, **kwargs)

    def insere_lst_elem_treeView1(self, lst_itens, **kwargs):
        self.treeView1.insere_lst_elem_treeView(lst_itens, **kwargs)

    def clear_treeView1(self):
        self.treeView1.clear_treeView()


    def config_tit_text(self, titulo):
        self.tit_text.config(text = titulo)
    
    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def config_comando_B2(self, comando):
        self.botao2.config(command = comando)
        
    def config_comando_B3(self, comando):
        self.botao3.config(command = comando)

    def config_comando_B4(self, comando):
        self.botao4.config(command = comando)

    def item_treeView1(self, idd):
        return(self.treeView1.item_treeView(idd))


    def config_tit_CBox1(self, tit):
        self.CBox1.config_tit_CBox(tit)

    def config_tit_CBox2(self, tit):
        self.CBox2.config_tit_CBox(tit)

    def config_tit_CBox3(self, tit):
        self.CBox3.config_tit_CBox(tit)

    def config_tit_CBox4(self, tit):
        self.CBox4.config_tit_CBox(tit)
        
    def config_tit_CBox5(self, tit):
        self.CBox5.config_tit_CBox(tit)


    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)
        

    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)
        
    def define_values_CBox3(self, lst):
        self.CBox3.define_values_CBox(lst)

    def define_values_CBox4(self, lst):
        self.CBox4.define_values_CBox(lst)

    def define_values_CBox5(self, lst):
        self.CBox5.define_values_CBox(lst)

    def define_values_CBox6(self, lst):
        self.sub_LFrame_3CBox.define_values_CBox1(lst)

    def define_values_CBox7(self, lst):
        self.sub_LFrame_3CBox.define_values_CBox2(lst)

    def define_values_CBox8(self, lst):
        self.sub_LFrame_3CBox.define_values_CBox3(lst)

    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
    
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())

    def retorna_escolha_CBox3(self):
        return(self.CBox3.retorna_escolha_CBox())
    
    def retorna_escolha_CBox4(self):
        return(self.CBox4.retorna_escolha_CBox())
    
    def retorna_escolha_CBox5(self):
        return(self.CBox5.retorna_escolha_CBox())
    
    def retorna_escolha_CBox6(self):
        return(self.sub_LFrame_3CBox.retorna_escolha_CBox1())

    def retorna_escolha_CBox7(self):
        return(self.sub_LFrame_3CBox.retorna_escolha_CBox2())

    def retorna_escolha_CBox8(self):
        return(self.sub_LFrame_3CBox.retorna_escolha_CBox3())



    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())
        
    def pointer_CBox2(self):
        return(self.CBox2.pointer_CBox())

    def pointer_CBox3(self):
        return(self.CBox3.pointer_CBox())

    def pointer_CBox4(self):
        return(self.CBox4.pointer_CBox())

    def pointer_CBox5(self):
        return(self.CBox5.pointer_CBox())

    def pointer_CBox6(self):
        return(self.sub_LFrame_3CBox.pointer_CBox1())

    def pointer_CBox7(self):
        return(self.sub_LFrame_3CBox.pointer_CBox2())
        
    def pointer_CBox8(self):
        return(self.sub_LFrame_3CBox.pointer_CBox3())
        
    
    def pointer_treeView1(self):
        return(self.treeView1.pointer_treeView())

    '''
    DEPRECIADA:
    def CBox1_bind(self, comando):
        self.CBox1.bind("<<ComboboxSelected>>", comando)
    '''
    
    '''
    DEPRECIADA:
    def CBox2_bind(self, bind_tuple):
        self.CBox2.bind(bind_tuple)
    '''
    
    '''
    DEPRECIADA:
    def CBox3_bind(self, comando):
        self.CBox3.bind('<<ComboboxSelected>>', comando)
    '''
    
    def config_CBox1_state(self, estado):
        self.CBox1.config_CBox_state(estado)
    
    def config_CBox2_state(self, estado):
        self.CBox2.config_CBox_state(estado)

    def config_CBox3_state(self, estado):
        self.CBox3.config_CBox_state(estado)
        
    def config_CBox4_state(self, estado):
        self.CBox4.config_CBox_state(estado)

    def config_CBox5_state(self, estado):
        self.CBox5.config_CBox_state(estado)

    def config_CBox6_state(self, estado):
        self.sub_LFrame_3CBox.config_CBox1_state(estado)

    def config_CBox7_state(self, estado):
        self.sub_LFrame_3CBox.config_CBox2_state(estado)
    
    def config_CBox8_state(self, estado):
        self.sub_LFrame_3CBox.config_CBox3_state(estado)


    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set_CBox_default(tit)
        
    def set_CBox3_default(self, tit):
        self.CBox3.set_CBox_default(tit)

    def set_CBox4_default(self, tit):
        self.CBox4.set_CBox_default(tit)
        
    def set_CBox5_default(self, tit):
        self.CBox5.set_CBox_default(tit)
        
    def set_CBox6_default(self, tit):
        self.CBox6.set_CBox1_default(tit)
        
    def set_CBox7_default(self, tit):
        self.CBox7.set_CBox2_default(tit)
    
    def set_CBox8_default(self, tit):
        self.CBox8.set_CBox3_default(tit)

    def insereTexto(self, txtStr):
        self.blocoText.config(state=NORMAL)
        self.blocoText.insert(1.0, txtStr)
        #~ self.blocoText.config(state=DISABLED)

    def limpa_CaixaTexto(self):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete('1.0', END)
        #~ self.blocoText.config(state=DISABLED)


    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E, padx = 10, pady = 20)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()

class c_frame_insere_fornec:
    
    def __init__(self, framePai):
        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(framePai, text = "Titulo 1", relief=FLAT, borderwidth=2, padx ="10", pady = "10")
        #self.frameLocal.grid(row = 0, column = 0, sticky = W+E+S+N)

        #Bloco (2): Configurando o título d, que receberá variável "tit2":
        self.tit2 = Label(self.frameLocal, text= "Titulo 2", pady = 5)
        self.tit2.grid(row=0, column=0, columnspan = 3, sticky = W+N)

        self.entr1 = sub_Entry(self.frameLocal, width = 51)
        self.entr1.grid_frame(column = 0, row = 2, padx = 5, columnspan = 3, sticky = W+E)

        self.CBox1 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox1.grid_frame(row = 1, column = 0, padx = 5)
        
        self.CBox2 = sub_CBox(self.frameLocal, set_CBox_default = '')
        self.CBox2.grid_frame(row = 1, column = 1, padx = 5)
        
        self.entr2 = sub_Entry(self.frameLocal)
        self.entr2.grid_frame(row = 1, column = 2, padx = 5, sticky = W+E)
        
        self.entr3 = sub_Entry(self.frameLocal)
        self.entr3.grid_frame(row = 1, column = 3, padx = 5, sticky = W+E)
        
        self.entr4 = sub_Entry(self.frameLocal)
        self.entr4.grid_frame(row = 2, column = 2, padx = 5, sticky = W+E)
        
        self.entr5 = sub_Entry(self.frameLocal)
        self.entr5.grid_frame(row = 2, column = 3, padx = 5, sticky = W+E)
        
        self.entr6 = sub_Entry(self.frameLocal)
        self.entr6.grid_frame(row = 3, column = 3, padx = 5, sticky = W+E)
        
        self.entr7 = sub_Entry(self.frameLocal)
        self.entr7.grid_frame(row = 3, column = 2, padx = 5, sticky = W+E)
        
        #Bloco botao1:
        self.botao1 = ttk.Button(self.frameLocal, text = "Botão 1", padding = '30 5 30 5')
        self.botao1.grid(row = 4, column = 2, sticky = W+E)

        #Bloco (3.1): Instanciando o frame_blocoText, cujo frame-pai é o frameLocal, que conterá o bloco Text(necessário por causa das scrollbars)
        self.frame_blocoText = Frame(self.frameLocal)
        self.frame_blocoText.grid(row = 3, column = 0, rowspan = 2, columnspan = 2, sticky = W+E, padx = 10, pady = 5)
        
        self.tit_text = ttk.Label(self.frame_blocoText, text = "Descrição:")
        self.tit_text.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self.blocoText = Text(self.frame_blocoText, insertborderwidth = 5, bd = 3, font = "Arial 9", wrap = WORD, width = 50, height = 4, state = NORMAL, autoseparators=True)
        self.blocoText.grid(row = 1, column = 0)
        
        #~ self.blocoText.insert(1.0, txtStr)

            #Bloco (3.2): Instanciando as Scrollbars(barras de rolagem):
        self.scrollbarY = Scrollbar(self.frame_blocoText, command=self.blocoText.yview)
        self.scrollbarY.grid(row = 1, column = 2,sticky=N+S)
        
        self.scrollbarX = Scrollbar(self.frame_blocoText, command=self.blocoText.xview, orient = HORIZONTAL)
        self.scrollbarX.grid(row= 2, column = 0, sticky = E+W)
            
            #Bloco (3.3): Declaradas as Scrollbars, o blocoText é configurado a recebê-las:
        self.blocoText.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)

        self.separador1 = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separador1.grid(row = 5, column = 0, columnspan = 5, sticky = "we")

        #Bloco do frame da Treeview:
        self.treeView1 = sub_Treeview(self.frameLocal, num_cols = 5)
        self.treeView1.grid_frame(row = 6, column = 0, sticky = W, columnspan = 4, padx = 5, pady = 5)
        
        #Bloco do botão2:
        self.botao2 = ttk.Button(self.frameLocal, text = "Botão 2")
        self.botao2.grid(row = 7, column = 0, padx = 8, pady = 6, sticky = W+E)
        
        #BLoco do botão3:
        self.botao3 = ttk.Button(self.frameLocal, text = "Botão 3")
        self.botao3.grid(row = 7, column = 1, padx = 8, pady = 6, sticky = W+E)

        #########################################################################
        ## LEMBRAR DE AJUSTAR OS ATRIBUTOS ABAIXO JUNTO ÀS INSTANCIAÇÕES
        self.config_nome_tit1("Cadastro de fornecedores")
        self.config_nome_tit2("Especifique os dados:")

        # Configurações iniciais da combobox1:
        self.config_tit_CBox1("Tipo:")
        self.set_CBox1_default("Escolha a opção:")
        self.define_values_CBox1(["Estabelecimento", "Pessoa"])
        self.config_CBox1_state('readonly')

        # Configurações iniciais da combobox2:
        # Falta fazer
        # Configurações iniciais da combobox3:
        # Falta fazer
        # Configurações iniciais da combobox4:
        # Falta fazer

        # Configurando o título da entrada do nome:
        self.config_tit_entr1("Nome/Nome fantasia:")
        self.config_tit_entr2("Telefone principal:")
        self.config_tit_entr3("Telefone alternativo:")
        self.config_tit_entr4("e-mail:")
        self.config_tit_entr5("CNPJ/CPF\n(Sómente números):")
        self.config_tit_entr6("Estado:")
        self.config_tit_entr7("Cidade:")

        self.config_tit_treeView1("Fornecedores a cadastrar:")
        self.config_tit_col_treeView1(0, "Nome:")
        self.config_tit_col_treeView1(1, "Categoria:")
        self.config_tit_col_treeView1(2, "Telefone:")
        self.config_tit_col_treeView1(3, "Email:")
        self.config_tit_col_treeView1(4, "Cidade:")

        self.config_tit_B1("Enviar para a lista:")
        self.config_tit_B2("Cancelar cadastro")
        self.config_tit_B3("Salvar cadastro")
        ##########

    def config_B1(self, **kwargs):
        self.botao1.config(kwargs)
        
    def config_B2(self, **kwargs):
        self.botao2.config(kwargs)
        
    def config_B3(self, **kwargs):
        self.botao3.config(kwargs)
    
    def config_nome_tit1(self, titulo):
        self.frameLocal.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)
        
    def config_tit_B1(self, titulo):
        self.botao1.config(text = titulo)
        
    def config_tit_B2(self, titulo):
        self.botao2.config(text = titulo)
    
    def config_tit_B3(self, titulo):
        self.botao3.config(text = titulo)
    
    def retorna_text1(self):
        text1 = self.blocoText.get(1.0, "end")
        print(text1)
        return (text1)
    
    def retorna_entr1(self):
        return(self.entr1.retorna_entr())

    def messagebox_info(self, tit, msg):
        messagebox.showinfo(tit, msg)

    def retorna_entr2(self):
        return(self.entr2.retorna_entr())
        
    def retorna_entr3(self):
        return(self.entr3.retorna_entr())

    def retorna_entr4(self):
        return(self.entr4.retorna_entr())
        
    def retorna_entr5(self):
        return(self.entr5.retorna_entr())
        
    def retorna_entr6(self):
        return(self.entr6.retorna_entr())
        
    def retorna_entr7(self):
        return(self.entr7.retorna_entr())

    def limpa_entr1(self):
        self.entr1.limpa_entr()
        
    def limpa_entr2(self):
        self.entr2.limpa_entr()

    def limpa_entr3(self):
        self.entr3.limpa_entr()
        
    def limpa_entr4(self):
        self.entr4.limpa_entr()
        
    def limpa_entr5(self):
        self.entr5.limpa_entr()

    def limpa_entr6(self):
        self.entr6.limpa_entr()
        
    def limpa_entr7(self):
        self.entr7.limpa_entr()


    def insert_entrN(self, n, tit):
        if n == 1:
            self.entr1.insert_Entry(tit)
            
        elif n == 2:
            self.entr2.insert_Entry(tit)
        
        elif n == 3:
            self.entr3.insert_Entry(tit)
            
        elif n == 4:
            self.entr4.insert_Entry(tit)
        
        elif n == 5:
            self.entr5.insert_Entry(tit)
        
        elif n == 6:
            self.entr6.insert_Entry(tit)
        
        elif n == 7:
            self.entr7.insert_Entry(tit)

        elif n == 8:
            self.entr8.insert_Entry(tit)

        elif n == 9:
            self.entr9.insert_Entry(tit)

        elif n == 10:
            self.entr10.insert_Entry(tit)

        elif n == 11:
            self.entr11.insert_Entry(tit)
            
        elif n == 12:
            self.entr12.insert_Entry(tit)
        
        elif n == 13:
            self.entr13.insert_Entry(tit)
        
        elif n == 14:
            self.entr14.insert_Entry(tit)
        
        elif n == 15:
            self.entr15.insert_Entry(tit)
        
        elif n == 16:
            self.entr16.insert_Entry(tit)
        
        elif n == 17:
            self.entr17.insert_Entry(tit)
            


    def config_tit_entrN(self, n, tit):
        if n == 1:
            self.entr1.config_tit_Entry(tit)
            
        elif n == 2:
            self.entr2.config_tit_Entry(tit)
        
        elif n == 3:
            self.entr3.config_tit_Entry(tit)
            
        elif n == 4:
            self.entr4.config_tit_Entry(tit)
        
        elif n == 5:
            self.entr5.config_tit_Entry(tit)
        
        elif n == 6:
            self.entr6.config_tit_Entry(tit)
        
        elif n == 7:
            self.entr7.config_tit_Entry(tit)

        elif n == 8:
            self.entr8.config_tit_Entry(tit)

        elif n == 9:
            self.entr9.config_tit_Entry(tit)

        elif n == 10:
            self.entr10.config_tit_Entry(tit)

        elif n == 11:
            self.entr11.config_tit_Entry(tit)
        
        elif n == 12:
            self.entr12.config_tit_Entry(tit)
        
        elif n == 13:
            self.entr13.config_tit_Entry(tit)
        
        elif n == 14:
            self.entr14.config_tit_Entry(tit)
        
        elif n == 15:
            self.entr15.config_tit_Entry(tit)
        
        elif n == 16:
            self.entr16.config_tit_Entry(tit)
        
        elif n == 17:
            self.entr17.config_tit_Entry(tit)
            



    def config_tit_entr1(self, tit):
        self.entr1.config_tit_Entry(tit)
    
    def config_tit_entr2(self, tit):
        self.entr2.config_tit_Entry(tit)
        
    def config_tit_entr3(self, tit):
        self.entr3.config_tit_Entry(tit)
        
        
    def config_tit_entr4(self, tit):
        self.entr4.config_tit_Entry(tit)
        
        
    def config_tit_entr5(self, tit):
        self.entr5.config_tit_Entry(tit)
        
        
    def config_tit_entr6(self, tit):
        self.entr6.config_tit_Entry(tit)
        
        
    def config_tit_entr7(self, tit):
        self.entr7.config_tit_Entry(tit)
        

    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)


    def config_tit_col_treeView1(self, col, titulo):
        self.treeView1.config_tit_col_treeView(col, titulo)
    
    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView1.insere_elem_treeView(value0, value1, value2, value3, value4)

    def insere_lst_elem_treeView1(self, lst_itens):
        self.treeView1.insere_lst_elem_treeView(lst_itens)


    def clear_treeView1(self):
        self.treeView1.clear_treeView()



    def config_tit_text(self, titulo):
        self.tit_text.config(text = titulo)
    
    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def config_comando_B2(self, comando):
        self.botao2.config(command = comando)
        
    def config_comando_B3(self, comando):
        self.botao3.config(command = comando)



    def config_tit_CBox1(self, tit):
        self.CBox1.config_tit_CBox(tit)

    def config_tit_CBox2(self, tit):
        self.CBox2.config_tit_CBox(tit)

    def config_tit_CBox3(self, tit):
        self.CBox3.config_tit_CBox(tit)

    def config_tit_CBox4(self, tit):
        self.CBox4.config_tit_CBox(tit)

    def insere_nova_CBox1(self, CBox):
        self.CBox1.insere_nova_CBox(CBox)

    def insere_nova_CBox2(self, CBox):
        self.CBox2.insere_nova_CBox(CBox)


    '''
    def insere_nova_CBox3(self, CBox):
        self.CBox3.insere_nova_CBox(CBox)
        
    def insere_nova_CBox4(self, CBox):
        self.CBox4.insere_nova_CBox(CBox)

    '''
    
    '''
    DEPRECIADA:
    def add_value_CBox1(self, lst):
        self.CBox1.config(state = "normal")
        aux = list(self.CBox1["values"])
        aux.append(lst)
        self.CBox1["values"] = lst
        self.CBox1.config(state = "readonly")
    '''
    
    '''
    DEPRECIADA:
    def add_value_CBox2(self, lst):
        self.CBox2.config(state = "normal")
        list_values = list(self.CBox2["values"])
        list_values.append(lst)
        self.CBox2["values"] = list_values
        self.CBox2.config(state = "readonly")
    '''
    
    '''
    DEPRECIADA:
    def add_value_CBox3(self, lst):
        self.CBox3.config(state = "normal")
        list_values = list(self.CBox3["values"])
        list_values.append(lst)
        self.CBox3["values"] = list_values
        self.CBox3.config(state = "readonly")
    '''
    
    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)
        

    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)


    '''
    def define_values_CBox3(self, lst):
        self.CBox3.define_values_CBox(lst)
    
    def define_values_CBox4(self, lst):
        self.CBox4.define_values_CBox(lst)
    '''
    
    
    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
    
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())
    
    
    '''
    def retorna_escolha_CBox3(self):
        return(self.CBox3.retorna_escolha_CBox())
    
    def retorna_escolha_CBox4(self):
        return(self.CBox4.retorna_escolha_CBox())
    '''
    
    
    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())
        
    def pointer_CBox2(self):
        return(self.CBox2.pointer_CBox())
        
        
    '''
    def pointer_CBox3(self):
        return(self.CBox3.pointer_CBox())

    def pointer_CBox4(self):
        return(self.CBox4.pointer_CBox())
    '''
    
    '''
    DEPRECIADA:
    def CBox1_bind(self, comando):
        self.CBox1.bind("<<ComboboxSelected>>", comando)
    '''
    
    '''
    DEPRECIADA:
    def CBox2_bind(self, bind_tuple):
        self.CBox2.bind(bind_tuple)
    '''
    
    '''
    DEPRECIADA:
    def CBox3_bind(self, comando):
        self.CBox3.bind('<<ComboboxSelected>>', comando)
    '''
    
    def config_CBox1_state(self, estado):
        self.CBox1.config_CBox_state(estado)
    
    def config_CBox2_state(self, estado):
        self.CBox2.config_CBox_state(estado)

    #~ def config_CBox3_state(self, estado):
        #~ self.CBox3.config_CBox_state(estado)
        
    #~ def config_CBox4_state(self, estado):
        #~ self.CBox4.config_CBox_state(estado)
        
    def set_CBox1_default(self, tit):
        self.CBox1.set_CBox_default(tit)
        
    def set_CBox2_default(self, tit):
        self.CBox2.set_CBox_default(tit)
        
    #~ def set_CBox3_default(self, tit):
        #~ self.CBox3.set_CBox_default(tit)

    #~ def set_CBox4_default(self, tit):
        #~ self.CBox4.set_CBox_default(tit)

    def insereTexto(self, txtStr):
        self.blocoText.config(state=NORMAL)
        self.blocoText.insert(1.0, txtStr)
        #~ self.blocoText.config(state=DISABLED)

    def limpa_CaixaTexto(self):
        self.blocoText.config(state=NORMAL)
        self.blocoText.delete('1.0', END)
        #~ self.blocoText.config(state=DISABLED)
        

        
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E, padx = 10, pady = 20)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()




class c_frame_insere_mov(LabelFrame):
    
    def __init__(self, framePai):
        LabelFrame.__init__(self, framePai)
        self.grid(row = 0, column = 0)
        
        #Bloco: Configurando frameLocal e seu título (LabelFrame):
        self.subFrame1 = Frame(self, padx ="8", pady = "8")
        self.subFrame1.grid(row = 0, column = 0, sticky = N)
        
        #Bloco: Configurando o título d, que receberá variável "tit2":
        self.tit2 = Label(self.subFrame1, text= "Titulo 2", pady = 5)
        self.tit2.grid(row=0, column=0,columnspan = 5, sticky = W+N)

        
        #Bloco CBox1:
        self.CBox1 = sub_CBox(self.subFrame1, CBox_values = ["Opção 1", "Opção 2"], set_CBox_default = '', width = 23)
        self.CBox1.grid_frame(row = 1, column = 0, padx = 10, sticky = W+N)
        
        #Bloco CBox2: 
        self.CBox2 = sub_CBox(self.subFrame1, tit_Cbox = 'CBox2', set_CBox_default = '', width = 23)
        self.CBox2.grid_frame(row = 1, column = 1, sticky = W+N, padx = 10)
        
        #Bloco CBox3: 
        self.CBox3 = sub_CBox(self.subFrame1, tit_Cbox = 'CBox3', set_CBox_default = '', width = 23)
        self.CBox3.grid_frame(row = 1, column = 2, sticky = W+N, padx = 10)
        


    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())

    def config_tit2(self, **kwargs):
        self.tit2.config(text = titulo)
    
    def config_nome_tit1(self, titulo):
        self.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)
    
    def config_tit_entr1(self, titulo):
        self.tit_entr1.config_tit_Entry(titulo)
    
    def config_tit_entr2(self, titulo):
        self.tit_entr2.config(text = titulo)
    
    def set_CBox1_default(self, titulo):
        self.CBox1.set_CBox_default(titulo)
    
    def config_tit_CBox1(self, titulo):
        self.CBox1.config_tit_CBox(titulo)
        
    def config_tit_CBox2(self, titulo):
        self.CBox2.config_tit_CBox(titulo)
    
    def config_tit_CBox3(self, titulo):
        self.CBox3.config_tit_CBox(titulo)


    def config_tit_text(self, titulo):
        self.tit_text.config(text = titulo)
    
    def add_value_CBox1(self, lst):
        self.CBox1.add_value_CBox(lst)

    
    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)

    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())

    def grid_frame(self):
        self.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.grid_forget()
    
    def finaliza(self):
        self.destroy()



class c_frame_insere_mov_antigo(LabelFrame):
    
    def __init__(self, framePai):
        LabelFrame.__init__(self, framePai)
        self.grid(row = 0, column = 0)
        
        #Bloco: Configurando frameLocal e seu título (LabelFrame):
        self.subFrame1 = Frame(self, padx ="8", pady = "8")
        self.subFrame1.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        #Bloco: Configurando o título d, que receberá variável "tit2":
        self.tit2 = Label(self.subFrame1, text= "Titulo 2", pady = 5)
        self.tit2.grid(row=0, column=0,columnspan = 5, sticky = W+N)

        #Bloco entr1: 
        self.entr1 = sub_Entry(self.subFrame1, tit_Entry = 'entr1', width = 55)
        self.entr1.grid_frame(row = 1, column = 1, sticky = W+E, padx = 10, columnspan = 2)
   
        #Bloco entr2: 
        self.entr2 = sub_Entry(self.subFrame1, tit_Entry = 'entr2', state_Entry = 'readonly', width = 26)
        self.entr2.grid_frame(row = 4, column = 0, sticky = W+N, padx = 10)

        #Bloco entr3: 
        self.entr3 = sub_Entry(self.subFrame1, tit_Entry = 'entr3', state_Entry = 'readonly', width = 55)
        self.entr3.grid_frame(row = 1, column = 3, sticky = W+E, padx = 10, columnspan = 2)
        
        #Bloco entr4: 
        self.entr4 = sub_Entry(self.subFrame1, tit_Entry = 'entr4', state_Entry = 'readonly', width = 26)
        self.entr4.grid_frame(row = 2, column = 3, sticky = W+N, padx = 10)
        
        #Bloco entr5: 
        self.entr5 = sub_Entry(self.subFrame1, tit_Entry = 'entr5', state_Entry = 'readonly', width = 26)
        self.entr5.grid_frame(row = 2, column = 4, sticky = W+N, padx = 10)
        
        #Bloco CBox1:
        self.CBox1 = sub_CBox(self.subFrame1, CBox_values = ["Opção 1", "Opção 2"], set_CBox_default = '', width = 23)
        self.CBox1.grid_frame(row = 5, column = 0, padx = 10, sticky = W+N)
        
        #Bloco CBox2: 
        self.CBox2 = sub_CBox(self.subFrame1, tit_Cbox = 'CBox2', set_CBox_default = '', width = 23)
        self.CBox2.grid_frame(row = 3, column = 3, sticky = W+N, padx = 10)
        
        #Bloco CBox3: 
        self.CBox3 = sub_CBox(self.subFrame1, tit_Cbox = 'CBox3', set_CBox_default = '', width = 23)
        self.CBox3.grid_frame(row = 3, column = 4, sticky = W+N, padx = 10)
        
        #~ #Bloco CBox2:
        #~ self.CBox2 = sub_CBox(self.subFrame1, CBox_values = ["Opção 1", "Opção 2"])
        #~ self.CBox2.grid_frame(row = 0 , column=4, sticky = W, padx = 10)
        
        #~ #Bloco CBox3:
        #~ self.CBox3 = sub_CBox(self.subFrame1, CBox_values = ["Opção 1", "Opção 2"])
        #~ self.CBox3.grid_frame(row = 2, column = 5, padx = 10)

        #Bloco botao1:
        self.botao1 = ttk.Button(self.subFrame1, text = "Botao 1", padding = "6 6 6 6")
        self.botao1.grid(row = 4, column = 1, pady = 3, sticky = S)

        #Bloco botao2:
        self.botao2 = ttk.Button(self.subFrame1, text = "Botao 2", padding = "6 6 6 6")
        self.botao2.grid(row = 5, column = 1, pady = 3, sticky = N)

        #Bloco botao3:
        self.botao3 = ttk.Button(self.subFrame1, text = "Botao 3", padding = "6 6 6 6")
        self.botao3.grid(row = 4, column = 2, pady = 3, sticky = S)

        #Bloco botao4:
        self.botao4 = ttk.Button(self.subFrame1, text = "Botao 4", padding = "6 6 6 6")
        self.botao4.grid(row = 5, column = 2, pady = 3, sticky = N)
            
        #Instanciando o CheckButton:
        #~ self.Cb = ttk.Checkbutton(self.frame_blocoText, text = "CheckButton:")
        #~ self.Cb.grid(row = 0, column = 0, sticky = W+E)
        #~ self.Cb.config(state = "deselected")

        #Instanciando o bloco Text:
        self.blocoText = sub_Text(self.subFrame1, width = 35, height = 3, bd = 3, tit = "Descrição:")
        self.blocoText.grid_frame(row = 2, column = 1, rowspan = 2, columnspan = 2, sticky = W, padx = 11, pady = 12)

        #Bloco 4: instanciando o frame que conterá o calendário:
        self.calendario = frame_calendario(self.subFrame1)
        self.calendario.grid_frame(row = 1, column = 0, rowspan = 3, padx = 10)
        
        #~ #Bloco 5.1 instanciando a Treeview:
        #~ self.treeView1 = sub_Treeview(self.subFrame1, numCols = 5)
        #~ self.treeView1.grid_frame(row = 7, column = 0,  columnspan = 7, padx = 5, sticky = W)
        
    def dat_select(self, **kwargs):
        return(self.calendario.selection_date(**kwargs))

    def pointer_CBox1(self):
        return(self.CBox1.pointer_CBox())
    
    def pointer_calendario(self):
        return(self.calendario.pointer_frameLocal())

    def config_label_entr1(self, **kwargs):
        self.entr1.config_Label(**kwargs)

    def config_label_entr2(self, **kwargs):
        self.entr2.config_Label(**kwargs)

    def config_label_entr3(self, **kwargs):
        self.entr3.config_Label(**kwargs)

    def config_label_entr4(self, **kwargs):
        self.entr4.config_Label(**kwargs)

    def config_label_entr5(self, **kwargs):
        self.entr5.config_Label(**kwargs)
        
    def config_label_entr6(self, **kwargs):
        self.entr6.config_Label(**kwargs)

    def config_label_entr7(self, **kwargs):
        self.entr7.config_Label(**kwargs)

    def config_tit2(self, **kwargs):
        self.tit2.config(text = titulo)
    
    def config_nome_tit1(self, titulo):
        self.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)
    
    def config_tit_entr1(self, titulo):
        self.tit_entr1.config_tit_Entry(titulo)
    
    def config_tit_entr2(self, titulo):
        self.tit_entr2.config(text = titulo)
    
    def set_CBox1_default(self, titulo):
        self.CBox1.set_CBox_default(titulo)
    
    def config_tit_CBox1(self, titulo):
        self.CBox1.config_tit_CBox(titulo)
        
    def config_tit_CBox2(self, titulo):
        self.CBox2.config_tit_CBox(titulo)
    
    def config_tit_CBox3(self, titulo):
        self.CBox3.config_tit_CBox(titulo)
    
    def config_B1(self, **kwargs):
        self.botao1.config(kwargs)
        
    def config_B2(self, **kwargs):
        self.botao2.config(kwargs)
        
    def config_B3(self, **kwargs):
        self.botao3.config(kwargs)
        
    def config_B4(self, **kwargs):
        self.botao4.config(kwargs)

    def config_tit_text(self, titulo):
        self.tit_text.config(text = titulo)
    
    def insert_entr1(self, entr):
        self.entr1.insert_Entry(entr)

    def insert_entr2(self, entr):
        self.entr2.insert_Entry(entr)

    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def add_value_CBox1(self, lst):
        self.CBox1.add_value_CBox(lst)

    def add_value_CBox2(self, lst):
        self.CBox2.add_value_CBox(lst)
    
    def define_values_CBox1(self, lst):
        self.CBox1.define_values_CBox(lst)
        
    def define_values_CBox2(self, lst):
        self.CBox2.define_values_CBox(lst)
    
    def retorna_escolha_CBox1(self):
        return(self.CBox1.retorna_escolha_CBox())
    
    def retorna_escolha_CBox2(self):
        return(self.CBox2.retorna_escolha_CBox())
    
    def insereTexto(self, txtStr):
        self.blocoText.insert_text(state = txtStr)

    def limpaCaixaTexto(self):
        self.blocoText.clear_text()
        
    def grid_frame(self):
        self.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.grid_forget()
    
    def finaliza(self):
        self.destroy()



class c_frame_ref_compra_list(c_frame_insere_mov):
        
    def __init__(self, framePai):
        c_frame_insere_mov.__init__(self, framePai)

        #Bloco (1): Configurando frameLocal e seu título (LabelFrame):
        self.frameLocal = LabelFrame(self, text = "Titulo 1", borderwidth=2, padx ="10", pady = "10")
        self.frameLocal.grid(row = 1, column = 0)


########## BLOCO DO SUBFRAME1: ###########
        self.subFrame2 = Frame(self.frameLocal, padx = 5, pady = 5)
        self.subFrame2.grid(row = 0, column = 0, sticky = W+E+S+N)
        
        #Bloco (2): Configurando o tit2:
        self.tit2 = Label(self.subFrame1, text= "Titulo 2", pady = 5)
        self.tit2.grid(row=0, column=0,columnspan = 2, sticky = W+N)


        #Bloco entr1 (3): 
        self.entr6 = sub_Entry(self.subFrame2, width = 51, tit_Entry = "testando")
        self.entr6.grid_frame(row=1, column=0, columnspan = 2, sticky = W, padx = 5)
        

        #Bloco botao1:
        self.botao1 = ttk.Button(self.subFrame2, text = "Enviar")
        self.botao1.grid(row = 1, column = 2, sticky = S)


        #Bloco do frame da Treeview1:
        self.treeView1 = sub_Treeview(self.subFrame2, num_cols = 4, height = 3)
        self.treeView1.grid_frame(row = 5, column = 0, sticky = W, columnspan = 4, pady = 5, padx = 5)
        
        #Bloco do separador1:
        self.separador1 = ttk.Separator(self.subFrame2, orient = HORIZONTAL)
        self.separador1.grid(row = 6, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "we")



############## BLOCO DO SUBFRAME2: ############
        self.subFrame3 = Frame(self.frameLocal, padx = 5, pady = 5)
        self.subFrame3.grid(row = 1, column = 0, sticky = W+E+S+N)

        #Bloco (2): Configurando o tit2:
        self.tit3 = Label(self.subFrame3, text= "Titulo 3", pady = 5)
        self.tit3.grid(row = 7, column = 0,columnspan = 2, sticky = W+N)


        #Bloco entr2: 
        self.entr7 = sub_Entry(self.subFrame3, width = 51, tit_Entry = "testando")
        self.entr7.grid_frame(row=8, column=0, columnspan = 3, sticky = W+E, padx = 5)

        #Bloco CBox1:
        self.CBox1 = sub_CBox(self.subFrame3, tit_Entry = "Combo Box")
        self.CBox1.grid_frame(row=8, column = 2, padx = 5)

        #Bloco entr3: 
        self.entr8 = sub_Entry(self.subFrame3, tit_Entry = "testando", width = 10)
        self.entr8.grid_frame(row=9, column=0, sticky = W, padx = 5)


        #Bloco entr4: 
        self.entr9 = sub_Entry(self.subFrame3, tit_Entry = "testando", width = 10)
        self.entr9.grid_frame(row=9, column=1, sticky = W, padx = 5)


        #Bloco entr5: 
        self.entr10 = sub_Entry(self.subFrame3, tit_Entry = "testando", width = 10)
        self.entr10.grid_frame(row = 9, column=2, sticky = W, padx = 5)


        #Bloco botao2:
        self.botao2 = ttk.Button(self.subFrame3, text = "Enviar")
        self.botao2.grid(row = 9, column = 2, sticky = E+S)



        #Bloco do frame da Treeview2:
        self.treeView2 = sub_Treeview(self.subFrame3, num_cols = 4)
        self.treeView2.grid_frame(row = 14, column = 0, sticky = W, padx = 5, pady = 5, columnspan = 4)
        
        #~ #Bloco do separador2:
        #~ self.separador2 = ttk.Separator(self.subFrame3, orient = HORIZONTAL)
        #~ self.separador2.grid(row = 15, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "we")



########### BLOCO DO SUBFRAME3: ##########
        self.subFrame4 = Frame(self.frameLocal, padx = 5, pady = 5)
        self.subFrame4.grid(row = 0, column = 1, rowspan = 2, sticky = W+E+S+N)
        
        self.separador3 = ttk.Separator(self.subFrame4, orient = VERTICAL)
        self.separador3.grid(row = 0, column = 0, rowspan = 40, pady = 10, padx = 10, sticky = "sn")
        
        self.entr11 = sub_Entry(self.subFrame4, width = 51, tit_Entry = 'entr8')
        self.entr11.grid_frame(row=0, column=1, sticky = W, padx = 5)


        self.treeView3 = sub_Treeview(self.subFrame4, num_cols = 4, height = 17)
        self.treeView3.grid_frame(row = 1, column = 1, sticky = W, padx = 5, pady = 5, rowspan = 18, columnspan = 4, num_cols = 4)
        
        self.botao3 = ttk.Button(self.subFrame4, text = "Enviar")
        self.botao3.grid(row = 20, column = 1, sticky = W, pady = 10)
        
        self.label4 = ttk.Label(self.subFrame4, text = 'label4')
        self.label4.grid(row = 20, column = 2, sticky = E)
        
     
        
        
    def pointer_treeView1(self):
        return(self.treeView1.pointer_treeView())
        
        
    def pointer_treeView2(self):
        return(self.treeView2.pointer_treeView())
        
   
    def pointer_treeView3(self):
        return(self.treeView3.pointer_treeView())
        
    def insert_entr1(self, entr):
        self.entr1.insert_Entry(entr)
        
    def insert_entr2(self, entr):
        self.entr2.insert_Entry(entr)
        
    def insert_entr3(self, entr):
        self.entr3.insert_Entry(entr)

    def insert_entr4(self, entr):
        self.entr4.insert_Entry(entr)

    def insert_entr5(self, entr):
        self.entr5.insert_Entry(entr)

    def insert_entr6(self, entr):
        self.entr6.insert_Entry(entr)

    def insert_entr7(self, entr):
        self.entr7.insert_Entry(entr)
        
    def insert_entr8(self, entr):
        self.entr8.insert_Entry(entr)

    def idd_selection_treeView1(self):
        return(self.treeView1.idd_selection_treeView())

    def idd_selection_treeView2(self):
        return(self.treeView2.idd_selection_treeView())
    
    def idd_selection_treeView3(self):
        return(self.treeView3.idd_selection_treeView())


    def config_tit_treeView1(self, titulo):
        self.treeView1.config_tit_treeView(titulo)
        
    def config_tit_col0_treeView1(self, titulo):
        self.treeView1.heading("#0", text = titulo)

    def config_tit_col1_treeView1(self, titulo):
        self.treeView1.heading("coluna1", text = titulo)

    def config_tit_col2_treeView1(self, titulo):
        self.treeView1.heading("coluna2", text = titulo)

    def config_tit_col3_treeView1(self, titulo):
        self.treeView1.heading("coluna3", text = titulo)
        
    def config_tit_col4_treeView1(self, titulo):
        self.treeView1.heading("coluna4", text = titulo)

    def insere_elem_treeView1(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        self.treeView1.insert.insere_elem_treeView(value0, value1, value2, value3, value4)


    def insere_lst_elem_treeView1(self, lst_itens):
        self.treeView1.insere_lst_elem_treeView(lst_itens)


    def config_B1(self, **kwargs):
        self.botao1.config(kwargs)
        
    def config_B2(self, **kwargs):
        self.botao2.config(kwargs)
        
    def config_B3(self, **kwargs):
        self.botao3.config(kwargs)
    
    def config_B4(self, **kwargs):
        self.botao4.config(kwargs)
        
    def config_B5(self, **kwargs):
        self.botao5.config(kwargs)


    def config_tit_treeView2(self, titulo):
        self.treeView2.config_tit_treeView(titulo)
        
    def config_tit_col0_treeView2(self, titulo):
        self.treeView2.heading("#0", text = titulo)

    def config_tit_col1_treeView2(self, titulo):
        self.treeView2.heading("coluna1", text = titulo)

    def config_tit_col2_treeView2(self, titulo):
        self.treeView2.heading("coluna2", text = titulo)

    def config_tit_col3_treeView2(self, titulo):
        self.treeView2.heading("coluna3", text = titulo)
        
    def config_tit_col4_treeView2(self, titulo):
        self.treeView2.heading("coluna4", text = titulo)

    def insere_elem_treeView2(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        elems = (value1, value2, value3, value4)
        self.treeView2.insert('', 0, text = value0, values = elems)

    def insere_lst_elem_treeView2(self, lst_itens):
        self.treeView2.insere_lst_elem_treeView(lst_itens)


    def clear_treeView1(self):
        self.treeView1.clear_treeView()
        
    def clear_treeView2(self):
        self.treeView2.clear_treeView()
        
        
    def clear_treeView3(self):
        self.treeView3.clear_treeView()


    #~ def config_tit_treeView3(self, titulo):
        #~ self.tit_treeView3.config(text = titulo)
        
    def config_tit_col0_treeView3(self, titulo):
        self.treeView3.heading("#0", text = titulo)

    def config_tit_col1_treeView3(self, titulo):
        self.treeView3.heading("coluna1", text = titulo)

    def config_tit_col2_treeView3(self, titulo):
        self.treeView3.heading("coluna2", text = titulo)

    def config_tit_col3_treeView3(self, titulo):
        self.treeView3.heading("coluna3", text = titulo)
        
    def config_tit_col4_treeView3(self, titulo):
        self.treeView3.heading("coluna4", text = titulo)

    def insere_elem_treeView3(self, value0 = '', value1 = '', value2 = '', value3 = '', value4 = ''):
        elems = (value1, value2, value3, value4)
        self.treeView3.insert('', 0, text = value0, values = elems)


    def insert_lst_treeView1(self, lst_treeView):
        self.treeView1.insert_lst_treeView(lst_treeView)

    def insert_lst_treeView2(self, lst_treeView):
        self.treeView2.insert_lst_treeView(lst_treeView)

    def insert_lst_treeView3(self, lst_treeView):
        self.treeView3.insert_lst_treeView(lst_treeView)
        

    def insere_lst_elem_treeView3(self, lst_itens):
        for item in lst_itens:
            self.treeView3.insert('', 0, text = item[0], values = item[1:])

    def retorna_entr1(self):
        return(self.entr1.retorna_entr())
    
    def retorna_entr2(self):
        return(self.entr2.retorna_entr())

    def retorna_entr3(self):
        return(self.entr3.retorna_entr())
        
    def retorna_entr4(self):
        return(self.entr4.retorna_entr())

    def retorna_entr5(self):
        return(self.entr5.retorna_entr())

    def retorna_entr6(self):
        return(self.entr6.retorna_entr())

    def retorna_entr7(self):
        return(self.entr7.retorna_entr())



    def config_label_entr1(self, **kwargs):
        self.entr1.config_Label(**kwargs)
        

    def config_label_entr2(self, **kwargs):
        self.entr2.config_Label(**kwargs)


    def config_label_entr3(self, **kwargs):
        self.entr3.config_Label(**kwargs)
        

    def config_label_entr4(self, **kwargs):
        self.entr4.config_Label(**kwargs)
        

    def config_label_entr5(self, **kwargs):
        self.entr5.config_Label(**kwargs)
        

    def config_label_entr6(self, **kwargs):
        self.entr6.config_Label(**kwargs)
        

    def config_label_entr7(self, **kwargs):
        self.entr7.config_Label(**kwargs)


    def config_tit_entr1(self, tit):
        self.entr1.config_tit_Entry(tit)

    
    def config_tit_entr2(self, tit):
        self.entr2.config_tit_Entry(tit)
        
    def config_tit_entr3(self, tit):
        self.entr3.config_tit_Entry(tit)


    def config_tit_entr4(self, tit):
        self.entr4.config_tit_Entry(tit)
        
        
    def config_tit_entr5(self, tit):
        self.entr5.config_tit_Entry(tit)

    def config_tit_entr6(self, tit):
        self.entr6.config_tit_Entry(tit)
        
        
    def config_tit_entr7(self, tit):
        self.entr7.config_tit_Entry(tit)

    def config_tit_entr8(self, tit):
        self.entr8.config_tit_Entry(tit)


    def pointer_entr1(self):
        return(self.entr1.pointer_Entry())
        
    def pointer_entr2(self):
        return(self.entr2.pointer_Entry())
        
    def pointer_entr3(self):
        return(self.entr3.pointer_Entry())
        
    def pointer_entr4(self):
        return(self.entr4.pointer_Entry())
        
    def pointer_entr5(self):
        return(self.entr5.pointer_Entry())
        
    def pointer_entr6(self):
        return(self.entr6.pointer_Entry())
        
        
    def pointer_entr7(self):
        return(self.entr7.pointer_Entry())


    def pointer_entr8(self):
        return(self.entr8.pointer_Entry())

    def limpa_entr1(self):
        self.entr1.limpa_entr()

    def limpa_entr2(self):
        self.entr2.limpa_entr()
        
    def limpa_entr3(self):
        self.entr3.limpa_entr()

    def limpa_entr4(self):
        self.entr4.limpa_entr()
        
    def limpa_entr5(self):
        self.entr5.limpa_entr()

    def limpa_entr6(self):
        self.entr6.limpa_entr()

    def limpa_entr7(self):
        self.entr7.limpa_entr()

    def limpa_entr8(self):
        self.entr8.limpa_entr()



    def config_entr1(self, **kwargs):
        self.entr1.config_Entry(**kwargs)
    
    def config_entr2(self, **kwargs):
        self.entr2.config_Entry(**kwargs)
   
    def config_entr3(self, **kwargs):
        self.entr3.config_Entry(**kwargs)
   
    def config_entr4(self, **kwargs):
        self.entr4.config_Entry(**kwargs)
   
    def config_entr5(self, **kwargs):
        self.entr5.config_Entry(**kwargs)
   
    def config_entr6(self, **kwargs):
        self.entr6.config_Entry(**kwargs)



    def config_entr1_state(self, estado):
        self.entr1.config_Entry_state(estado)

    def config_entr2_state(self, estado):
        self.entr2.config_Entry_state(estado)
        
    def config_entr3_state(self, estado):
        self.entr3.config_Entry_state(estado)

    def config_entr4_state(self, estado):
        self.entr4.config_Entry_state(estado)
        
        
    def config_entr5_state(self, estado):
        self.entr5.config_Entry_state(estado)
        

    def config_entr6_state(self, estado):
        self.entr6.config_Entry_state(estado)
        
    def config_entr7_state(self, estado):
        self.entr7.config_Entry_state(estado)
        
    def config_entr8_state(self, estado):
        self.entr8.config_Entry_state(estado)
        

    def config_nome_tit1(self, titulo):
        self.frameLocal.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)

    def config_nome_tit3(self, titulo):
        self.tit3.config(text = titulo)


    def config_tit_CBox1(self, titulo):
        self.CBox1.config_tit_CBox(titulo)
        
    def config_tit_CBox2(self, titulo):
        self.CBox2.config_tit_CBox(titulo)

    def config_tit_CBox3(self, titulo):
        self.CBox3.config_tit_CBox(titulo)

    def set_CBox1_default(self, titulo):
        self.CBox1.set_CBox_default(titulo)

    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def insere_nova_CBox1(self, CBox):
        self.CBox1.destroy()
        self.CBox1 = CBox(self.frameLocal)
        self.CBox1.grid(row = 2, column = 1)

    def insere_nova_CBox2(self, CBox):
        self.CBox2.destroy()
        self.CBox2 = CBox(self.frameLocal)
        self.CBox2.grid(row = 2, column = 2)
    
    def add_value_CBox1(self, lst):
        self.CBox1.config(state = "normal")
        aux = list(self.CBox1["values"])
        aux.append(lst)
        self.CBox1["values"] = lst
        self.CBox1.config(state = "readonly")

        
    def add_value_CBox2(self, lst):
        self.CBox2.config(state = "normal")
        list_values = list(self.CBox2["values"])
        list_values.append(lst)
        self.CBox2["values"] = list_values
        self.CBox2.config(state = "readonly")
    
    
    def define_values_CBox1(self, lst):
        self.CBox1["values"] = lst

    def define_values_CBox2(self, lst):
        self.CBox2["values"] = lst
    
    def retorna_escolha_CBox1(self):
        return(self.var_CBox1.get())
    
    def retorna_escolha_CBox2(self):
        return(self.var_CBox2.get())

    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)#, padx = 10, pady = 20)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
    
    def finaliza(self):
        self.frameLocal.destroy()


class c_frame_menu_inic:

    def __init__(self, framePai, **kwargs):

        #Bloco (2.1): Abaixo, é declarado o frame que conterá o menu. O frame está contido no frame-pai:
        self.frameLocal = Frame(framePai)
        #self.frameLocal.grid(row = 0, column=0, sticky = N+S, pady = 2, padx = 2)
        
        
        #Subtítulos do programa:
        #O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.tit1 = Label(self.frameLocal, anchor = CENTER, width = 18)
        self.tit1.grid(row = 0, column=0, sticky = E+W)#Subtitulo fixado na origem do "frameLocal"(row=0, column=0)
        
        self.separator = ttk.Separator(self.frameLocal, orient = HORIZONTAL)
        self.separator.grid(row = 1, column=0, sticky = 'we', pady = 2, padx = 2)

        #O subtitulo3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.tit2 = Label(self.frameLocal, padx = 5)
        self.tit2.grid(row = 2,column = 0, sticky = E+W)
        
        #O botao1 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao1 = ttk.Button(self.frameLocal)
        self.botao1.grid(row = 3, column = 0, sticky = W+E, padx = 2)
        
        #O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao2 = ttk.Button(self.frameLocal)
        self.botao2.grid(row = 4, column = 0, sticky = W+E, padx = 2)
        
        
        #O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.botao3 = ttk.Button(self.frameLocal)
        self.botao3.grid(row = 5, column = 0, sticky = W+E, padx = 2)
                
    
    def config_nome_tit1(self, titulo):
        self.tit1.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)

    def config_nome_B1(self, titulo):
        self.botao1.config(text = titulo)

    def config_nome_B2(self, titulo):
        self.botao2.config(text = titulo)
    
    def config_nome_B3(self, titulo):
        self.botao3.config(text = titulo)	
            
    def config_comando_B1(self, comando):
        self.botao1.config(command = comando)

    def config_comando_B2(self, comando):
        self.botao2.config(command = comando)
        
    def config_comando_B3(self, comando):
        self.botao3.config(command = comando)
    
    def grid_frame(self):
        self.frameLocal.grid(row = 0, column=0, sticky = N+S, pady = 2, padx = 2)
        
    def ungrid_frame(self):
        self.frameLocal.grid_forget()
        
    def finaliza(self):
        self.frameLocal.destroy()

class frame_calendario(Frame):
    
    def __init__(self, framePai, **kwargs):
        self.frameLocal = Frame(framePai, padx = 2, pady = 4)
        self.calendario = Calendar(self.frameLocal, firstweekday=calendar.SUNDAY)
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
        self.calendario.grid(row = 0, column = 0, sticky = N+S+W+E)
        
    
    def pointer_frameLocal(self):
        return(self.calendario.pointer_frameLocal())

    def grid_frame(self, **kwargs):
        self.frameLocal.grid(kwargs)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def selection_date(self, **kwargs):
        dat = self.calendario.select_dat(**kwargs)
        return(dat)
    
    def finaliza(self):
        self.frameLocal.destroy()

class coll_menu(Frame):

    def __init__(self, frame_master):
        #Bloco (2.1): Abaixo, é declarado o frame que conterá o menu. O frame está contido no frame-pai:
        super().__init__(frame_master)
        self.frameLocal = Frame(self, padx = 2, pady = 4)
        #self.frameLocal.grid(row = 0, column=0, sticky = N+S)
        
        
        #Subtítulos do programa:
        #O subTitulo1 é declarado e "fixado"(.grid) dentro do frameLocal com o nome do programa:
        self.tit1 = Label(self.frameLocal, text = 'pyMoney v0.01', font= 'Verdana', anchor = CENTER, relief = GROOVE, padx = 3, pady = 3)
        self.tit1.grid(row = 0, column=0, sticky = E+W, padx = 3, pady = 3)#, sticky = E+W)#Subtitulo fixado na origem do "frameLocal"(row=0, column=0)
        
        
        self.separadorV1 = ttk.Separator(self.frameLocal, orient = VERTICAL, style = "TSeparator")
        self.separadorV1.grid(row = 0, column = 1, rowspan = 13, sticky="ns", padx = 2, pady = 3)

        #O subtitulo3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.tit2 = Label(self.frameLocal,text = "Carregue uma conta", font = 'Verdana', anchor = CENTER, relief = GROOVE, padx = 3, pady = 3)
        self.tit2.grid(row=1,column=0, sticky = E+W, padx = 3, pady = 3)
        
        #O subtitulo4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.tit3 = Label(self.frameLocal, text = "Menu", relief= FLAT, font = 'Verdana', anchor = CENTER)
        self.tit3.grid(row = 2, column = 0, sticky = E+W)
        
        #ttk.Style().configure("Toolbutton", relief = "ridge")
        #ttk.Style().configure('Toolbutton.label', 'sticky' = 'we')
        #~ print(ttk.Style().layout('Toolbutton'))
        
        #O botao1 é declarado no sub-bloco abaixo, dentro do frameLocal:
            #A variável varRb guardará o valor dos Radiobuttons
        self.varRb = IntVar()



        self.Rb1 = ttk.Radiobutton(self.frameLocal,text = "Status geral - Mês atual", value = 1, variable=self.varRb, style = 'Toolbutton')
        self.Rb1.grid(row = 3, column = 0, sticky = E+W, padx = 3, pady = 1)
        
        #O  botao2 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb2 = ttk.Radiobutton(self.frameLocal,text = "Status geral - Meses anteriores", value = 2, variable=self.varRb, style = 'Toolbutton')
        self.Rb2.grid(row=4, column = 0, sticky = E+W, padx = 3, pady = 1)
        
        #O  botao3 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb3 = ttk.Radiobutton(self.frameLocal,text = "Análises/relatórios", value = 3, variable=self.varRb, style = 'Toolbutton')
        self.Rb3.grid(row=5, column = 0, sticky = E+W, padx = 3, pady = 1)

        #O  botao4 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb4 = ttk.Radiobutton(self.frameLocal,text = "Editar/inserir referente", value = 4, variable=self.varRb, style = 'Toolbutton')
        self.Rb4.grid(row=6, column = 0, sticky = E+W, padx = 3, pady = 1)	
    
        #O  botao5 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb5 = ttk.Radiobutton(self.frameLocal,text = "Inserir movimentação", value = 5, variable=self.varRb, style = 'Toolbutton')
        self.Rb5.grid(row=7, column = 0, sticky = E+W, padx = 3, pady = 1)	


        #O  botao6 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb6 = ttk.Radiobutton(self.frameLocal,text = "Estoque de Itens", value = 6, variable=self.varRb, style = 'Toolbutton')
        self.Rb6.grid(row=8, column = 0, sticky = E+W, padx = 3, pady = 1)	


        self.separadorH2 = ttk.Separator(self.frameLocal, orient = HORIZONTAL, style = "TSeparator")
        self.separadorH2.grid(row = 9, column = 0, sticky="we", padx = 4, pady = 3)


        #O  botao7 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb7 = ttk.Radiobutton(self.frameLocal,text = "Banco de itens/Serviços", value = 7, variable=self.varRb, style = 'Toolbutton')
        self.Rb7.grid(row=10, column = 0, sticky = E+W, padx = 3, pady = 1)	

        #O  botao8 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb8 = ttk.Radiobutton(self.frameLocal,text = "Banco de fornecedores", value = 8, variable=self.varRb, style = 'Toolbutton')
        self.Rb8.grid(row=11, column = 0, sticky = E+W, padx = 3, pady = 1)	
        
        
        #O  botao9 é declarado no sub-bloco abaixo, dentro do frameLocal:
        self.Rb9 = ttk.Radiobutton(self.frameLocal,text = "Banco de clientes", value = 9, variable=self.varRb, style = 'Toolbutton')
        self.Rb9.grid(row=12, column = 0, sticky = E+W, padx = 3, pady = 1)	
        



    def desativa_todos_Rb(self):
        self.Rb1.config(state = "disabled")
        self.Rb2.config(state = "disabled")
        self.Rb3.config(state = "disabled")
        self.Rb4.config(state = "disabled")
        self.Rb5.config(state = "disabled")
        self.Rb6.config(state = "disabled")
        self.Rb7.config(state = "disabled")
        self.Rb8.config(state = "disabled")
        self.Rb9.config(state = "disabled")
        
        
    def ativa_todos_Rbs(self):
        self.Rb1.config(state = "eneable")
        self.Rb2.config(state = "eneable")
        self.Rb3.config(state = "eneable")
        self.Rb4.config(state = "eneable")
        self.Rb5.config(state = "eneable")
        self.Rb6.config(state = "eneable")
        self.Rb7.config(state = "eneable")
        self.Rb8.config(state = "eneable")
        self.Rb9.config(state = "eneable")
            

    def ativa_Rb(self, Rb):
        self.Rb.config(state = "active")
        
    def desativa_Rb(self, Rb):
        self.Rb.config(state = "disabled")
    
    def config_nome_tit1(self, titulo):
        self.tit1.config(text = titulo)
        
    def config_nome_tit2(self, titulo):
        self.tit2.config(text = titulo)

    def config_nome_tit3(self, titulo):
        self.tit3.config(text = titulo)
        
    def config_nome_Rb1(self, titulo):
        self.Rb1.config(text = titulo)
    
    def config_nome_Rb2(self, titulo):
        self.Rb2.config(text = titulo)
        
    def config_nome_Rb3(self, titulo):
        self.Rb3.config(text = titulo)
        
    def config_nome_Rb4(self, titulo):
        self.Rb4.config(text = titulo)
        
    def config_nome_Rb5(self, titulo):
        self.Rb5.config(text = titulo)
        
    def config_nome_Rb6(self, titulo):
        self.Rb6.config(text = titulo)
    
    def config_nome_Rb7(self, titulo):
        self.Rb7.config(text = titulo)
    
    def config_nome_Rb8(self, titulo):
        self.Rb8.config(text = titulo)
    
    def config_nome_Rb9(self, titulo):
        self.Rb9.config(text = titulo)

        
    def config_comando_Rb1(self, comando):
        self.Rb1.config(command = comando)

    def config_comando_Rb2(self, comando):
        self.Rb2.config(command = comando)

    def config_comando_Rb3(self, comando):
        self.Rb3.config(command = comando)

    def config_comando_Rb4(self, comando):
        self.Rb4.config(command = comando)

    def config_comando_Rb5(self, comando):
        self.Rb5.config(command = comando)

    def config_comando_Rb6(self, comando):
        self.Rb6.config(command = comando)

    def config_comando_Rb7(self, comando):
        self.Rb7.config(command = comando)
    
    def config_comando_Rb8(self, comando):
        self.Rb8.config(command = comando)
    
    def config_comando_Rb9(self, comando):
        self.Rb9.config(command = comando)


    def pointer_frameLocal(self):
        return(self.frameLocal)

    def grid_frame(self):
        self.frameLocal.grid(row = 0, column = 0, sticky = N+S+W+E)
    
    def ungrid_frame(self):
        self.frameLocal.grid_forget()

    def escolha_Rb(self):
        escolha = self.varRb.get()
        return(escolha)
    
    def finaliza(self):
        self.frameLocal.destroy()

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


    def __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        # creating a scrollbars
        self.xscrlbr = ttk.Scrollbar(self.parent, orient = 'horizontal')
        self.xscrlbr.grid(column = 0, row = 1, sticky = 'ew', columnspan = 2)
        self.yscrlbr = ttk.Scrollbar(self.parent)
        self.yscrlbr.grid(column = 1, row = 0, sticky = 'ns')
        # creating a canvas
        self.canv = Canvas(self.parent)
        self.canv.config(relief = 'flat',
                         width = 10,
                         heigh = 10, bd = 2)
        # placing a canvas into frame
        self.canv.grid(column = 0, row = 0, sticky = 'nsew')
        # accociating scrollbar comands to canvas scroling
        self.xscrlbr.config(command = self.canv.xview)
        self.yscrlbr.config(command = self.canv.yview)

        # creating a frame to inserto to canvas
        self.scrollwindow = ttk.Frame(self.parent)

        self.canv.create_window(0, 0, window = self.scrollwindow, anchor = 'nw')

        self.canv.config(xscrollcommand = self.xscrlbr.set,
                         yscrollcommand = self.yscrlbr.set,
                         scrollregion = (0, 0, 100, 100))

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
        self.canv.yview_scroll(int(-1*(event.delta/120)), "units")

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
        self.canv.config(scrollregion='0 0 %s %s' % size)
        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canv.config(width = self.scrollwindow.winfo_reqwidth())
        if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
            # update the canvas's width to fit the inner frame
            self.canv.config(height = self.scrollwindow.winfo_reqheight())

class janelaPrincipal_3f_N_H:

    def __init__(self, master):
        
        # Bloco (1) Configurando frame principal(janela-pai):
        
        #Comando abaixo configura a resoluação padrão da janela como sendo a resolução do PC em questão:
        
        '''
        A presente classe retorna uma janela na resolução automática.
        Por esse motivo, o bloco abaixo será ignorado.
        master.geometry("{}x{}".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        #Comando abaixo configura a janela para iniciar como "maximizada":
        master.state('zoomed')	
        '''
        
        #Comando abaixo configura o título da janela:
        self.mastermaster.title(' ')
        #Comando abaixo printa no terminal a resolução configurada para a máquina em questão:
        print(self.master.winfo_screenwidth(), self.master.winfo_screenheight()) 
        
        #Abaixo é declarada a janela-pai
        self.framePai = ttk.Frame(self.master, padding="4 4 8 8")
        framePai.grid(sticky = E+W+S+N)


        
        #
        #Fim do Bloco (1)
        #------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        #------------------------------------------------------------------------------------------------------------------#
        
        # Bloco (2) Declaração do menu superior da janela-pai:
        menuSuperior = Menu(master)

        
        #Abaixo a declaração e as Sub-opções dentro da opção "Arquivo":
        menuArquivo = Menu(menuSuperior, tearoff=0)
        menuSuperior.add_cascade(menu=menuArquivo, label='Arquivo')
        #Sub-opções dentro da opção "Arquivo":
        menuArquivo.add_command(label="Carregar ",  command ='')
        menuArquivo.add_command(label="Novo",  command = self.load_file_txt)	
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        menuArquivo.add_separator()  #Esse comando adciona um layout de separação entre as opções do menu
        
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Configurações":
        menuConfiguracoes = Menu(menuSuperior, tearoff=0)
        menuSuperior.add_cascade(menu=menuConfiguracoes,label='Ferramentas')
        #Sub-opções dentro da opção "Configurações":,
        menuConfiguracoes.add_command(label="Configurações")
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        menuConfiguracoes.add_separator() 
        
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Ajuda":
        menuAjuda = Menu(menuSuperior, tearoff=0)
        menuSuperior.add_cascade(menu=menuAjuda,label='Ajuda')
        #Sub-opções dentro da opção "Ajuda":
        menuAjuda.add_command(label="Tutorial")	
        menuAjuda.add_command(label="Sobre")	
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        menuAjuda.add_separator()
        
        
        
        #Comando que exibe o menu:
        master.config(menu=menuSuperior)
        
        #Fim do bloco (2)
        #------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        #------------------------------------------------------------------------------------------------------------------#
        
        # Bloco (3) Declarando sub-frames da janela-pai:
        '''A janela-pai está dividida em três sub-frames, lateral esquerdo, central, e lateral direito.
                Na presente classe, cada um dos três sub-frames admite apenas um sub-frame.
                Sendo assim, adimitindo o maior grau de divisão de frames na classe, a janela-pai terá a seguinte divisão:
                
                ______________________________janela-pai______________________________
                |(subFrameLateralEsquerdo)|(subFrameCentral)|(subFrameLateralDireito)|
                
        '''	
        
        #Bloco (3.1): Abaixo, é declarado o frame lateral que conterá um menu. O frame está contido no frame-pai:
        self.frame_esquerdo = Frame(self.framePai)
        self.frame_esquerdo.grid(row = 0, column=0, sticky = N+S)
        
        
        
        #Bloco (3.3): Abaixo, é declarado o frame central. O frame está contido no frame-pai:
        self.frame_central = Frame(self.framePai)
        self.frame_central.grid(row = 0, column = 1, sticky = N+S+W+E)
    
        


        #Bloco (3.4): Abaixo, é declarado o frame lateral direito. O frame está contido no frame-pai:
        self.frame_direito = Frame(self.framePai)
        self.frame_direito.grid(row = 0, column = 2, sticky = N+S+W+E)



        #Bloco (3.5): Abaixo, é declarado o frame inferior no rodapé da do frame-pai(note o columnspan = 3):
        self.frame_infe = Frame(self.framePai)
        self.frame_infe.grid(row = 1, column = 0, columnspan = 3, sticky = N+S+W+E)


    def add_wid_frame_esqr(self, wid_frame):
        self.wid_frame_esq = wid_frame(self.frame_esquerdo)
        return(self.wid_frame_esq)
        
    def add_wid_frame_cent(self, wid_frame):
        self.wid_frame_cent = wid_frame(self.frame_central)
        return(self.wid_frame_cent)
        
    def add_wid_frame_dire(self, wid_frame):
        self.wid_frame_dire = wid_frame(self.frame_direito)
        return(self.wid_frame_dire)
    
    def add_wid_frame_infe(self, wid_frame):
        self.wid_frame_infe = wid_frame(self.wid_frame_infe)
        return(self.wid_frame_infe)
    
        
    
    def pointer_frame_esq(self):
        return(self.frame_esquerdo)
    
    def pointer_frame_cent(self):
        return(self.frame_central)
        
    def pointer_frame_dire(self):
        return(self.frame_direito)
        
    def pointer_frame_infe(self):
        return(self.frame_infe)




    def load_file_txt(self):

        #A rotina abaixo abre o .txt, retornando um string, tratando eventuais erros com o encode:
        def tryOpen(filename):
            try:
                arq = open(filename, 'r', encoding = 'utf-8')
            except (UnicodeDecodeError, UnicodeEncodeError): #Aqui a função trata erros de enconding
                try:
                    print('\n*** Observação: UnicodeDecodeError, tentando encoding = charmap ***')
                    arq = open(filename, 'r', encoding ='charmap')
                except (UnicodeDecodeError, UnicodeEncodeError):
                    try:
                        print('\n*** Observação: UnicodeDecodeError, tentando encoding = CP-1252 ***')
                        arq = open(filename, 'r', encoding ='cp1252')
                    except (UnicodeDecodeError, UnicodeEncodeError):
                        print('\n*** Atenção, não foi possível carregar o texto:',arqtxt,'por erros no encoding ***')
                        arq.close()	
            string = arq.read()
            arq.close()
            return(string)
        
        
        filename =  filedialog.askopenfilename()
        print("\n" + filename)
        string = tryOpen(filename)


        #Abaixo, vamos extrair o nome do texto carregador:
        listaux = filename.split('/')
        nomeTxt = listaux[len(listaux)-1]
        
        
        return(string, nomeTxt)

    def destroiFrameFilho(self, frame):
        if frame.winfo_children() != []:
            frame.winfo_children()[0].destroy()
        else:
            return None
    
    def ungrid_frames_filhos(self, frame):
        if  frame.winfo_children() != []:
            cont = 0
            while cont < len(frame.winfo_children()):
                lst_frames = frame.winfo_children()
                lst_frames[cont].grid_forget()
                cont = cont + 1
    
    
    def finaliza(self):
        self.framePai.destroy()
            
class main_frame:

    def __init__(self, master):
        # Bloco (1) Configurando frame principal(janela-pai):
        
        self.master = master
        #Comando abaixo configura a resoluação padrão da janela como sendo a resolução do PC em questão:
        self.master.geometry("{}x{}".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        #Comando abaixo configura a janela para iniciar como "maximizada":
        self.master.state('zoomed')	
        #Comando abaixo configura o título da janela:
        self.master.title(' ')
        #Comando abaixo printa no terminal a resolução configurada para a máquina em questão:
        #~ print(self.master.winfo_screenwidth(), self.master.winfo_screenheight())
        
        #Abaixo é declarada a janela-pai
        self.scroll_win = ScrolledWindow(self.master)#, relief = GROOVE, padx = 10, pady = 4)

        self.framePai = self.scroll_win.scrollwindow
        
        #
        #Fim do Bloco (1)
        #------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        #------------------------------------------------------------------------------------------------------------------#
        
        # Bloco (2) Declaração do menu superior da janela-pai:
        self.menuSuperior = Menu(self.master)
        self.master.config(menu=self.menuSuperior)
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Arquivo":
        self.menuArquivo = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuArquivo, label='Arquivo')
        #Sub-opções dentro da opção "Arquivo":
        self.menuArquivo.add_command(label="Carregar",  command ='')
        self.menuArquivo.add_command(label="Novo",  command = self.load_file_txt)	
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuArquivo.add_separator()  #Esse comando adciona um layout de separação entre as opções do menu
        
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Configurações":
        self.menuConfiguracoes = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuConfiguracoes,label='Ferramentas')
        #Sub-opções dentro da opção "Configurações":,
        self.menuConfiguracoes.add_command(label="Configurações")
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuConfiguracoes.add_separator() 
        
        
        
        #Abaixo a declaração e as Sub-opções dentro da opção "Ajuda":
        self.menuAjuda = Menu(self.menuSuperior, tearoff=0)
        self.menuSuperior.add_cascade(menu=self.menuAjuda,label='Ajuda')
        #Sub-opções dentro da opção "Ajuda":
        self.menuAjuda.add_command(label="Tutorial")	
        self.menuAjuda.add_command(label="Sobre")	
        #Comando abaixo adciona um layout de separação entre as opções do menu:
        self.menuAjuda.add_separator()
        
        
        
        #Comando que exibe o menu:
        #master.config(menu=self.menuSuperior)
        
        #Fim do bloco (2)
        #------------------------------------------------------------------------------------------------------------------#
        ####################################################################################################################
        #------------------------------------------------------------------------------------------------------------------#
        
        # Bloco (3) Declarando sub-frames da janela-pai:
        '''A janela-pai está dividida em três sub-frames, lateral esquerdo, central, lateral direito, e um sub-frame de rodapé.
                Na presente classe, cada um dos três sub-frames não admite sub-divisões, sendo containeres.
                Sendo assim, adimitindo o maior grau de divisão de frames na classe, a janela-pai terá a seguinte divisão:
                
                ______________________________janela-pai______________________________
                |(subFrameLateralEsquerdo)|(subFrameCentral)|(subFrameLateralDireito)|
                |							subFrameInferior-rodapé						 |
                        
        '''	
        
        #Bloco (3.1): Abaixo, é declarado o frame lateral esquerdo. O frame está contido no frame-pai:
        self.frame_esquerdo = Frame(self.framePai, padx ="4", pady = "4")
        self.frame_esquerdo.grid(row = 0, column=0, sticky = N+S)
        
        
        
        #Bloco (3.3): Abaixo, é declarado o frame central. O frame está contido no frame-pai:
        self.frame_central = Frame(self.framePai)#, padx ="4", pady = "4")
        self.frame_central.grid(row = 0, column = 1)#, sticky = N+S+W+E)
    
        


        #Bloco (3.4): Abaixo, é declarado o frame lateral direito. O frame está contido no frame-pai:
        self.frame_direito = Frame(self.framePai, padx ="4", pady = "4")
        self.frame_direito.grid(row = 0, column = 2, sticky = N+S)

        #Bloco (3.5): Abaixo, é declarado o frame inferior no rodapé da do frame-pai(note o columnspan = 3):
        self.frame_infe = Frame(self.framePai, padx ="4")
        self.frame_infe.grid(row = 1, column = 0, columnspan = 3, sticky = W+E)

#####################################################################
#############  FIM DA __init__  #####################################
#####################################################################

    def add_wid_frame_esqr(self, wid_frame):
        self.wid_frame_esq = wid_frame(self.frame_esquerdo)
        return(self.wid_frame_esq)

    def add_wid_frame_cent(self, wid_frame):
        self.wid_frame_cent = wid_frame(self.frame_central)
        return(self.wid_frame_cent)

    def add_wid_frame_dire(self, wid_frame):
        self.wid_frame_dire = wid_frame(self.frame_direito)
        return(self.wid_frame_dire)

    def add_wid_frame_infe(self, wid_frame):
        self.wid_frame_infe = wid_frame(self.wid_frame_infe)
        return(self.wid_frame_infe)



    def pointer_frame_esq(self):
        return(self.frame_esquerdo)

    def pointer_frame_cent(self):
        return(self.frame_central)

    def pointer_frame_dire(self):
        return(self.frame_direito)

    def pointer_frame_infe(self):
        return(self.frame_infe)

    def pointer_frame_master(self):
        return(self.master)



    def load_file_txt(self):
        #A rotina abaixo abre o .txt, retornando um string, tratando eventuais erros com o encode:
        def tryOpen(filename):
            try:
                arq = open(filename, 'r', encoding = 'utf-8')
            except (UnicodeDecodeError, UnicodeEncodeError): #Aqui a função trata erros de enconding
                try:
                    print('\n*** Observação: UnicodeDecodeError, tentando encoding = charmap ***')
                    arq = open(filename, 'r', encoding ='charmap')
                except (UnicodeDecodeError, UnicodeEncodeError):
                    try:
                        print('\n*** Observação: UnicodeDecodeError, tentando encoding = CP-1252 ***')
                        arq = open(filename, 'r', encoding ='cp1252')
                    except (UnicodeDecodeError, UnicodeEncodeError):
                        print('\n*** Atenção, não foi possível carregar o texto:',arqtxt,'por erros no encoding ***')
                        arq.close()	
            string = arq.read()
            arq.close()
            return(string)

        filename =  filedialog.askopenfilename()
        print("\n" + filename)
        string = tryOpen(filename)

        #Abaixo, vamos extrair o nome do texto carregador:
        listaux = filename.split('/')
        nomeTxt = listaux[len(listaux)-1]
        
        
        return(string, nomeTxt)



    def destroi_framesFilhos(self, frame):
        if  frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].destroy()
                cont = cont + 1
        else:
            return None


    def ungrid_framesFilhos(self, frame):
        if  frame.winfo_children() != []:
            lst_frames = frame.winfo_children()
            cont = 0
            while cont < len(lst_frames):
                lst_frames[cont].grid_forget()
                cont = cont + 1
        else:
            return None


    def ungrid_framesFilhos_cent(self):
        self.ungrid_framesFilhos(self.frame_central)
    
    def destroi_framesFilhos_cent(self):
        self.destroi_framesFilhos(self.frame_central)


    def ungrid_framesFilhos_esqr(self):
        self.ungrid_framesFilhos(self.frame_esquerdo)


    def ungrid_framesFilhos_dire(self):
        self.ungrid_framesFilhos(self.frame_direito)


    def ungrid_framesFilhos_infe(self):
        self.ungrid_framesFilhos(self.frame_infe)


    def lst_framesFilhos_cent(self):
        return(self.frame_central.winfo_children())


    def finaliza(self):
        self.framePai.destroy()
