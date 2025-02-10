import random
from time import sleep
from pystyle import *

Singapore = """
   ▄████████  ▄█  ███▄▄▄▄      ▄██████▄     ▄████████    ▄███████▄  ▄██████▄     ▄████████    ▄████████ 
  ███    ███ ███  ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███▌ ███   ███   ███    █▀    ███    ███   ███    ███ ███    ███   ███    ███   ███    █▀  
  ███        ███▌ ███   ███  ▄███          ███    ███   ███    ███ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
▀███████████ ███▌ ███   ███ ▀▀███ ████▄  ▀███████████ ▀█████████▀  ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
         ███ ███  ███   ███   ███    ███   ███    ███   ███        ███    ███ ▀███████████   ███    █▄  
   ▄█    ███ ███  ███   ███   ███    ███   ███    ███   ███        ███    ███   ███    ███   ███    ███ 
 ▄████████▀  █▀    ▀█   █▀    ████████▀    ███    █▀   ▄████▀       ▀██████▀    ███    ███   ██████████ 
                                                                                ███    ███              
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
System.Title("SINGAPORE by NinjaPanic")
System.Clear()
Cursor.HideCursor()

Anime.Fade(Center.Center(BTC),Colors.red_to_green,Colorate.Vertical,interval=0.025,enter=True)

def random_char(y):
       return ''.join(random.choice(r) for x in range(y))

while 1 == 1:
    System.Clear()
    print("\n"*2)
    print(Colorate.Vertical(Colors.red_to_green, Center.XCenter(Singapore)))
    print("\n"*3)
    Write.Print("  [>] Singapore has been created by NinjaPanic on Github | https://github.com/NinjaPanic/Singapore", Colors.red_to_green, interval=0.0125)
    Write.Print("\n  [>] Discord server : https://discord.gg/X9MxZ3JnXy", Colors.red_to_green, interval=0.0125)
    print("\n"*2)

    Wallet = Write.Input("  [>] Enter your wallet -> ", Colors.red_to_green, interval=0.025)

    if Wallet[0] == 1 or 3 and len(Wallet) >= 27 and len(Wallet) <= 34:
        print()
        Write.Print("  [>] Valid Wallet adress!",Colors.red_to_green, interval=0.025)
        a = 1
        i = 2
        sleep(2.5)
        
    else:
        print()
        print(Colorate.Error("  [>] Error! Wallet adress incorect!"))
        

    while i == 2 :
        System.Clear()
        while a < 2 :
            d = round(random.uniform(0.00005, 0.0001),5)
            print(random_char(34) + Colorate.Color(Colors.red," -> " + str(b) + " BTC",True))
            a = a + d
            sleep(0.04)
        print(random_char(34) + Colorate.Color(Colors.green," -> " + str(round(random.uniform(0.00001, 0.01),5)) + " BTC",True))
        a = 1
        sleep(3)
        Write.Print("\n\n  [>] Connecting with your wallet!",Colors.red_to_green, interval=0.025)
        sleep(5)
        Write.Print("\n\n  [>] Sending Bitcoin to your wallet!",Colors.red_to_green, interval=0.025)
        sleep(8)
        Write.Print("\n\n  [>] Successful transaction!",Colors.red_to_green, interval=0.025)
        sleep(1)
        Write.Print("\n\n  [>] Wait for restarting!",Colors.red_to_green, interval=0.025)
        sleep(12)
