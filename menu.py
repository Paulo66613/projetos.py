import i_pedido
import c_pedido
linha = ('='*50)
import cupom


def menu_caixa ():
    print(linha)
    print('''
    = [1] entra no menu
    =
    = [2] cupom fiscal 
    =
    = [0] feicha caixa            
         ''')
    print(linha)
    menu_p = int(input('= '))
    if menu_p == 1 :
        i_pedido.cls()    
        menu_pedido ()
    elif menu_p == 2 :       
        cupom.total()
    elif menu_p == 0 :
        i_pedido.cls()
        print('tenha um otimo fim de semana')       


def menu_pedido ():
    print(linha)
    print('''
    ==========[ lanches ]==================[ bebidas ]===============  
    =                             =                                 =
    = [1] = hanburguer            = [4] refrigerante                =
    =                             =                                 =
    = [2] = pastel                = [5] suco                        =
    =                             =                                 =
    = [3] = pizza                 = [6] cerveja                     =
    =                             =                                 =
    =                             =
    =                [0] menu inicial                                                     =
    =================================================================      
          
          ''')
    print(linha)
    menu_p = int(input('selecione seu pedido ='))
    if menu_p == 1 :
        i_pedido.cls()
        c_pedido.hamburguer_1()
        print('1')
    elif menu_p == 2 :
        i_pedido.cls()
        c_pedido.pastel_1()
        print('2')    
    elif menu_p == 3 :
        i_pedido.cls()
        c_pedido.pizza_1()
        print('3') 
    elif menu_p == 4 :
        i_pedido.cls()
        c_pedido.refrigerante_1()
        print('4')       
    elif menu_p == 5 :
        i_pedido.cls()
        c_pedido.suco_1()
        print('5')
    elif menu_p == 6 :
        i_pedido.cls()
        c_pedido.cerveja_1()
        print('6')  
        
    elif menu_p == 0 :
        i_pedido.cls()
        menu_caixa ()      
            