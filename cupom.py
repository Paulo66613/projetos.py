from i_pedido import *
import menu


def total():
    cls()
    global hp_total
    global pl_total
    global pz_total
    global ref_total
    global sc_total
    global cv_total
# -------------------------------------------------------------------------------------------------------------------                 
    if hanburgue_total.x_bacon > 0 :
        print('x bacom................. {} un'.format(hanburguer_quantidade.x_bacon))
        print('............................... = {0:.2f} $'.format(hanburgue_total.x_bacon))
    if hanburgue_total.x_calabresa > 0 :
        print('x calabresa............. {} un'.format(hanburguer_quantidade.x_calabresa))
        print('............................... = {0:.2f} $',format(hanburgue_total.x_calabresa)) 
    if hanburgue_total.x_egg > 0 :
        print('x egg................... {} un'.format(hanburguer_quantidade.x_egg))
        print('............................... = {0:.2f} $'.format(hanburgue_total.x_egg))
    if hanburgue_total.x_tudo > 0:
        print('x tudo.................. {} un'.format(hanburguer_quantidade.x_tudo))
        print('............................... = {0:.2f} $'.format(hanburgue_total.x_tudo))
            
    hp_total= hanburgue_total.x_bacon + hanburgue_total.x_calabresa + hanburgue_total.x_egg + hanburgue_total.x_tudo  
#-----------------------------------------------------------------------------------------------------------------------          
    if pastel_total.pastel_calabresa > 0 :
        print('pastel de calabresa..... {} un'.format(pastel_quantidade.pastel_calabresa))
        print('............................... = {0:.2f} $'.format(pastel_total.pastel_calabresa))
    if pastel_total.pastel_carne > 0 :
        print('pastel de carne......... {} un'.format(pastel_quantidade.pastel_carne))
        print('...........................,... = {0:.2f} $'.format(pastel_total.pastel_carne)) 
    if pastel_total.pastel_chocolate > 0 :
        print('pastel de chocolate..... {} un'.format(pastel_quantidade.pastel_chocolate))
        print('............................,.. = {0:.2f} $'.format(pastel_total.pastel_chocolate)) 
    if pastel_total.pastel_queijo > 0 :
        print('pastel de queijo........ {} un'.format(pastel_quantidade.pastel_queijo))
        print('............................... = {0:.2f} $'.format(pastel_total.pastel_queijo)) 
       
    pl_total = pastel_total.pastel_calabresa + pastel_total.pastel_carne + pastel_total.pastel_chocolate + pastel_total.pastel_queijo 
# -------------------------------------------------------------------------------------------------------------------------------------    
    if pizza_total.pizza_bacon > 0 :
        print('pizza de bacon.......... {} un'.format(pizza_quantidade.pizza_bacon))
        print('............................... = {0:.2f} $'.format(pizza_total.pizza_bacon))
    if pizza_total.pizza_calabresa > 0 :
        print('pizza de calabresa...... {} un'.format(pizza_quantidade.pizza_calabresa))
        print('............................... = {0:.2f} $'.format(pastel_total.pastel_calabresa))
    if pizza_total.pizza_queijo > 0 :
        print('pizza de queijo......... {} un'.format(pizza_quantidade.pizza_queijo)) 
        print('............................... = {0:.2f} $'.format(pizza_total.pizza_queijo))
    if pizza_total.pizza_tradicional > 0 :
        print('pizza tradicional....... {} un'.format(pizza_quantidade.pizza_tradicional))
        print('............................... = {0:.2f} $'.format(pizza_total.pizza_tradicional))  
        
    pz_total = pizza_total.pizza_bacon + pizza_total.pizza_calabresa + pizza_total.pizza_queijo + pizza_total.pizza_tradicional 
# -------------------------------------------------------------------------------------------------------------------------------------------    
    if refrigerante_total.coca > 0 :
        print('refrigerante coca....... {} un'.format(refrigerante_quantidade.coca))
        print('............................... = {0:.2f} $'.format(refrigerante_total.coca))
    if refrigerante_total.fanta > 0 :
        print('refrigerante fanta...... {} un'.format(refrigerante_quantidade.fanta))
        print('............................... = {0:.2f} $'.format(refrigerante_total.fanta))
    if refrigerante_total.guarana > 0 :
        print('refrigerante guarana.... {} un'.format(refrigerante_quantidade.guarana))
        print('............................... = {0:.2f} $'.format(refrigerante_total.guarana))
    if refrigerante_total.pepis > 0 :
        print('refrigerante pepis...... {} un'.format(refrigerante_quantidade.pepis))
        print('............................... = {0:.2f} $'.format(refrigerante_total.pepis))            
         
    ref_total = refrigerante_total.coca + refrigerante_total.fanta + refrigerante_total.guarana + refrigerante_total.pepis     
# --------------------------------------------------------------------------------------------------------------------------------------
    if suco_total.laranja > 0 :
        print('suco de laranja......... {} un'.format(suco_quantidade.laranja))
        print('............................... = {0:.2f} $'.format(suco_total.laranja))
    if suco_total.manga > 0 :
        print('suco de manga........... {} un'.format(suco_quantidade.manga))
        print('............................... = {0:.2f} $'.format(suco_total.manga))  
    if suco_total.uva > 0 :
        print('suco de uva............. {} un'.format(suco_quantidade.uva))
        print('............................... = {0:.2f} $'.format(suco_total.uva))    
    if suco_total.goiaba > 0 :
        print('suco de goiaba.......... {} un'.format(suco_quantidade.goiaba))
        print('............................... = {0:.2f} $'.format(suco_total.goiaba))
        
    sc_total = suco_total.laranja + suco_total.manga + suco_total.uva + suco_total.uva        
# ---------------------------------------------------------------------------------------------------------------------------------
    if cerveja_total.brahma > 0 :
        print('cerveja brahma.......... {} un'.format(cerveja_quantidade.brahma))
        print('............................... = {0:.2f} $'.format(cerveja_total.brahma))
    if cerveja_total.kaiser > 0 :
        print('cerveja kaiser.......... {} un'.format(cerveja_quantidade.kaiser))
        print('............................... = {0:.2f} $'.format(cerveja_total.kaiser))
    if cerveja_total.schin > 0 :
        print('cerveja schin........... {} un'.format(cerveja_quantidade.schin))
        print('............................... = {0:.2f} $'.format(cerveja_total.schin))
    if cerveja_total.devassa > 0 :
        print('cerveja devassa......... {} un'.format(cerveja_quantidade.devassa))
        print('............................... = {0:.2f} $'.format(cerveja_total.devassa))
    cv_total = cerveja_total.brahma +cerveja_total.kaiser + cerveja_total.schin + cerveja_total.devassa   
# -----------------------------------------------------------------------------------------------------------------------------
    total_global = hp_total + pl_total + pz_total + ref_total + sc_total + cv_total
    if total_global > 0 :       
        print('  ')
        print('  ')
        print("total....................................................... = {0:.2f} $".format(total_global))
    else:
        print('  ')  
        print('desculpe mas nao a resgistro no seu carrinho de compras') 
        print('  ') 
        menu.menu_caixa()
        

           