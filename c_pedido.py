from i_pedido import *
import menu



def hamburguer_1 ():
    cls()
    print('''
 -----------hamburguer----------
          
    [1] x tudo
================================          
    [2] x bacon
================================          
    [3] x calabresa
================================          
    [4] x egg
================================ 
    [0] menu pedidos  
--------------------------------
''')
    global hamburguer
    hamburguer = int(input('qual iten = '))
    if hamburguer == 1 :
        hanburguer_quantidade1.x_tudo = int(input('x tudo = '))
        hanburguer_quantidade.x_tudo = hanburguer_quantidade.x_tudo + hanburguer_quantidade1.x_tudo
        hanburgue_total.x_tudo = hanburguer_preco.x_tudo * hanburguer_quantidade.x_tudo
        hamburguer_1()
        
    elif hamburguer == 2 :
        hanburguer_quantidade1.x_bacon = int(input('x bacon = '))
        hanburguer_quantidade.x_bacon = hanburguer_quantidade.x_bacon + hanburguer_quantidade1.x_bacon
        hanburgue_total.x_bacon = hanburguer_preco.x_bacon * hanburguer_quantidade.x_bacon
        hamburguer_1()
        
    elif hamburguer == 3 :
        hanburguer_quantidade1.x_calabresa = int(input('x calabresa = '))
        hanburguer_quantidade.x_calabresa = hanburguer_quantidade.x_calabresa + hanburguer_quantidade1.x_calabresa
        hanburgue_total.x_calabresa = hanburguer_preco.x_calabresa * hanburguer_quantidade.x_calabresa
        hamburguer_1()
              
    elif hamburguer == 4 :
        hanburguer_quantidade1.x_egg = int(input('x egg = '))
        hanburguer_quantidade.x_egg = hanburguer_quantidade.x_egg + hanburguer_quantidade1.x_egg
        hanburgue_total.x_egg = hanburguer_preco.x_egg * hanburguer_quantidade.x_egg
        hamburguer_1()
        
    elif hamburguer == 0 :
        cls()
        menu.menu_pedido()
            
        
    else:
        print('codigo invalido retorne')
        hamburguer_1()    
            
def pastel_1 ():
    cls()
    print('''
 -----------pastel--------------
          
    [1] pastel de carne
================================          
    [2] pastel de calabresa
================================          
    [3] pastel de queijo
================================          
    [4] pastel de chocolate
================================
    [0] menu pedidos    
--------------------------------  
          ''') 
    global pastel
    pastel_2 = int(input('qual iten = '))
      
    if pastel_2 == 1 :
        pastel_quant1dade1.pastel_carne = int(input('pastel de carne = '))
        pastel_quantidade.pastel_carne = pastel_quantidade.pastel_carne + pastel_quant1dade1.pastel_carne
        pastel_total.pastel_carne = pastel_preco.pastel_carne * pastel_quantidade.pastel_carne
        pastel_1()
        
    elif pastel_2 == 2 :
        pastel_quant1dade1.pastel_calabresa = int(input('pastel de calabresa = '))
        pastel_quantidade.pastel_calabresa = pastel_quantidade.pastel_calabresa + pastel_quant1dade1.pastel_calabresa
        pastel_total.pastel_calabresa = pastel_preco.pastel_calabresa * pastel_quantidade.pastel_calabresa
        pastel_1()    
        
    elif pastel_2 == 3 :
        pastel_quant1dade1.pastel_queijo = int(input('pastel de queijo = '))
        pastel_quantidade.pastel_queijo = pastel_quantidade.pastel_queijo + pastel_quant1dade1.pastel_queijo
        pastel_total.pastel_queijo = pastel_preco.pastel_queijo * pastel_quantidade.pastel_queijo
        pastel_1()
        
    elif pastel_2 == 4 :
        pastel_quant1dade1.pastel_chocolate = int(input('pastel de chocolate = '))
        pastel_quantidade.pastel_chocolate = pastel_quantidade.pastel_chocolate + pastel_quant1dade1.pastel_chocolate
        pastel_total.pastel_chocolate = pastel_preco.pastel_chocolate * pastel_quantidade.pastel_chocolate
        pastel_1()        
        
    elif pastel_2 == 0 :
        cls()
        menu.menu_pedido()
            
        
    else:
        print('codigo invalido retorne')
        pastel_1() 
         
