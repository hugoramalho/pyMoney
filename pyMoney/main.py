from GUIProg.gui_constr import *
from .BDProg.pyMoney_BD_prog import conexao_BD_prog

__author__ = "Ramalho, Hugo <ramalho.hg@gmail.com>"
__copyright__ = "Copyright 2017 -  pyMoney"
__credits__ = ["Instituto Federal do Espirito Santo, Campus SERRA", "Hugo Ramalho"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Hugo Ramalho"
__email__ = "ramalho.hg@gmail.com"
__status__ = "Testing"

def main():
    #root = Tk()
    #janela_app = root_constr(root)
    con_bd = conexao_BD_prog()
    app = App_controller(con_bd)
    app.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())