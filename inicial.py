import menu
import i_pedido
    
menu.linha =('='*50)    
i_pedido.cls()
print(menu.linha)
print('''
=======================================      
    olá seja bem vindo ! 
    
    gostaria de inicia seu caixa ?
       
    precione 
    
=======================================    

    [1] para inicia
    
    [2] para sai     
      ''')
print(menu.linha)
in_go = int(input('= '))
if in_go == 1 :
    i_pedido.cls()
    menu.menu_caixa()
elif in_go == 2 :
    i_pedido.cls()
    print('boa noite')