def pizza_1 ():
    cls()
    print('''
 -------=----pizza--------------
          
    [1] pizza de calabresa
================================          
    [2] pizza de queijjo
================================          
    [3] pizza de bacon 
================================          
    [4] pizza de tradiciolal
================================ 
    [0] menu pedidos 
--------------------------------  
          ''')
    global pizza
    pizza_2 = int(input('qual iten = '))
    if pizza_2 == 1 :
        pizza_quantidade1.pizza_calabresa = int(input('pizza de calabresa = '))
        pizza_quantidade.pizza_calabresa = pizza_quantidade.pizza_calabresa + pizza_quantidade1.pizza_calabresa
        pizza_total.pizza_calabresa = pizza_preco.pizza_calabresa * pizza_quantidade.pizza_calabresa
        pizza_1 () 
         
    elif pizza_2 == 2 :
        pizza_quantidade1.pizza_queijo = int(input('pizza de queijo = '))
        pizza_quantidade.pizza_queijo = pizza_quantidade.pizza_queijo + pizza_quantidade1.pizza_queijo
        pizza_total.pizza_queijo = pizza_preco.pizza_queijo * pizza_quantidade.pizza_queijo
        pizza_1 ()
        
    elif pizza_2 == 3 :
        pizza_quantidade1.pizza_bacon = int(input('pizza de bacon = '))
        pizza_quantidade.pizza_bacon = pizza_quantidade.pizza_bacon + pizza_quantidade1.pizza_bacon
        pizza_total.pizza_bacon = pizza_preco.pizza_bacon * pizza_quantidade.pizza_bacon
        pizza_1 ()
        
    elif pizza_2 == 4 :
        pizza_quantidade1.pizza_tradicional = int(input('pizza tradicional = '))
        pizza_quantidade.pizza_tradicional = pizza_quantidade.pizza_tradicional + pizza_quantidade1.pizza_tradicional
        pizza_total.pizza_tradicional = pizza_preco.pizza_tradicional * pizza_quantidade.pizza_tradicional
        pizza_1 ()
        
    elif pizza_2 == 0 :
        cls()
        menu.menu_pedido()
            
        
    else:
        print('codigo invalido retorne')
        pizza_1()              
    
    ###=======================      
def refrigerante_1 ():
    cls()
    print('''
 ---------refrigerante----------
          
    [1] coca cola
================================          
    [2] guaranna
================================          
    [3] fanta
================================          
    [4] pepis
================================ 
    [0] menu pedidos 
--------------------------------  
          ''')
    global refrigerante
    refrigerante_2 = int(input('qual iten = '))
   
        
    if  refrigerante_2 == 1 :
        refrigerante_quantidade1.coca = int(input('refrigerante coca = '))
        refrigerante_quantidade.coca = refrigerante_quantidade.coca + refrigerante_quantidade1.coca
        refrigerante_total.coca = refrigerante_preco.coca * refrigerante_quantidade.coca
        refrigerante_1 () 
        
    elif refrigerante_2 == 2 :
        refrigerante_quantidade1.guarana = int(input('refrigerante guarana = '))
        refrigerante_quantidade.guarana = refrigerante_quantidade.guarana + refrigerante_quantidade1.guarana
        refrigerante_total.guarana = refrigerante_preco.guarana * refrigerante_quantidade.guarana    
        refrigerante_1 ()     
        
    elif refrigerante_2 == 3 :
        refrigerante_quantidade1.fanta = int(input('refrigerante fanta = '))
        refrigerante_quantidade.fanta = refrigerante_quantidade.fanta + refrigerante_quantidade1.fanta
        refrigerante_total.fanta = refrigerante_preco.fanta * refrigerante_quantidade.fanta
        refrigerante_1 () 
        
    elif refrigerante_2 == 4 :
        refrigerante_quantidade1.pepis = int(input('refrigerante pepis = '))
        refrigerante_quantidade.pepis = refrigerante_quantidade.pepis + refrigerante_quantidade1.pepis
        refrigerante_total.pepis = refrigerante_preco.pepis * refrigerante_quantidade.pepis
        refrigerante_1 ()
        
    elif refrigerante_2 == 0 :
        cls()
        menu.menu_pedido()
            
        
    else:
        print('codigo invalido retorne')
        refrigerante_1()                   
    
