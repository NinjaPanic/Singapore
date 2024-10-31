import random
from time import sleep
from pystyle import *

Singapore = r"""
   .-'''-. .-./`) ,---.   .--.  .-_'''-.      ____    .-------.     ,-----.    .-------.        .-''-.   
  / _     \\ .-.')|    \  |  | '_( )_   \   .'  __ `. \  _(`)_ \  .'  .-,  '.  |  _ _   \     .'_ _   \  
 (`' )/`--'/ `-' \|  ,  \ |  ||(_ G _)|  ' /   '  \  \| (_ P._)| / ,-.|  \ _ \ | ( ' )  |    / ( ` )   ' 
(_ S _).    `-'`"`|  |\_ \|  |. (_,_)/___| |___|  /  ||  (_,_) /;  \  '_ /  | :|(_ R _) /   . (_ E _)  | 
 (_,_). '.  .---. |  _( )_\  ||  |  .-----.   _.-`   ||   '-.-' |  _`,/O\ _/  || (_,_).' __ |  (_,_)___| 
.---.  \  : |   | | (_ N _)  |'  \  '-   .'.'   _    ||   |     : (  '\_/ \   ;|  |\ \  |  |'  \   .---. 
\    `-'  | | I | |  (_,_)\  | \  `-'`   | |  _( )_  ||   |      \ `"/  \  ) / |  | \ `'   / \  `-'    / 
 \       /  |   | |  |    |  |  \        / \ (_ A _) //   )       '. \_/``".'  |  |  \    /   \       /  
  `-...-'   '---' '--'    '--'   `'-...-'   '.(_,_).' `---'         '-----'    ''-'   `'-'     `'-..-'   
"""[1:]


BTC = """
                                                  !!*%%$$@@@@@@$$$%**!                                                  
                                             !*$@&&##&&@@@$$$$$@@&&&##&&$%*!                                            
                                         !*$&##&@%*!!              !!*%$@&#&@%!                                         
                                       *@##&$*!                           !%@##&$!                                      
                                    !$&#&$*                                  !*@##@%                                    
                                  !$##@*            !*!!*!  *****!              !%&#&%                                  
                                !$##@!              $####@  @####$                 %&#&*                                
                               *&#@*                $####@  @####$                   %##@!                              
                              $##%           !!!!!! @####@  @####$                    !@#&*                             
                             @#&*           !&&&&&&&######&&#####&@@$%!                 $##%                            
                            @#&!            !##########################@%                %##%                           
                           $#&!              %%%%%$######&%%%%%$$@&######@                %##*                          
                          %##*                    *######@         *&#####%                @#&!                         
                         !&#$                     *######@          %#####@                !&#$                         
                         %##!                     *######@          $#####$                 $#&!                        
                         @#@                      *######@        *$#####&!                 !##%                        
                        !&#$                      *######&$$$$@@@&#####&$!                   &#$                        
                        !##%                      *######NinjaPanic####@*                    @#@                        
                        !##%                      *######&@@@@@@&&&######&%                  @#@                        
                        !&#%                      *######@        !*%&#####@                 &#$                        
                         @#@                      *######@           !@#####%               !##%                        
                         %##!                     *######@            %#####@               %##!                        
                         !&#$                     *######@            @#####$              !&#$                         
                          %##*                    *######@         !*@#####&!              $#&!                         
                           @#&!              %%%%%$######&%%%%%%$$@&######&!              %##*                          
                            @#&!            !###########################@%               %##%                           
                            !@#&!           !&&&&&&&######&&#####&&@@$*!                %##%                            
                              $##%           !!!!!! @####@ !@####$                    !@##*                             
                               %&#@!                $####@  @####$                   %&#@!                              
                                !$##$!              @####@  @####$                 *@#&%                                
                                  *@##$*            *%%%%*  *****!               %@#&$!                                 
                                    !$##&%!                                   *$&#&%!                                   
                                      !%@##&$*!                           !*$&#&$*                                      
                                         !%@&##&$%*!                !!*%@&##&$*                                         
                                             !%$@&##&&@@$$$$$$$$@@&&&##&@$*!                                            
                                                  !*%%$$@@@@@@@@@$$%*!!                                                 
"""[1:]

r = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
a = 5
b = 0
h = i = 1


System.Size(140, 40)
System.Title("Singapore")
System.Clear()

Anime.Fade(Center.Center(BTC),Colors.red_to_green,Colorate.Vertical,interval=0.025,enter=True)

def random_char(y):
       return ''.join(random.choice(r) for x in range(y))

while 1 == 1:
    System.Clear()
    print("\n"*2)
    print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(Singapore)))
    print("\n"*5)

    Wallet = Write.Input("Enter your wallet -> ", Colors.red_to_purple, interval=0.0025)

    if Wallet[0] == 1 or 3 and len(Wallet) >= 27 and len(Wallet) <= 34:
        print()
        Write.Print("Valid Wallet adress!",Colors.green_to_blue, interval=0.005)
        a = 1
        i = 2
        sleep(2.5)
        
    else:
        print()
        print(Colorate.Error("Error! Wallet adress incorect!"))
        

    while i == 2 :
        System.Clear()
        while a < 2 :
            d = round(random.uniform(0.00005, 0.0001),5)
            print(random_char(34) + Colorate.Color(Colors.red," -> "+str(b)+" BTC",True))
            a = a + d
            sleep(0.04)
        print(random_char(34) + Colorate.Color(Colors.green," -> "+str(round(random.uniform(0.00001, 0.01),5))+" BTC",True))
        a = 1
        sleep(3)
        Write.Print("Connect with your wallet!",Colors.green_to_blue, interval=0.005)
        print()
        print()
        sleep(5)
        Write.Print("Send Bitcoin to your wallet!",Colors.green_to_blue, interval=0.005)
        print()
        print()
        sleep(8)
        Write.Print("Successful transaction!",Colors.green_to_blue, interval=0.005)
        print()
        print()
        sleep(1)
        Write.Print("Wait for restarting!",Colors.green_to_blue, interval=0.005)
        sleep(12)
