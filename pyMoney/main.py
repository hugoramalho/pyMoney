from pyMoney.controllerProg.controller import App_controller

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
    app = App_controller()
    app.mainloop()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())