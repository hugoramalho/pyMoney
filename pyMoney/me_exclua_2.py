from pyMoney_BD_prog import *
import time


def main(args):
    #~ conect = conexao_BD_ender()

    #~ ini = time.time()
    #~ lst_ender = conect.fetch_ender_rua('Ludwik Macal')
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n\nfetch_ender_rua: ', delta_t, '\n\n')
    #~ print(lst_ender)
    #~ for elem in lst_ender:
        #~ print(elem)


    #~ ini = time.time()
    #~ dic_ender = conect.fetch_ender_cep(29060030)
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n\nfetch_ender_cep: ', delta_t, '\n\n', dic_ender)


    #~ ini = time.time()
    #~ lst_ender = conect.fetch_ender_cep_like(290600)
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n\fetch_ender_cep_like: ', delta_t, '\n\n', lst_ender)


    #~ ini = time.time()
    #~ lst_ender = conect.fetch_ender_rua_like('Ludwi')
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n\fetch_ender_rua_like: ', delta_t, '\n\n', lst_ender)

    #~ ini = time.time()
    #~ lst_ender = conect.fetch_cidade('Vitória')
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n\fetch_cidade: ', delta_t, '\n\n', lst_ender)


    #~ ini = time.time()
    #~ nome1 = 'Se'
    #~ nome1 = str(nome1)
    #~ print(nome1)
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n', delta_t)
    
    #~ ini = time.time()
    #~ print(nome1)
    #~ fim = time.time()
    #~ delta_t = fim - ini
    #~ print('\n', delta_t)
    
    t = True
    f = str(t)
    print(f)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