def suco_1 ():
    cls()
    print('''
 -------------suco--------------
          
    [1] suco de laranja
================================          
    [2] suco de manga
================================          
    [3] suco de uva
================================          
    [4] suco de goiaba
================================ 
    [0] menu pedidos 
--------------------------------  
          ''') 
    global suco
    suco_2 = int(input('qual iten = '))
   
        
    if  suco_2 == 1 :
        suco_quantidade1.laranja = int(input('suco de laranja = '))
        suco_quantidade.laranja = suco_quantidade.laranja + suco_quantidade1.laranja
        suco_total.laranja = suco_preco.laranja * suco_quantidade.laranja
        suco_1 ()
        
    elif  suco_2 == 2 :
        suco_quantidade1.manga = int(input('suco de manga = '))
        suco_quantidade.manga = suco_quantidade.manga + suco_quantidade1.manga
        suco_total.manga = suco_preco.manga * suco_quantidade.manga
        suco_1 ()
        
    elif  suco_2 == 3 :
        suco_quantidade1.uva = int(input('suco de uva = '))
        suco_quantidade.uva = suco_quantidade.uva + suco_quantidade1.uva
        suco_total.uva = suco_preco.uva * suco_quantidade.uva
        suco_1 ()
        
    elif  suco_2 == 4 :
        suco_quantidade1.laranja = int(input('suco de laranja = '))
        suco_quantidade.laranja = suco_quantidade.laranja + suco_quantidade1.laranja
        suco_total.laranja = suco_preco.laranja * suco_quantidade.laranja
        suco_1 ()
        
    elif suco_2 == 0 :
        cls()
        menu.menu_pedido()
            
        
    else:
        print('codigo invalido retorne')
        suco_1()                
        
         
    
def cerveja_1 ():
    cls()
    print('''
 -----------cerveja----------
          
    [1] brahma
================================          
    [2] kaiser
================================          
    [3] schin
================================          
    [4] devassa
================================
    [0] menu pedidos 
--------------------------------  
          ''') 
    
    global cerveja
    cerveja_2 = int(input('qual iten = '))
   
        
    if  cerveja_2 == 1 :
        cerveja_quantidade1.brahma = int(input('cerveja brahma = '))
        cerveja_quantidade.brahma = cerveja_quantidade.brahma + cerveja_quantidade1.brahma
        cerveja_total.brahma = cerveja_preco.brahma * cerveja_quantidade.brahma
        cerveja_1 ()
        
    elif  cerveja_2 == 2 :
        cerveja_quantidade1.kaiser = int(input('cerveja kaiser = '))
        cerveja_quantidade.kaiser = cerveja_quantidade.kaiser + cerveja_quantidade1.kaiser
        cerveja_total.kaiser = cerveja_preco.kaiser * cerveja_quantidade.kaiser
        cerveja_1 ()
        
    elif  cerveja_2 == 3 :
        cerveja_quantidade1.schin = int(input('cerveja schin = '))
        cerveja_quantidade.schin = cerveja_quantidade.schin + cerveja_quantidade1.schin
        cerveja_total.schin = cerveja_preco.schin * cerveja_quantidade.schin
        cerveja_1 ()
        
    elif cerveja_2 == 4 :
        cerveja_quantidade1.devassa = int(input('cerveja devassa = '))
        cerveja_quantidade.devassa = cerveja_quantidade.devassa + cerveja_quantidade1.devassa
        cerveja_total.devassa = cerveja_preco.devassa * cerveja_quantidade.devassa
        cerveja_1 ()
        
    elif cerveja_2 == 0 :
        cls()
        menu.menu_pedido()
            
        
    else:
        print('codigo invalido retorne')
        cerveja_1()                         